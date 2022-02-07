import numpy as np
import skimage.measure 

label_train00 = np.load('cw1/task2/label_train00.npy')

def normals_tc(p1, p2, p3):
    Normal = np.cross(p2-p1, p3-p1)
    Normal = Normal / Normal.sum()
    return Normal

verts, faces, normals_vt_sk, values = skimage.measure.marching_cubes(label_train00)

verts_range = np.arange(0, len(verts)-2)
normals_tc_sk = []
for i in verts_range:
    normals_tc_sk.append(normals_tc(verts[i], verts[i+1], verts[i+2]))


print("normals_tc_sk= \n", normals_tc_sk)
print("normals_tc_sk.len= \n", len(normals_tc_sk))




print("verts= \n", verts)
print("verts.shape= \n", verts.shape)
print("faces= \n", faces)
print("faces.shape= \n", faces.shape)
print("normals= \n", normals_vt_sk)
print("normals.shape= \n", normals_vt_sk.shape)
print("values= \n", values)
print("values.shape= \n", values.shape)

print(len(verts), len(faces), len(normals_vt_sk), len(values))

print("________First function end________")

def normalize_v3(target_array):
    temp_array = np.sqrt(target_array[:,0]**2 + target_array[:,1]**2 + target_array[:,2]**2)     
    target_array[:,0] /= temp_array
    target_array[:,1] /= temp_array
    target_array[:,2] /= temp_array
    return target_array

#Create a zeroed array with the same type and shape as our vertices i.e., per vertex normal 
normals_vt_np = np.zeros( verts.shape, dtype=verts.dtype ) 
#Create an indexed view into the vertex array using the array of three indices for triangles 
tris = verts[faces] 
#Calculate the normal for all the triangles, by taking the cross product of the vectors v1-v0, and v2-v0 in each triangle             
n = np.cross( tris[::,1 ] - tris[::,0]  , tris[::,2 ] - tris[::,0] )

n = normalize_v3(n)

normals_vt_np[ faces[:,0] ] += n 
normals_vt_np[ faces[:,1] ] += n 
normals_vt_np[ faces[:,2] ] += n 
normals_vt_np = normalize_v3(normals_vt_np)
normals_vt_np = -normals_vt_np

# how to caculate the normals in triangle centres

print("verts= \n", verts)
print("verts.shape= \n", verts.shape)
print("faces= \n", faces)
print("faces.shape= \n", faces.shape)
print("norm= \n", normals_vt_np)
print("norm.shape= \n", normals_vt_np.shape)
