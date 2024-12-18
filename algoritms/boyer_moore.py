def boyer_moore_majority_vote(arr):
    candidate = None  # Initialize the candidate to None
    count = 0  # Initialize the count of votes for the candidate to zero

    # First pass: find a potential majority candidate
    for num in arr:
        if count == 0:
            # No current candidate, so select the current element as the new candidate
            candidate = num
            count = 1  # Set the count for this new candidate to 1
        elif num == candidate:
            # Current element is the same as the current candidate, increment the vote count
            count += 1
        else:
            # Current element is different from the candidate, decrement the vote count
            count -= 1

    # Second pass: verify if the candidate is actually the majority element
    if arr.count(candidate) > len(arr) // 2:
        # Count how many times the candidate appears in the array
        # If it appears more than half the time, return it as the majority element
        return candidate
    else:
        # If no element appears more than half the time, return None
        return None



