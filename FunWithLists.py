
WhiteList = []

for i in range(0, 3):    
    for ii in range(0, 3):
        for iii in range(0, 3):
            print(f'i = {i} ii = {ii} iii = {iii} ')
            if (ii + iii == 3):
                Result = "Yes!"
                print (f'Yes!')
                MyResultsList =  [i,ii,ii,Result]                
                WhiteList.append(MyResultsList)

print(WhiteList)

# Get x's
for item in WhiteList:
    print(f'x = {item[0]} y = {item[1]} z = {item[2]} Result = {item[3]} ')

    



        

