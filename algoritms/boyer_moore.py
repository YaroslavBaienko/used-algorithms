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


def boyer_moore_text_pattern(text, pattern):
    """
    Performs the Boyer-Moore string search algorithm on given text with a specific pattern.

    Parameters:
        text (str): The text in which to search for the pattern.
        pattern (str): The pattern to search for in the text.

    Returns:
        int: The index of the start of the pattern in the text, or -1 if the pattern is not found.
    """

    # Lengths of the text and the pattern
    n, m = len(text), len(pattern)

    # Generate the bad character shift values
    bad_char = get_bad_char_shift(pattern)

    # Generate the good suffix shift values
    good_suffix = get_good_suffix_shift(pattern)

    # Index at which to start the pattern in the text
    i = 0

    while i <= n - m:
        # Start comparing from the end of the pattern
        j = m - 1

        # Decrease j while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # If the pattern is completely found, return its start index
        if j < 0:
            return i
        else:
            # Calculate the shift using the maximum value given by bad character and good suffix rules
            i += max(good_suffix[j], j - bad_char.get(text[i + j], -1))

    return -1

def get_bad_char_shift(pattern):
    """
    Creates the bad character shift table used by the Boyer-Moore algorithm.

    Parameters:
        pattern (str): The pattern to generate the bad character shifts for.

    Returns:
        dict: A dictionary with each character in the pattern and its last occurrence index.
    """
    shift = {}
    for index, char in enumerate(pattern):
        shift[char] = index
    return shift

def get_good_suffix_shift(pattern):
    """
    Creates the good suffix shift table used by the Boyer-Moore algorithm.

    Parameters:
        pattern (str): The pattern to generate the good suffix shifts for.

    Returns:
        list: A list containing the shift sizes for each position in the pattern.
    """
    m = len(pattern)
    good_suffix = [0] * m
    border = [0] * (m + 1)

    # Position of the rightmost occurrence of the suffix which is also a prefix
    i = m
    j = m + 1
    border[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j - 1] == 0:
                good_suffix[j - 1] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    # Case where the suffix becomes a prefix
    j = border[0]
    for i in range(m):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border[j]

    return good_suffix



