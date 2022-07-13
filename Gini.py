import numpy as np

#Unosimo listu atributa (zadnja lista je odluka)
list = np.array([["sunce","sunce","vjetar","kiša","kiša","kiša","vjetar","vjetar","vjetar","sunce"],
                 ["da","ne","da","da","ne","da","ne","ne","da","ne"],
                 ["bogat","bogat", "bogat", "siromašan", "bogat", "siromašan", "siromašan", "bogat", "bogat", "bogat"],
                 ["kino", "tenis","kino",  "kino","doma","kino","kino",  "šoping","kino",  "tenis"]
                 ])
                 

#Podjelimo listu na odluku i atribute
h,w = list.shape
features = np.array(list[0:h-1])
decision = np.array(list[h-1:])
h,w = features.shape

#For loop nađe weight i unique iteme
weight_total = []
for i in range(h):
    #MAIN
    key = ""
    weight_column = []
    for i1 in features[i]:
        weight = 0
        if key == "":
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
            a = 0
            y = decision[:,cnt][0]
            index = 0
            if x == key:                
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


#Calculate ginny for columns
table_ginny=[]
for i in index_list_final:
    row_ginny=[]  
    for i1 in i:
        x = sum(i1)
        G = 0
        for i2 in i1:
            G = G + (i2/x)**2
        row_ginny.append(1-G)
    table_ginny.append(row_ginny)

final_ginny_table=[]
c=0
for i in table_ginny:
    c1=0
    ginny=0.0
    for i1 in i:
        ginny = ginny + (i1*table_weights_normalized[c][c1])
        c1+=1
    final_ginny_table.append(ginny)
    c+=1

#Rezultat
print("Ginny vrijednosti stupaca tablice: ",final_ginny_table)






    
    
    


            
            
