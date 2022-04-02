""" Given an n x n binary matrix image,
    flip the image horizontally,
    then invert it, and return the resulting image."""

''' Input: image = [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]'''


def flip_img(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
        eachlist = arr[i]
        for j in range(len(eachlist)):
            eachlist[j] = eachlist[j] ^ 1
            
    return arr


image = [[1,1,0],[1,0,1],[0,0,0]]
flip_img(image)