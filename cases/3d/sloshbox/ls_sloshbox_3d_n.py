from proteus import *
from proteus.default_n import *
from ls_sloshbox_3d_p import *

if useBackwardEuler_ls:
    timeIntegration = BackwardEuler_cfl
    stepController = Min_dt_controller
    if timeOrder == 2:
        timeIntegration = VBDF
        stepController = Min_dt_cfl_controller
#    timeIntegration = BackwardEuler
#    stepController = FixedStep
else:
    timeIntegration = FLCBDF
    stepController = FLCBDF_controller_sys
    rtol_u[0] = 1.0e-2
    atol_u[0] = 1.0e-2

if useHex:
    if spaceOrder == 1:
        femSpaces = {0:C0_AffineLinearOnCubeWithNodalBasis}
    elif spaceOrder == 2:
        femSpaces = {0:C0_AffineLagrangeOnCubeWithNodalBasis}
    elementQuadrature = CubeGaussQuadrature(nd,sloshbox_quad_order)
    elementBoundaryQuadrature = CubeGaussQuadrature(nd-1,sloshbox_quad_order)
else:
    if spaceOrder == 1:
        femSpaces = {0:C0_AffineLinearOnSimplexWithNodalBasis}
    elif spaceOrder == 2:
        femSpaces = {0:C0_AffineQuadraticOnSimplexWithNodalBasis}
    elementQuadrature = SimplexGaussQuadrature(nd,sloshbox_quad_order)
    elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,sloshbox_quad_order)


subgridError = HamiltonJacobi_ASGS_opt(coefficients,nd,lag=False)#it's  linear anyway

massLumping = False

numericalFluxType = None

shockCapturing = ResGradQuad_SC(coefficients,nd,shockCapturingFactor=ls_shockCapturingFactor,lag=lag_ls_shockCapturing)

multilevelNonlinearSolver  = Newton#NLNI

levelNonlinearSolver = Newton

nonlinearSmoother = NLGaussSeidel

fullNewtonFlag = True

tolFac = 0.0

nl_atol_res = 1.0e-4#0.01*he#1.0e-4#should be linear with lagging

levelNonlinearSolverConvergenceTest='rits'
maxNonlinearIts = 2#it's linear so  if it needs more than one our linear solver i s not working

matrix = SparseMatrix

if usePETSc:
    numericalFluxType = DoNothing
    multilevelLinearSolver = KSP_petsc4py
    levelLinearSolver = KSP_petsc4py
    linear_solver_options_prefix = 'ncls_'
    linearSmoother = None
    linearSolverConvergenceTest = 'r-true'
else:
    numericalFluxType = DoNothing
    
    multilevelLinearSolver = LU
    
    levelLinearSolver = LU
   
linTolFac = 0.001

conservativeFlux = None
#if not applyCorrection:
#    auxiliaryVariables = [AuxiliaryVariables.ConservationHistoryLS("sloshbox3dnc"+`lRefinement`)]
