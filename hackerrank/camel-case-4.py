##
#### Camel Case 4 (hard)
############################


def camel_case(method, name_type, string):
    # combine
    if method == "C":
        string = string.split(" ")
        if name_type == "M":
            print("{}{}()".format(string[0], ("".join(x.title() for x in string[1:]))))
        if name_type == "C":
            print("".join(x.title() for x in string))
        if name_type == "V":
            print("{}{}".format(string[0], ("".join(x.title() for x in string[1:]))))

    # split
    if method == "S":
        result, temp = [], ""
        for char in string.replace("()", ""):
            if char.isupper():
                if temp:
                    result.append(temp)
                temp = char.lower()
            else:
                temp += char
        result.append(temp)

        print(" ".join(result))


## Tests
############

test1 = [
    "S;V;iPad",  # i pad
    "C;M;mouse pad",  # mousePad()
    "C;C;code swarm",  # CodeSwarm
    "S;C;OrangeHighlighter",  # orange highlighter
]
test2 = [
    "C;V;can of coke",  # canOfCoke
    "S;M;sweatTea()",  # sweat tea
    "S;V;epsonPrinter",  # epson printer
    "C;M;santa claus",  # santaClaus()
    "C;C;mirror",  # Mirror
]
