import numpy as np
import skimage.measure 


def surface_normals_np(verts_function, faces_function):
    '''
    Find the normal vector in vertice with numpy.
    Parameters: 
        verts_function: array_like 
            input the array of vertice.
    
        faces_function: array_like
            input the array of faces.

    Returns:
        normals_vt_np_function
            array of normal vectors in vertice from numpy algorithm. 

    '''

    def normalize_v3(target_array):
        temp_array = np.sqrt(target_array[:,0]**2 + target_array[:,1]**2 + target_array[:,2]**2)     
        target_array[:,0] /= temp_array
        target_array[:,1] /= temp_array
        target_array[:,2] /= temp_array
        return target_array

    normals_vt_np_function = np.zeros( verts_function.shape, dtype=verts_function.dtype ) 
    tris = verts_function[faces_function] 
    n = np.cross( tris[::,1 ] - tris[::,0]  , tris[::,2 ] - tris[::,0] )

    n = normalize_v3(n)

    normals_vt_np_function[ faces_function[:,0] ] += n 
    normals_vt_np_function[ faces_function[:,1] ] += n 
    normals_vt_np_function[ faces_function[:,2] ] += n 
    normals_vt_np_function = normalize_v3(normals_vt_np_function)
    normals_vt_np_function = -normals_vt_np_function

    return normals_vt_np_function

def normals_tc(p1, p2, p3):
    Normal = np.cross(p2-p1, p3-p1)
    return Normal

def vetors_angle(vector1, vector2):

    dot_product = np.dot(vector1, vector2)
    angle = np.arccos(dot_product)

    return angle

label_train00 = np.load('cw1/task2/label_train00.npy')
verts, faces, normals_vt_sk, values = skimage.measure.marching_cubes(label_train00)

normals_tc_sk = []
normals_tc_np = []
verts_range = np.arange(0, len(verts)-2)
for i in verts_range:
    normals_tc_sk.append(normals_tc(verts[i], verts[i+1], verts[i+2]))
    normals_tc_np.append(normals_tc(verts[i], verts[i+1], verts[i+2]))

np.nan_to_num(normals_tc_sk)
np.nan_to_num(normals_tc_np)

normals_vt_np = surface_normals_np(verts, faces)

np.nan_to_num(normals_vt_np)
np.nan_to_num(normals_vt_sk)


'''
Compare the vertex normal vectors calculated from the two implementations, 
measre.marching_cubes and surface_normals_np, by calculating the mean and 
standard deviation of the angle between two vectors. 
The output is 0.20763443 and 0.17888054.
There are some differences between the vectors calculated by two methods. 
However, the differences can be condisidered as in the acceptable range.
'''
vt_normals_range = np.arange(0, len(normals_vt_np))
vt_normals_angles = []
for i in vt_normals_range:
    vt_normals_angles.append(vetors_angle(normals_vt_np[i], normals_vt_sk[i]))
mean_deviation_angles = np.mean(vt_normals_angles)
standard_deviation_angles = np.std(vt_normals_angles)

print(mean_deviation_angles)
print(standard_deviation_angles)

'''
Compare the vertices and triangle center's normal vectors 
by calculating the mean and standard deviation of the angle between two vectors. 
The output is 0.35218898 and 0.19223856.
There are some differences between the vectors calculated by two methods. 
However, the differences can be condisidered as in the acceptable range.
'''
vt_tc_normals_range = np.arange(0, len(normals_tc_np))
vt_tc_normals_angles = []
for i in vt_tc_normals_range:
    vt_tc_normals_angles.append(vetors_angle(normals_tc_np[i], normals_vt_np[i]))
mean_deviation_vt_tc_angles = np.mean(vt_tc_normals_angles)
standard_deviation_vt_tc_angles = np.std(vt_tc_normals_angles)

print(mean_deviation_vt_tc_angles)
print(standard_deviation_vt_tc_angles)

'''
When sigma become too big, the triangle can not be recognised. 
When sigma become too small, the image is not smooth enough.
As a result, sigma should be in the resonable range. 
If the threshold of recognition is sigma=0.5, the range of sigma could be 0.2-0.5.
'''

from vis import visualise_the_surface

visualise_the_surface(label_train00, normals_tc_sk, normals_vt_sk)