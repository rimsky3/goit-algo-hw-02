from collections import deque

def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalpha())
    char_deque = deque(cleaned)


    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":

    test_string = [
        "racecar",
        "madam",
        "abba",
        "hello",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "Python",
        ]
    
    print("=" * 40)
    for text in test_string:
        result = is_palindrome(text)
        print(f"'{text}' -> {'Palindrome' if result else 'Not a palindrome'}")