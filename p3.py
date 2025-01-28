def count_subarrays_with_sum(arr, sum):
    initial_sums = {0:1}
    result = 0
    current_sum = 0

    for val in arr:
        current_sum += val

        if (current_sum - sum) in initial_sums:
            result += initial_sums[current_sum - sum]

        initial_sums[current_sum] = initial_sums.get(current_sum, 0) + 1
    
    return result