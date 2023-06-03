
# Hello world of PyVista

import pyvista as pv

sphere = pv.Sphere()
sphere.plot()

# or

plotter = pv.Plotter()
plotter.add_mesh(sphere)
plotter.show()

# You can save image

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(sphere)
plotter.screenshot(
    "img/hello-world.png"
)

# You can get image

import pyvista as pv
from pyvista import examples
from pyvista.examples.planets import load_saturn, load_saturn_rings

# Load Saturn
saturn = load_saturn(
    radius=60268.0
)

# Load Saturn's rings
inner = 60268.0 + 7000.0
outer = 60268.0 + 80000.0
rings = load_saturn_rings(
    inner=inner,
    outer=outer,
    c_res=50
)

# We can plot planet.

plotter = pv.Plotter()
plotter.add_mesh(saturn)
plotter.add_mesh(rings)
plotter.show()
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(saturn)
plotter.add_mesh(rings)
cubemap = examples.download_cubemap_space_16k()
_ = plotter.add_actor(cubemap.to_skybox())
plotter.set_environment_texture(cubemap, True)
plotter.screenshot("img/saturn.png")

from pyvista import examples
grid = examples.load_hydrogen_orbital(3, 2, -2)

# And also can plot atoms!

grid.plot(
    volume=True,
    opacity=[1, 0, 1],
    cmap='magma',
)
plotter = pv.Plotter(off_screen=True)
plotter.add_volume(grid, opacity=[1, 0, 1], cmap='magma')
plotter.screenshot("img/atom.png")
