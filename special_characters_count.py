string=input()
spcl_char=0
for i in range(0,len(string)):
    if(string[i].isalpha()):
        continue
    elif(string[i].isdigit()):
        continue
    elif(string[i]==' '):
        continue
    else:
        spcl_char+=1
print(spcl_char)