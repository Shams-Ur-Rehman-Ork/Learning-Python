# Step: 1 => We need an array

# Methods => 2
# 1st => get array values from user
# 2nd => Provide static values

arr = [12, 5, 4, 15]


# myNameIsShams => camel
# MyNameIsShams => Pascal

def sumOfNumbers(arrayElements):
    # To store the sum of all elements of array.
    totalSum = 0
    for item in arrayElements:
        totalSum = totalSum + item
    return totalSum


total = sumOfNumbers(arr)
print(total)

#
