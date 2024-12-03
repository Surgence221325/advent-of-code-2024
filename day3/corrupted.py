import re
with open('corrupted.txt', 'r') as file:
    ## some version of left and right window pointers for each line?
    res = 0
    for line in file:
        temp = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        print(temp)
        for item in temp:
            print(item)
            l = 0
            r = 1
            while item[l:r] != "mul(":
                r += 1
            l = r
            while item[r] != ",":
                r+= 1
            val1 = item[l:r]
            print(val1)
            l = r + 1
            while item[r] != ")":
                r+= 1
            val2 = item[l:r] 
            print(val2)
            res += int(val1) * int(val2)
    print(res)
    