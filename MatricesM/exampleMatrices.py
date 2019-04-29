# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from MatricesM.matrix import Matrix
from MatricesM.constructors.matrices import Identity
try:
    plotting=bool(int(input("Enable plotting ?(0/1) (Requires matplotlib)")))
except:
    plotting=0
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
o=Matrix(8,fill=0)
b=Matrix(1)
c=Matrix(dim=[2,4],ranged=[-50,50])
d=Matrix([4,3],dtype="float")
e=Matrix(8,fill="gauss",ranged=[0,3])
f=Matrix(dim=6,ranged=[-1250,1250],dtype="float")
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=Matrix(4,dtype="float")
q1=Matrix(9,decimal=2,dtype="float")
q2=Matrix(6,decimal=6,dtype="float")
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
c1=Matrix(5,dtype="complex")
c2=Matrix([7,3],ranged=[-10,10],dtype="complex")
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid,dtype="integer")
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
# Identity Matrices
# =============================================================================
id1=Matrix(listed=Identity())
id2=Matrix(listed=Identity(5))
id3=id2[:3,:3]
id4=Matrix(listed=Identity(6))

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
l=[proj,o,b,c,d,e,f,g,p,q,q1,q2,y,c1,c2]
for matrix in l:
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
      
print("f[:4,1:3]:\n",f[:4,1:3],"\n")
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
print("q1.decimal",q1.decimal)
q1.p
print("q1.decimal=5")
q1.decimal=5
q1.p
print('################')      
h=proj[11:18,4:11]
print("h=proj[11:18,4:11]:\n",h)
print("h.mean():",h.mean())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g[:2,:4]
print("j=g.[:2,:4]:\n",j,"\n")
print("j.obj:\n",j.obj)

print('\n################')
      
print("proj=proj[:5,:15]:\n")
proj=proj[:5,:15]
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
print("p.remove(col=1) and p.remove(row=2)")
p.remove(col=1)
p.remove(row=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print("p.sdev()")
print(p.sdev())

print('################\n')

print("proj.find(40)")
print(proj.find(40))
print("\nproj.find(40,0)")
print(proj.find(40,0))
print("\nproj.find(111)")
proj.find(111)

print("################\n")

print("r=p.t")
r=p.t
print("r.remove(row=2):")
r.remove(row=2)
print(r)
print("r.rank:",r.rank)
print("\nr.matrix[0]=r.matrix[1][:]")
r.matrix[0]=r.matrix[1][:]
print(r)
print("r.rank:",r.rank)    

      
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
      
print("f:\n",f)
print("f1=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("e+=Matrix(listed=Identity(e.dim[0]))*99")
e+=Matrix(listed=Identity(e.dim[0]))*99
print(e)
print("\ne-=33:")
e-=33
print(e)
print("\ne+=Matrix(e.dim):")
e+=Matrix(e.dim,dtype="float")
print(e)
print("\ne*=[2,1,1,0.5,0.2,0.0003,1,3]:")
e*=[2,1,1,0.5,0.2,0.0003,1,3]
print(e)
print("e%=[2,2,2,2,1,1,1,1]")
e%=[5,5,5,5,3,3,1,1]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("\nbool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)):")
print(bool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)))
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

print("validStr4.sdev()")
print(validStr4.sdev())
print("")

print("validStr4.median()")
print(validStr4.median())
print("")

print("validStr4.freq()")
print(validStr4.freq())
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

print("validStr4.var()")
print(validStr4.var())
print("")

print('################')
print("Linear model for validStr4:")
print("""
validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var = validStr4[:,1:2]
var.add([1]*validStr4.dim[0],col=1,feature="bias")

out = validStr4[:,:1]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

""")

validStr4.corr().p

var = validStr4[:,1:2]
var.add([1]*validStr4.dim[0],col=1,feature="bias")

out = validStr4[:,:1]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

print("Height={0} + {1}*{2}".format(coefs[0,0],coefs[1,0],validStr4.features[1]))
print("\nModel range:",var.ranged(2))
print("\nAverage error:",err.mean(1)[err.features[0]])

if plotting:
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        print("Couldn't import matplotlib")
    else:
        model = plt.figure()
        
        #Data in a scatter plot
        plt.scatter(var.col(2,0),out.col(1,0))
        
        #Linear model to predict
        plt.plot(var.col(2,0),preds.col(1,0),c="red")
        
        #Titles
        plt.xlabel(validStr4.features[1])
        plt.ylabel(validStr4.features[0])
        plt.legend(["Linear model","Data points"],loc=4)
        model.suptitle("Height prediction")

# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15', 'Col 16', 'Col 17', 'Col 18', 'Col 19', 'Col 20']

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
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 


Square matrix
Dimension: 1x1
Features: ['Col 1']

0.4310 


Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

-28.0747  15.6996   0.0789 -10.7128 
 -5.6635  24.9928 -29.4843 -13.8732 


Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.3849 0.7320 0.3906 
0.8209 0.4617 0.3172 
0.2916 0.7665 0.8270 
0.7083 0.6154 0.9713 


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

 5.1730  1.6577  1.5694  0.5161 -1.9224  1.1032 -1.1170  0.1398 
 2.9434 -4.2640  1.9678 -3.9351 -1.4649  3.6151 -3.5471 -2.0428 
-2.0017 -0.9270  2.0305  2.7202 -8.8327 -3.4743  6.0660  3.4165 
 0.6164  3.0089  2.8462  0.0527  2.3636 -0.4878  0.4194 -0.4743 
 0.7894  0.7708  1.6977 -9.4982 -0.9175  1.5582 -1.9132 -3.8159 
-4.1194  0.7784  0.9843  2.2589  3.9924 -7.5980 -1.5181  2.0175 
-1.3713  3.1610 -0.4605  2.3610 -3.4492  1.9280  0.1111 -2.7905 
 3.3713  2.3135 -2.3140  5.3670 -0.0021  1.2367  1.6213 -2.0576 


Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.7631  -666.8193    96.2193   -33.6361  1069.2287  -467.4311 
 -762.1580   323.0769   -15.3735   409.0589   338.1398  -357.0178 
   74.1055  -448.9217   139.3914  -298.1998  -645.5700   379.2103 
 -180.2643   766.0699  -829.1708  1070.6528  -294.1339     8.8911 
  -17.0203  -100.1903   500.9381   -42.9804  1236.9605  -502.5160 
-1111.6573  -244.0657  1214.0243   894.0824  -875.6326  -593.8387 


Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

2.1383 8.4193 2.8346 8.8166 2.5650 9.6404 
5.3686 8.1115 2.7949 8.7601 7.3950 4.0669 
3.0803 5.3293 2.5627 2.9482 4.8391 4.2044 


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

48.5404  6.7117 57.7453 18.8885 40.9168 
75.5790 52.3226 79.8068 48.7370 51.6487 
68.6324 93.4797 78.8650  0.7820  2.6045 
89.9955 25.0315 83.1865 90.7468 74.0611 
28.3632 13.4245 40.6711 26.7685 82.7988 


Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

0.8778 0.2477 0.2579 0.6835 
0.9140 0.2171 0.6177 0.8680 
0.2022 0.6218 0.6411 0.6090 
0.1673 0.3849 0.4878 0.7651 


Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.21 0.79 0.00 0.63 0.18 0.32 0.62 0.03 0.35 
0.64 0.28 0.33 0.83 0.45 0.62 0.78 0.69 0.20 
0.98 0.75 0.82 0.65 0.65 0.50 0.22 0.03 0.67 
0.93 0.83 0.62 0.02 0.01 0.86 0.85 0.94 0.54 
0.36 0.50 0.64 0.34 0.58 0.53 0.19 0.78 0.26 
0.54 0.32 0.93 0.80 0.57 0.14 0.49 0.06 0.07 
0.70 0.88 0.47 0.88 0.59 0.99 0.02 0.74 0.38 
0.62 0.69 0.78 0.49 0.55 0.31 0.83 0.19 0.56 
0.82 0.54 0.65 0.25 0.52 0.07 0.72 0.03 0.67 


Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

0.019481 0.329755 0.805569 0.408451 0.985813 0.898311 
0.906358 0.765723 0.086422 0.879039 0.131641 0.807063 
0.303762 0.995401 0.859738 0.030612 0.789736 0.856186 
0.687379 0.429990 0.077339 0.424900 0.180151 0.867060 
0.824186 0.059135 0.339624 0.204326 0.614691 0.538494 
0.834478 0.684209 0.611336 0.751512 0.544877 0.639099 


Square matrix
Dimension: 3x3
Features: ['Col 1', 'Col 2', 'Col 3']

3.0000 5.0000 7.0000 
8.0000 3.0000 4.0000 
5.0000 2.0000 5.0000 


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

 0.7674+0.0523j   0.9958+0.3205j    0.208+0.4435j   0.9381+0.4368j   0.1266+0.4189j  
 0.5002+0.9161j   0.1836+0.9193j   0.5091+0.2834j   0.4814+0.9236j   0.4369+0.1941j  
 0.0929+0.0184j   0.4468+0.9247j   0.9681+0.4922j   0.8374+0.4977j   0.3042+0.5706j  
 0.5304+0.6734j   0.0069+0.4462j   0.7065+0.6893j   0.4414+0.5085j   0.9688+0.9912j  
 0.4968+0.3293j    0.014+0.6842j    0.889+0.8487j   0.2241+0.8141j   0.2209+0.7442j  


Dimension: 7x3
Features: ['Col 1', 'Col 2', 'Col 3']

 -4.8867-1.4249j   -2.6756+1.1489j    2.6205-8.5707j  
 -4.7767-4.2618j    5.1691+4.5926j   -4.4416-8.2034j  
  7.4019-9.1516j    4.3393+9.5876j    5.7368+4.6598j  
  8.1659+0.0624j    9.5513+6.5109j   -3.5569+2.0891j  
  6.4577+6.9575j    4.3772+4.2963j   -2.0039+4.2686j  
  1.1141+4.2492j   -5.3245+9.0996j     -6.3834-8.16j  
   3.651+0.2617j    1.1932-7.9907j     -0.79+4.2741j  

################################
################################
Identity matrices

Square matrix
Dimension: 1x1
Features: ['Col 1']

1.0000 


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 


Square matrix
Dimension: 3x3
Features: ['Col 1', 'Col 2', 'Col 3']

1.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 
0.0000 0.0000 1.0000 


Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 

################################
################################
Attribute call outputs

################

d:

Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.3849 0.7320 0.3906 
0.8209 0.4617 0.3172 
0.2916 0.7665 0.8270 
0.7083 0.6154 0.9713 

d.matrix:

[[0.3848900793248752, 0.7319531029862231, 0.3905928054094886], [0.8208913761645129, 0.4616679590199183, 0.3172070518460861], [0.2915523505139642, 0.7664713181520729, 0.8270047774848448], [0.7082663471852679, 0.6154463957070743, 0.9712518678954005]]

################

f[:4,1:3]:
 
Dimension: 4x2
Features: ['Col 2', 'Col 3']

-666.8193   96.2193 
 323.0769  -15.3735 
-448.9217  139.3914 
 766.0699 -829.1708 
 


Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.7631  -666.8193    96.2193   -33.6361  1069.2287  -467.4311 
 -762.1580   323.0769   -15.3735   409.0589   338.1398  -357.0178 
   74.1055  -448.9217   139.3914  -298.1998  -645.5700   379.2103 
 -180.2643   766.0699  -829.1708  1070.6528  -294.1339     8.8911 
  -17.0203  -100.1903   500.9381   -42.9804  1236.9605  -502.5160 
-1111.6573  -244.0657  1214.0243   894.0824  -875.6326  -593.8387 

f.delDim(4)

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.7631  -666.8193    96.2193   -33.6361  1069.2287  -467.4311 
 -762.1580   323.0769   -15.3735   409.0589   338.1398  -357.0178 
   74.1055  -448.9217   139.3914  -298.1998  -645.5700   379.2103 
 -180.2643   766.0699  -829.1708  1070.6528  -294.1339     8.8911 
  -17.0203  -100.1903   500.9381   -42.9804  1236.9605  -502.5160 
-1111.6573  -244.0657  1214.0243   894.0824  -875.6326  -593.8387 

f.uptri.p

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  -528.7631   -666.8193     96.2193    -33.6361   1069.2287   -467.4311 
     0.0000   1284.2289   -154.0637    457.5419  -1203.0444    316.7364 
     0.0000      0.0000     87.8098   -109.6777  -1003.8073    447.4695 
     0.0000      0.0000      0.0000   -199.5900  -8219.4459   3708.4667 
     0.0000      0.0000      0.0000      0.0000 -17839.5522   8120.3284 
     0.0000      0.0000      0.0000      0.0000      0.0000  -1029.0417 

f.lowtri.p

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 1.0000  0.0000  0.0000  0.0000  0.0000  0.0000 
 1.4414  1.0000  0.0000  0.0000  0.0000  0.0000 
-0.1401 -0.4223  1.0000  0.0000  0.0000  0.0000 
 0.3409  0.7735 -8.4592  1.0000  0.0000  0.0000 
 0.0322 -0.0613  5.5620 -2.9870  1.0000  0.0000 
 2.1024  0.9016 13.1037 -9.9678  3.9696  1.0000 

f-(f.lowtri@f.uptri)

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

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
 {'Col 1': [2.1383, 5.3686], 'Col 2': [5.3293, 8.4193], 'Col 3': [2.5627, 2.8346], 'Col 4': [2.9482, 8.8166], 'Col 5': [2.565, 7.395], 'Col 6': [4.0669, 9.6404]}
g: 
Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

2.1383 8.4193 2.8346 8.8166 2.5650 9.6404 
5.3686 8.1115 2.7949 8.7601 7.3950 4.0669 
3.0803 5.3293 2.5627 2.9482 4.8391 4.2044 

g.remove(3):

Dimension: 2x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

2.1383 8.4193 2.8346 8.8166 2.5650 9.6404 
5.3686 8.1115 2.7949 8.7601 7.3950 4.0669 

################
q1.decimal 2

Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.21 0.79 0.00 0.63 0.18 0.32 0.62 0.03 0.35 
0.64 0.28 0.33 0.83 0.45 0.62 0.78 0.69 0.20 
0.98 0.75 0.82 0.65 0.65 0.50 0.22 0.03 0.67 
0.93 0.83 0.62 0.02 0.01 0.86 0.85 0.94 0.54 
0.36 0.50 0.64 0.34 0.58 0.53 0.19 0.78 0.26 
0.54 0.32 0.93 0.80 0.57 0.14 0.49 0.06 0.07 
0.70 0.88 0.47 0.88 0.59 0.99 0.02 0.74 0.38 
0.62 0.69 0.78 0.49 0.55 0.31 0.83 0.19 0.56 
0.82 0.54 0.65 0.25 0.52 0.07 0.72 0.03 0.67 

q1.decimal=5

Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.20515 0.79336 0.00831 0.62877 0.17892 0.31975 0.61596 0.02837 0.35085 
0.64412 0.27969 0.32554 0.82983 0.45181 0.61813 0.77634 0.69162 0.20432 
0.98024 0.74933 0.82385 0.64609 0.64503 0.50325 0.22175 0.03247 0.67383 
0.93096 0.83320 0.62165 0.01597 0.01319 0.85741 0.85020 0.93797 0.53841 
0.35693 0.49928 0.63699 0.33836 0.58117 0.52933 0.18511 0.78436 0.26399 
0.53679 0.31841 0.92862 0.79672 0.56690 0.14003 0.49401 0.06106 0.07101 
0.70060 0.87702 0.46982 0.87856 0.58736 0.99400 0.02407 0.74378 0.37889 
0.61975 0.69181 0.77917 0.48886 0.55248 0.31244 0.83272 0.19206 0.55752 
0.81986 0.53985 0.65389 0.25075 0.51846 0.07374 0.71584 0.03181 0.67466 

################
h=proj[11:18,4:11]:
 
Square matrix
Dimension: 7x7
Features: ['Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11']

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.mean(): {'Col 5': 57.142857142857146, 'Col 6': 50.285714285714285, 'Col 7': 49.714285714285715, 'Col 8': 44.285714285714285, 'Col 9': 22.285714285714285, 'Col 10': 67.71428571428571, 'Col 11': 69.28571428571429}

h.det: 1287494716522.8682

h.rank: 7

h.rrechelon: 
Square matrix
Dimension: 7x7
Features: ['Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11']

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 


h.inv:

Square matrix
Dimension: 7x7
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7']

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0015  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.[:2,:4]:
 
Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

2.1383 8.4193 2.8346 8.8166 
5.3686 8.1115 2.7949 8.7601 
 

j.obj:
 Matrix(dim=[2, 4],listed=[[2.1382641429331253, 8.41934051147626, 2.834634629370159, 8.816586778723964], [5.368646078742537, 8.111493683937239, 2.7949025414014663, 8.760071799601818]],ranged=[0, 1],fill='uniform',features=['Col 1', 'Col 2', 'Col 3', 'Col 4'],header=False,directory='',decimal=4,seed=None,dtype='float')

################
proj=proj[:5,:15]:


Dimension: 5x15
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15']

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

48.5404  6.7117 57.7453 18.8885 40.9168 
75.5790 52.3226 79.8068 48.7370 51.6487 
68.6324 93.4797 78.8650  0.7820  2.6045 
89.9955 25.0315 83.1865 90.7468 74.0611 
28.3632 13.4245 40.6711 26.7685 82.7988 

p.det:
 -18487527.8192653

p.adj:
 
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

  -278269.9781  17778918.0419  -7205319.6416  -8509788.2524  -3114320.8106 
   448961.8062   -157890.2479   -129732.9411     37567.5052   -152896.1785 
  -295232.5827 -15338395.0686   6210340.5294   7386995.8586   2910967.5375 
   388532.9459  -6421307.7356   2644285.5423   2772412.6263   1250499.8198 
    41939.2344   3545588.5165  -1416171.5096  -1615844.1272   -965823.7864 

p.inv:


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

 0.0151 -0.9617  0.3897  0.4603  0.1685 
-0.0243  0.0085  0.0070 -0.0020  0.0083 
 0.0160  0.8297 -0.3359 -0.3996 -0.1575 
-0.0210  0.3473 -0.1430 -0.1500 -0.0676 
-0.0023 -0.1918  0.0766  0.0874  0.0522 

################
p:

Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

48.5404  6.7117 57.7453 18.8885 40.9168 
75.5790 52.3226 79.8068 48.7370 51.6487 
68.6324 93.4797 78.8650  0.7820  2.6045 
89.9955 25.0315 83.1865 90.7468 74.0611 
28.3632 13.4245 40.6711 26.7685 82.7988 

p.remove(col=1) and p.remove(row=2)

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 6.7117 57.7453 18.8885 40.9168 
93.4797 78.8650  0.7820  2.6045 
25.0315 83.1865 90.7468 74.0611 
13.4245 40.6711 26.7685 82.7988 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Features: ['Col 1', 'Col', 'Col 2', 'Col 3', 'Col 4']

 6.7117 55.0000 57.7453 18.8885 40.9168 
93.4797 55.0000 78.8650  0.7820  2.6045 
25.0315 55.0000 83.1865 90.7468 74.0611 
13.4245 55.0000 40.6711 26.7685 82.7988 

p.sdev()
{'Col 1': 34.585103513318444, 'Col': 0.0, 'Col 2': 17.084056749336664, 'Col 3': 33.926169687617744, 'Col 4': 31.557496460629554}
################

proj.find(40)
[(1, 8), (2, 4), (2, 12), (3, 11), (5, 14), (5, 15)]

proj.find(40,0)
[(0, 7), (1, 3), (1, 11), (2, 10), (4, 13), (4, 14)]

proj.find(111)
Value not in the matrix
################

r=p.t
r.remove(row=2):

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col', 'Col 2', 'Col 3']

 6.7117 93.4797 25.0315 13.4245 
57.7453 78.8650 83.1865 40.6711 
18.8885  0.7820 90.7468 26.7685 
40.9168  2.6045 74.0611 82.7988 

r.rank: 4

r.matrix[0]=r.matrix[1][:]

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col', 'Col 2', 'Col 3']

57.7453 78.8650 83.1865 40.6711 
57.7453 78.8650 83.1865 40.6711 
18.8885  0.7820 90.7468 26.7685 
40.9168  2.6045 74.0611 82.7988 

r.rank: 3
################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 -5.4825 -19.8340 -16.3253 
 -0.0856 -23.7441 -32.1423 


((((mMulti)+125)**3)%2):

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.8443 0.0795 1.9748 
0.5105 0.5756 1.6491 

################

f:
 
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.7631  -666.8193    96.2193   -33.6361  1069.2287  -467.4311 
 -762.1580   323.0769   -15.3735   409.0589   338.1398  -357.0178 
   74.1055  -448.9217   139.3914  -298.1998  -645.5700   379.2103 
 -180.2643   766.0699  -829.1708  1070.6528  -294.1339     8.8911 
  -17.0203  -100.1903   500.9381   -42.9804  1236.9605  -502.5160 
-1111.6573  -244.0657  1214.0243   894.0824  -875.6326  -593.8387 

f1=f.intForm

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.0000  -666.0000    96.0000   -33.0000  1069.0000  -467.0000 
 -762.0000   323.0000   -15.0000   409.0000   338.0000  -357.0000 
   74.0000  -448.0000   139.0000  -298.0000  -645.0000   379.0000 
 -180.0000   766.0000  -829.0000  1070.0000  -294.0000     8.0000 
  -17.0000  -100.0000   500.0000   -42.0000  1236.0000  -502.0000 
-1111.0000  -244.0000  1214.0000   894.0000  -875.0000  -593.0000 

f2=f.roundForm(3)

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 -528.7600  -666.8200    96.2200   -33.6400  1069.2300  -467.4300 
 -762.1600   323.0800   -15.3700   409.0600   338.1400  -357.0200 
   74.1100  -448.9200   139.3900  -298.2000  -645.5700   379.2100 
 -180.2600   766.0700  -829.1700  1070.6500  -294.1300     8.8900 
  -17.0200  -100.1900   500.9400   -42.9800  1236.9600  -502.5200 
-1111.6600  -244.0700  1214.0200   894.0800  -875.6300  -593.8400 

f2-f1

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

-0.7600 -0.8200  0.2200 -0.6400  0.2300 -0.4300 
-0.1600  0.0800 -0.3700  0.0600  0.1400 -0.0200 
 0.1100 -0.9200  0.3900 -0.2000 -0.5700  0.2100 
-0.2600  0.0700 -0.1700  0.6500 -0.1300  0.8900 
-0.0200 -0.1900  0.9400 -0.9800  0.9600 -0.5200 
-0.6600 -0.0700  0.0200  0.0800 -0.6300 -0.8400 

################
e+=Matrix(listed=Identity(e.dim[0]))*99

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

 5.1730  1.6577  1.5694  0.5161 -1.9224  1.1032 -1.1170  0.1398 
 2.9434 -4.2640  1.9678 -3.9351 -1.4649  3.6151 -3.5471 -2.0428 
-2.0017 -0.9270  2.0305  2.7202 -8.8327 -3.4743  6.0660  3.4165 
 0.6164  3.0089  2.8462  0.0527  2.3636 -0.4878  0.4194 -0.4743 
 0.7894  0.7708  1.6977 -9.4982 -0.9175  1.5582 -1.9132 -3.8159 
-4.1194  0.7784  0.9843  2.2589  3.9924 -7.5980 -1.5181  2.0175 
-1.3713  3.1610 -0.4605  2.3610 -3.4492  1.9280  0.1111 -2.7905 
 3.3713  2.3135 -2.3140  5.3670 -0.0021  1.2367  1.6213 -2.0576 


e-=33:

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

-27.8270 -31.3423 -31.4306 -32.4839 -34.9224 -31.8968 -34.1170 -32.8602 
-30.0566 -37.2640 -31.0322 -36.9351 -34.4649 -29.3849 -36.5471 -35.0428 
-35.0017 -33.9270 -30.9695 -30.2798 -41.8327 -36.4743 -26.9340 -29.5835 
-32.3836 -29.9911 -30.1538 -32.9473 -30.6364 -33.4878 -32.5806 -33.4743 
-32.2106 -32.2292 -31.3023 -42.4982 -33.9175 -31.4418 -34.9132 -36.8159 
-37.1194 -32.2216 -32.0157 -30.7411 -29.0076 -40.5980 -34.5181 -30.9825 
-34.3713 -29.8390 -33.4605 -30.6390 -36.4492 -31.0720 -32.8889 -35.7905 
-29.6287 -30.6865 -35.3140 -27.6330 -33.0021 -31.7633 -31.3787 -35.0576 


e+=Matrix(e.dim):

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

-26.8393 -30.8062 -31.0888 -32.4425 -34.5352 -31.3750 -33.5307 -32.1463 
-29.4241 -36.7049 -30.4382 -36.4155 -34.3999 -28.6521 -36.4338 -34.3414 
-34.2354 -33.4636 -30.2616 -29.5206 -41.6612 -35.7197 -26.1925 -29.0655 
-31.7550 -29.5091 -29.2234 -32.1987 -30.0524 -33.3640 -32.4950 -33.1523 
-32.1707 -31.9334 -30.9006 -41.7960 -33.5568 -31.4348 -34.8988 -36.0085 
-36.6675 -31.6448 -31.6049 -30.6966 -28.9601 -40.2071 -33.8100 -30.0219 
-33.6180 -29.7188 -33.0470 -29.7260 -36.0199 -30.7100 -31.9456 -34.9298 
-29.1925 -29.9658 -34.6130 -27.4355 -32.0834 -31.2910 -30.9427 -34.7958 


e*=[2,1,1,0.5,0.2,0.0003,1,3]:

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

 -53.6786  -30.8062  -31.0888  -16.2212   -6.9070   -0.0094  -33.5307  -96.4388 
 -58.8481  -36.7049  -30.4382  -18.2078   -6.8800   -0.0086  -36.4338 -103.0243 
 -68.4709  -33.4636  -30.2616  -14.7603   -8.3322   -0.0107  -26.1925  -87.1966 
 -63.5099  -29.5091  -29.2234  -16.0994   -6.0105   -0.0100  -32.4950  -99.4568 
 -64.3413  -31.9334  -30.9006  -20.8980   -6.7114   -0.0094  -34.8988 -108.0254 
 -73.3350  -31.6448  -31.6049  -15.3483   -5.7920   -0.0121  -33.8100  -90.0656 
 -67.2361  -29.7188  -33.0470  -14.8630   -7.2040   -0.0092  -31.9456 -104.7894 
 -58.3851  -29.9658  -34.6130  -13.7178   -6.4167   -0.0094  -30.9427 -104.3875 

e%=[2,2,2,2,1,1,1,1]

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

1.3214 4.1938 3.9112 3.7788 2.0930 2.9906 0.4693 0.5612 
1.1519 3.2951 4.5618 1.7922 2.1200 2.9914 0.5662 0.9757 
1.5291 1.5364 4.7384 0.2397 0.6678 2.9893 0.8075 0.8034 
1.4901 0.4909 0.7766 3.9006 2.9895 2.9900 0.5050 0.5432 
0.6587 3.0666 4.0994 4.1020 2.2886 2.9906 0.1012 0.9746 
1.6650 3.3552 3.3951 4.6517 0.2080 2.9879 0.1900 0.9344 
2.7639 0.2812 1.9530 0.1370 1.7960 2.9908 0.0544 0.2106 
1.6149 0.0342 0.3870 1.2822 2.5833 2.9906 0.0573 0.6125 

################

c%j

Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

1.8610 7.2803 0.0789 6.9204 
5.0738 0.6583 1.2597 3.6469 


bool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)):
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 34.0000 -52.0000  33.0000 
  9.0000  88.0000  -3.0000 

################
validStr2:

Dimension: 1x10
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

312.0000  45.0000  12.0000  44.0000 352.0000  45.0000  12.0000  44.0000   3.0000  -5.0000 

################
validStr3:

Dimension: 1x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 34.0000   5.0000  44.0000 659.0000 

################
validStr4:

Dimension: 22x3
Features: ['Height', 'Weight', 'Age']

130.0000  30.0000  10.0000 
125.0000  36.0000  11.0000 
135.0000  34.0000  10.0000 
133.0000  30.0000   9.0000 
129.0000  38.0000  12.0000 
180.0000  90.0000  30.0000 
190.0000  80.0000  25.0000 
175.0000  90.0000  35.0000 
177.0000  60.0000  22.0000 
185.0000 105.0000  33.0000 
165.0000  55.0000  27.0000 
155.0000  50.0000  44.0000 
160.0000  58.0000  39.0000 
162.0000  59.0000  41.0000 
167.0000  62.0000  55.0000 
174.0000  70.0000  47.0000 
193.0000  90.0000  23.0000 
187.0000  80.0000  27.0000 
183.0000  88.0000  28.0000 
159.0000  40.0000  29.0000 
164.0000  66.0000  32.0000 
166.0000  56.0000  42.0000 

################

validStr4.ranged()
{'Height': [125.0, 193.0], 'Weight': [30.0, 105.0], 'Age': [9.0, 55.0]}

validStr4.mean()
{'Height': 163.36363636363637, 'Weight': 62.13636363636363, 'Age': 28.681818181818183}

validStr4.sdev()
{'Height': 20.592464320155067, 'Weight': 21.774245534462064, 'Age': 12.68996154316246}

validStr4.median()
{'Height': 166.0, 'Weight': 60.0, 'Age': 29.0}

validStr4.freq()
{'Height': {130.0: 1, 125.0: 1, 135.0: 1, 133.0: 1, 129.0: 1, 180.0: 1, 190.0: 1, 175.0: 1, 177.0: 1, 185.0: 1, 165.0: 1, 155.0: 1, 160.0: 1, 162.0: 1, 167.0: 1, 174.0: 1, 193.0: 1, 187.0: 1, 183.0: 1, 159.0: 1, 164.0: 1, 166.0: 1}, 'Weight': {30.0: 2, 36.0: 1, 34.0: 1, 38.0: 1, 90.0: 3, 80.0: 2, 60.0: 1, 105.0: 1, 55.0: 1, 50.0: 1, 58.0: 1, 59.0: 1, 62.0: 1, 70.0: 1, 88.0: 1, 40.0: 1, 66.0: 1, 56.0: 1}, 'Age': {10.0: 2, 11.0: 1, 9.0: 1, 12.0: 1, 30.0: 1, 25.0: 1, 35.0: 1, 22.0: 1, 33.0: 1, 27.0: 2, 44.0: 1, 39.0: 1, 41.0: 1, 55.0: 1, 47.0: 1, 23.0: 1, 28.0: 1, 29.0: 1, 32.0: 1, 42.0: 1}}

validStr4.mode()
{'Height': {'All': 1}, 'Weight': {90.0: 3}, 'Age': {(10.0, 27.0): 2}}

validStr4.iqr()
{'Height': 25.0, 'Weight': 40.0, 'Age': 17.0}

validStr4.iqr(as_quartiles=True)
{'Height': [155.0, 166.0, 180.0], 'Weight': [40.0, 60.0, 80.0], 'Age': [22.0, 29.0, 39.0]}

validStr4.var()
{'Height': 424.0495867768595, 'Weight': 474.1177685950411, 'Age': 161.03512396694214}

################
Linear model for validStr4:

validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var = validStr4[:,1:2]
var.add([1]*validStr4.dim[0],col=1,feature="bias")

out = validStr4[:,:1]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]



Square matrix
Dimension: 3x3
Features: ['Height', 'Weight', 'Age']

1.0000 0.8992 0.5087 
0.8992 1.0000 0.4233 
0.5087 0.4233 1.0000 

Height=110.5244538162 + 0.850374553976*Weight

Model range: {'Weight': [30.0, 105.0]}

Average error: 3.4473087980173164e-08
"""
# =============================================================================

