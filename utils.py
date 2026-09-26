def is_palindrome(s):
    """
    Check whether a string is a palindrome.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]
def count_words(text):
    """
    Count the number of words in a text.
    """
    return len(text.split())
def celsius_to_fahrenheit(c):
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return (c * 9 / 5) + 32
# --- Simple testing section ---
print(is_palindrome("madam"))
print(count_words("Python is easy"))
print(celsius_to_fahrenheit(25))