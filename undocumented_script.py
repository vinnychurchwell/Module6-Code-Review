"""Refactored script for processing numeric values and strings."""


def process_numbers(numbers):
    """Return processed numbers using an alternating transformation.

    Args:
        numbers: A list of numeric values to process.

    Returns:
        A list in which values at odd indexes are reduced by four and
        values at even indexes remain unchanged.
    """
    # Keep this simple transformation in one expression for readability.
    return [
        number if index % 2 == 0 else number - 4
        for index, number in enumerate(numbers)
    ]


def process_strings(words):
    """Convert selected words to uppercase.

    Args:
        words: A list of strings to process.

    Returns:
        A list with banana, grapefruit, and cherry converted to uppercase.
    """
    uppercase_words = {"banana", "grapefruit", "cherry"}
    return [
        word.upper() if word in uppercase_words else word
        for word in words
    ]


def main():
    """Run the examples and display processed numbers and strings."""
    numbers = [3, 8, 9, 12, 15, 16, 21]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(words)

    print(f"Processed Numbers: {processed_numbers}")
    print(f"Processed Strings: {' '.join(processed_strings)}")


if __name__ == "__main__":
    main()
