#Question 6
#Assuming you are given an image as a two dimensional array of shape 28 x 28. Write a small piece of python code to reshape this image to a vector of  length 784 (=28 x 28).
#Hint: This can be a one-liner.

import numpy as np
def reshape(x):
  """return x_reshaped as a flattened vector of the multi-dimensional array x"""
  
  x_reshaped = x.flatten() #간단하네 
  return x_reshaped