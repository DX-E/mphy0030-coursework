import numpy as np
import pyvista as pv # in requirement.txt: pip install pyvista
from pyvista import examples
import SimpleITK as sitk # in requirement.txt: pip install SimpleITK


image_id = sitk.ReadImage("image.nii.gz", imageIO="NiftiImageIO")
image = sitk.GetArrayFromImage(image_id)
vox_dims = image_id.GetSpacing()



image_list = np.ndarray.tostring(image)
image_string = ' '.join(image_list) 
mesh = image

# Create vector
vec = np.random.rand(3)
# Normalize the vector
normal = vec / np.linalg.norm(vec)

# Make points along that vector for the extent of your slices
a = mesh.center + normal * mesh.length / 3.0
b = mesh.center - normal * mesh.length / 3.0

# Define the line/points for the slices
n_slices = 5
line = pv.Line(a, b, n_slices)

# Generate all of the slices
slices = pv.MultiBlock()
for point in line.points:
    slices.append(mesh.slice(normal=normal, origin=point))



p = pv.Plotter()
p.add_mesh(mesh.outline(), color="k")
p.add_mesh(slices, opacity=0.75)
p.add_mesh(line, color="red", line_width=5)
p.show()
