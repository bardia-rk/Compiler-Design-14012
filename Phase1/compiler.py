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
        elif (inp[i] in letters or inp[i] == "!") and flag:
            flag = False
        elif not (inp[i] in nums or inp[i] in letters) and flag:
            foundNums.append(inp[start:i])
            flag = False
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

a= "if123(12b=321=1123!){"
print(get_numbers(a))
print(get_symbols(a))

# def get_next_token():
#     inputs = open("input.txt").readlines()
