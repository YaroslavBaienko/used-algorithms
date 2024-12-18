from algoritms import boyer_moore_majority_vote, population, fitness, boyer_moore_text_pattern

if __name__ == "__main__":
    presidents = ['Donald Trump'] * 245
    presidents += [
        "George Washington", "John Adams", "Thomas Jefferson", "James Madison",
        "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
        "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
        "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
        "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",
        "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland",
        "William McKinley", "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson",
        "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt",
        "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson",
        "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",
        "Bill Clinton", "George W. Bush", "Barack Obama", "Joe Biden"
    ]
    print(boyer_moore_majority_vote(presidents))

    # Get the best individual after the last generation.
    best = max(population, key=fitness)
    print("Best individual:", best, "Fitness:", fitness(best))

    # Example usage
    text = "HERE IS A SIMPLE EXAMPLE"
    pattern = "EXAMPLE"
    index = boyer_moore_text_pattern(text, pattern)
    print(f"Pattern found at index: {index}")  # Output should be the starting index of "EXAMPLE" in text