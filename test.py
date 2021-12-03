def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

def percentile(k,data):
    first_index = get_nth_key(data, 0)
    data[first_index].append(data[first_index][0])
    data[first_index].append(range(1,data[first_index][0]))

    n = 0
    ctr = -1
    for i in data:
        n+=data[i][0]
        if len(data[i]) == 1:
            data[i].append(data[get_nth_key(data,ctr)][1] + data[i][0])
            data[i].append(range(data[get_nth_key(data,ctr)][1]+1,data[i][1]))
        ctr+=1
    location = (k*n)//100
    ctr = 0


    for i in data:
        if location in list(data[i][2]):
            l = i[0] - .5
            cf = data[get_nth_key(data,ctr-1)][1]
            f = data[i][0]
            h = min(i) - min(get_nth_key(data, ctr-1))
        ctr+=1

    P = l +((k*n/100)-cf)/f*h
    print(P)
    
    # print(data, location)

percentile(35,{range(40,50):[3], range(50,60):[5], range(60,70):[6], range(70,80):[9],
range(80,90):[8],range(90,100):[7]})
# data = {range(40,50):[3], range(50,60):[4]}
# print(data[get_nth_key(data, 1)])