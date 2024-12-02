def is_valid(nums):
    first = True
    second = True
    positive = True
    prev = 0
    for n in nums:
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
                        return False
                    second = False
                else:
                    curRes = n - prev
                    if curRes > 0 and positive and abs(curRes) > 0 and abs(curRes) < 4:
                        prev = n
                    elif curRes < 0 and not positive and abs(curRes) > 0 and abs(curRes) < 4:
                        prev = n
                    else: 
                        return False
    return True
                        

with open('levels.txt', 'r') as file:
    res = 0
    for line in file:
        nums = line.strip().split()
        if is_valid(nums):
            res += 1
        else: 
            for i in range(len(nums)):
                modified_nums = nums[:i] + nums[i+1:]
                if is_valid(modified_nums):
                    res += 1
                    break
    print(res)

        
                    
                    



                



