'''
import numpy as np
import skimage.measure 

label_train00 = np.load('label_train00.npy')

verts, faces, normals, values = skimage.measure.marching_cubes(label_train00)

print("verts= \n", verts)
print("verts.shape= \n", verts.shape)
print("faces= \n", faces)
print("faces.shape= \n", faces.shape)
print("normals= \n", normals)
print("normals.shape= \n", normals.shape)
print("values= \n", values)
print("values.shape= \n", values.shape)

print(len(verts), len(faces), len(normals), len(values))

print("________First function end________")

def normalize_v3(target_array):
    array_temp = np.sqrt(target_array[:,0]**2 + target_array[:,1]**2 + target_array[:,2]**2)     
    target_array[:,0] /= array_temp
    target_array[:,1] /= array_temp
    target_array[:,2] /= array_temp
    return target_array

#Create a zeroed array with the same type and shape as our vertices i.e., per vertex normal 
norm = np.zeros( verts.shape, dtype=verts.dtype ) 
#Create an indexed view into the vertex array using the array of three indices for triangles 
tris = verts[faces] 
#Calculate the normal for all the triangles, by taking the cross product of the vectors v1-v0, and v2-v0 in each triangle             
n = np.cross( tris[::,1 ] - tris[::,0]  , tris[::,2 ] - tris[::,0] )

n = normalize_v3(n)

norm[ faces[:,0] ] += n 
norm[ faces[:,1] ] += n 
norm[ faces[:,2] ] += n 
norm = normalize_v3(norm)
norm = -norm

print("verts= \n", verts)
print("verts.shape= \n", verts.shape)
print("faces= \n", faces) # may not be the same as above faces
print("faces.shape= \n", faces.shape)
print("norm= \n", norm)
print("norm.shape= \n", norm.shape)

'''