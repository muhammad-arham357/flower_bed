flower_bed = [1, 0, 0, 0, 1]

for i in range(len(flower_bed)-2):  
    if flower_bed[i+2] == 0 and flower_bed[i+1] == 0 and flower_bed[i+3] == 0:
        flower_bed[i+2] = 1
print(flower_bed)

