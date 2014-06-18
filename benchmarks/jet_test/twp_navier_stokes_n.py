from proteus import *
from twp_navier_stokes_p import *
from jet_test3D import *

timeIntegration = BackwardEuler_cfl
stepController  = Min_dt_controller

femSpaces = {0:basis,
	     1:basis,
	     2:basis,
             3:basis}

massLumping       = False
numericalFluxType = None
conservativeFlux  = None

numericalFluxType = RANS2P.NumericalFlux
subgridError = RANS2P.SubgridError(coefficients,nd,lag=ns_lag_subgridError,hFactor=hFactor)
shockCapturing = RANS2P.ShockCapturing(coefficients,nd,ns_shockCapturingFactor,lag=ns_lag_shockCapturing)

fullNewtonFlag = True
multilevelNonlinearSolver = NewtonNS
levelNonlinearSolver      = NewtonNS

nonlinearSmoother = None
linearSmoother    = SimpleNavierStokes2D

matrix = SparseMatrix

if not use_petsc4py:
    multilevelLinearSolver = LU
    levelLinearSolver      = LU
else:
    multilevelLinearSolver = KSP_petsc4py
    levelLinearSolver      = KSP_petsc4py

linear_solver_options_prefix = 'rans2p_'
levelNonlinearSolverConvergenceTest = 'r'
linearSolverConvergenceTest             = 'r-true'

tolFac = 0.0
l_atol_res = 0.001*ns_nl_atol_res
nl_atol_res = ns_nl_atol_res
useEisenstatWalker = True
maxNonlinearIts = 50
maxLineSearches = 0
