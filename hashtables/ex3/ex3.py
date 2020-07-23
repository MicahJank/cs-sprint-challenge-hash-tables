# was able to successfully lower time to complete from 5 seconds to 1.2
# time complexity is O(n) i believe

# basically take the first array and assign its values to the count dictionary
# i can then take the other arrays and only add to the count dictionary counter if the value is in both the array and count dictionary
# at the end i can compare the counts in the count dictionary to the number of arrays - if they are the same it means
# that number was in all the arrays
def intersection(arrays):
    number_of_arrays = len(arrays)
    results = []
    count = {}
    first_array = arrays[0]
    for num in first_array:
        count[num] = 1

    # loop over the remaining arrays and check to see if there are any interestions with the first one
    for i in range(1, number_of_arrays):
        for num in arrays[i]:
            if num in count:
                count[num] += 1
   
    for key, value in count.items():
        if value == number_of_arrays:
            results.append(key)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
