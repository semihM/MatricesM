def find(mat,element,start=1):
    """
    element: Real number
    start: 0 or 1. Index to start from 
    Returns the indeces of the given elements, multiple occurances are returned in a list
    """
    indeces=[]
    temp=mat.copy.matrix
    try:
        assert start==0 or start==1
        assert isinstance(element,int) or isinstance(element,float) or isinstance(element,complex)
        for row in range(mat.dim[0]):
            while element in temp[row]:
                n=temp[row].index(element)
                indeces.append((row+start,n+start))
                temp[row][n]=""
    except AssertionError:
        print("Invalid arguments")
    else:
        if len(indeces):
            return indeces
        print("Value not in the matrix")
        return None