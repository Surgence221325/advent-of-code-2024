with open('pairs.txt', 'r') as file:
    map1 = {}
    map2 = {}
    dist = 0
    
    for line in file:
        
        numbers = line.strip().split()
        val1 = int(numbers[0])
        val2 = int(numbers[1])

        if val1 in map1:
            map1[val1] += 1
        else:
            map1[val1] = 1
        
        if val2 in map2:
            map2[val2] += 1
        else:
            map2[val2] = 1
    for k, v in map1.items():
        if k in map2:
            dist += v * k * map2[k]
    print(dist)