# Matrices (Alpha)
#### Python 3 code to create and operate on matrices
   
### Install using pip:
   
   <code>pip install MatricesM</code>
   
### Import by using:
   <code>import matrices </code>
   #### OR
   <code>from matrices import *</code>
   ##### -<a href=https://github.com/MathStuff/MatricesM/blob/master/src/matrices.py>matrices.py</a> contains Matrix class and FMatrix, CMatrix and Identity sub-classes
  
   ##### -<a href=https://github.com/MathStuff/MatricesM/blob/master/src/exampleMatrices.py>exampleMatrices.py</a> contains example matrices
   
   ##### -Check the <a href="https://github.com/semihM/Matrices/projects">project tab</a> to see the progress
-------------- 
Some examples:
--------------
##### Create matrices filled with random integers
```python 
A=Matrix(4) #Creates a 4x4 matrix filled with random integers from the default range which is [-5,5]

B=Matrix([3,5],ranged=[10,25]) #Creates a 3x5 matrix with elements ranged between 10 and 25
``` 
----------------------------------------
##### Give list of numbers to create matrices
```python 
filled_rows=[[1,2,3],[4,5,6],[7,8,9]]

C=Matrix(listed=filled_rows) #Creates a matrix with the given list of numbers

C1=Matrix(3,"1 0 -1 4 5 5 1 2 2") #Creates a 3x3 matrix from the given string

C2=Matrix([2,4],"5 -2 -3 2 1 0 0 4") #Creates a 2x4 matrix from the given string
``` 
----------------------------------------
##### Generate randomly filled matrices
```python
randomData1=FMatrix([10000,4],ranged={"height":[10,100],"weight":[200,500],"cost":[200,1000],"quality":[0,10]})

randomData2=Matrix([10000,4],ranged={"feature1":[0,25],"feature2":[100,200],"feature3":[1000,10000],"feature4":[1,100]})
```
----------------------------------------
##### Give a string filled with data and use the numbers in it to create a matrix
```python 
data="""1,K,60,69900,6325
2,K,30,79000,5200
3,E,52,85500,7825
4,E,57,17100,8375
5,E,55,5500,5450
6,E,68,27200,8550
7,E,41,20500,4500
8,E,20,69000,5050
9,K,33,13200,8325
10,E,37,31800,5975"""

D=Matrix(dim=[10,4],listed=data,features=["id","age","num1","num2") #Creates a matrix form of the given string's *integers*, dimension is *required* as [dataAmount,features]
```
##### OR

##### Read data from files (Only tested on CSV and TXT files)
###### header: boolean value, **True** if data file has a header as the **first** row, default is **False**

###### If bool(header) is True, feature names automatically get picked up from the first row
```python 
data_directory="Example\Directory\DATAFILE"
data_dim=[data_amount,feature_amount]
data_matrix=FMatrix(dim=data_dim,directory=data_directory,header=1) #Create a float matrix from a table of data
```
----------------------------------------
##### Create matrices filled with random float numbers
```python 
E=FMatrix(6) #Create a matrix filled with random float values in the default range

F=FMatrix(dim=[2,5],randomFill=0) #Fill the matrix with zeros
```
----------------------------------------
##### Create matrices filled with random complex numbers (Not 100% functional, check https://github.com/MathStuff/MatricesM/issues )
```python 
Cm1=CMatrix(5) #Create a matrix filled with random float values in the default range
```
----------------------------------------
##### Create identity matrices
```python 
i=Identity(3) #3x3 identity matrix

i.addDim(2) #Add 2 dimensions to get a 5x5 identity matrix
``` 
----------------------------------------
##### Use your matrix's methods and properties 
```python 
C.grid #Prints the matrix's elements as a grid

C.p #Print the type, dimension, column names and the grid

C.directory #Returns the directory of the matrix if there is any given

C.matrix #Returns the matrix's rows as lists in a list

C.dim #Returns the dimension of the matrix; can be used to change the dimensions, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

C.string #Returns the string form of the matrix's elements

C.features #Returns the column names if given, can also be used to set column names

C.col(n,as_matrix) #Returns nth column of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.row(n,as_matrix) #Returns nth row of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.intForm #Returns integer form of the matrix

C.floatForm #Returns integer form of the matrix

C.ceilForm #Returns a matrix of all the elements' ceiling value

C.floorForm #Returns the same matrix as "intForm"

C.roundForm(decimal=n) #Returns a matrix of elements' rounded up to n decimal digits 

C.uptri #Returns the upper triangular form of the matrix

C.lowtri #Returns the lower triangular form of the matrix

C.mean(n) #Returns the nth column's average, give None as argument to get the all columns' averages

C.ranged(n) #Returns the nth column's range, give None as argument to get the all columns' ranges

C.median(n) #Returns the nth column's median, give None to get all columns' medians

C.freq(n) #Returns the nth column's elements frequency as a dictionary where elements are keys and how often they repeat as values. If called without arguments, returns every column"s frequencies 

C.mode(n) #Returns the nth column's mode, give None to get all columns' modes

C.iqr(n,as_quartiles) #Returns the nth column's iqr, give None to get all columns' iqr values. If first,second and third quartiles is desired, give as_quartiles parameter bool(True)

C.sdev(n,population) #Returns the nth column's standard deviation, if None is given as an argument returns all columns' standard deviations. Give population parameter True if calculation is not for samples

C.variance(n,population) #Returns the nth column's variance, if None is given as an argument returns all columns' variance. Give population parameter True if calculation is not for samples

C.z(row,col) #Returns the z-scores of the desired row and/or column, call without arguments to get the all z-scores as a matrix

C.pearson_r(column_1,column_2) #Returns linear correlation of 2 columns chosen from the matrix

C.det #Returns the determinant of the matrix

C.t #Returns the transposed matrix

C.minor(m,n) #Returns the mth row's nth element's minor matrix

C.adj #Returns the adjoint matrix

C.inv #Returns the inversed matrix

C.rank #Returns the rank of the matrix

C.rrechelon #Returns the reduced row echelon form of the matrix

C.head(n) #Returns the first n rows (if there are less than n rows it returns all the rows)

C.tail(n) #Returns the last n rows (if there are less than n rows it returns all the rows)

C.concat(matrix,concat_as) #Merges a matrix to itself. concat_as is set to "row" by default; if concatenation required is as columns, give "col" as the argument

C.copy #Returns a copy of the matrix

C.summary #Returns the string form of the object 

C.setFeatures() #Can be used to fix column naming issues, sets the column names to defaults


```

----------------------------------------

##### Add or remove rows/columns and operate on them
```python 
E.add(r=3,lis=[1.0 ,2.5 ,52,242 ,-9883,212, 0.000001, -555,554]) #Make the list given the 3rd row

A.remove(c=2) #Remove the second column 

for a in A.matrix: a[0]%=2 #Change first column's values to the remainder of division by 2 

B @ B.t #Matrix multiplication example
```
----------------------------------------


##### All calculations below returns True
```python 
   A**2 == A * A
   
   A*2==A+A
   
   A.t.t==A
   
   A.lowtri@A.uptri==A
   
   A.inv.inv==A (Doesn't always work for matrices with big numbers,due to decimal rounding,but gets close estimations)
   
   A.adj.t[1][2]==A.minor(2,3).det*-1
   
   (B @ B.inv).roundForm() == Identity(B.dim[0]) # roundForm call is currently required due to %0.001 error rate on calculations 
``` 
----------------------------------------

#### More examples can be found in <a href=https://github.com/MathStuff/MatricesM/blob/master/src/exampleMatrices.py>exampleMatrices.py</a>
