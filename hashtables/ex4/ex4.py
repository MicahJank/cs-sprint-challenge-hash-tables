    # a is a list of numbers
    # both negative and positive values present
    # i need to find the numbers that have both negative and positive values in the list
    # can use the abs() to get the absolute
    # can use if num < 0 to determine if the number is negative
    # im assuming there are no duplicate numbers

    # PLAN
    # create a dictionary to store the values that have both negaitve and positive values
    # take the list and loop over it
    # take the absolute value of the current number and check if it is in the dict
    # if it is: set its value to true
    # if it isnt: add it to the dict
    # loop over the dict and add any numbers that have a true value to the results list
    # return the list
# def has_negatives(a):
#     nums = {}
#     result = []
    
#     for num in a:
#         if abs(num) in nums:
#             nums[abs(num)] = True
#         else:
#             nums[abs(num)] = False
    
#     for key, value in nums.items():
#         if value == True:
#             result.append(key)
#     return result


# new version - significant time reduction from 1.7s to 0.7s
def has_negatives(a):
    nums = {}
    result = []
    
    for num in a:
        if num > 0:
            nums[num] = num
    
    for num in a:
        if num < 0 and abs(num) in nums:
            result.append(nums[abs(num)])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
