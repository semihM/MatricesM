def betterslice(oldslice,dim):
    s,e,t = 0,dim,1
    vs,ve,vt = oldslice.start,oldslice.stop,oldslice.step
    if vs!=None:
        if vs>0 and vs<dim:
            s = vs
        elif vs<0 and abs(vs)-1<dim:
            return slice(vs,ve,t)
    if ve!=None:
        if ve>0 and ve<dim:
            if ve<=s:
                e = s
            else:
                e = ve
        elif ve<0 and abs(ve)-1<dim:
            e = dim+ve
    if vt!=None:
        if abs(vt)<=dim:
            t = vt
        else:
            t = dim
    return slice(s,e,t)

def getitem(mat,pos,obj,useindex):
    mat._Matrix__useind = 0 #Reset ind
    #Get 1 row
    if isinstance(pos,int):
        if useindex:
            ind = mat.index.index(pos)
            return obj(listed=[mat._matrix[ind]],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[pos],indexname=mat.indexname)
        return obj(listed=[mat._matrix[pos]],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[mat.index[pos]],indexname=mat.indexname)

    #Get multiple rows
    elif isinstance(pos,slice):
        if useindex:
            indices = mat.index
            start = pos.start if pos.start != None else 0
            end = pos.stop if pos.stop != None else mat.d1
            rowrange,mm = [],mat.matrix
            for i in range(mat.d0):
                if indices[i]>=start:
                    if indices[i]>=end:
                        break
                    rowrange.append(i)
            lastinds = [indices[i] for i in rowrange]
            lastmatrix = [mm[i] for i in rowrange]
            return obj(listed=lastmatrix,features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds,indexname=mat.indexname)
        return obj(listed=mat._matrix[pos],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=mat.index[pos],indexname=mat.indexname)
    
    #Get 1 column or use a specific row index
    elif isinstance(pos,str):
        if useindex:
            index = mat.index
            if not pos in index:
                raise ValueError(f"{pos} is not a row index")
            else:
                mm = mat.matrix
                rowinds = [i for i in range(mat.d0) if index[i]==pos]
                return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                           dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[pos for _ in range(len(rowinds))],
                           indexname=mat.indexname)

        if not pos in mat.features:
            raise ValueError(f"{pos} is not in column names")
        else:
            pos = mat.features.index(pos)
        
        mat =  obj(dim=[mat.d0,1],listed=[[i[pos]] for i in mat._matrix],features=[mat.features[pos]],
                   decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[pos]],index=mat.index[:],
                   indexname=mat.indexname,implicit=True)
        mat.NOTES = f"n:{mat.d0},type:{mat.coldtypes[0].__name__},invalid:{mat.d0-mat.count(get=0)}\n\n"
        return mat

    #Get rows from given indices
    elif isinstance(pos,list):
        d0 = mat.d0
        if useindex:
            indices = mat.index
            if not all([1 if i in indices else 0 for i in pos]):
                raise ValueError(f"Given list can't be used as row indices")
            else:
                mm = mat.matrix
                rowinds = [i for i in range(d0) if indices[i] in pos]
                return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                           dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[indices[a] for a in rowinds],
                           indexname=mat.indexname)

        if not all([1 if isinstance(i,int) else 0 for i in pos]):
            raise TypeError("Given list should only have integers")
        if any([0 if i<d0 else 1 for i in pos]):
            raise IndexError(f"Given list should have integers in range [0,{d0})")

        mm = mat.matrix
        i = mat.index
        inds = [i[index] for index in pos] if mat._dfMat else []
        return obj(listed=[mm[i][:] for i in pos],features=mat.features,coldtypes=mat.coldtypes,dtype=mat.dtype,decimal=mat.decimal,index=inds,indexname=mat.indexname)

    #Get certain parts of the matrix
    elif isinstance(pos,tuple):
        pos = list(pos)
        #Column names or row indices given
        if all([1 if isinstance(i,str) else 0 for i in pos]):
            #Use as row indices
            if useindex:
                indices = mat.index
                rowinds = [i for i in range(mat.d0) if indices[i] in pos]
                return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                           dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[indices[a] for a in rowinds],
                           indexname=mat.indexname)

            #Use as column names
            colinds = [mat.features.index(i) for i in pos]
            temp = obj((mat.dim[0],len(pos)),fill=0,features=list(pos),decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[i] for i in colinds],index=mat.index[:],indexname=mat.indexname)
            mm = mat.matrix
            for row in range(mat.dim[0]):
                c = 0
                for col in colinds:
                    temp._matrix[row][c] = mm[row][col]
                    c+=1
            return temp
        
        #Tuple given    
        if len(pos)==2:
            pos = list(pos)
            # Matrix[slice,column_index]
            if isinstance(pos[0],slice):
                if useindex:
                    indices = mat.index
                    start = pos[0].start if pos[0].start != None else 0
                    end = pos[0].stop if pos[0].stop != None else mat.d1
                    rowrange,mm = [],mat.matrix
                    for i in range(mat.d0):
                        if indices[i]>=start:
                            if indices[i]>=end:
                                break
                            rowrange.append(i)
                else:
                    newslice = betterslice(pos[0],mat.dim[0])
                    rowrange = range(newslice.start,min(newslice.stop,mat.dim[0]),newslice.step)
            # Matrix[int,column_index]
            elif isinstance(pos[0],int):
                if useindex:
                    indices = mat.index
                    rowrange = [i for i in range(mat.d0) if indices[i]==pos[0]]
                else:
                    rowrange = [pos[0]]
            # Matrix[list,column_index]
            elif isinstance(pos[0],list):
                d0 = mat.d0
                if useindex:
                    indices = mat.index
                    if not all([1 if i in indices else 0 for i in pos[0]]):
                        raise ValueError(f"Given list can't be used as row indices")
                    rowrange = [i for i in range(d0) if indices[i] in pos[0]]
                else:
                    if not all([1 if isinstance(i,int) else 0 for i in pos[0]]):
                        raise TypeError("Given list should only have integers")
                    if any([0 if i<d0 else 1 for i in pos[0]]):
                        raise IndexError(f"Given list should have integers in range [0,{d0}) for rows")
                    rowrange = pos[0]
            # Matrix(Matrix,column_index]
            elif isinstance(pos[0],obj):
                if useindex:
                    return None
                rowrange = [i[0] for i in pos[0].find(1,0)]
            else:
                raise TypeError(f"{pos[0]} can't be used as row index")
            #########################
            # Matrix[row_index,str]
            if isinstance(pos[1],str):
                pos[1] = mat.features.index(pos[1])

            # Matrix[row_index,slice]
            elif isinstance(pos[1],slice):
                default_st = pos[1].start if pos[1].start!=None else 0
                default_en = pos[1].stop if pos[1].stop!=None else mat.d1
                start = mat.features.index(pos[1].start) if isinstance(pos[1].start,str) else default_st
                end = mat.features.index(pos[1].stop) if isinstance(pos[1].stop,str) else default_en
                pos[1] = betterslice(slice(start,end),mat.d1)

            # Matrix[row_index,Tuple(str)]
            elif isinstance(pos[1],(tuple,list)):
                if all([1 if isinstance(i,str) else 0 for i in pos[1]]) or all([1 if isinstance(i,int) else 0 for i in pos[1]]):
                    colinds = [mat.features.index(i) if isinstance(i,str) else i for i in pos[1]]
                    d0 = mat.d0
                    if any([0 if i<d0 else 1 for i in colinds]):
                        raise IndexError(f"Given list should have integers in range [0,{d0}) for columns")

                    inds = mat.index
                    indices = [inds[row] for row in rowrange] if mat._dfMat else []
                    temp = []
                    mm = mat.matrix
                    r=0
                    rowrange = list(set(rowrange))
                    for row in rowrange:
                        temp.append([])
                        for col in colinds:
                            temp[r].append(mm[row][col])
                        r+=1

                    return obj((len(rowrange),len(colinds)),temp,
                                features=[mat.features[i] for i in colinds],
                                decimal=mat.decimal,dtype=mat.dtype,
                                coldtypes=[mat.coldtypes[i] for i in colinds],
                                index=indices,
                                indexname=mat.indexname)

                else:
                    raise ValueError(f"{pos[1]} has inconsistant values,should be all integers or strings")
            
            t = mat.coldtypes[pos[1]]
            mm = mat.matrix
            inds = mat.index
            rowrange = list(set(rowrange))
            lastinds = [inds[i] for i in rowrange] if mat._dfMat else []

            if type(t) != list:
                t = [t]

            if isinstance(pos[0],int) and isinstance(pos[1],int):
                return mat._matrix[rowrange[0]][pos[1]]
                
            elif isinstance(pos[1],int):
                return obj(listed=[[mm[i][pos[1]]] for i in rowrange],features=[mat.features[pos[1]]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t,index=lastinds,indexname=mat.indexname)
            
            elif isinstance(pos[1],slice):
                return obj(listed=[mm[i][pos[1]] for i in rowrange],features=mat.features[pos[1]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t,index=lastinds,indexname=mat.indexname)
            
            # Matrix[Matrix,column_index]
            elif isinstance(pos[0],obj):
                temp = []
                if isinstance(pos[1],int): #Force slice
                    if pos[1]>=mat.dim[1] or pos[1]<0:
                        raise IndexError(f"{pos[1]} can't be used as column index")
                    pos[1] = slice(pos[1],pos[1]+1)

                mm = mat.matrix

                for i in rowrange:
                    temp.append(mm[i][pos[1]])

                return obj(listed=temp,features=mat.features[pos[1]],dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes[pos[1]],index=lastinds,indexname=mat.indexname)
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces
    elif isinstance(pos,obj):
        if useindex:
            return None
        rowrange = [i for i in range(mat.d0) if pos._matrix[i][0]==1]
        rowrange = list(set(rowrange))
        mm = mat.matrix
        temp = [mm[i] for i in rowrange]
        indices = mat.index
        return obj(listed=temp,features=mat.features,dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes,index=[indices[i] for i in rowrange],indexname=mat.indexname)

def setitem(mat,pos,item,obj):
    #Change rows
    #Lists should be given as [[1,2,...],[3,4,...],...]
    from MatricesM.errors.errors import MatrixError,InconsistentValues,DimensionError
    if isinstance(pos,slice):
        newslice = betterslice(pos,mat.dim[0])
        rowrange = range(newslice.start,min(newslice.stop,mat.dim[0]),newslice.step)

        if isinstance(item,list):        
            typ = type(item[0])
            if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                raise InconsistentValues("Given list has varying types of values") 
            
            elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                rrange_len,item_len,ind_len,inneritem_len = len(rowrange),len(item),mat.dim[1],len(item[0])
                
                if len(item_len)!=len(rrange_len) and len(inneritem_len)!=len(ind_len): #Given list of lists should have all the items to replace the old ones with
                    raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
            
            else:#Single values given in a list, 
                item = [item for i in rowrange]

        elif isinstance(item,obj):
            if item.dim[1] != mat.dim[1]  or item.dim[0] != len(rowrange):
                raise DimensionError(f"Given matrix's dimensions should be {len(rowrange)}x{mat.dim[1]}")
            item = item.matrix
        #If given 'item' is not in a list or a matrix
        else:
            item = [[item for j in range(mat.dim[1])] for i in rowrange]

        mat._matrix[pos] = item 

    #Change a row
    #Lists should be given as [1,2,...]
    elif isinstance(pos,int):
        if pos not in range(mat.dim[0]):
            raise IndexError(f"{pos} index is out of range")

        if isinstance(item,obj):
            if item.dim[0] != 1:
                raise ValueError("Given matrix should have 1 row")
            item = item.matrix[0]

        elif isinstance(item,list):
            if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                raise InconsistentValues("Given list has varying types of values") 
            if len(item)!=mat.dim[1]: 
                raise AssertionError(f"Expected length of the list to be :{mat.dim[1]}, but got {len(item)}")
        
        #If given 'item' is not in a list or a matrix
        else:
            item = [item for j in range(mat.dim[1])]

        mat._matrix[pos] = item

    #Change a column
    elif isinstance(pos,str):
        new_col = 0
        if not pos in mat.features:
            new_col = 1
        if isinstance(item,list):        
            typ = type(item[0])
            if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                raise InconsistentValues("Given list has varying types of values") 
            
            elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                rrange_len,item_len,ind_len,inneritem_len = mat.dim[0],len(item),1,len(item[0])
                
                if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                    raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")

                if inneritem_len == 1:
                    item = [i[0] for i in item]
            else:#Single values given in a list, 
                pass

        elif isinstance(item,obj):
            if item.dim[1] == 1  ^ item.dim[0] == 1:
                raise ValueError("Given matrix should have 1 column or row")
            if item.dim[0] == 1:
                item = item.matrix[0]
            else:
                item = item.col(1,0)
        #If given 'item' is not in a list or a matrix
        else:
            item = [item for i in range(mat.dim[0])]

        try:
            if not new_col:
                ind = mat.features.index(pos)
                for i in range(mat.dim[0]):
                    mat._matrix[i][ind] = item[i]
            else:
                for i in range(mat.dim[0]):
                    mat._matrix[i].append(item[i])
                mat._Matrix__features.append(pos)
                mat._Matrix__coldtypes.append(type(item[i]))
                mat._Matrix__dim = [mat.dim[0],mat.dim[1]+1]
        except:
            raise IndexError(f"Given list: {item} doesn't have enough items to use")

    #Change certain parts of the matrix
    elif isinstance(pos,tuple):
        #Change given columns
        pos = list(pos)
        if all([1 if isinstance(i,str) else 0 for i in pos]):
            colrange = [mat.features.index(v) for v in pos]
            if isinstance(item,list):        
                typ = type(item[0])
                if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                    raise InconsistentValues("Given list has varying types of values") 
                
                elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                    rrange_len,item_len,ind_len,inneritem_len = mat.dim[0],len(item),len(colrange),len(item[0])
                    
                    if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                        raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                
                else:#Single values given in a list, 
                    item = [item for i in range(mat.dim[0])]

            elif isinstance(item,obj):
                item = item.matrix
            #If given 'item' is not in a list or a matrix
            else:
                item = [[item for i in range(len(colrange))] for j in range(mat.dim[0])]

            try:
                row = 0
                for r in range(mat.dim[0]):
                    i = 0
                    for c in colrange:
                        mat._matrix[r][c] = item[row][i]
                        i+=1
                    row+=1
            except:
                raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

        #Tuple with row indices first, column indices/names second
        elif len(pos)==2:
            pos = list(pos)
            newpos = []
            ind = 0
            for p in pos:
                if type(p) == slice:
                    newpos.append(betterslice(p,mat.dim[0]))
                else:
                    newpos.append(p)
                ind += 1
            pos = newpos

            # (row_index,column_name)
            if isinstance(pos[1],str):
                pos[1] = mat.features.index(pos[1])

            # (row_index,tuple_of_column_names)
            if isinstance(pos[1],tuple):
                rowrange = range(1)
                #Check row indices
                if isinstance(pos[0],slice):
                    newslice = betterslice(pos[0],mat.dim[0])
                    rowrange = range(newslice.start,min(newslice.stop,mat.dim[0]),newslice.step)
                
                elif isinstance(pos[0],int):
                    rowrange = [pos[0]]
                
                elif isinstance(pos[0],obj):
                    rowrange = [i[0] for i in pos[0].find(1,0)]

                else:
                    raise TypeError("Row indices should be either an integer, a slice or a boolean matrix")
                
                #Assert second index contains column names
                if all([1 if isinstance(i,str) else 0 for i in pos[1]]):
                    if isinstance(item,list):
                        
                        typ = type(item[0])
                        if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                            raise InconsistentValues("Given list has varying types of values") 
                        
                        elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                            rrange_len,item_len,ind_len,inneritem_len = len(rowrange),len(item),len(pos[1]),len(item[0])
                            
                            if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                                raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                        
                        else:#Single values given in a list, 
                            item = [item for i in rowrange]

                    elif isinstance(item,obj):
                        item = item.matrix
                    #If given 'item' is not in a list or a matrix
                    else:
                        item = [[item for i in range(len(pos[1]))] for j in rowrange]
                    
                else:
                    raise ValueError(f"{pos[1]} has non-string values")

                #Replace values
                try:
                    colinds = [mat.features.index(i) for i in pos[1]]
                    r1=0
                    for r in rowrange:
                        c1=0
                        for c in colinds:
                            mat._matrix[r][c] = item[r1][c1]
                            c1+=1
                        r1+=1
                except:
                    raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

            # mat[ slice, slice ]
            elif isinstance(pos[0],slice) and isinstance(pos[1],slice):
                #Get indices
                rowrange = range(pos[0].start,min(pos[0].stop,mat.dim[0]),pos[0].step)
                colrange = range(pos[1].start,min(pos[1].stop,mat.dim[1]),pos[1].step)

                #If given 'item' is not in a list or a matrix
                if isinstance(item,list):
                    typ = type(item[0])
                    if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                        raise InconsistentValues("Given list has varying types of values") 
                    
                    elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                        rrange_len,item_len,ind_len,inneritem_len = len(rowrange),len(item),len(colrange),len(item[0])
                        
                        if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                            raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                    
                    else:#Single values given in a list, 
                        item = [item[:] for i in rowrange]
                
                elif isinstance(item,obj):
                    item = item.matrix

                else:
                    item = [[item for i in colrange] for j in rowrange]
                
                #Replace values
                try:
                    row=0
                    for r in rowrange:
                        col=0
                        for c in colrange:
                            mat._matrix[r][c] = item[row][col]
                            col+=1
                        row+=1
                
                except:
                    raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

            # mat[ slice, int ] 
            elif isinstance(pos[0],slice) and isinstance(pos[1],int):
                #Get indices
                rowrange = range(pos[0].start,min(pos[0].stop,mat.dim[0]),pos[0].step)
                #If given 'item' is not in a list or a matrix
                if isinstance(item,list): #Item is a list
                    typ = type(item[0])
                    if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                        raise InconsistentValues("Given list has varying types of values") 
                    
                    elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                        rrange_len,item_len,ind_len,inneritem_len = len(rowrange),len(item),1,len(item[0])
                        
                        if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                            raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                    
                    else:#Single values given in a list, 
                        item = [[i] for i in item]

                elif isinstance(item,obj):
                    if item.dim[1]!=1:
                        raise DimensionError("Given matrix should be a column matrix")
                    item = item.matrix

                else:  #Item is a single value
                    item = [[item] for j in rowrange]
                
                #Replace values
                try:
                    row=0
                    for r in rowrange:
                        mat._matrix[r][pos[1]] = item[row][0]
                        row+=1
                except:
                    raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

            # mat[ int, slice ]
            elif isinstance(pos[0],int) and isinstance(pos[1],slice):
                #Get indices
                colrange = range(pos[1].start,min(pos[1].stop,mat.dim[1]),pos[1].step)
                #If given 'item' is not in a list or a matrix
                if isinstance(item,list): #Item is a list
                    typ = type(item[0])
                    if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                        raise InconsistentValues("Given list has varying types of values") 
                    
                    elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                        rrange_len,item_len,ind_len,inneritem_len = 1,len(item),len(colrange),len(item[0])
                        
                        if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                            raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                    
                    else:#Single values given in a list, 
                        pass

                elif isinstance(item,obj):
                    if item.dim[0]!=1:
                        raise DimensionError("Given matrix should be a row matrix")
                    item = item.matrix[0]

                else:  #Item is a single value
                    item = [item for j in colrange]
                
                #Replace values
                try:
                    col=0
                    for c in colrange:
                        mat._matrix[pos[0]][c] = item[col]
                        col+=1
                except:
                    raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

            # mat[ int, int ]
            elif isinstance(pos[0],int) and isinstance(pos[1],int):
                mat._matrix[pos[0]][pos[1]] = item

            #0-1 filled matrix given as indeces
            elif isinstance(pos[0],obj):
                if pos[0].dim[1]!=1:
                    raise DimensionError("Boolean matrix should be a column matrix")

                #Get row indices from the bool matrix
                inds = [i[0] for i in pos[0].find(1,0)]

                #Set column indices
                #[bool_matrix,int]
                if isinstance(pos[1],int):
                    cols = [pos[1]]
                #[bool_matrix,column name]
                elif isinstance(pos[1],str):
                    cols = [mat.features.index(pos[1])]
                #[bool_matrix,tuple_of_column_names]
                elif isinstance(pos[1],tuple):
                    cols = [mat.features.index(i) for i in pos[1]]
                else:
                    raise TypeError(f"{pos[1]} can't be used as column indices")

                #Given item is list of lists   
                if isinstance(item,list): #Item is a list
                    typ = type(item[0])
                    if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                        raise InconsistentValues("Given list has varying types of values") 
                    
                    elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                        rrange_len,item_len,ind_len,inneritem_len = len(inds),len(item),len(colrange),len(item[0])
                        
                        if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                            raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
                    
                    else:#Single values given in a list, 
                        item = [item for _ in range(len(inds))]

                elif isinstance(item,obj):
                    if item.dim[0]!=len(inds) or item.dim[1]!=len(colrange):
                        raise DimensionError(f"Given matrix's dimensions should be {len(inds)}x{len(colrange)}")
                    item = item.matrix

                else:  #Item is a single value
                    item = [[item for j in cols] for _ in range(len(inds))]

                try:
                    r=0
                    for row in inds:
                        c=0
                        for col in cols:
                            mat._matrix[row][col] = item[r][c]
                            c+=1
                        r+=1
                except:
                    raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

            else:
                raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces, change the whole row with given items
    elif isinstance(pos,obj):
        if pos.dim[1]!=1:
            raise DimensionError("Boolean matrix should be a column matrix")
        inds = [i[0] for i in pos.find(1,0)]

        if isinstance(item,list): #Item is a list
            typ = type(item[0])
            if not all([1 if isinstance(i,typ) else 0 for i in item]): #Differing data types given in the list
                raise InconsistentValues("Given list has varying types of values") 
            
            elif all([1 if isinstance(i,list) else 0 for i in item]): #Lists of values given in a list    
                rrange_len,item_len,ind_len,inneritem_len = len(inds),len(item),mat.dim[1],len(item[0])
                
                if item_len!=rrange_len and inneritem_len!=ind_len: #Given list of lists should have all the items to replace the old ones with
                    raise DimensionError(f"Given {item} was expected to have dimensions:{rrange_len}x{ind_len}, got {item_len}x{inneritem_len} instead.")
            
            else:#Single values given in a list, 
                item = [item for _ in range(len(inds))]

        elif isinstance(item,obj):
            if item.dim[0]!=len(inds) or item.dim[1]!=mat.dim[1]:
                raise DimensionError(f"Given matrix's dimensions should be {len(inds)}x{mat.dim[1]}")
            item = item.matrix

        else:  #Item is a single value
            item = [[item for j in range(mat.dim[1])] for _ in range(len(inds))]

        try:
            r=0
            for row in inds:
                mat._matrix[row] = item[r]
                r+=1
        except:
            raise IndexError(f"Given list: {item} doesn't have enough items to replace the old values with")

    else:
        raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")

    return mat

def delitem(mat,val,obj):
        #A string passed == delete a column
        if isinstance(val,str):
            #Assertion
            if not val in mat.features:
                raise ValueError(f"'{val}' isn't a column name")
            #Indices
            colind = mat.features.index(val)
            #Remove the desired column
            for i in range(mat.dim[0]):
                del mat.matrix[i][colind]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0],mat.dim[1]-1]
            del mat.features[colind]
            del mat.coldtypes[colind]

        #An integer passed == delete a row
        elif isinstance(val,int):
            #Assertion
            if not (val>=0 and val<mat.dim[0]):
                raise ValueError("Row index out of range")
            #Remove the desired row
            del mat.matrix[val]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-1,mat.dim[1]]

        #Slice object passed == delete 1 or more rows
        elif isinstance(val,slice):
            from math import ceil
            #Check how many rows will be deleted
            newslice = betterslice(val,mat.dim[0])
            s,e,t = newslice.start,newslice.stop,newslice.step
            #Remove rows
            mat._matrix = [mat._matrix[i] for i in range(mat.dim[0]) if not i in range(mat.dim[0])[val]]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-ceil((e-s)/t),mat.dim[1]]

        #Multiple arguments passed == delete 1 or more rows and columns
        elif isinstance(val,tuple):
            #Column names given == delete all rows of the given columns
            if all([1 if isinstance(i,str) else 0 for i in val]):
                #Indices
                colinds = [mat.features.index(i) for i in val if i in mat.features]
                #Remove columns
                for r in range(mat.dim[0]):
                    mat._matrix[r] = [mat._matrix[r][i] for i in range(mat.dim[1]) if not i in colinds]
                #Remove column names and dtypes        
                mat._Matrix__features = [mat.features[i] for i in range(mat.dim[1]) if not i in colinds]
                mat._Matrix__coldtypes = [mat.coldtypes[i] for i in range(mat.dim[1]) if not i in colinds]
                #Set new dimensions
                mat._Matrix__dim = [mat.dim[0],mat.dim[1]-len(colinds)]

            #Columns can't be deleted just for some rows
            else:
                if isinstance(val[0],slice):
                    if betterslice(val[0],mat.dim[0]) != slice(0,mat.dim[0],1):
                        raise TypeError("Rows or columns should be deleted entirely not at all. Use 'replace' method to change individual values in rows")
                    else:
                        if isinstance(val[1],slice):
                            cols = mat.features[val[1]]
                        for col in cols:
                            mat.__delitem__(col)
                else:
                    raise TypeError("Rows or columns should be deleted entirely not at all. Use 'replace' method to change individual values in rows")
                    
        #Boolean matrix given as indeces == remove 0 or more rows
        elif isinstance(val,obj):
            #Assertion
            if val.dim[0] != mat.dim[0]:
                raise ValueError("Dimensions don't match")
            #Remove rows and keep track of how many of them are deleted
            rowinds = [i[0] for i in val.find(1,0)]
            deleted = len(rowinds)
            mat._matrix = [mat._matrix[i] for i in range(mat.dim[0]) if i not in rowinds]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-deleted,mat.dim[1]]