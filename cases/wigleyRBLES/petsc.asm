-rans2p_ksp_type bcgsl -rans2p_pc_type asm     -rans2p_ksp_rtol 1.0e-3 -rans2p_ksp_max_it 175 -rans2p_ksp_gmres_modifiedgramschmidt
-ncls_ksp_type   bcgsl -ncls_pc_type   bjacobi -ncls_ksp_rtol   1.0e-3 -ncls_ksp_max_it   175 -ncls_ksp_gmres_modifiedgramschmidt
-vof_ksp_type    bcgsl -vof_pc_type    bjacobi -vof_ksp_rtol    1.0e-3 -vof_ksp_max_it    175 -vof_ksp_gmres_modifiedgramschmidt
-rdls_ksp_type   bcgsl -rdls_pc_type   bjacobi -rdls_ksp_rtol   1.0e-3 -rdls_ksp_max_it   175 -rdls_ksp_gmres_modifiedgramschmidt
-mcorr_ksp_type  cg    -mcorr_pc_type  bjacobi -mcorr_ksp_rtol  1.0e-8 -mcorr_ksp_max_it  175 -mcorr_ksp_gmres_modifiedgramschmidt

-rans2p_pc_asm_type basic
