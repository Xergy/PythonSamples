
WhiteList = []

for i in range(0, 3):    
    for ii in range(0, 3):
        for iii in range(0, 3):
            print(f'i = {i} ii = {ii} iii = {iii} ')
            if (i == 1):
                Result = "Yes!"
                print (f'Yes!')
                MyResultsList =  [i,ii,ii,Result]                
                WhiteList.append(MyResultsList)

print(WhiteList)


        

