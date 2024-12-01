
with open('pairs.txt', 'r') as file:
    list1 = []
    list2 = []
    dist = 0
    
    for line in file:
        
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        dist += abs(list1[i] - list2[i])
    print(dist)

