from proteus import *
from proteus.default_p import *
from math import *
from wigley import *
from proteus.mprans import RDLS

LevelModelType = RDLS.LevelModel
coefficients = RDLS.Coefficients(applyRedistancing=applyRedistancing,
                                 epsFact=epsFact_redistance,
                                 nModelId=1,
                                 rdModelId=3,
		                 useMetrics=useMetrics)

def getDBC_rd(x,flag):
    pass
    
dirichletConditions = {0:getDBC_rd}

if freezeLevelSet:
    if LevelModelType == RDLS.LevelModel:
        weakDirichletConditions = {0:RDLS.setZeroLSweakDirichletBCs}
    else:
        weakDirichletConditions = {0:coefficients.setZeroLSweakDirichletBCs}

class Flat_phi:
    def __init__(self):
        pass
    def uOfXT(self,x,t):
        return  ls_wave(x,t)

initialConditions  = {0:Flat_phi()}

fluxBoundaryConditions = {0:'noFlow'}

advectiveFluxBoundaryConditions =  {}

diffusiveFluxBoundaryConditions = {0:{}}
