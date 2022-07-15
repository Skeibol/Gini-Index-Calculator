import numpy as np
#GINI za kompleksnije 
#---------RESHAPE----------

#data = np.array(data)
#print(data.transpose())  -> flipa axis
#data = data.transpose()
#ginii



#Unosimo listu atributa (zadnja lista je odluka)
list = np.array([["F1Cat1", "F1Cat1", "F1Cat2", "F1Cat3", "F1Cat3", "F1Cat3", "F1Cat2", "F1Cat1", "F1Cat1", "F1Cat3", "F1Cat1", "F1Cat2", "F1Cat2", "F1Cat3"],
                 ["F2Cat1", "F2Cat1", "F2Cat1", "F2Cat2", "F2Cat3", "F2Cat3", "F2Cat3", "F2Cat2", "F2Cat3", "F2Cat2", "F2Cat2", "F2Cat2", "F2Cat1", "F2Cat2"],
                 ["F3Cat1", "F3Cat1", "F3Cat1", "F3Cat1", "F3Cat2", "F3Cat2", "F3Cat2", "F3Cat1", "F3Cat2", "F3Cat2", "F3Cat2", "F3Cat1", "F3Cat2", "F3Cat1"],
                 ["F4Cat1", "F4Cat2", "F4Cat1", "F4Cat1", "F4Cat1", "F4Cat2", "F4Cat2", "F4Cat1", "F4Cat1", "F4Cat1", "F4Cat2", "F4Cat2", "F4Cat1", "F4Cat2"],
                 ["KL1",    "KL1",    "KL2",    "KL2",    "KL2",    "KL1",    "KL2",    "KL1",    "KL2",    "KL2",    "KL2",    "KL2",    "KL2",    "KL1"]
                 ])
                 
head = ["F1", "F2", "F3", "F4", "K"]

#Podjelimo listu na odluku i atribute
h,w = list.shape
features = np.array(list[0:h-1])
decision = np.array(list[h-1:])
h,w = features.shape

#For loop nađe weight i unique iteme

weight_total = []

for i in range(h):
    #MAIN
    key = None
    weight_column = []
    for i1 in features[i]:
        weight = 0
        if key == None:
            key = i1
        elif key == i1:
            continue
        else:
            key = i1
        for i2 in features[i]:
            if i2 == key:
                weight+=1

        if [key, weight] not in weight_column:
            weight_column.append([key,weight])

    
    weight_total.append(weight_column)

#For loop koji vraca listu parova za određeni atribut

cnt_1 = 0
index_list_final=[]

for i in weight_total:
    index_list=[]
    for i1 in i:
        key = i1[0]
        cnt = 0
        decided=[]
        amounts=[]
        for x in features[cnt_1]:
            if x == key:                
                y = decision[:,cnt][0]
                index = 0
                a = 0
                if decided==[]:
                    decided.append(y)
                    while a<w:
                        if features[:,a][cnt_1] == key and decision[:,a][0] == y:
                            index+=1
                        a+=1
                        
                elif y not in decided:
                    decided.append(y)
                    while a<w:
                        if features[:,a][cnt_1] == key and decision[:,a][0] == y:
                            index+=1
                        a+=1
                
                if index!=0:
                    amounts.append(index)
            cnt+=1

        index_list.append(amounts)
    
    index_list_final.append(index_list)                
    cnt_1+=1

#Get weights

table_weights=[]

for i in weight_total:
    row_weight=[]
    for i1 in i:
        row_weight.append(i1[1])
    table_weights.append(row_weight)

#Normalize weights

table_weights_normalized=[]

for i in table_weights:
    x = sum(i)
    row_weight=[]
    for i1 in i:
        row_weight.append(i1/x)
    table_weights_normalized.append(row_weight)


#Calculate gini for columns

table_gini=[]

for i in index_list_final:
    row_gini=[]  
    for i1 in i:
        x = sum(i1)
        G = 0
        for i2 in i1:
            G = G + (i2/x)**2
        row_gini.append(1-G)
    table_gini.append(row_gini)

#Apply weights to calculated values

final_gini_table=[]
c=0

for i in table_gini:
    c1=0
    gini=0.0
    for i1 in i:
        gini = gini + (i1*table_weights_normalized[c][c1])
        c1+=1
    final_gini_table.append(gini)
    c+=1

#Rezultat 

print("Gini vrijednosti stupaca tablice: ")
for i, j in zip(head,final_gini_table):
    print(i,j)






    
    
    


            
            
