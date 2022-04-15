def get_input():
    n=int(input("Enter the number of elements"))
    data=[]
    for item in range(0,n):
        data.append(int(input()))

    return data

def sorter_asc(data):
    data.sort()
    return data

def sorter_dsc(data):
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if data[i]<data[j]:
                data[i],data[j]=data[j],data[i]
            else:
                continue
    return data


print(sorter_asc(get_input()))
 


   
