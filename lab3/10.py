def uni_list():
    for i in range(len(nums)):
        unums.append(nums[i])
        if nums[i] == nums[i - 1]:
            unums.pop()
            
    print(unums)

x = int(input())
nums = []
unums = []
for i in range(x):
    nums.append(int(input()))

uni_list()