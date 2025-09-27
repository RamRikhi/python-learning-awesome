nums = [1, 2, 3]
prices = [10.0, 20.4, 30.6]
names = ['John', 'Michael', 'Sarah']
values = [24, 'Rikhi', '34.5']

collections = [nums, prices, names, values]

# Append at the end
nums.append(4)

# insert based on given index number
nums.insert(2, 5)

# remove element which you want to remove it like 5
nums.remove(5)

# remove element based on index
nums.pop(1)

nums.extend([2,4,6,8])

print(min(nums))
print(max(nums))
print(len(nums))
print(sorted(nums))
print(sorted(nums, reverse=True))
print(sorted(nums, reverse=True, key=lambda num: num))
print(sum(nums))



print(nums)
print(prices)
print(names)
print(values)
print(collections)

nums = [1, 2, 3, 4, 5]

del nums[2:4]
print(nums)