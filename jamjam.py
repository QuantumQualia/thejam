#init

def consecutive_mismatches(str1, str2, threshold=5):
    current_count = 0
    max_count = 1  # Initialize to 1 to handle the case of no consecutive mismatches
    total_count_threshold = 0  # Initialize count of consecutive mismatches with threshold
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            current_count += 1
            max_count = max(max_count, current_count)
            if current_count >= threshold:
                total_count_threshold += 1
        else:
            current_count = 0  # Reset the count if consecutive characters match
    return max_count, current_count, total_count_threshold

def generate_repeating_string(pattern, length):
    repeated_string = ""
    while len(repeated_string) < length:
        repeated_string += pattern
    return repeated_string[:length]  # Trim the excess if it's longer than needed

# Example usage
str1 = "xooooxxoxoxxxoxxoxoxoxxoooxoooooxxxxxxxoxxxxxooxxxxxxxxxxooxxxoooxxooxxxxxoxxoxoxoxoxoxxxxxoxxoxoxoxoxoxxxooxoxxxxooxooxoxxooxxoxoxxoxooooooxoooxooxoooxxoxxoxooxxoxxxxxooxoxoxooxxxoxxoxooxxoxoooxoxoxxxxxxxooxxoxxxxoxooxoooxooxxxxxooxooxxxoxxxooxxxxoooxxoxxoxooooox"


# Example usage
desired_length = len(str1)
pattern = "oxoxooxx"
repeated_string = generate_repeating_string(pattern, desired_length)
print(f"Repeating String: {pattern}")

str2 = repeated_string

max_count, current_count, total_count_threshold = consecutive_mismatches(str1, str2)
print(f"Longest press for {pattern} is: {max_count}")
# print(f"The current consecutive mismatch count is: {current_count}")
print(f"Press of 5 or more count is: {total_count_threshold}")
