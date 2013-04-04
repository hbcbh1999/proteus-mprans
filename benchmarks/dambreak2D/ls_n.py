from proteus import *
from ls_p import *

if timeDiscretization=='vbdf':
    timeIntegration = VBDF
    timeOrder=2
elif timeDiscretization=='flcbdf':
    timeIntegration = FLCBDF
else:
    timeIntegration = BackwardEuler_cfl

stepController  = Min_dt_cfl_controller

femSpaces = {0:basis}

massLumping       = False
conservativeFlux  = None
numericalFluxType = DoNothing
subgridError      = NCLS.SubgridError(coefficients,nd)
shockCapturing    = NCLS.ShockCapturing(coefficients,nd,shockCapturingFactor=ls_shockCapturingFactor,lag=ls_lag_shockCapturing)

fullNewtonFlag  = True
multilevelNonlinearSolver = Newton
levelNonlinearSolver      = Newton

nonlinearSmoother = None
linearSmoother    = None

matrix = SparseMatrix

if useOldPETSc:
    multilevelLinearSolver = PETSc
    levelLinearSolver      = PETSc
else:
    multilevelLinearSolver = KSP_petsc4py
    levelLinearSolver      = KSP_petsc4py

if useSuperlu:
    multilevelLinearSolver = LU
    levelLinearSolver      = LU

linear_solver_options_prefix = 'ncls_'
levelNonlinearSolverConvergenceTest = 'r'
linearSolverConvergenceTest         = 'r-true'

tolFac = 0.0
linTolFac = 0.0
l_atol_res = 0.001*ls_nl_atol_res
nl_atol_res = ls_nl_atol_res
useEisenstatWalker = True

maxNonlinearIts = 50
maxLineSearches = 0

