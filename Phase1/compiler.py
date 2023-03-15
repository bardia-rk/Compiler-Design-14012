keywords = ["if", "else", "void", "int", "repeat", "break", "until", "return"]
symbols = [";", ":", "[", "]","(", ")", "{", "}", "+", "-", "*", "=", "<", "==", "/"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z",
          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]


def get_numbers(inp):
    foundNums = []
    parts = inp.split(" ")
    number = ""
    for i in range(0,len(parts)):
        for j in range(0,len(parts[i])):
            if parts[i][j] in nums and j != len(parts[i])-1:
                number += parts[i][j]
            elif parts[i][j] in nums and j == len(parts[i])-1:
                number += parts[i][j]
                foundNums.append(number)
                number=""
            elif parts[i][j] in letters:
                break
            else:
                foundNums.append(number)
                number=""
    
    return foundNums
                
        

    return foundNums

def get_symbols(inp):
    foundSymbols = []
    for i in range(0,len(inp)):
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
            if i == len(inp)-1:
                foundSymbols.append("=")
            else:
                if inp[i+1]=="=":
                    foundSymbols.append("==")
                    i += 1
                else:
                    foundSymbols.append("=")
            
    return foundSymbols

def get_keywords(inp):
    found_keywords = []
    words = inp.split(" ")
    for i in range (0,len(words)):
        if words[i] in keywords:
            found_keywords.append(words[i])
    return found_keywords

print(get_numbers("123 123"))

# def get_next_token():
#     inputs = open("input.txt").readlines()