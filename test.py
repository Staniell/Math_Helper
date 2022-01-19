# sample_space = []
# possible_sum = []
# for i in range(1,13):
#     for j in range(1,13):
#         sample_space.append([i,j])
#         if i+j == 18:
#             possible_sum.append([i,j])
# print(len(sample_space))
# print(len(possible_sum))
# print(min([25     ,55     ,60    ,74     ,15     ,66     ,23     ,30     ,65
# ,22     ,8     ,13    ,20     ,25     ,55     ,30     ,58]))
# data = "2 4 6 8 "
# data = data.strip()
# data = list(map(int, data.split(" ")))
# print(data)
import ast
x = ast.literal_eval("{70,{range(40,50):[3], range(50,60):[5], range(60,70):[6], range(70,80):[9],range(80,90):[8],range(90,100):[7]}}")
print(x)