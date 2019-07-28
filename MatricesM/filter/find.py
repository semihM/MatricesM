def find(mat,dims,element,start,rowind):
    assert isinstance(start,int), "Starting index have to be an integer"
    
    from MatricesM.customs.objects import null
    
    indices=[]
    for row in range(dims[0]):
        while element in mat[row]:
            n=mat[row].index(element)
            indices.append((row+start,n+start))
            mat[row][n]=null

    if len(indices):
        if rowind:
            return list(set([i[0] for i in indices]))
        return indices
    return None
