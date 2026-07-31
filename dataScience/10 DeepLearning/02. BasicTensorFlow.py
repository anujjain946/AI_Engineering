#Import tensorflow and keras
import tensorflow as tf

old_task =  False 

if old_task :
    ### Task 1

    # 1. check if CPU is available
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))  

    # 2. check if GPU is available
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

    #3.Print TensorFlow version
    print("TensorFlow Version: ", tf.__version__)



    ### Task 2
    #4.Create Scalar, Vector, Matrix, 3D Tensor
    scalar = tf.constant(5)
    print("Scalar: ", scalar)

    vector = tf.constant([1, 2, 3])
    print("Vector: ", vector)

    matrix = tf.constant([[1, 2], [3, 4]])
    print("Matrix: ", matrix)

    tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("3D Tensor: ", tensor_3d)

    #5.Print shape and dtype
    print("Shape of Scalar: ", scalar.shape, "Dtype: ", scalar.dtype)
    print("Shape of Vector: ", vector.shape, "Dtype: ", vector.dtype)
    print("Shape of Matrix: ", matrix.shape, "Dtype: ", matrix.dtype)
    print("Shape of 3D Tensor: ", tensor_3d.shape, "Dtype: ", tensor_3d.dtype)


    ### Task 3
    '''
    * Tensor Operations

    * Addition
    * Subtraction
    * Multiplication
    * Division
    '''

    a = tf.constant(50)
    b = tf.constant(10)

    print("Addition: ", tf.add(a, b))
    print("Subtraction: ", tf.subtract(a, b))
    print("Multiplication: ", tf.multiply(a, b))
    print("Division: ", tf.divide(a, b))


    ### Task 4

    '''
    * Tensor Functions

    * `tf.ones()`
    * `tf.zeros()`
    * `tf.random.normal()`
    * `tf.random.uniform()`
    '''

    print("Ones Tensor: ", tf.ones((2, 3)))
    print("Zeros Tensor: ", tf.zeros((2, 3)))
    print("Random Normal Tensor: ", tf.random.normal((2, 3)))
    print("Random Uniform Tensor: ", tf.random.uniform((2, 3), minval=0, maxval=10))


    #### Task 5
    '''
    * Tensor ↔ NumPy conversion
    '''

    import numpy as np

    a = tf.constant([[1, 2], [3, 4]])
    # Tensor to NumPy
    numpy_array = a.numpy()
    print("Tensor to NumPy: ", numpy_array)

    # NumPy to Tensor
    numpy_array = np.array([[5, 6], [7, 8]])
    tensor_from_numpy = tf.convert_to_tensor(numpy_array)
    print("NumPy to Tensor: ", tensor_from_numpy)

    ### Task 6

    '''
    * tf.Variable
    * assign()
    * assign_add()
    '''

    str_var = tf.Variable("50")
    print(str_var)


    w = tf.Variable(10)

    print("Before:", w.numpy())

    w.assign(25)

    print("After:", w.numpy())




'''
### Task 7

* Reshape
* Expand Dims
* Squeeze
'''
x = tf.constant([1,2,3,4,5,6])
print(x.shape)
y = tf.reshape(x,(2,3))
print(y)
print(y.shape)



x = tf.constant([1,2,3])

print(x.shape)

y = tf.expand_dims(x, axis=0)

print(y)
print(y.shape)