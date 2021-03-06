from proteus import *
from proteus.default_p import *
from wavetank import *
from proteus.mprans import RANS2P

LevelModelType = RANS2P.LevelModel

if spongeLayer or levee or slopingSpongeLayer:
    coefficients = RANS2P.Coefficients(epsFact=epsFact_viscosity,
                                       sigma=0.0,
                                       rho_0 = rho_0,
                                       nu_0 = nu_0,
                                       rho_1 = rho_1,
                                       nu_1 = nu_1,
                                       g=g,
                                       nd=nd,
                                       LS_model=1,
                                       epsFact_density=epsFact_density,
                                       stokes=False,
                                       useRBLES=useRBLES,
                                       useMetrics=useMetrics,
                                       porosityTypes=porosityTypes,
                                       dragAlphaTypes=dragAlphaTypes,
                                       dragBetaTypes=dragBetaTypes,
                                       epsFact_solid = epsFact_solid)
else:
    coefficients = RANS2P.Coefficients(epsFact=epsFact_viscosity,
                                       sigma=0.0,
                                       rho_0 = rho_0,
                                       nu_0 = nu_0,
                                       rho_1 = rho_1,
                                       nu_1 = nu_1,
                                       g=g,
                                       nd=nd,
                                       LS_model=1,
                                       epsFact_density=epsFact_density,
                                       stokes=False,
                                       useRBLES=useRBLES,
                                       useMetrics=useMetrics)

def getDBC_p(x,flag):
    if flag == boundaryTags['top']:
        return outflowPressure
    elif (not rightEndClosed) and flag == boundaryTags['right']:
        return outflowPressure

def getDBC_u(x,flag):
    if flag == boundaryTags['left']:
        return twpflowVelocity_u
    elif (not rightEndClosed) and flag == boundaryTags['right']:
        return lambda x,t: outflowVelocity[0]
    elif flag == boundaryTags['top']:
        return lambda x,t: windspeed_u
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0

def getDBC_v(x,flag):
    if flag == boundaryTags['left']:
        return twpflowVelocity_v
    elif (not rightEndClosed) and flag == boundaryTags['right']:
       return lambda x,t: outflowVelocity[1]
    elif flag == boundaryTags['top']:
        return lambda x,t: windspeed_v
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0

def getDBC_w(x,flag):
    if flag == boundaryTags['left']:
        return twpflowVelocity_w
    elif (not rightEndClosed) and flag == boundaryTags['right']:
        return lambda x,t: outflowVelocity[2]
    elif flag == boundaryTags['top']:
        return lambda x,t: windspeed_w
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0

dirichletConditions = {0:getDBC_p,
                       1:getDBC_u,
                       2:getDBC_v,
                       3:getDBC_w}

def getAFBC_p(x,flag):
    if flag == boundaryTags['left']:
        return twpflowFlux
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
	    return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0
    else:
        return lambda x,t: 0.0

def getAFBC_u(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
	    return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0
    else:
        return lambda x,t: 0.0

def getAFBC_v(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
	    return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0
    else:
        return lambda x,t: 0.0

def getAFBC_w(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
	    return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return lambda x,t: 0.0
    elif flag == boundaryTags['bottom']:
        return lambda x,t: 0.0
    else:
        return lambda x,t: 0.0

def getDFBC_u(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
	    return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return None
    elif flag == boundaryTags['bottom']:
        return None
    else:
        return lambda x,t: 0.0

def getDFBC_v(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
            return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return None
    elif flag == boundaryTags['bottom']:
        return None
    else:
        return lambda x,t: 0.0

def getDFBC_w(x,flag):
    if flag == boundaryTags['left']:
        return None
    elif flag == boundaryTags['right']:
	if rightEndClosed:
	    return lambda x,t: 0.0
	else:
            return None
    elif flag == boundaryTags['top']:
        return None
    elif flag == boundaryTags['obstacle']:
        return None
    elif flag == boundaryTags['bottom']:
        return None
    else:
        return lambda x,t: 0.0

advectiveFluxBoundaryConditions =  {0:getAFBC_p,
                                    1:getAFBC_u,
                                    2:getAFBC_v,
                                    3:getAFBC_w}

diffusiveFluxBoundaryConditions = {0:{},
                                   1:{1:getDFBC_u},
                                   2:{2:getDFBC_v},
                                   3:{3:getDFBC_w}}

class P_IC:
    def uOfXT(self,x,t):
        return twpflowPressure_init(x,t)

class U_IC:
    def uOfXT(self,x,t):
        return twpflowVelocity_u_init(x,t)

class V_IC:
    def uOfXT(self,x,t):
        return twpflowVelocity_v_init(x,t)

class W_IC:
    def uOfXT(self,x,t):
        return twpflowVelocity_w_init(x,t)

initialConditions = {0:P_IC(),
                     1:U_IC(),
                     2:V_IC(),
                     3:W_IC()}

