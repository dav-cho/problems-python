##
#### Stop gninnipS My sdroW! (6 kyu)
########################################

def spin_words(sentence):
    result = []

    for word in sentence.split(" "):
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    sentence = " ".join(result)

    return sentence


## Tests
############

print(spin_words("Hey fellow warriors"))   # "Hey wollef sroirraw" 
print(spin_words("This is a test"))        # "This is a test" 
print(spin_words("This is another test"))  # "This is rehtona test"
print(spin_words("Welcome"))               # "emocleW"
