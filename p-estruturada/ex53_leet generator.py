def main():

    while True:
        opcao = menu()

        if opcao == "1":
            text = input("Insert text to Encode: \n")
            leetText = encode(text)
            print(leetText)
        elif opcao == "2":
            text = input("Insert text to Decode: \n")
            decodeText = decode(text)
            print(decodeText)
        elif opcao == "3":
            print("exiting......")
            break
        else:
            print("please select a valid option!")

def menu():
    print("======== l337 93N3r47()r ========")
    print("1 - encode text")
    print("2 - decode text")
    print("3 - exit")
    selec = input("============= opc: ")

    return selec

def encode(txt):
    txt = txt.upper()
    code = ""

    for char in txt:
        if char == "A":
            code += "4"
        elif char == "B":
           code += "8"
        elif char == "C":
            code += "<"
        elif char == "D":
            code += ")"
        elif char == "E":
            code += "3"
        elif char == "F":
            code += "/="
        elif char == "G":
            code += "9"
        elif char == "H":
            code += "#"
        elif char == "I":
            code += "1"
        elif char == "J":
            code += "j"
        elif char == "K":
            code += "k"
        elif char == "L":
            code += "2"
        elif char == "M":
            code += "m"
        elif char == "N":
            code += "n"
        elif char == "O":
            code += "()"
        elif char == "P":
            code += "|>"
        elif char == "Q":
            code += "<|"
        elif char == "R":
            code += "r"
        elif char == "S":
            code += "5"
        elif char == "T":
            code += "7"
        elif char == "U":
            code += "v"
        elif char == "W":
            code += "vv"
        elif char == "X":
            code += "%"
        elif char == "Y":
            code += "j"
        elif char == "Z":
            code += "7_"
        else:
            code += char

    return code

def decode(txt):
    txt = txt.upper()
    code = ""

    for char in txt:
        if char == "4":
            code += "A"
        elif char == "8":
           code += "B"
        elif char == "<":
            code += "C"
        elif char == ")":
            code += "D"
        elif char == "3":
            code += "E"
        elif char == "/=":
            code += "F"
        elif char == "9":
            code += "G"
        elif char == "#":
            code += "H"
        elif char == "1":
            code += "I"
        elif char == "j":
            code += "J"
        elif char == "k":
            code += "K"
        elif char == "2":
            code += "L"
        elif char == "m":
            code += "M"
        elif char == "N":
            code += "n"
        elif char == "()":
            code += "O"
        elif char == "|>":
            code += "P"
        elif char == "<|":
            code += "Q"
        elif char == "r":
            code += "R"
        elif char == "5":
            code += "S"
        elif char == "7":
            code += "T"
        elif char == "v":
            code += "U"
        elif char == "vv":
            code += "W"
        elif char == "%":
            code += "X"
        elif char == "j":
            code += "Y"
        elif char == "7_":
            code += "Z"
        else:
            code += char

    return code

main()
