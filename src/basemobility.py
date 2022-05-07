import geopandas
import numpy as np

from abc import ABC, abstractmethod
from shapely.geometry import Point

from .movement import Movement
from .resultcollection import Resultcollection
from .simulationparameter import Simulationparameter

from .baseenergy import Baseenergy 

class Basemobility(ABC):
    
    def __init__(self, uid,  startPos, endPos):
        self._uid = uid
        self._move = Movement()
        self._resultcollection =  Resultcollection()
        self._baseenergy = Baseenergy()
        self._startPos = startPos
        self._endPos = endPos
        self._currentPos = Point(0,0,0) 
        pass

    def getMove(self):
        return self._move


    def getCurrentPos(self):
        passedTime = (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime()
        if passedTime==0.0:
            return self._startPos
        else:
            currentDirection = self.getMove().getCurrentDirection()

        #if self.getMove().getLinearMobilitySpFlag():
            #currentDirection = self.getMove().getCurrentDirection()
            #if self.getMove().getLinearMobilitySpFlag():

                # currentPos = self.getMove().getNextCoordinate()
                # if (self.getMove().getFinalFlag()):
                #     currentPos = self.getMove().getNextCoordinate()

                #return currentPos

            #elif self.getMove().getFinalFlag():
                # currentPos=Point(self.getMove().getTempStartPos().x, self.getMove().getTempStartPos().y, 0.0)
                #currentPos=Point(self.getMove().getNextCoordinate().x, self.getMove().getNextCoordinate().y, 0.0)
                # currentPos = self.getMove().getNextCoordinate()

            previousPos = self.getMove().getTempStartPos()

            if self.getMove().getFinalFlag():
                return Point(previousPos.x,previousPos.y,0.0)

            x = previousPos.x + (currentDirection.x*self.getMove().getSpeed()*Simulationparameter.stepLength)
            y = previousPos.y + (currentDirection.y*self.getMove().getSpeed()*Simulationparameter.stepLength)
            z = previousPos.z + (currentDirection.z*self.getMove().getSpeed()*Simulationparameter.stepLength)
            # print(x, flush=True)
            # print(y, flush=True)
            currentPos = Point(x,y,z)
            self.getMove().setTempStartPos(currentPos)
        
            return currentPos

    # current position function for spline mobility
    def getCurrentPosSp(self):
        passedTime = (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime()
        # currenPos = Point(0, 0, 0)
        if not self.getMove().getFinalFlag():

            currentPos = self.getMove().getNextCoordinate()
        # if (self.getMove().getFinalFlag()):
        #     currentPos = self.getMove().getNextCoordinate()
            return currentPos

        elif self.getMove().getFinalFlag():
            # currentPos=Point(self.getMove().getTempStartPos().x, self.getMove().getTempStartPos().y, 0.0)
            currentPos=Point(self.getMove().getNextCoordinate().x, self.getMove().getNextCoordinate().y, 0.0)
            # currentPos=Point(self.getMove().getNextCoordinate().x, self.getMove().getNextCoordinate().y, self.getMove().getNextCoordinate().z)
            # currentPos = self.getMove().getNextCoordinate()


        return currentPos


    def makeMove(self):
        self.doLog()

    def doLog(self):
        #print("do log")
        if self.getMove().getLinearMobilitySpFlag():   # log for spline mobility
            self._resultcollection.logCurrentPosition(self._uid, self.getCurrentPosSp(), self.getMove())

        else:   # log for linear mobility
            self._resultcollection.logCurrentPosition(self._uid, self.getCurrentPos(), self.getMove())
        currentEnergy = self._baseenergy.getcurrentEnergy(self.getMove().getSpeed(), (Simulationparameter.currentSimStep * Simulationparameter.stepLength) - self.getMove().getStartTime())

        self._resultcollection.logCurrentEnergy(self._uid,currentEnergy[0], currentEnergy[1])

        pass
