from cs50 import get_string
import string

text = get_string("Text: ")

flag = True
letter, word, sen = 0, 0, 0

# iterate through the string
for ch in text:
    # counting letter
    if ch in string.ascii_letters:
        letter += 1
        # counting word
        if flag:
            word += 1
            flag = False
    elif ch == ' ':
        flag = True
    # counting sentence
    elif ch in ['.', '!', '?']:
        flag = True
        sen += 1
# end for
L = (100.0 * letter) / word
S = (100.0 * sen) / word
X = 0.0588 * L - 0.296 * S - 15.8

if X < 1:
    print("Before Grade 1")
elif X >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(X)}")