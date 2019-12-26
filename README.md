# matrixMultiplicationGraph
A python script that plots a time vs input size graph for 3 methods to multiply matrices  
  
# Why is numpy so much faster ?
Numpy multiplies much faster than pure python by storing the values of an array using the same type and side-by-side in memory. A Python list, by contrast, contains addresses to Python objects. So python has an additional step of having to visit these memory addresses. 
  
# Why is numba.jit so much faster than pure python?
Numba is a library that enables just-in-time (JIT) compiling of Python code. It uses the LLVM tool chain to do this. Briefly, what LLVM does takes an intermediate representation of your code and compile that down to highly optimized machine code, as the code is running. Therefore it is much faster than the pure python code and even competes with the numpy multiplication
  
# OUTPUT:
![Alt text](ouput_graph.png?raw=true "Title")

  
