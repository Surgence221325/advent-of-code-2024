with open('levels.txt', 'r') as file:
    res = 0
    for line in file:
        numbers = line.strip().split()
        first = True
        second = True
        valid = True
        positive = True
        prev = 0
        for n in numbers:
            n = int(n)
            if first:
                prev = n
                first = False
            else:
                if second:
                    curRes = n - prev
                    prev = n
                    if curRes > 0 and abs(curRes) > 0 and abs(curRes) < 4:
                        positive = True
                    elif curRes < 0 and abs(curRes) > 0 and abs(curRes) < 4:
                        positive = False
                    else:
                        valid = False
                        break
                    second = False
                else:
                    curRes = n - prev
                    if curRes > 0 and positive and abs(curRes) > 0 and abs(curRes) < 4:
                        prev = n
                    elif curRes < 0 and not positive and abs(curRes) > 0 and abs(curRes) < 4:
                        prev = n
                    else:
                        valid = False
                        break
        if valid:
            res += 1
    print(res)
                    
                    



                



