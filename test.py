sample_space = []
possible_sum = []
for i in range(1,13):
    for j in range(1,13):
        sample_space.append([i,j])
        if i+j == 18:
            possible_sum.append([i,j])
print(len(sample_space))
print(len(possible_sum))
