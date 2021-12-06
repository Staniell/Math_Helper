import math

class Central_Tendency:

    def mode(self,array):
        # array = [8,9,9,14,8,8,10,7,6,9,7,8,10,14,11,8,14,11]
        print(max(array, key = array.count))
        numbers = {}
        for i in array:
            if i in numbers:
                numbers[i]+=1
            else:
                numbers[i] = 0

        k = dict(sorted(numbers.items(),key=lambda x:x[1],reverse = True))
        print(k)
    

class Variation_Measure:
    def pop_variance(self,data):
        # data = [10,60,50,30,40,20]
        mean = sum(data)/len(data)
        variance = 0

        for i in data:
            variance += (i-mean)*(i-mean)
        variance=variance/len(data)

        print(f'Mean:{mean}\nVariance:{variance}\nSD:{math.sqrt(variance)}')

    def sample_variance(self,data):
        # data = [16,19,15,15,14]
        mean = sum(data)/len(data)
        variance = 0

        for i in data:
            variance += (i-mean)*(i-mean)
        variance=variance/(len(data)-1)

        print(f'Mean:{mean}\nVariance:{variance}\nSD:{math.sqrt(variance)}')

    #z score



    #percentile rank
    def percentile(self,find, scores):
        # find = 12
        # scores = [18,15,12,6,8,2,3,5,20,10]
        new_scores = sorted(scores)
        numbers_below = new_scores.index(12)
        print(new_scores)
        percentile = ((len(new_scores[:6])+0.5)/len(scores))*100
        print(percentile)

class Grouped_Data:

    def get_nth_key(self,dictionary, n=0):
        if n < 0:
            n += len(dictionary)
        for i, key in enumerate(dictionary.keys()):
            if i == n:
                return key
        raise IndexError("dictionary index out of range") 
    
    def mean(self, data):
        pass

    def mode(self,data):
        pass

    def percentile(self,k,data):
        # Add the frequency value of the first index
        first_index = self.get_nth_key(data, 0)
        data[first_index].append(data[first_index][0])
        data[first_index].append(range(1,data[first_index][0]))

        n = 0
        ctr = -1
        # Adding of frequency for the rest of the data 
        # values and their cumulative frequency
        for i in data:
            n+=data[i][0]
            if len(data[i]) == 1:
                data[i].append(data[self.get_nth_key(data,ctr)][1] + data[i][0])
                data[i].append(range(data[self.get_nth_key(data,ctr)][1]+1,data[i][1]))
            ctr+=1
        location = (k*n)//100
        ctr = 0


        for i in data:
            if location in list(data[i][2]):
                if ctr-1 < 0:
                    cf = 0
                else:
                    cf = data[self.get_nth_key(data,ctr-1)][1]
                l = i[0] - .5
                f = data[i][0]
                h = min(i) - min(self.get_nth_key(data, ctr-1))
            ctr+=1

        P = l +((k*n/100)-cf)/f*h
        print(f"l:{l}\tcf:{cf}\nf:{f}\th:{h}\nPercentile:{P}")
    
    def sample_variance(self, data):
        n = 0
        fx = 0
        fx2 = 0
        for i in data:
            n+=data[i][0]
            data[i].append((min(i)+max(i))/2)
            fx += data[i][0]*(min(i)+max(i))/2
            fx2 += data[i][0]*((min(i)+max(i))/2)**2
        
        variance = ((fx2 - ((fx)**2/n)))/(n-1)
        print(f"fx:{fx}\tfx2:{fx2}\nn:{n}\tSample Variance:{variance}\nSample SD:{math.sqrt(variance)}")
        
x = Grouped_Data()

x.sample_variance({range(40,50):[3], range(50,60):[5], range(60,70):[6], range(70,80):[9],
range(80,90):[8], range(90,100):[7]})




# x.percentile(70,{range(40,50):[3], range(50,60):[5], range(60,70):[6], range(70,80):[9],
# range(80,90):[8],range(90,100):[7]})



# x = Variation_Measure()
# x.sample_variance([75, 71, 64, 56, 53, 55, 47, 51, 51, 50, 50, 50, 47])
# print(list(range(1,9)))
# # print(sum([75, 71, 64, 56, 53, 55, 47, 51, 51, 50, 50, 50, 47]))

# # numbers = [27087,37534,32472,19843,29248,37741,30255,28995]
# # print(sorted(numbers))

# # print((29248+30255)/2)

# # print(sum([75, 71, 64, 56, 53, 55, 47, 51, 51, 50, 50, 50, 47])/len([75, 71, 64, 56, 53, 55, 47, 51, 51, 50, 50, 50, 47]))