def molemass2(compound):
    elements = ["H", "C", "N", "O", "P", "S", "K", "F"]
    MW = [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
    dict1=dict(zip(elements,MW))
    mass = 0
    for i in range(len(compound)):
        if compound[i].isdigit() == True:
            mass+=dict1[compound[i-1]]*(int(compound[i])-1)
        else:
            mass+=dict1[compound[i]]
    return mass