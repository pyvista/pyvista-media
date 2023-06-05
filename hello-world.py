from pyvista import examples
from pyvista.examples.planets import load_saturn, load_saturn_rings

saturn = load_saturn(radius=60268.0)

inner = 60268.0 + 7000.0
outer = 60268.0 + 80000.0
rings = load_saturn_rings(inner=inner, outer=outer, c_res=50)

grid = examples.load_hydrogen_orbital(3, 2, -2)

# Hello, world!

import pyvista as pv

sphere = pv.Sphere()
sphere.plot()

# We can plot the planet

plotter = pv.Plotter()
plotter.add_mesh(saturn)
plotter.add_mesh(rings)

# and the atom!

grid.plot(
    volume=True,
    opacity=[1, 0, 1],
    cmap="magma",
)
