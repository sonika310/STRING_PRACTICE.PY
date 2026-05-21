# Task 1: Remove Vowels
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return "".join([char for char in input_string if char not in vowels])

print(remove_vowels("Hello World"))


# Task 2: Capitalize Full Name
user_name = input("Enter your full name: ")
print(f"Hello, {user_name.title()}!")


# Task 3: Split Words and Find Length
sentence = input("Enter a sentence: ")
for word in sentence.split():
    print(f"Word: {word}, Length: {len(word)}")