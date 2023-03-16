keywords = ["if", "else", "void", "int", "repeat", "break", "until", "return"]
symbols = [";", ":", "[", "]", "(", ")", "{", "}", "+", "-", "*", "=", "<", "==", "/"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def get_numbers(inp):
    foundNums = []
    i = 0
    start = 0
    flag = False
    while i < len(inp):

        if inp[i] in nums and not flag:
            start = i
            flag = True
        elif inp[i] in letters and flag:
            flag = False
        elif not (inp[i] in nums or inp[i] in letters) and flag:
            foundNums.append(inp[start:i])

        i += 1

    return foundNums


def get_symbols(inp):
    foundSymbols = []
    i = 0
    while i < len(inp):
        if inp[i] == ":":
            foundSymbols.append(":")
        elif inp[i] == ";":
            foundSymbols.append(";")
        elif inp[i] == ",":
            foundSymbols.append(",")
        elif inp[i] == "*":
            foundSymbols.append("*")
        elif inp[i] == "[":
            foundSymbols.append("[")
        elif inp[i] == "{":
            foundSymbols.append("{")
        elif inp[i] == "(":
            foundSymbols.append("(")
        elif inp[i] == ")":
            foundSymbols.append(")")
        elif inp[i] == "}":
            foundSymbols.append("}")
        elif inp[i] == "]":
            foundSymbols.append("]")
        elif inp[i] == "<":
            foundSymbols.append("<")
        elif inp[i] == ">":
            foundSymbols.append(">")
        elif inp[i] == "=":
            if i == len(inp) - 1:
                foundSymbols.append("=")
            else:
                if inp[i + 1] == "=":
                    foundSymbols.append("==")
                    i += 1
                else:
                    foundSymbols.append("=")
        i += 1

    return foundSymbols


# def get_keywords(inp):
    # found_keywords = []
    # words = inp.split(" ")
    # for i in range(0, len(words)):
    #     if words[i] in keywords:
    #         found_keywords.append(words[i])
    # return found_keywords


print(get_numbers("if(b==1123){"))

# def get_next_token():
#     inputs = open("input.txt").readlines()
