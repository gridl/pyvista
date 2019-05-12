"""
Parallel Files
~~~~~~~~~~~~~~

The VTK library supports parallel file foramts. Reading meshes broken up into
several files is natively supported by VTK and PyVista
"""
# sphinx_gallery_thumbnail_number = 1
import pyvista
from pyvista import examples
import os

################################################################################
# Let's go ahead and download the sample dataset containing an
# :class:`pyvista.UnstructuredGrid` broken up into several files.

# Do not capture output because we'll demo how to read the file
examples.download_blood_vessels()

################################################################################
# The above code downloaded a dataset containing a set of parallel files for a
# blood vessel mesh and returned an :class:`pyvista.UnstructuredGrid` - we did not
# grab that UnstructuredGrid, so that we could demo how to use these types of
# files.
#
# Let's inspect where this downloaded our dataset:
path = os.path.join(pyvista.EXAMPLES_PATH, 'blood_vessels')
print(os.listdir(path))

################################################################################
print(os.listdir(os.path.join(path, 'T0000000500')))

################################################################################
# Note that a ``.pvtu`` file is available along side a directory. This directory
# contains all the parallel files or pieces that make the whole mesh. We can
# simply read the ``.pvtu`` file and VTK will handle putting the mesh together.
filename = os.path.join(path, 'T0000000500.pvtu')
mesh = pyvista.read(filename)
print(mesh)

################################################################################
# Plot the pieced together mesh
mesh.plot(scalars='node_value', categories=True)


################################################################################
mesh.plot(scalars='density')