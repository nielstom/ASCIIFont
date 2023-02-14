
def main():

    # Define valid ASCII font characters (same ordering as input colossalFontSymbols.txt)
    font_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?! "

    # Get the input string passed in.
    input_text = input("Convert text: ")
    for x in input_text:
        if x not in font_alphabet:
            exit("Invalid Character")

    # Look up the position of each input string character in the font alphabet.
    character_positions = [font_alphabet.index(x) for x in input_text]

    # Read in the ASCII symbols for the ASCII font from file, store them in a format that will help you later when
    # building an ASCII art string out of the input string (e.g. a list of lists, see hint below).
    with open('colossalFontSymbols.txt') as fontSymbolsFile:
        parsed_lines = fontSymbolsFile.readlines()

    font_symbol_2d_list = []
    nLetters, letter_height = len(font_alphabet), len(parsed_lines)//len(font_alphabet)
    counter = 0
    for _ in range(nLetters):
        letter_list = []
        for _ in range(letter_height):
            letter_string = parsed_lines[counter]
            counter += 1
            letter_list.append(letter_string[:-1])  # Remove newline char
        font_symbol_2d_list.append(letter_list)

    # Build a string that represents the input string expressed as ASCII art.
    ascii_string = ""
    for height_idx in range(letter_height):
        for character_idx in character_positions:
            ascii_string += font_symbol_2d_list[character_idx][height_idx]
        ascii_string += "\n"

    # Print the ASCII art string.
    print(ascii_string)


if __name__ == "__main__":
    main()
