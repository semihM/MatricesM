# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from matrices import Matrix,FMatrix,Identity

# =============================================================================
"""Example Inputs"""      
# =============================================================================
projectGrid="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# =============================================================================
# Valid Matrices
# =============================================================================
o=Matrix(dim=8,randomFill=0)
b=Matrix(1)
c=Matrix(dim=[2,4],ranged=[-50,50])
d=FMatrix([4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,ranged=[-1250,1250])
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=FMatrix(4)
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid)
validStr1=Matrix(dim=[2,3],listed=" 34-52\n33a c9d88 hello\n--3-")
validStr2=Matrix(listed="312as45\ndid12,,,44\ncc352as45\ndid12,,,44\ncc3-5")
validStr3=Matrix(listed="\n\n\ndd34 5\n\n44\nn659")
validStr4=Matrix(dim=[22,3],listed="""ulke,boy,kilo,yas,cinsiyet
tr,130,30,10,e
tr,125,36,11,e
tr,135,34,10,k
tr,133,30,9,k
tr,129,38,12,e
tr,180,90,30,e
tr,190,80,25,e
tr,175,90,35,e
tr,177,60,22,k
us,185,105,33,e
us,165,55,27,k
us,155,50,44,k
us,160,58,39,k
us,162,59,41,k
us,167,62,55,k
fr,174,70,47,e
fr,193,90,23,e
fr,187,80,27,e
fr,183,88,28,e
fr,159,40,29,k
fr,164,66,32,k
fr,166,56,42,k
""",features=["Height","Weight","Age"])

# =============================================================================
# InvalidMatrices
# =============================================================================
#You have to give the matrix a valid dimension, or a list to get a dimension, or it won't be a valid matrix

#a=Matrix(0)
#v=Matrix()
#k=Matrix(dim=-1)
#l=Matrix(ranged=[0])
#m=Matrix(randomFill=1)

# =============================================================================
# Identity Matrices
# =============================================================================
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
l=[proj,o,b,c,d,e,f,g,p,q,y]
for matrix in l:
    print(matrix)
print('################################')     
# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving strings or a directory")
for matrix in [validStr1,validStr2,validStr3,validStr4]:
    print(matrix)
print('################################') 
# =============================================================================
"""PRINT THE IDENTITY MATRICES """
# =============================================================================
print('################################') 
print("Identity matrices")
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')     
# =============================================================================
"""PROPERTIES, METHODS CALLS"""   
# =============================================================================
print('################################')  
print("Attribute call outputs\n")
print('################\n')
      
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)

print('\n################\n')
      
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print(f)
print("f.delDim(4)")
print(f)
print("f.uptri.p")
f.uptri.p
print("f.lowtri.p")
f.lowtri.p
print("f-(f.lowtri@f.uptri)")
print(f-(f.lowtri@f.uptri))
print('################')
      
print("g.dim:\n",g.dim)
print("g.ranged():\n",g.ranged())
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
      
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):\n",h)
print("h.mean():",h.mean())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary:\n",j.summary)

print('\n################')
      
print("proj=proj.subM(5,15).copy:\n")
proj=proj.subM(5,15).copy
print(proj)

print('################')
      
print("p:",p)
print("p.det:\n",p.det)
print("\np.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)

print('################')
      
print("p:")
print(p)
print("p.remove(c=1) and p.remove(r=2)")
p.remove(c=1)
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print("p.sdev()")
print(p.sdev())
print('################\n')
      
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)

print("################")
      
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)

print('\n################')
      
print("id3:\n")
print(id3)

print('################')
      
print("id4:\n")
print(id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))

print('################')
      
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10))

# =============================================================================
"""OPERATIONS ON ELEMENTS"""    
# =============================================================================

print("################################")   
print("Operator examples")
print("################")
      
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))

print("################\n")
      
print(f)
print("f=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("r.remove(r=2):")
r.remove(r=2)
print(r)
print("r.rank:",r.rank)
print("\nr[0]=r[1][:]")
r[0]=r[1][:]
print(r)
print("r.rank:",r.rank)    

print("################")
      
print("for i in range(len(e.matrix)): e[i][-i-1]=99")
for i in range(len(e.matrix)):e[i][i]=99
print(e)
print("\ne+=50:")
e+=50
print(e)
print("for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:\n")
for i in range(len(e.matrix)):e[i]=[b%2 for b in e[i]]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("################")
      
print("\nf.roundForm(3)>f.roundForm(1)")
print(f.roundForm(3)>f.roundForm(1))

# =============================================================================
""" STRING MATRICES' OUTPUTS"""
# =============================================================================
print("\n################################")
print("Strings' matrices:")
print("################\n")
      
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print("validStr"+str(numb+1)+":")
    print(strings)         
    print('################')
print("")
# =============================================================================
"""Basic statistical properties"""
# =============================================================================
print("validStr4.ranged()")
print(validStr4.ranged())
print("")

print("validStr4.mean()")
print(validStr4.mean())
print("")

print("validStr4.median()")
print(validStr4.median())
print("")

print("validStr4.mode()")
print(validStr4.mode())
print("")

print("validStr4.iqr()")
print(validStr4.iqr())
print("")

print("validStr4.iqr(as_quartiles=True)")
print(validStr4.iqr(as_quartiles=True))
print("")
# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Range: {'Col 1': [1, 88], 'Col 2': [2, 98], 'Col 3': [0, 99], 'Col 4': [5, 97], 'Col 5': [2, 99], 'Col 6': [0, 94], 'Col 7': [0, 99], 'Col 8': [1, 89], 'Col 9': [0, 97], 'Col 10': [17, 97], 'Col 11': [3, 99], 'Col 12': [5, 80], 'Col 13': [0, 98], 'Col 14': [8, 88], 'Col 15': [12, 84], 'Col 16': [1, 97], 'Col 17': [4, 89], 'Col 18': [2, 93], 'Col 19': [5, 98], 'Col 20': [0, 95]}
Mean: {'Col 1': 35.8, 'Col 2': 49.85, 'Col 3': 41.65, 'Col 4': 52.2, 'Col 5': 52.7, 'Col 6': 48.6, 'Col 7': 46.4, 'Col 8': 40.3, 'Col 9': 40.3, 'Col 10': 63.9, 'Col 11': 50.75, 'Col 12': 46.6, 'Col 13': 43.6, 'Col 14': 51.85, 'Col 15': 42.75, 'Col 16': 47.1, 'Col 17': 40.75, 'Col 18': 44.6, 'Col 19': 52.6, 'Col 20': 54.4}

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 


Square matrix
Dimension: 8x8
Range: {'Col 1': [0, 0], 'Col 2': [0, 0], 'Col 3': [0, 0], 'Col 4': [0, 0], 'Col 5': [0, 0], 'Col 6': [0, 0], 'Col 7': [0, 0], 'Col 8': [0, 0]}
Mean: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0, 'Col 7': 0.0, 'Col 8': 0.0}

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 1x1
Range: {'Col 1': [0, 0]}
Mean: {'Col 1': 0.0}

0 


Dimension: 2x4
Range: {'Col 1': [-34, -22], 'Col 2': [-19, 28], 'Col 3': [-47, 11], 'Col 4': [-7, 29]}
Mean: {'Col 1': -28.0, 'Col 2': 4.5, 'Col 3': -18.0, 'Col 4': 11.0}

-22  28 -47  29 
-34 -19  11  -7 


Float Matrix
Dimension: 4x3
Range: {'Col 1': [-2.1814, 4.896], 'Col 2': [0.5439, 2.9539], 'Col 3': [-4.5229, 4.7431]}
Mean: {'Col 1': 1.3363, 'Col 2': 1.7718, 'Col 3': -0.0261}

 4.3031  2.9539  4.7431 
-2.1814  0.5439 -1.1724 
 4.8960  1.9025 -4.5229 
-1.6724  1.6871  0.8479 


Square matrix
Dimension: 8x8
Range: {'Col 1': [0, 0], 'Col 2': [0, 0], 'Col 3': [0, 0], 'Col 4': [0, 0], 'Col 5': [0, 0], 'Col 6': [0, 0], 'Col 7': [0, 0], 'Col 8': [0, 0]}
Mean: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0, 'Col 7': 0.0, 'Col 8': 0.0}

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075.9945, 759.4706], 'Col 2': [-845.7041, 1134.9966], 'Col 3': [-1091.4118, 1123.2568], 'Col 4': [-1045.8382, 1239.2187], 'Col 5': [-398.1801, 921.7467], 'Col 6': [-551.8543, 1146.8152]}
Mean: {'Col 1': 85.363, 'Col 2': 400.8076, 'Col 3': 250.3036, 'Col 4': -91.9595, 'Col 5': 323.4482, 'Col 6': 436.0397}

  574.9827   961.8092   -87.6183 -1045.8382   575.2843   227.7721 
  185.9335   -49.7724   487.8279    66.1055   119.8225  1146.8152 
   28.6117   867.7352   542.3528  -742.5873   921.7467   447.7875 
-1075.9945  -845.7041 -1091.4118  1239.2187  -398.1801   484.2901 
   39.1739  1134.9966   527.4141   949.6051   613.5237   861.4276 
  759.4706   335.7809  1123.2568 -1018.2605   108.4920  -551.8543 


Dimension: 3x6
Range: {'Col 1': [3, 4], 'Col 2': [3, 6], 'Col 3': [7, 9], 'Col 4': [5, 9], 'Col 5': [6, 10], 'Col 6': [8, 9]}
Mean: {'Col 1': 3.6667, 'Col 2': 4.0, 'Col 3': 7.6667, 'Col 4': 6.6667, 'Col 5': 7.3333, 'Col 6': 8.6667}

 4  3  9  9 10  9 
 4  6  7  5  6  9 
 3  3  7  6  6  8 


Square matrix
Dimension: 5x5
Range: {'Col 1': [7, 55], 'Col 2': [30, 90], 'Col 3': [23, 93], 'Col 4': [11, 63], 'Col 5': [10, 99]}
Mean: {'Col 1': 39.0, 'Col 2': 68.8, 'Col 3': 58.0, 'Col 4': 34.8, 'Col 5': 50.2}

55 30 34 29 16 
28 83 23 11 55 
53 75 92 17 99 
 7 90 93 63 10 
52 66 48 54 71 


Float Matrix
Square matrix
Dimension: 4x4
Range: {'Col 1': [-3.6874, 3.884], 'Col 2': [-4.4259, 2.9159], 'Col 3': [-4.8623, 3.1422], 'Col 4': [-2.9901, 2.2278]}
Mean: {'Col 1': 0.7938, 'Col 2': -0.7319, 'Col 3': -1.0723, 'Col 4': -0.4417}

-0.0307 -4.4259 -2.6375 -2.9901 
 3.0092  2.8563  0.0685  0.3905 
 3.8840  2.9159  3.1422 -1.3949 
-3.6874 -4.2739 -4.8623  2.2278 


Square matrix
Dimension: 3x3
Range: {'Col 1': [3, 8], 'Col 2': [2, 5], 'Col 3': [4, 7]}
Mean: {'Col 1': 5.3333, 'Col 2': 3.3333, 'Col 3': 5.3333}

3 5 7 
8 3 4 
5 2 5 

################################
################################
Matrices created by giving strings or a directory

Dimension: 2x3
Range: {'Col 1': [9, 34], 'Col 2': [-52, 88], 'Col 3': [-3, 33]}
Mean: {'Col 1': 21.5, 'Col 2': 18.0, 'Col 3': 15.0}

 34 -52  33 
  9  88  -3 

You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x10
Range: {'Col 1': [312, 312], 'Col 2': [45, 45], 'Col 3': [12, 12], 'Col 4': [44, 44], 'Col 5': [352, 352], 'Col 6': [45, 45], 'Col 7': [12, 12], 'Col 8': [44, 44], 'Col 9': [3, 3], 'Col 10': [-5, -5]}
Mean: {'Col 1': 312.0, 'Col 2': 45.0, 'Col 3': 12.0, 'Col 4': 44.0, 'Col 5': 352.0, 'Col 6': 45.0, 'Col 7': 12.0, 'Col 8': 44.0, 'Col 9': 3.0, 'Col 10': -5.0}

312  45  12  44 352  45  12  44   3  -5 

You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x4
Range: {'Col 1': [34, 34], 'Col 2': [5, 5], 'Col 3': [44, 44], 'Col 4': [659, 659]}
Mean: {'Col 1': 34.0, 'Col 2': 5.0, 'Col 3': 44.0, 'Col 4': 659.0}

 34   5  44 659 


Dimension: 22x3
Range: {'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}
Mean: {'Height': 163.3636, 'Weight': 62.1364, 'Age': 28.6818}

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################################
################################
Identity matrices

Identity Matrix
Dimension: 1x1

 1 


Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
################################
Attribute call outputs

################

d:

Float Matrix
Dimension: 4x3
Range: {'Col 1': [-2.1814, 4.896], 'Col 2': [0.5439, 2.9539], 'Col 3': [-4.5229, 4.7431]}
Mean: {'Col 1': 1.3363, 'Col 2': 1.7718, 'Col 3': -0.0261}

 4.3031  2.9539  4.7431 
-2.1814  0.5439 -1.1724 
 4.8960  1.9025 -4.5229 
-1.6724  1.6871  0.8479 

d.matrix:

[[4.3031, 2.9539, 4.7431], [-2.1814, 0.5439, -1.1724], [4.896, 1.9025, -4.5229], [-1.6724, 1.6871, 0.8479]]

################

f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Range: {'Col 1': [-845.7041, 961.8092], 'Col 2': [-1091.4118, 542.3528]}
Mean: {'Col 1': 233.517, 'Col 2': -37.2124}

  961.8092   -87.6183 
  -49.7724   487.8279 
  867.7352   542.3528 
 -845.7041 -1091.4118 
 


Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075.9945, 759.4706], 'Col 2': [-845.7041, 1134.9966], 'Col 3': [-1091.4118, 1123.2568], 'Col 4': [-1045.8382, 1239.2187], 'Col 5': [-398.1801, 921.7467], 'Col 6': [-551.8543, 1146.8152]}
Mean: {'Col 1': 85.363, 'Col 2': 400.8076, 'Col 3': 250.3036, 'Col 4': -91.9595, 'Col 5': 323.4482, 'Col 6': 436.0397}

  574.9827   961.8092   -87.6183 -1045.8382   575.2843   227.7721 
  185.9335   -49.7724   487.8279    66.1055   119.8225  1146.8152 
   28.6117   867.7352   542.3528  -742.5873   921.7467   447.7875 
-1075.9945  -845.7041 -1091.4118  1239.2187  -398.1801   484.2901 
   39.1739  1134.9966   527.4141   949.6051   613.5237   861.4276 
  759.4706   335.7809  1123.2568 -1018.2605   108.4920  -551.8543 

f.delDim(4)

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075.9945, 759.4706], 'Col 2': [-845.7041, 1134.9966], 'Col 3': [-1091.4118, 1123.2568], 'Col 4': [-1045.8382, 1239.2187], 'Col 5': [-398.1801, 921.7467], 'Col 6': [-551.8543, 1146.8152]}
Mean: {'Col 1': 85.363, 'Col 2': 400.8076, 'Col 3': 250.3036, 'Col 4': -91.9595, 'Col 5': 323.4482, 'Col 6': 436.0397}

  574.9827   961.8092   -87.6183 -1045.8382   575.2843   227.7721 
  185.9335   -49.7724   487.8279    66.1055   119.8225  1146.8152 
   28.6117   867.7352   542.3528  -742.5873   921.7467   447.7875 
-1075.9945  -845.7041 -1091.4118  1239.2187  -398.1801   484.2901 
   39.1739  1134.9966   527.4141   949.6051   613.5237   861.4276 
  759.4706   335.7809  1123.2568 -1018.2605   108.4920  -551.8543 

f.uptri.p

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [0, 574.9827], 'Col 2': [-360.7949, 961.8092], 'Col 3': [-87.6183, 1719.6438], 'Col 4': [-1045.8382, 404.3006], 'Col 5': [-3146.7756, 742.6669], 'Col 6': [-20019.0999, 3565.2732]}
Mean: {'Col 1': 95.8304, 'Col 2': 100.1691, 'Col 3': 358.0311, 'Col 4': -12.7628, 'Col 5': -239.8544, 'Col 6': -1939.685}

   574.9827    961.8092    -87.6183  -1045.8382    575.2843    227.7721 
     0.0000   -360.7949    516.1612    404.3006    -66.2085   1073.1600 
     0.0000      0.0000   1719.6438    228.1923    742.6669   2875.1150 
     0.0000      0.0000      0.0000    336.7687    455.9067   3565.2732 
     0.0000      0.0000      0.0000      0.0000  -3146.7756 -20019.0999 
     0.0000      0.0000      0.0000      0.0000      0.0000    639.6695 

f.lowtri.p

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1.8714, 1.3209], 'Col 2': [-2.9642, 2.5905], 'Col 3': [-0.0571, 1.1999], 'Col 4': [-1.993, 5.7769], 'Col 5': [-0.1497, 1], 'Col 6': [0, 1]}
Mean: {'Col 1': 0.1485, 'Col 2': -0.7151, 'Col 3': 0.3678, 'Col 4': 0.7973, 'Col 5': 0.1417, 'Col 6': 0.1667}

 1.0000  0.0000  0.0000  0.0000  0.0000  0.0000 
 0.3234  1.0000  0.0000  0.0000  0.0000  0.0000 
 0.0498 -2.2724  1.0000  0.0000  0.0000  0.0000 
-1.8714 -2.6447  0.0638  1.0000  0.0000  0.0000 
 0.0681 -2.9642  1.1999  5.7769  1.0000  0.0000 
 1.3209  2.5905 -0.0571 -1.9930 -0.1497  1.0000 

f-(f.lowtri@f.uptri)

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [0.0, 0.0], 'Col 2': [0.0, 0.0], 'Col 3': [0.0, 0.0], 'Col 4': [0.0, 0.0], 'Col 5': [0.0, 0.0], 'Col 6': [0.0, 0.0]}
Mean: {'Col 1': 0.0, 'Col 2': 0.0, 'Col 3': 0.0, 'Col 4': 0.0, 'Col 5': 0.0, 'Col 6': 0.0}

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 

################
g.dim:
 [3, 6]
g.ranged():
 {'Col 1': [3, 4], 'Col 2': [3, 6], 'Col 3': [7, 9], 'Col 4': [5, 9], 'Col 5': [6, 10], 'Col 6': [8, 9]}
g: 
Dimension: 3x6
Range: {'Col 1': [3, 4], 'Col 2': [3, 6], 'Col 3': [7, 9], 'Col 4': [5, 9], 'Col 5': [6, 10], 'Col 6': [8, 9]}
Mean: {'Col 1': 3.6667, 'Col 2': 4.0, 'Col 3': 7.6667, 'Col 4': 6.6667, 'Col 5': 7.3333, 'Col 6': 8.6667}

 4  3  9  9 10  9 
 4  6  7  5  6  9 
 3  3  7  6  6  8 

g.remove(3):

Dimension: 2x6
Range: {'Col 1': [4, 4], 'Col 2': [3, 6], 'Col 3': [7, 9], 'Col 4': [5, 9], 'Col 5': [6, 10], 'Col 6': [9, 9]}
Mean: {'Col 1': 4.0, 'Col 2': 4.5, 'Col 3': 8.0, 'Col 4': 7.0, 'Col 5': 8.0, 'Col 6': 9.0}

 4  3  9  9 10  9 
 4  6  7  5  6  9 

################
h=proj.subM(12,18,5,11):
 
Square matrix
Dimension: 7x7
Range: {'Col 1': [5, 97], 'Col 2': [25, 94], 'Col 3': [20, 99], 'Col 4': [7, 88], 'Col 5': [3, 55], 'Col 6': [44, 97], 'Col 7': [33, 99]}
Mean: {'Col 1': 57.1429, 'Col 2': 50.2857, 'Col 3': 49.7143, 'Col 4': 44.2857, 'Col 5': 22.2857, 'Col 6': 67.7143, 'Col 7': 69.2857}

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.mean(): {'Col 1': 57.1429, 'Col 2': 50.2857, 'Col 3': 49.7143, 'Col 4': 44.2857, 'Col 5': 22.2857, 'Col 6': 67.7143, 'Col 7': 69.2857}

h.det: 1287494735579.9985

h.rank: 7

h.rrechelon: 
Float Matrix
Square matrix
Dimension: 7x7
Range: {'Col 1': [0, 1.0], 'Col 2': [0, 1.0], 'Col 3': [0, 1.0], 'Col 4': [0, 1.0], 'Col 5': [0, 1.0], 'Col 6': [0, 1.0], 'Col 7': [0, 1.0]}
Mean: {'Col 1': 0.1429, 'Col 2': 0.1429, 'Col 3': 0.1429, 'Col 4': 0.1429, 'Col 5': 0.1429, 'Col 6': 0.1429, 'Col 7': 0.1429}

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 


h.inv:

Float Matrix
Square matrix
Dimension: 7x7
Range: {'Col 1': [-0.0195, 0.0398], 'Col 2': [-0.0745, 0.0605], 'Col 3': [-0.0501, 0.071], 'Col 4': [-0.0545, 0.063], 'Col 5': [-0.0317, 0.0197], 'Col 6': [-0.0622, 0.0471], 'Col 7': [-0.0487, 0.041]}
Mean: {'Col 1': 0.0046, 'Col 2': -0.0086, 'Col 3': 0.0091, 'Col 4': 0.0085, 'Col 5': -0.0032, 'Col 6': -0.0081, 'Col 7': -0.0052}

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0014  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Range: {'Col 1': [35, 97], 'Col 2': [25, 71], 'Col 3': [20, 99], 'Col 4': [3, 55], 'Col 5': [44, 97], 'Col 6': [33, 99]}
Mean: {'Col 1': 65.8333, 'Col 2': 43.0, 'Col 3': 50.1667, 'Col 4': 21.3333, 'Col 5': 66.8333, 'Col 6': 65.5}

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Range: {'Col 1': [4, 4], 'Col 2': [3, 6], 'Col 3': [7, 9], 'Col 4': [5, 9]}
Mean: {'Col 1': 4.0, 'Col 2': 4.5, 'Col 3': 8.0, 'Col 4': 7.0}

4 3 9 9 
4 6 7 5 
 

j.summary:
 Matrix(dim=[2, 4],listed=[[4, 3, 9, 9], [4, 6, 7, 5]],ranged=[-5, 5],randomFill=1,features=[],header=None,directory='')

################
proj=proj.subM(5,15).copy:


Dimension: 5x15
Range: {'Col 1': [8, 81], 'Col 2': [2, 70], 'Col 3': [16, 99], 'Col 4': [23, 97], 'Col 5': [4, 55], 'Col 6': [15, 81], 'Col 7': [0, 63], 'Col 8': [29, 89], 'Col 9': [0, 93], 'Col 10': [24, 92], 'Col 11': [4, 68], 'Col 12': [5, 67], 'Col 13': [1, 98], 'Col 14': [32, 88], 'Col 15': [30, 69]}
Mean: {'Col 1': 42.4, 'Col 2': 40.2, 'Col 3': 52.6, 'Col 4': 60.8, 'Col 5': 33.0, 'Col 6': 60.4, 'Col 7': 21.2, 'Col 8': 51.4, 'Col 9': 52.6, 'Col 10': 69.8, 'Col 11': 33.0, 'Col 12': 44.4, 'Col 13': 36.2, 'Col 14': 56.2, 'Col 15': 49.4}

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Range: {'Col 1': [7, 55], 'Col 2': [30, 90], 'Col 3': [23, 93], 'Col 4': [11, 63], 'Col 5': [10, 99]}
Mean: {'Col 1': 39.0, 'Col 2': 68.8, 'Col 3': 58.0, 'Col 4': 34.8, 'Col 5': 50.2}

55 30 34 29 16 
28 83 23 11 55 
53 75 92 17 99 
 7 90 93 63 10 
52 66 48 54 71 

p.det:
 1089174695.0000002

p.adj:
 
Float Matrix
Square matrix
Dimension: 5x5
Range: {'Col 1': [-17225190.0, 25951065.0], 'Col 2': [-11532603.0, 19525948.0], 'Col 3': [-11492299.0, 12641174.0], 'Col 4': [-6309650.0, 6453291.0], 'Col 5': [-10729814.0, 26334244.0]}
Mean: {'Col 1': 1201038.6, 'Col 2': -794448.4, 'Col 3': 171439.8, 'Col 4': 314898.2, 'Col 5': 3129457.2}

 25951065.0000   3473085.0000   -337365.0000  -6306965.0000  -7179830.0000 
  3037323.0000  19525948.0000  -5621371.0000   4028946.0000  -8539409.0000 
  2666323.0000 -10851882.0000  12641174.0000   6453291.0000 -10729814.0000 
 -8424328.0000 -11532603.0000 -11492299.0000   3708869.0000  26334244.0000 
-17225190.0000  -4586790.0000   5667060.0000  -6309650.0000  15762095.0000 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Range: {'Col 1': [-0.0158, 0.0238], 'Col 2': [-0.0106, 0.0179], 'Col 3': [-0.0106, 0.0116], 'Col 4': [-0.0058, 0.0059], 'Col 5': [-0.0099, 0.0242]}
Mean: {'Col 1': 0.0011, 'Col 2': -0.0007, 'Col 3': 0.0002, 'Col 4': 0.0003, 'Col 5': 0.0029}

 0.0238  0.0032 -0.0003 -0.0058 -0.0066 
 0.0028  0.0179 -0.0052  0.0037 -0.0078 
 0.0024 -0.0100  0.0116  0.0059 -0.0099 
-0.0077 -0.0106 -0.0106  0.0034  0.0242 
-0.0158 -0.0042  0.0052 -0.0058  0.0145 

################
p:

Square matrix
Dimension: 5x5
Range: {'Col 1': [7, 55], 'Col 2': [30, 90], 'Col 3': [23, 93], 'Col 4': [11, 63], 'Col 5': [10, 99]}
Mean: {'Col 1': 39.0, 'Col 2': 68.8, 'Col 3': 58.0, 'Col 4': 34.8, 'Col 5': 50.2}

55 30 34 29 16 
28 83 23 11 55 
53 75 92 17 99 
 7 90 93 63 10 
52 66 48 54 71 

p.remove(c=1) and p.remove(r=2)

Square matrix
Dimension: 4x4
Range: {'Col 1': [30, 90], 'Col 2': [34, 93], 'Col 3': [17, 63], 'Col 4': [10, 99]}
Mean: {'Col 1': 65.25, 'Col 2': 66.75, 'Col 3': 40.75, 'Col 4': 49.0}

30 34 29 16 
75 92 17 99 
90 93 63 10 
66 48 54 71 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Range: {'Col 1': [30, 90], 'Col 2': [55, 55], 'Col 3': [34, 93], 'Col 4': [17, 63], 'Col 5': [10, 99]}
Mean: {'Col 1': 65.25, 'Col 2': 55.0, 'Col 3': 66.75, 'Col 4': 40.75, 'Col 5': 49.0}

30 55 34 29 16 
75 55 92 17 99 
90 55 93 63 10 
66 55 48 54 71 

p.sdev()
{'Col 1': 25.5, 'Col 2': 0.0, 'Col 3': 30.280631873636104, 'Col 4': 21.391197566600457, 'Col 5': 43.18178628387977}
################

r: 
Dimension: 5x4
Range: {'Col 1': [16, 55], 'Col 2': [17, 99], 'Col 3': [10, 93], 'Col 4': [48, 71]}
Mean: {'Col 1': 32.8, 'Col 2': 67.6, 'Col 3': 62.2, 'Col 4': 58.8}

30 75 90 66 
55 55 55 55 
34 92 93 48 
29 17 63 54 
16 99 10 71 

p==r.t:

True
################
id2:
 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


id2.addDim(2): 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 

id2.matrix:
 [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

################
id3:


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 

################
id4:


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


id4.delDim(6):

All rows have been deleted

Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################
id4: 
Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


id4.addDim(10)):
 
Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Float Matrix
Dimension: 2x3
Range: {'Col 1': [-434.359, -39.296], 'Col 2': [-101.6489, -90.2482], 'Col 3': [-194.677, 99.99]}
Mean: {'Col 1': -236.8275, 'Col 2': -95.9485, 'Col 3': -47.3435}

-434.3590  -90.2482   99.9900 
 -39.2960 -101.6489 -194.6770 


((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Range: {'Col 1': [0.444, 0.931], 'Col 2': [0.7447, 1.3181], 'Col 3': [0.2246, 0.3175]}
Mean: {'Col 1': 0.6875, 'Col 2': 1.0314, 'Col 3': 0.2711}

0.4440 1.3181 0.3175 
0.9310 0.7447 0.2246 

################


Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075.9945, 759.4706], 'Col 2': [-845.7041, 1134.9966], 'Col 3': [-1091.4118, 1123.2568], 'Col 4': [-1045.8382, 1239.2187], 'Col 5': [-398.1801, 921.7467], 'Col 6': [-551.8543, 1146.8152]}
Mean: {'Col 1': 85.363, 'Col 2': 400.8076, 'Col 3': 250.3036, 'Col 4': -91.9595, 'Col 5': 323.4482, 'Col 6': 436.0397}

  574.9827   961.8092   -87.6183 -1045.8382   575.2843   227.7721 
  185.9335   -49.7724   487.8279    66.1055   119.8225  1146.8152 
   28.6117   867.7352   542.3528  -742.5873   921.7467   447.7875 
-1075.9945  -845.7041 -1091.4118  1239.2187  -398.1801   484.2901 
   39.1739  1134.9966   527.4141   949.6051   613.5237   861.4276 
  759.4706   335.7809  1123.2568 -1018.2605   108.4920  -551.8543 

f=f.intForm

Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075, 759], 'Col 2': [-845, 1134], 'Col 3': [-1091, 1123], 'Col 4': [-1045, 1239], 'Col 5': [-398, 921], 'Col 6': [-551, 1146]}
Mean: {'Col 1': 85.0, 'Col 2': 400.5, 'Col 3': 250.1667, 'Col 4': -91.8333, 'Col 5': 323.0, 'Col 6': 435.6667}

  574   961   -87 -1045   575   227 
  185   -49   487    66   119  1146 
   28   867   542  -742   921   447 
-1075  -845 -1091  1239  -398   484 
   39  1134   527   949   613   861 
  759   335  1123 -1018   108  -551 

f2=f.roundForm(3)

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-1075.99, 759.47], 'Col 2': [-845.7, 1135.0], 'Col 3': [-1091.41, 1123.26], 'Col 4': [-1045.84, 1239.22], 'Col 5': [-398.18, 921.75], 'Col 6': [-551.85, 1146.82]}
Mean: {'Col 1': 85.3617, 'Col 2': 400.81, 'Col 3': 250.3033, 'Col 4': -91.9583, 'Col 5': 323.4467, 'Col 6': 436.0417}

  574.9800   961.8100   -87.6200 -1045.8400   575.2800   227.7700 
  185.9300   -49.7700   487.8300    66.1100   119.8200  1146.8200 
   28.6100   867.7400   542.3500  -742.5900   921.7500   447.7900 
-1075.9900  -845.7000 -1091.4100  1239.2200  -398.1800   484.2900 
   39.1700  1135.0000   527.4100   949.6100   613.5200   861.4300 
  759.4700   335.7800  1123.2600 -1018.2600   108.4900  -551.8500 

f2-f1

Float Matrix
Square matrix
Dimension: 6x6
Range: {'Col 1': [-0.99, 0.98], 'Col 2': [-0.77, 1.0], 'Col 3': [-0.62, 0.83], 'Col 4': [-0.84, 0.61], 'Col 5': [-0.18, 0.82], 'Col 6': [-0.85, 0.82]}
Mean: {'Col 1': 0.3617, 'Col 2': 0.31, 'Col 3': 0.1367, 'Col 4': -0.125, 'Col 5': 0.4467, 'Col 6': 0.375}

 0.9800  0.8100 -0.6200 -0.8400  0.2800  0.7700 
 0.9300 -0.7700  0.8300  0.1100  0.8200  0.8200 
 0.6100  0.7400  0.3500 -0.5900  0.7500  0.7900 
-0.9900 -0.7000 -0.4100  0.2200 -0.1800  0.2900 
 0.1700  1.0000  0.4100  0.6100  0.5200  0.4300 
 0.4700  0.7800  0.2600 -0.2600  0.4900 -0.8500 

################
r.remove(r=2):

Square matrix
Dimension: 4x4
Range: {'Col 1': [16, 34], 'Col 2': [17, 99], 'Col 3': [10, 93], 'Col 4': [48, 71]}
Mean: {'Col 1': 27.25, 'Col 2': 70.75, 'Col 3': 64.0, 'Col 4': 59.75}

30 75 90 66 
34 92 93 48 
29 17 63 54 
16 99 10 71 

r.rank: 4

r[0]=r[1][:]

Square matrix
Dimension: 4x4
Range: {'Col 1': [16, 34], 'Col 2': [17, 99], 'Col 3': [10, 93], 'Col 4': [48, 71]}
Mean: {'Col 1': 28.25, 'Col 2': 75.0, 'Col 3': 64.75, 'Col 4': 55.25}

34 92 93 48 
34 92 93 48 
29 17 63 54 
16 99 10 71 

Determinant is 0, can't get lower/upper triangular matrices
r.rank: 3
################
for i in range(len(e.matrix)): e[i][-i-1]=99

Square matrix
Dimension: 8x8
Range: {'Col 1': [0, 99], 'Col 2': [0, 99], 'Col 3': [0, 99], 'Col 4': [0, 99], 'Col 5': [0, 99], 'Col 6': [0, 99], 'Col 7': [0, 99], 'Col 8': [0, 99]}
Mean: {'Col 1': 12.375, 'Col 2': 12.375, 'Col 3': 12.375, 'Col 4': 12.375, 'Col 5': 12.375, 'Col 6': 12.375, 'Col 7': 12.375, 'Col 8': 12.375}

99  0  0  0  0  0  0  0 
 0 99  0  0  0  0  0  0 
 0  0 99  0  0  0  0  0 
 0  0  0 99  0  0  0  0 
 0  0  0  0 99  0  0  0 
 0  0  0  0  0 99  0  0 
 0  0  0  0  0  0 99  0 
 0  0  0  0  0  0  0 99 


e+=50:

Square matrix
Dimension: 8x8
Range: {'Col 1': [50, 149], 'Col 2': [50, 149], 'Col 3': [50, 149], 'Col 4': [50, 149], 'Col 5': [50, 149], 'Col 6': [50, 149], 'Col 7': [50, 149], 'Col 8': [50, 149]}
Mean: {'Col 1': 62.375, 'Col 2': 62.375, 'Col 3': 62.375, 'Col 4': 62.375, 'Col 5': 62.375, 'Col 6': 62.375, 'Col 7': 62.375, 'Col 8': 62.375}

149  50  50  50  50  50  50  50 
 50 149  50  50  50  50  50  50 
 50  50 149  50  50  50  50  50 
 50  50  50 149  50  50  50  50 
 50  50  50  50 149  50  50  50 
 50  50  50  50  50 149  50  50 
 50  50  50  50  50  50 149  50 
 50  50  50  50  50  50  50 149 

for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:


Square matrix
Dimension: 8x8
Range: {'Col 1': [0, 1], 'Col 2': [0, 1], 'Col 3': [0, 1], 'Col 4': [0, 1], 'Col 5': [0, 1], 'Col 6': [0, 1], 'Col 7': [0, 1], 'Col 8': [0, 1]}
Mean: {'Col 1': 0.125, 'Col 2': 0.125, 'Col 3': 0.125, 'Col 4': 0.125, 'Col 5': 0.125, 'Col 6': 0.125, 'Col 7': 0.125, 'Col 8': 0.125}

1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 

################

c%j

Dimension: 2x4
Range: {'Col 1': [2, 2], 'Col 2': [1, 5], 'Col 3': [4, 7], 'Col 4': [2, 3]}
Mean: {'Col 1': 2.0, 'Col 2': 3.0, 'Col 3': 5.5, 'Col 4': 2.5}

2 1 7 2 
2 5 4 3 

################

f.roundForm(3)>f.roundForm(1)
False

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Range: {'Col 1': [9, 34], 'Col 2': [-52, 88], 'Col 3': [-3, 33]}
Mean: {'Col 1': 21.5, 'Col 2': 18.0, 'Col 3': 15.0}

 34 -52  33 
  9  88  -3 

################
validStr2:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x10
Range: {'Col 1': [312, 312], 'Col 2': [45, 45], 'Col 3': [12, 12], 'Col 4': [44, 44], 'Col 5': [352, 352], 'Col 6': [45, 45], 'Col 7': [12, 12], 'Col 8': [44, 44], 'Col 9': [3, 3], 'Col 10': [-5, -5]}
Mean: {'Col 1': 312.0, 'Col 2': 45.0, 'Col 3': 12.0, 'Col 4': 44.0, 'Col 5': 352.0, 'Col 6': 45.0, 'Col 7': 12.0, 'Col 8': 44.0, 'Col 9': 3.0, 'Col 10': -5.0}

312  45  12  44 352  45  12  44   3  -5 

################
validStr3:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x4
Range: {'Col 1': [34, 34], 'Col 2': [5, 5], 'Col 3': [44, 44], 'Col 4': [659, 659]}
Mean: {'Col 1': 34.0, 'Col 2': 5.0, 'Col 3': 44.0, 'Col 4': 659.0}

 34   5  44 659 

################
validStr4:

Dimension: 22x3
Range: {'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}
Mean: {'Height': 163.3636, 'Weight': 62.1364, 'Age': 28.6818}

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################

validStr4.ranged()
{'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}

validStr4.mean()
{'Height': 163.3636, 'Weight': 62.1364, 'Age': 28.6818}

validStr4.median()
{'Height': 166, 'Weight': 60, 'Age': 29}

validStr4.mode()
{'Height': {'All': 1}, 'Weight': {'90': 3}, 'Age': {'10, 27': 2}}

validStr4.iqr()
{'Height': 25, 'Weight': 40, 'Age': 17}

validStr4.iqr(as_quartiles=True)
{'Height': [155, 166, 180], 'Weight': [40, 60, 80], 'Age': [22, 29, 39]}
"""
# =============================================================================

