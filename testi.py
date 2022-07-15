import numpy as np


l=np.array([["A","A","B","A","C","B"],["plava","zuta","zuta","plava","crvena","crvena"]])
l_uniques_total=[]
for i in l:
    l_uniques=[]
    for i1 in i:
        if i1 not in l_uniques:
            l_uniques.append(i1)
    l_uniques_total.append(l_uniques)



l_new_column_total = []
c=0
for i in l_uniques_total:
    l_new_column=[]
    for i1 in i:
        l_row=[]
        for i2 in l[c]:
            if i2==i1:
                l_row.append(1)
            else:
                l_row.append(0)
        l_new_column.append(l_row)
    c+=1
    l_new_column_total.append(l_new_column)

for i, j in zip(l_new_column_total,l_uniques_total):
    print(i , j)





