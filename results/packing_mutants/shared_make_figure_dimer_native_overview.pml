@shared_make_figure_dimer.pml

set ray_shadows, 1
set surface_proximity, off

orient dimer_native_polymer 
zoom dimer_native_polymer, 4
#turn x, 180
turn y, 180

hide everything

show cartoon, dimer_native
set cartoon_transparency, 0.5

# show spheres, dimer_het

