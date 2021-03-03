#1==================================
def calculate(min, max):
    print(f"min: {min} max: {max}")
    sum=0
    for a in range(min,max+1):
        sum+=a
    print(sum)

calculate(1,3)
calculate(4,8)

#你的程式要能夠計算 1+2+3，最後印出 6 calculate(4, 8)​ # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#2==================================
def avg(data):
    sum=0
    for i in data['employees']:
        sum+=i['salary']
    average=sum/data['count']
    print(average)

avg({"count":3, "employees":[{"name":"John","salary":30000 },
{"name":"Bob","salary":60000 },
{"name":"Jenny","salary":50000 }]
})

#3==================================

def maxProduct(nums):
    print(f"input: {nums}")
    max1=0
    max2=0
    min1=0
    min2=0
    max=1
    for num in nums:
        if len(nums)<3:
            max=max*num
        if len(nums)>=3:
            if num>0:
                if num>max1:
                    if num>max2:
                        max2=max1
                    max1=num
                elif num<max1 and num>=max2:
                    max2=num
            elif num<0:
                if num<min1:
                    if num<min2:
                        min2=min1
                    min1=num
                elif num<min2 and num>=min1:
                    min2=num
        # print(min1,min2)
        # print(max1,max2,min1,min2)
    if(len(nums)<3):
        print(max)
    elif max1*max2>=min1*min2:
        print(max1*max2)
    elif min1*min2>=max1*max2:
        print(min1*min2)


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-3, 1])
#4==================================

def twoSum(nums, target):
    print(f"nums: {nums}, taget: {target} ")
    for num in nums:
        pair = target- num
        if pair in nums:
            num=nums.index(num)
            pair=nums.index(pair)
            return [num,pair]
      
    
result=twoSum([2,11,7,15],9)
print(result)
# show [0, 2] because nums[0]+nums[2] is 9

#5==================================
def maxZeros(nums):
    t=0
    higes_t=0
    print(f"input: {nums}")
    if nums[-1]==0:
        nums.append(1)
        for num in nums:
            if num == 1:
                if higes_t>t:
                    higes_t=higes_t
                elif higes_t<t:
                    higes_t=t
                    t=0
            if num == 0:
                t+=1
    print(higes_t)
        
maxZeros([0,1,0,0])    
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1, 1, 1, 1, 1]) 
 