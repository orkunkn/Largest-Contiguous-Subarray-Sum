import random   # Import random class to create a list with random numbers
# Import time class to calculate the required time for an algorithm
from time import perf_counter

# A program to find the sum of contiguous subarray of numbers which has the largest sum

# Function with O(N^2) time complexity


def n_square(list):
    max = -1000000
    length = len(list)
    start_time = perf_counter()
    for i in range(length):
        n = list[i]
        if n > max:
            max = n
            start_index, end_index = i, i
        for k in range(i+1, length):
            n = n + list[k]
            if n > max:
                max = n
                start_index = i
                end_index = k
    end_time = perf_counter()
    print("----- N square -----")
    print("Maximum subarray sum =", max)
    print("Contiguous subarray between indexes", start_index, "and", end_index)
    print("Calculation time with", length, "length is",
          (end_time-start_time)*10**3, "ms")

# Function with O(Nlog(N)) time complexity


def n_logn(list):
    print("----- N log(N) -----")
    start_time = perf_counter()
    max_sum = find_max_sum(list, 0, len(list)-1)
    print("Maximum subarray sum =", max_sum)
    end_time = perf_counter()
    print("Calculation time with",
          len(list), "length is", (end_time-start_time)*10**3, "ms")


def find_max_sum(list, start_index=None, end_index=None):

    if start_index is None and end_index is None:
        start_index, end_index = 0, len(list) - 1

    if start_index == end_index:
        return list[start_index]

    mid = (start_index + end_index) // 2

    left_max = -1000000
    total = 0
    for i in range(mid, start_index - 1, -1):
        total += list[i]
        if total > left_max:
            left_max = total
            start = i

    right_max = -1000000
    total = 0

    for i in range(mid + 1, end_index + 1):
        total += list[i]
        if total > right_max:
            right_max = total
            end = i

    left_right_max = max(find_max_sum(list, start_index, mid),
                         find_max_sum(list, mid + 1, end_index))

    if mid == len(list)/2 - 1:
        print("Contiguous subarray between indexes",
              start, "and", end)

    return max(left_right_max, left_max + right_max)


# Function with O(N) time complexity


def n(list):
    max = -1000000
    n, temp = 0, 0
    start_time = perf_counter()
    for i in range(len(list)):
        n += list[i]
        if n > max:
            max = n
            start_index = temp
            end_index = i
        if n < 0:
            n = 0
            temp = i + 1
    end_time = perf_counter()
    print("----- N -----")
    print("Maximum subarray sum =", max)
    print("Contiguous subarray between indexes", start_index, "and", end_index)
    print("Calculation time with",
          len(list), "length is", (end_time-start_time)*10**3, "ms")

# Function to create array


def create_list(length):
    list = []
    for i in range(length):
        if random.random() < 0.5:
            sign = -1
        else:
            sign = 1
        random_number = int(random.random() * 10000) * sign
        list.insert(i, random_number)
    return list


length = 10
i = 0
while i < 9:
    list = create_list(length)
    n_square(list)
    n_logn(list)
    n(list)
    if i % 2 == 0:
        length = length * 5
    else:
        length = length * 2
    i += 1
