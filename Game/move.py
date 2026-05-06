def crd_to_rowcol(xy_tuple):
    # for x:350-1150 y:0-800
    '''if xy_tuple[0]>1150 or xy_tuple[0]<350 or xy_tuple[1]>800 or xy_tuple[1]<0:
        return 'not available coordinate'

    cul = int((xy_tuple[0] - 350)/100)
    row = int((xy_tuple[1]/100))
    return (row,cul)'''

    """ Implemented for 800x800 screen """
    if xy_tuple[0]>800 or xy_tuple[0]<0 or xy_tuple[1]>800 or xy_tuple[1]<0:
        return 'not available coordinate'

    cul = int((xy_tuple[0])/100)
    row = int((xy_tuple[1]/100))
    return (row,cul)



def rowcol_to_crd(pos_tuple): # returns the center of the postion
    # for x:350-1150 y:0-800
    '''if pos_tuple[0]>7 or pos_tuple[0]<0 or pos_tuple[1]>7 or pos_tuple[1]<0:
         return 'not available row or cul'
    y = 350 + (pos_tuple[0]+1)*100 - 50
    x = (pos_tuple[1]+1)*100 - 50
    return (x,y)'''

    """ Implemented for 800x800 screen """
    if pos_tuple[0] > 7 or pos_tuple[0] < 0 or pos_tuple[1] > 7 or pos_tuple[1] < 0:
        return 'not available row or cul'

    row = (pos_tuple[1] + 1) * 100 - 50
    col = (pos_tuple[0] + 1) * 100 - 50

    return (row,col)





