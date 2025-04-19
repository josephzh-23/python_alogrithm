from collections import defaultdict

'''


'''
def process_queries(data, query):
    # Step 1: Initialize frequency map and compute initial sum
    freq_map = defaultdict(int)
    current_sum = 0

    # Fill the frequency map and calculate the initial sum
    for num in data:
        freq_map[num] += 1
        current_sum += num

    # Step 2: Process each query
    result = []
    for old_val, new_val in query:
        if old_val != new_val:  # Only update if the values are different
            if old_val in freq_map:
                count_old = freq_map[old_val]
                current_sum -= old_val * count_old  # Remove old value's contribution
                freq_map[old_val] = 0  # Set old value count to zero

            freq_map[new_val] += count_old  # Add new value's count
            current_sum += new_val * count_old  # Add new value's contribution

        result.append(current_sum)  # Store the current sum after the update

    return result


# Example usage
data = [6, 2, 4, 6, 8, 10, 12, 5, 2]
query = [[2, 3], [5, 6], [8, 2], [4, 5], [6, 9]]

# Get the result
result = process_queries(data, query)
print(result)  # Expected Output: [43, 43, 37, 38, 41]