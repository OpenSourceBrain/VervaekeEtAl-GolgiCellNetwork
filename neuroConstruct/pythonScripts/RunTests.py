#
#
#   File to test current configuration of GranuleCell project.
#
#   To execute this type of file, type '..\..\..\nC.bat -python XXX.py' (Windows)
#   or '../../../nC.sh -python XXX.py' (Linux/Mac). Note: you may have to update the
#   NC_HOME and NC_MAX_MEMORY variables in nC.bat/nC.sh
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using ..\\..\\..\\nC.bat -python XXX.py' or '../../../nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc

projFile = File(os.getcwd(), "../VervaekeEtAl-GolgiCellNetwork.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("TestSimConfig")

simDt =                 0.001

simulators =            ["NEURON"]

varTimestepNeuron =     True
varTimestepTolerance =  0.00001

plotSims =              True
plotVoltageOnly =       True
runInBackground =       True
analyseSims =           True
verbose =               False

#############################################


def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading project from "+ projFile.getCanonicalPath()


    simManager = nc.SimulationManager(projFile,
                                      verbose = verbose)

    simManager.runMultipleSims(simConfigs =           simConfigs,
                               simDt =                simDt,
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron,
                               varTimestepTolerance = varTimestepTolerance)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    spikeTimesToCheck = {'CellGroup_2_0': [37.6197, 188.486, 344.911, 500.767, 655.888, 810.396, 964.435, 2047.61, 2110.95, 2199.24, 2283.86, 2367.08, 2450.04, 2533.3, 2617.19, 2701.82, 2787.27,2873.53, 2960.59, 3005.94, 3020.89, 3048.46, 3077.9, 3107.75, 3137.63, 3167.37, 3196.95, 3226.37, 3255.64, 3284.79, 3313.83, 3342.79, 3371.66, 3400.46, 3429.2, 3457.88, 3486.51, 3515.11, 3543.67, 3572.2, 3600.72, 3629.2, 3657.66, 3686.12, 3714.56, 3742.99, 3771.41, 3799.82, 3828.22, 3856.62, 3885.02, 3913.42, 3941.82, 3970.22, 3998.62, 4152.13, 4248.89, 4344.1, 4439.47, 4535.21, 4631.35, 4727.88, 4824.82, 4922.14]}
    
    spikeTimeAccuracy = 0.05

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


