import re
from lexer import Lexer

def open_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def add_all_dict(new_dict, key, values):
    if key not in new_dict:
        new_dict[key] = values
    else:
        new_dict[key].extend(values)
    return new_dict

def remove_dup(new_dict):
    for key in new_dict:
        new_dict[key] = sorted(set(new_dict[key]), key=new_dict[key].index)

def main():
    text = open_file("input_sourcecode.txt")

    # Remove comments
    comment_pattern = re.compile("//.*")
    text = re.sub(comment_pattern, " ", text)

    new_result = {}
    lines = text.splitlines()

    for line in lines:
        lexer = Lexer(line)
        tokens = lexer.make_tokens()

        for token in tokens:
            values = [token.value]
            add_all_dict(new_result, token.type, values)

    remove_dup(new_result)

    # Print table
    print("Token    Lexeme")
    for key, values in new_result.items():
        for value in values:
            print(f"{key}    {value}")

    # Write to output file
    with open("output.txt", 'w') as output_file:
        for key, values in new_result.items():
            for value in values:
                output_file.write(f"{key}    {value}\n")

if __name__ == "__main__":
    main()
