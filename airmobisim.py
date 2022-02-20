#!/usr/bin/env python3
import sys
import argparse
import pathlib

from shapely.geometry import Point
from src.simulation import Simulation
from src.simpleapp import Simpleapp

from src.yamlparser import Yamlparser

from src.resultcollection import Resultcollection
from src.plotting import load_Data, make_plot


from proto.DroCIBridge import startServer

simulation: Simulation


def main():
    global simulation

    # these flags decide which mobility model will be selected for milulation linearmobility of spline mobility
    linearMobilityFlag = False
    splineMobilityFlag = True

    parser = argparse.ArgumentParser(description='Importing configuration-file')
    # parser.add_argument('--path', type=str, required=True, help='reference folder path for waypoints and plotting')
    parser.add_argument('--configuration', action='store', type=str,
                        default="examples/simpleSimulation/simulation.config", help='configuration')
    parser.add_argument('--omnetpp', action='store_true', help='Start the OmNet++ simulator')

    parser.add_argument('--show', action='store_true', help='Show the Energy as Plot')



    print(
        """AirMobiSim Simulation  (C) 2021 Chair of Networked Systems Modelling TU Dresden.\nVersion: 0.0.1\nSee the license for distribution terms and warranty disclaimer""")

    args = parser.parse_args()


    # waypointTime, waypointX, waypointY, waypointZ = load_Data()



    p = Yamlparser(args.configuration)
    config = p.readConfig()
    ####################################


    waypointTime = []
    waypointX = []
    waypointY = []
    waypointZ = []


    if splineMobilityFlag:
        # uavStartPos.clear(), uavEndPos.clear(), totalFlightTime.clear(), waypointTime.clear(), waypointX.clear(), waypointY.clear(), waypointZ.clear()


        for uavsp in config['uavsp']:
            waypointX.append(uavsp['waypointX'])
            waypointY.append(uavsp['waypointY'])
            waypointZ.append(uavsp['waypointZ'])
            waypointTime.append(uavsp['waypointTime'])

        # passing file path to load measurements
        # waypointTime, waypointX, waypointY, waypointZ = load_Data()



    ###################################
    directory = pathlib.Path(args.configuration).parent.resolve()
    initializeSimulation(config, directory, waypointTime, waypointX, waypointY, waypointZ,linearMobilityFlag,splineMobilityFlag)

    # Start the DroCI Bridge - Listen to OmNet++ incomes
    if args.show:
        result = Resultcollection()
        result.showEnergy()
    else:
        if args.omnetpp:
            print("Start the AirMobiSim Server.....")
            startServer(simulation)
        else:
            simulation.startSimulation()

    # print("here")
    # print(simulation)
            make_plot()
            print('FINISH###########################')



def initializeSimulation(config, directory, waypointTime, waypointX, waypointY, waypointZ,linearMobilityFlag,splineMobilityFlag):

    global simulation
    simulation = Simulation(config['simulation']['stepLength'],
                            config['simulation']['simTimeLimit'],
                            config['simulation']['playgroundSizeX'],
                            config['simulation']['playgroundSizeY'],
                            config['simulation']['playgroundSizeZ'],
                            config['uav'],
                            waypointTime,
                            waypointX,
                            waypointY,
                            waypointZ,
                            linearMobilityFlag,
                            splineMobilityFlag,
                            directory,
                            )



if __name__ == "__main__":
    main()
