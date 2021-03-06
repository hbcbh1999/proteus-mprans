from proteus import *
from proteus.default_n import *
from twp_navier_stokes_beach_erosion_board_waves_3d_p import *
from beach_erosion_board_waves_3d import *

if useBackwardEuler:
#    timeIntegration = BackwardEuler
#    stepController  = FixedStep
    timeIntegration = BackwardEuler_cfl
    stepController = Min_dt_controller
else:
    timeIntegration = FLCBDF
    stepController = FLCBDF_controller_sys
    stepController = FLCBDF_controller
    rtol_u[1] = 1.0e-2
    rtol_u[2] = 1.0e-2
    atol_u[1] = 1.0e-2#1.0e-3
    atol_u[2] = 1.0e-2#1.0e-3

noPressureStabilization=False
if spaceOrder==1:
    femSpaces = {0:C0_AffineLinearOnSimplexWithNodalBasis,
                 1:C0_AffineLinearOnSimplexWithNodalBasis,
                 2:C0_AffineLinearOnSimplexWithNodalBasis,
                 3:C0_AffineLinearOnSimplexWithNodalBasis}
    hFactor=1.0
if spaceOrder==2:
    femSpaces = {0:C0_AffineQuadraticOnSimplexWithNodalBasis,
                 1:C0_AffineQuadraticOnSimplexWithNodalBasis,
                 2:C0_AffineQuadraticOnSimplexWithNodalBasis,
                 3:C0_AffineQuadraticOnSimplexWithNodalBasis}
    hFactor=0.5
elementQuadrature = SimplexGaussQuadrature(nd,sloshbox_quad_order)

elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,sloshbox_quad_order)

if LevelModelType == VANS2P.OneLevelVANS2P:
    subgridError = NavierStokesASGS_velocity_pressure_opt(coefficients,nd,lag=lag_ns_subgridError,delayLagSteps=2,hFactor=hFactor,noPressureStabilization=noPressureStabilization)
elif LevelModelType == VRANS2P.LevelModel:#RANS2P.LevelModel:#RANS2PV2.OneLevelRANS2PV2:
    subgridError = NavierStokesASGS_velocity_pressure_optV2(coefficients,nd,lag=lag_ns_subgridError,delayLagSteps=2,hFactor=hFactor,noPressureStabilization=noPressureStabilization)
else:
    subgridError = NavierStokesASGS_velocity_pressure(coefficients,nd,lag=lag_ns_subgridError,delayLagSteps=2,hFactor=hFactor,noPressureStabilization=noPressureStabilization)
    if useSpongeLayer == True:
        subgridError = NavierStokesWithBodyForceASGS_velocity_pressure(coefficients,nd,lag=lag_ns_subgridError,delayLagSteps=2,hFactor=hFactor,noPressureStabilization=noPressureStabilization)
massLumping = False

shockCapturing = None
if LevelModelType == VANS2P.OneLevelVANS2P:
    shockCapturing = NavierStokes_SC_opt(coefficients,nd,ns_shockCapturingFactor,lag=True)
elif LevelModelType == VRANS2P.LevelModel:#RANS2P.LevelModel:#RANS2PV2.OneLevelRANS2PV2:
    shockCapturing = NavierStokes_SC_opt(coefficients,nd,ns_shockCapturingFactor,lag=True)
else:
    shockCapturing = NavierStokes_SC(coefficients,nd,ns_shockCapturingFactor,lag=True)

numericalFluxType = None

multilevelNonlinearSolver  = NLNI

levelNonlinearSolver = Newton

nonlinearSmoother = NLGaussSeidel

fullNewtonFlag = True

maxNonlinearIts = 40#10
maxLineSearches =10

tolFac = 0.0#0.01

nl_atol_res = 1.0e-5#mwf hack 1.0e-6

matrix = SparseMatrix

#stick with weak bcs?
#numericalFluxType = NavierStokes_Advection_DiagonalUpwind_Diffusion_IIPG_exterior #need weak for parallel and global conservation

if usePETSc:    
    numericalFluxType = NavierStokes_Advection_DiagonalUpwind_Diffusion_IIPG_exterior #need weak for parallel and global conservation
    #numericalFluxType = NavierStokes_Advection_DiagonalUpwind_Diffusion_SIPG_exterior #need weak for parallel and global conservation
    multilevelLinearSolver = PETSc
    
    levelLinearSolver = PETSc
    parallelPartitioningType = partitioningType#MeshParallelPartitioningTypes.node
    nLayersOfOverlapForParallel = nOverlap#2
else:
    numericalFluxType = NavierStokes_Advection_DiagonalUpwind_Diffusion_IIPG_exterior #need weak for parallel and global conservation
    multilevelLinearSolver = LU
    
    levelLinearSolver = LU
    
conservativeFlux = None
linearSmoother = GaussSeidel

linTolFac = 1.0e-8

#if useVANS2P:
#    conservativeFlux = None
#else:
#conservativeFlux = {0:'pwl'}

