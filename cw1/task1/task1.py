import numpy as np

def distance_transform_np (a, voxel_dementions):
    
    '''
    original equation: distance = np.sqrt((np.square(x1-x2)) + (np.square(y1-y2)) + (np.square(z1-z2)))

    Firstly, the coordinats of 1s and 0s can be found by np.where. 
    Secondly, calculate the distance between a 1 point and all of 0 points. 
    Thirdly, take the minimal value as the distance.
    Then calculate all of the 1 points and store the distance in an 3D-array.
    Return the 3D-array.

    Parameters: 
        a: array_like 
            input the 3D volumetric binary image.
    
        voxel_dementions: array_like
            input the voxel dimensions in each axis, such as [1, 1, 1].

    Returns:
        distance_array: array_like
            a's 3D Euclidean distance transform array.
    
    '''

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

