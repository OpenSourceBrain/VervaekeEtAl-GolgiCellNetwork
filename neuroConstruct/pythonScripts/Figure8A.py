#
#
#   File to regenerate traces from Figure 8A in Vervaeke et al. 2010
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

projFile = File("../VervaekeEtAl-GolgiCellNetwork.ncx")


##############  Main settings  ##################

simConfigs = []

simConfigs.append("Default Simulation Configuration")

simDuration =           5000  # ms
simDt =                 0.05 # ms

## Note: This will only produce identical traces to Fig. 8A if the simulation
## is run over 8 processors
neuroConstructSeed =    1631914719
simulatorSeed =         2104606939
#mpiConf =               MpiSettings.LEGION_8PROC

simulators =            ["NEURON"]

varTimestepNeuron =     False

plotSims =              True
plotVoltageOnly =       True
runInBackground =       True
analyseSims =           True
verbose =               False


#############################################


print "Loading project from "+ projFile.getCanonicalPath()


simManager = nc.SimulationManager(projFile,
                                  1,
                                  verbose)

simManager.runMultipleSims(simConfigs =           simConfigs,
                           simDt =                simDt,
                           simDuration =          simDuration,
                           simulators =           simulators,
                           neuroConstructSeed =   neuroConstructSeed,
                           simulatorSeed =        simulatorSeed,
                           runInBackground =      runInBackground,
                           varTimestepNeuron =    varTimestepNeuron)

simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                      analyseSims =       analyseSims)




