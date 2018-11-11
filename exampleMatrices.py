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

#Valid Matrices
proj=Matrix(listed=projectGrid)
v=Matrix()
o=Matrix(dim=8,randomFill=0)
a=Matrix(0)
b=Matrix(1)
c=Matrix(dim=[2,4])
d=Matrix(dim=[4,3])
e=Matrix(8,randomFill=0)
f=Matrix(dim=6,inRange=[-1250,1250])
g=Matrix(dim=[3,6])
p=Matrix(5,inRange=[0,100])
q=FMatrix(4)
#String inputs Matrices
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
""")

#InvalidMatrices
k=Matrix(dim=-1)
l=Matrix(inRange=[0])
m=Matrix(inRange=[0,0],rangeLock=1)

#Identity Matrices
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
for matrix in [proj,v,o,a,b,validStr1,validStr2,validStr3,validStr4,c,d,e,f,g,p,q,k,l,m]:
    print(matrix)
 
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')
print("Attribute call outputs\n")
print("d.matix:\n",d.matrix,"\n")
print('################')
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print('################')
print("proj.dim:\n",proj.dim,"\n")
print('################')
print("validStr2.inRange:\n",validStr2.inRange,"\n")
print('################')
print("e.matrix:\n",e.matrix,"\n")
print('################')
print("f.avg:\n",f.avg,"\n")
print('################')
print("g:\n",g)
print('################')
print("g.delRC(3):\n")
g.delRC(3)
print(g)
print('################')
h=proj.subM(12,18,5,11)
print("h=proj.Msub(12,18,5,11):\n",h,"\n")
print("h.det:\n")
print(h.det)
print("\nh.inv:")
print(h.inv)
print('################')
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary\n",j.summary)
print('################')
print("Only give 1 argument, row/column! Or it will return an error like so")
print("proj.delRC(5,15):\n")
print(proj.delRC(5,15))
print('################')
print("p:",p)
print("p.det:\n",p.det)
print("p.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)
print('################')
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)
print("################")
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)
print('################')
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
print("################################")
print("Operator examples")
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("################")
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))
print("################")
print("\ne+50:")
print(e+50)
print("################")
print("\nc%j")
print(c%j)
print("################")
print("\na<b")
print(a<b)
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print('################')
    print("validStr",numb,":\n")
    print(strings)         
    print('################')
print("")
# =============================================================================
""" Expected Outputs """
# =============================================================================
"""

Square matrix
Dimension: 20x20
Numbers' range: [0, 99]
Average: 47

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
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67  4 


Square matrix
Dimension: 0x0
Numbers' range: [0, 0]
Average: None



Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 0x0
Numbers' range: [0, 0]
Average: None



Square matrix
Dimension: 1x1
Numbers' range: [-108, -108]
Average: -108

-108 


Dimension: 2x3
Numbers' range: [-52, 88]
Average: 18

 34 -52  33 
  9  88  -3 


Dimension: 1x10
Numbers' range: [-5, 352]
Average: 86

312  45  12  44 352  45  12  44   3  -5 


Dimension: 4x1
Numbers' range: [5, 65]
Average: 37

34 
 5 
44 
65 


Dimension: 22x3
Numbers' range: [9, 193]
Average: 84

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


Dimension: 2x4
Numbers' range: [-122, 109]
Average: -11

   2  109   51   36 
 -65   19 -118 -122 


Dimension: 4x3
Numbers' range: [-114, 105]
Average: -14

-114 -110  105 
  37   93  -20 
  68  -77 -107 
 -92   44   12 


Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 6x6
Numbers' range: [-1202, 1246]
Average: 21

  770   963   612   326   497 -1019 
-1182  -745   981   -46   375   -10 
 -470   -39   627  1246  -355   339 
  587   579   147  -145   463 -1162 
  -29 -1202   -30  -954  -594   388 
 -411  1013   579  -761  -538   -41 


Dimension: 3x6
Numbers' range: [-89, 118]
Average: 5

-71  53 -10 -33  65 -89 
118  12  84 -82 -68  88 
-66 110  53 -83 -86 112 


Square matrix
Dimension: 5x5
Numbers' range: [1, 100]
Average: 49

 88  61  60  12  64 
  4  72  66  40 100 
 18  94  76  17  91 
 68  73  11   1  28 
 17  57  62  32  15 


Square matrix
Dimension: 4x4
Numbers' range: [-105.2419, 70.0531]
Average: -13.700312500000003

  63.9834   70.0531  -35.2038  -32.6773 
  -2.6909  -94.0133   23.4622   13.2004 
   1.4931  -28.5788   -5.9082  -20.5926 
 -35.4233  -22.1851   -8.8820 -105.2419 

Invalid matrix

Invalid matrix

Invalid matrix


Identity Matrix
Dimension: 1x1

1 


Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0

1 0 0 
0 1 0 
0 0 1 


Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 

################################
Attribute call outputs

d.matix:
 [[-114, -110, 105], [37, 93, -20], [68, -77, -107], [-92, 44, 12]] 

################
f.subM(1,4,2,3):
 
Dimension: 4x2
Numbers' range: [-745, 981]
Average: 390

 963  612 
-745  981 
 -39  627 
 579  147 
 

################
proj.dim:
 [20, 20] 

################
validStr2.inRange:
 [-5, 352] 

################
e.matrix:
 [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]] 

################
f.avg:
 21 

################
g:
 
Dimension: 3x6
Numbers' range: [-89, 118]
Average: 5

-71  53 -10 -33  65 -89 
118  12  84 -82 -68  88 
-66 110  53 -83 -86 112 

################
g.delRC(3):


Dimension: 2x6
Numbers' range: [-89, 118]
Average: 5

-71  53 -10 -33  65 -89 
118  12  84 -82 -68  88 

################
h=proj.Msub(12,18,5,11):
 
Square matrix
Dimension: 7x7
Numbers' range: [3, 99]
Average: 51

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 
 

h.det:

1287494735580

h.inv:
Can't multiply

Square matrix
Dimension: 7x7
Numbers' range: [-104.9712, 101.583]
Average: -4.588628571428572

 -19.6440   -1.0518   -4.1094   22.0606  -62.8314   -6.9522  -15.4500 
  -2.2642   75.9250   40.9296  -83.2787    -0.2337    4.7196   22.5496 
   7.1989    4.9490  -54.8512  -48.4458  -54.7128  -67.6493   38.7574 
  41.8996  -81.7292   64.7852   16.5944  -12.6029   14.7660   -4.4974 
 -18.2623   26.5056   17.0883   36.9030    9.7586   -8.5954   96.3355 
 -85.8213  -11.7958   -6.6484   -7.0298    9.5234    2.7309 -104.9712 
 -15.3688  101.5830  -13.9207  -78.2215  -14.7989   16.8381  -11.5060 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: [-82, 118]
Average: 8

-71  53 -10 -33 
118  12  84 -82 
 

j.summary
 Matrix(dim=[2, 4],listed=[[-71, 53, -10, -33], [118, 12, 84, -82]],inRange=[-82, 118],rangeLock=0,randomFill=1)
################
Only give 1 argument, row/column! Or it will return an error like so
proj.delRC(5,15):

Bad arguments
None
################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [1, 100]
Average: 49

 88  61  60  12  64 
  4  72  66  40 100 
 18  94  76  17  91 
 68  73  11   1  28 
 17  57  62  32  15 

p.det:
 697331838
p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-25040648, 21168567]
Average: 696531

  7992620    790083  -6988162   1796954   -328530 
 -9552386  -2153424   5412208  10286632   3077232 
  7092372 -10910781   9896712 -12685680   6117636 
 -2279666  21168567 -25040648   6008134   9300876 
  2788914   7225869   -132834  -1508958  -9960456 

p.inv:

Can't multiply

Square matrix
Dimension: 5x5
Numbers' range: [-28.4946, 90.3125]
Average: 19.100111999999996

 32.7688  12.7941  14.3808   8.9398  85.5830 
 -5.1836   4.3977  54.0112   7.2807 -28.4946 
 21.1088  15.4475  59.5122   1.5819 -22.7052 
 13.3023 -11.8571  26.2729   8.0292 -14.5692 
 90.3125  -4.0462  16.2288  49.2258  43.1807 

################
r: 
Square matrix
Dimension: 5x5
Numbers' range: [1, 100]
Average: 49

 88   4  18  68  17 
 61  72  94  73  57 
 60  66  76  11  62 
 12  40  17   1  32 
 64 100  91  28  15 

p==r.t:

Same dimension
Same average
All the elements and their positions are same!
True
################
id2:
 
Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


id2.addDim(2): 
Identity Matrix
Dimension: 7x7

1 0 0 0 0 0 0 
0 1 0 0 0 0 0 
0 0 1 0 0 0 0 
0 0 0 1 0 0 0 
0 0 0 0 1 0 0 
0 0 0 0 0 1 0 
0 0 0 0 0 0 1 

id2.matrix:
 [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
################
id3:


Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0

1 0 0 
0 1 0 
0 0 1 

################
id4:


Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 


id4.delDim(6):

All rows have been deleted

Identity Matrix
Dimension: 0x0


################
id4: 
Identity Matrix
Dimension: 0x0



id4.addDim(10)):
 
Identity Matrix
Dimension: 10x10

1 0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 
0 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 1 

################################
Operator examples

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Dimension: 2x3
Numbers' range: [-6995, 12635]
Average: 5407

 3961  7574 -6995 
11313 12635  3957 

################

((((mMulti)+125)**3)%2):

Dimension: 2x3
Numbers' range: [0, 1]
Average: 0

0 1 0 
0 0 0 

################

e+50:

Square matrix
Dimension: 8x8
Numbers' range: [50, 50]
Average: 50

50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 

################

c%j

Dimension: 2x4
Numbers' range: [-69, 53]
Average: -5

-69   3  -9 -30 
 53   7  50 -40 

################

a<b
Lower dimension!
True
################
validStr 0 :


Dimension: 2x3
Numbers' range: [-52, 88]
Average: 18

 34 -52  33 
  9  88  -3 

################
################
validStr 1 :


Dimension: 1x10
Numbers' range: [-5, 352]
Average: 86

312  45  12  44 352  45  12  44   3  -5 

################
################
validStr 2 :


Dimension: 4x1
Numbers' range: [5, 65]
Average: 37

34 
 5 
44 
65 

################
################
validStr 3 :


Dimension: 22x3
Numbers' range: [9, 193]
Average: 84

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
"""
# =============================================================================

