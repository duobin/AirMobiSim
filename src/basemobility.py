import math
from abc import ABC
import os
from xml.dom import minidom

import numpy as np
from shapely.geometry import Point

from .baseenergy import Baseenergy
from .movement import Movement
from .resultcollection import Resultcollection
from .simulationparameter import Simulationparameter
import matplotlib.path as mplPath
import src.logWrapper as logWrapper


class Basemobility(ABC):
    polygon_file_path = None
    _uav = None
    def __init__(self, uav, uid, speed, polygon_file_path,collision_action):
        self._uav = uav
        self._uid = uid
        self._speed = speed
        self._move = Movement()
        self._resultcollection =  Resultcollection()
        self._baseenergy = Baseenergy()
        self._move.setStart(self._uav._waypoints[0], 0)
        self._move.setTempStartPos(self._uav._waypoints[0])
        self._move.setNextCoordinate(self._uav._waypoints[-1])
        self._move.setEndPos(self._uav._waypoints[-1])
        
        self._currentWaypointIndex = 0

        self._move.setSpeed(self._speed)
        self._move.setTotalDistance(self.computeTotalDistance())
        
        self._collisionAction = collision_action  # 1= warn, 2 = no action 3=remove uav; anything else is wrong
        self._obstacleDetector_flag = False
        self.polygon_file_path = polygon_file_path
        self._obstacles = self.ParsePolygonFileToObstacles()
        pass

    def getMove(self):
        return self._move

    def getCurrentPos(self):
        passedTime = (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime()
        if passedTime==0.0:
            return self._uav._waypoints[0]
        else:
            currentDirection = self.getMove().getCurrentDirection()

            previousPos = self.getMove().getTempStartPos()

            if self.getMove().getFinalFlag():
                return previousPos

            x = previousPos.x + (currentDirection.x*self.getMove().getSpeed()*Simulationparameter.stepLength)
            y = previousPos.y + (currentDirection.y*self.getMove().getSpeed()*Simulationparameter.stepLength)
            z = previousPos.z + (currentDirection.z*self.getMove().getSpeed()*Simulationparameter.stepLength)

            currentPos = Point(x,y,z)
            
            distancePerstep = self.getMove().getSpeed()*Simulationparameter.stepLength
            print("Current distance is " + currentPos.distance(self._uav._waypoints[self._currentWaypointIndex+1]).__str__())
            if currentPos.distance(self._uav._waypoints[self._currentWaypointIndex+1])<distancePerstep:
                print("Current waypoint index is " + self._currentWaypointIndex.__str__() + " position is " +  self._uav._waypoints[self._currentWaypointIndex].__str__())
                self._currentWaypointIndex = self._currentWaypointIndex  + 1
                print("Current waypoint index is " + self._currentWaypointIndex.__str__() + " position is " +  self._uav._waypoints[self._currentWaypointIndex].__str__())
                if self._currentWaypointIndex == len(self._uav._waypoints)-1: #there are no further waypoints
                    self.getMove().setFinalFlag(True)
                    print("No further waypoints!")
                    return currentPos
                print("next waypoint position: ", self._uav._waypoints[self._currentWaypointIndex+1])
                self.getMove().setNextCoordinate(self._uav._waypoints[self._currentWaypointIndex+1])
            self.getMove().setTempStartPos(currentPos)
            return currentPos

    # current position function for spline mobility
    def getCurrentPosSp(self):
        passedTime = (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime()
        if passedTime==0:
            return self._uav._waypoints[0]
        
        if not self.getMove().getFinalFlag():
            currentPos = self.getMove().getNextCoordinate()
            return currentPos

        elif self.getMove().getFinalFlag():
            currentPos = self.getMove().getNextCoordinate()

        return currentPos

    def makeMove(self):
        self.doLog()

    def doLog(self):
        if self.getMove().getLinearMobilitySpFlag():   # log for spline mobility
            self._resultcollection.logCurrentPosition(self._uid, self.getCurrentPosSp(), self.getMove())

        else:   # log for linear mobility
            self._resultcollection.logCurrentPosition(self._uid, self.getCurrentPos(), self.getMove())
        currentEnergy = self._baseenergy.getcurrentEnergy(self.getMove().getSpeed(), (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime())

        self._resultcollection.logCurrentEnergy(self._uid,currentEnergy[0], currentEnergy[1])
        pass

    def ParsePolygonFileToObstacles(self):
        if self.polygon_file_path is None or not os.path.exists(self.polygon_file_path):
            return None

        logWrapper.debug(("self.polygon_file_path: %s", str(self.polygon_file_path)))

        parsedFile= minidom.parse(self.polygon_file_path)
        polygons = parsedFile.getElementsByTagName('poly')
        buildings=[]
        for polygon in polygons:
            shape_of_polygon = polygon.attributes['shape'].value

            vertex_coordinates= shape_of_polygon.split(' ')       # coordinates are of string type

            list_of_coordinates=[]
            for single_vertex in vertex_coordinates:       # x and y coordinates are seperated and converted to float
                list_of_coordinates.append([float(single_vertex.split(',')[0]),float(single_vertex.split(',')[1])])


            # forming shape of polygon by joining the polygon coordinates and appended to building list
            buildings.append(mplPath.Path(np.array(list_of_coordinates)))


        return buildings



    def computeTotalFlightTime(self, currentTime, speed, acceleration):
        if speed == 0 and acceleration == 0:
            return 0
        distance = self.getMove().getTotalDistance()
        final_velocity = math.sqrt(speed ** 2 + 2 * acceleration * distance)  # v^2=u^2+2as
        average_velocity = (speed + final_velocity) / 2
        assert average_velocity != 0, 'avarage velocity can not be 0'
        flightTime = distance / average_velocity + currentTime
        return flightTime

    def manageObstacles(self, passedTime,futureTime):
        if self._obstacles == None:
            return
        futureCoordinate = self.getMove().getFutureCoordinate()

        detectObstacle = any(obstacle.contains_point(futureCoordinate) for obstacle in self._obstacles)
        if not self._obstacleDetector_flag and detectObstacle and self._collisionAction == 1:
            # warnings.warn('uav is going to collide in collide')
            print('WARNING!!!!')
            print('currentTime:', passedTime, 'uav is going to collide at ', futureTime)
            logWrapper.debug('WARNING!!!!')
            logWrapper.debug(('currentTime: %s, uav is going to collide at %s', str(passedTime), str(futureTime)))

        self._obstacleDetector_flag = True if detectObstacle == True else self._obstacleDetector_flag
