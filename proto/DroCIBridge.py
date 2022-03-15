import grpc
from google.protobuf import struct_pb2


from src.simulation import Simulation
from concurrent import futures
from src.simulationparameter import Simulationparameter
from shapely.geometry import Point
from src.uav import Uav

import time
import sys
import string
import os
import threading, _thread


from proto import airmobisim_pb2_grpc
from proto import airmobisim_pb2

ending = 0

class AirMobiSim(airmobisim_pb2_grpc.AirMobiSimServicer):


    def __init__(self, simulation_obj):
        self._isRunning = False
        self._isInitialized = True
        self.simulation_obj = simulation_obj
        self._lastUavReport = []
        self.finish = False

    def startSimulation(self):
        self.simulation_obj.initializeNodes()
        self._isRunning = True

    def Start(self, request, context):
        print("Start gets called")
        return struct_pb2.Value()

    """
        TODO:  ExecuteOneTimeStep should be an own method with the return GRPC statement 
    """

    def ExecuteOneTimeStep(self, request, context):
        """
            Execute one timestep - Update the values (positions, velocity,...)
        """
        print("Executing one Timestep")
        responseQuery = airmobisim_pb2.ResponseQuery()
        if not self._isRunning:
            self.startSimulation()
            for node in self.simulation_obj._managedNodes:
                startPos = node._mobility._startPos
                uav = airmobisim_pb2.Response(id=node._uid, x=startPos.x, y=startPos.y, z=startPos.z)
                responseQuery.responses.append(uav)

            Simulationparameter.incrementCurrentSimStep()

            return responseQuery
        else:
            # rt = Repeatedtimer(1, self.printStatus, "World")
            if Simulationparameter.currentSimStep < self.simulation_obj._simulationSteps:
                self._lastUavReport = []
                for node in self.simulation_obj._managedNodes:
                    node.getMobility().makeMove()
                    self._isInitialized = True
                    currentPos = node.getMobility().getCurrentPos()
                    print("##########################################################", flush=True)
                    print("THIS IS WHAT I AM SENDING ON THE INTERFACE", flush=True)
                    print("##########################################################", flush=True)
                    print("currentPos.x:"  + str(currentPos.x), flush=True)
                    print("currentPos.y:"  + str(currentPos.y), flush=True)
                    print("currentPos.z:"  + str(currentPos.z), flush=True)
                    uav = airmobisim_pb2.Response(id=node._uid, x=currentPos.x, y=currentPos.y, z=currentPos.z, speed=node.getMobility()._move.getSpeed(), angle=node.getMobility()._angle)
                    self._lastUavReport.append(uav)
                    responseQuery.responses.append(uav)

                Simulationparameter.incrementCurrentSimStep()
                return responseQuery

            else:
                # rt.stop()
                print("I finished simulation.")
                self.simulation_obj.finishSimulation()

    def Finish(self, request, context):
        #os.close(sys.stdout.fileno())
        #os.close(sys.stderr.fileno())
        self.finish = True
        return struct_pb2.Value()
    def GetManagedHosts(self, request, context):
        print("GetManagesHosts gets called!")
        responseQuery = airmobisim_pb2.ResponseQuery()

        if not self._isRunning:
            self.startSimulation()
       

        for node in self.simulation_obj._managedNodes:
            if self._isInitialized:
                node._mobility.makeMove()
                self._isInitialized = True
            currentPos = node._mobility.getCurrentPos()
            uav = airmobisim_pb2.Response(id=node._uid, x=currentPos.x, y=currentPos.y, z=currentPos.z,
                                          speed=node.getMobility()._move.getSpeed(), angle=node.getMobility()._angle)  # TODO: Make speed a correct parameter
            responseQuery.responses.append(uav)
        return responseQuery

    def InsertUAV(self, request, context):
        """
        Method inserts an UAV in simulation
        In the next timestep makeMove()
        """
        print("InsertUAV  gets called")
        self.simulation_obj._managedNodes.append(Uav(request.id, Point(request.coordinates[0].x, request.coordinates[0].y, request.coordinates[0].z), Point(request.coordinates[1].x, request.coordinates[1].y, request.coordinates[1].z), angle=request.angle, speed=request.speed))
        
        return struct_pb2.Value()

    def InsertWaypoints(self, request, context):
        pass

    def DeleteUAV(self, request, context):
       """
       Delete UAV with the given Id
       """
       print("DeleteUAV gets called")
       print(request.num)
       for node in range(len(self.simulation_obj._managedNodes)):
           print(node)
           print("I am printing the length of list")
           print(len(self.simulation_obj._managedNodes))
           if self.simulation_obj._managedNodes[node]._uid == request.num:
                self.simulation_obj._managedNodes.pop(node)
                print("I deleted a Node")
           print(len(self.simulation_obj._managedNodes))

       print("I am done.")

       for node in range(len(self.simulation_obj._managedNodes)):
           print(self.simulation_obj._managedNodes[node]._uid)

       return struct_pb2.Value()

    def getNumberCurrentUAV(self, request, context):
      """
       Return the number for current UAVs
      """
     
      print("getNumberCurrentUAV gets called")
      currentUAV = len(self.simulation_obj._managedNodes) 

      return airmobisim_pb2.Number(num=currentUAV)

def checkForParentProcess():
    ppid = os.getppid()
    print("checkForParentProcess!")
    while True:
        time.sleep(1)
        if os.getppid() != ppid:
            print("You are not my parent")
            sys.exit()
        else:
            pass




def startServer(simulation_object):
    """
        Start the AirMobiSim Server
    """
    threading.Thread(target = checkForParentProcess).start()

    print("I am still there", flush=True)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    airmobisim_object = AirMobiSim(simulation_object)
    airmobisim_pb2_grpc.add_AirMobiSimServicer_to_server(airmobisim_object, server)
    server.add_insecure_port('localhost:50051')
    server.start()

    print("AirMobiSim Server has started....")
    
    ppid = os.getppid()

    try:
        while True: 
            time.sleep(1);
    except:
        server.stop(0)
        print("Server has been stopped")
