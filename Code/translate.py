while (True):
    inp = input()
    final = ""
    for letter in inp:
        if(letter == "ק"):
            final = final + "E"
        elif(letter == "ר"):
            final = final + "R"
        elif(letter == "א"):
            final = final + "T"
        elif(letter == "ט"):
            final = final + "Y"
        elif(letter == "ו"):
            final = final + "U"
        elif(letter == "ן"):
            final = final + "I"
        elif(letter == "ם"):
            final = final + "O"
        elif(letter == "פ"):
            final = final + "P"
        elif(letter == "ש"):
            final = final + "A"
        elif(letter == "ד"):
            final = final + "S"
        elif(letter == "ג"):
            final = final + "D"
        elif(letter == "כ"):
            final = final + "F"
        elif(letter == "ע"):
            final = final + "G"
        elif(letter == "י"):
            final = final + "H"
        elif(letter == "ח"):
            final = final + "J"
        elif(letter == "ל"):
            final = final + "K"
        elif(letter == "ך"):
            final = final + "L"
        elif(letter == "ז"):
            final = final + "Z"
        elif(letter == "ס"):
            final = final + "X"
        elif(letter == "ב"):
            final = final + "C"
        elif(letter == "ה"):
            final = final + "V"
        elif(letter == "נ"):
            final = final + "B"
        elif(letter == "מ"):
            final = final + "N"
        elif(letter == "צ"):
            final = final + "M"
        elif(letter == "ת"):
            final = final + "W"
        elif(letter == "ף"):
            final = final + "}"
        elif(letter == "ץ"):
            final = final + "{"
        else:
            final = final + letter

    final = final[::-1]
    print(final)
