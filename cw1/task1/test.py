'''
import numpy as np

label_train00 = np.load('label_train00.npy')
'''

'''
print(a)
print(np.ndim(a))
print(a.shape)
'''

'''
ones_in_a = np.where(a == 1)
'''

'''
print(ones_in_a)
print(np.ndim(ones_in_a))
print(ones_in_a.shape)
'''


'''
print(len(ones_in_a))
print(ones_in_a[0][10000])
'''

'''
print(len(ones_in_a[2]))

for x_value in ones_in_a[0]:
    print()

for ones_coordinates in ones_in_a[][0]:
    print()
'''

'''
ones_in_a[0][0] - zeros_in_a[0][0]   ones_in_a[1][0] - zeros_in_a[1][0]  ones_in_a[2][0] - zeros_in_a[2][0]
ones_in_a[0][0] - zeros_in_a[0][1+]   ones_in_a[1][0] - zeros_in_a[1][1+]  ones_in_a[2][0] - zeros_in_a[2][1+]
'''

'''
test_array = []
point_range = np.arange(0, len(ones_in_a[0]))
for i in point_range:
    test_array.append(i)
# print(test_array)
print(test_array[1])
print(test_array[18049])
print(np.amax(test_array))
'''

'''
print(a[8,40,58])
print(ones_in_a)
'''

'''
import numpy as np
# def distance_transform_np (a, voxel_dementions = np.array[1, 1, 1]):
def distance_transform_np (a, voxel_dementions):
    # distance = np.sqrt((np.square(x1-x2)) + (np.square(y1-y2)) + (np.square(z1-z2)))

    distance_array = a
    
    ones_in_a = np.where(a == 1)
    zeros_in_a = np.where(a == 0)

    distance_temp2 = []
    ones_range = np.arange(0, len(ones_in_a[0]))
    zeros_range = np.arange(0, len(zeros_in_a[0]))
    
    for i in ones_range:
        for j in zeros_range:
            distance_temp1 = np.sqrt((voxel_dementions[0]*(np.square(ones_in_a[0][i] - zeros_in_a[0][j])))
             + (voxel_dementions[1]*(np.square(ones_in_a[1][i] - zeros_in_a[1][j])))
             + (voxel_dementions[2]*(np.square(ones_in_a[2][i] - zeros_in_a[2][j]))))
            distance_temp2.append(distance_temp1)
        distance = np.amin(distance_temp2)
        distance_array[ones_in_a[0][i], ones_in_a[1][i], ones_in_a[2][i]] = distance
    
    return distance_array




train_array = np.load('label_train00.npy')
final_array = distance_transform_np(train_array, [0.5, 0.5, 2])

print(final_array)
print(np.ndim(final_array))
print(final_array.shape)
print("final_array[8,40,58]", final_array[8,40,58]) #0
print("final_array[8,40,59]", final_array[8,40,59]) #1*0.5=0.5
print("final_array[8,40,61]", final_array[8,40,61]) #1*2=2
print("final_array[8,40,62]", final_array[8,40,62]) #1*2=2
print("final_array[16,45,61]", final_array[16,45,61]) #? max?

'''

""" 
import numpy as np

from scipy import ndimage

label_train00 = np.load('label_train00.npy')
final_array = ndimage.distance_transform_edt(label_train00, sampling=[0.5, 0.5, 2])
print(final_array)
print(np.ndim(final_array))
print(final_array.shape)
print("final_array[8,40,58]", final_array[8,40,58]) #0
print("final_array[8,40,59]", final_array[8,40,59]) #1*0.5=0.5
print("final_array[8,40,61]", final_array[8,40,61]) #1*2=2
print("final_array[8,40,62]", final_array[8,40,62]) #1*2=2
print("final_array[16,45,61]", final_array[16,45,61]) #? max?
 """

'''
from skimage import io
skimage.io
'''