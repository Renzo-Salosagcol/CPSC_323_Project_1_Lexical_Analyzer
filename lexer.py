KEYWORDS = ["while", "for", "cout", "return"]
OPERATORS = ['+', '<', '>', '=']
DOPERATORS = ["<=", ">=", "==", "<<"]
SEPARATORS = ['"', '(', ')', '{', '}']
BLANKSPACE = " \n\t"

TT_INT = "INT"
TT_FLOAT = "REAL"
TT_OPERATOR = "OPERATOR"
TT_QUOTE = "SEPARATOR"
TT_LPAREN = "SEPARATOR"
TT_RPAREN = "SEPARATOR"
TT_SEMICOL = "PUNCTUATION"
TT_EXCLAIM = "PUNCTUATION"
TT_OCBRAC = "SEPARATOR"
TT_CCBRAC = "SEPARATOR"
TT_DQUOTE = "PUNCTUATION"
TT_ASSIGN = "EQUALS"
TT_IDENTIFIER = "IDENTIFIER"
TT_KEYWORD = "KEYWORD"

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type} {self.value}" if self.value else f"{self.type}"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_num(self):
        num_str = ""
        dec_count = 0

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                dec_count += 1
                if dec_count > 1:
                    break
            num_str += self.current_char
            self.advance()

        return Token(TT_FLOAT, num_str) if dec_count == 1 else Token(TT_INT, num_str)

    def make_identifier(self):
        id_str = ""

        while self.current_char is not None and (self.current_char.isalpha() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()

        return Token(TT_KEYWORD, id_str) if id_str in KEYWORDS else Token(TT_IDENTIFIER, id_str)

    def make_operator(self):
        id_op = ""

        while self.current_char is not None and self.current_char in OPERATORS:
            id_op += self.current_char
            self.advance()
            if id_op in DOPERATORS:
                break

        return Token(TT_OPERATOR, id_op)

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in BLANKSPACE:
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.make_num())
            elif self.current_char in OPERATORS:
                tokens.append(self.make_operator())
            elif self.current_char == '"':
                tokens.append(Token(TT_DQUOTE, '"'))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, ')'))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(TT_SEMICOL, ';'))
                self.advance()
            elif self.current_char == '!':
                tokens.append(Token(TT_EXCLAIM, '!'))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_OCBRAC, '{'))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_CCBRAC, '}'))
                self.advance()
            elif self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.make_identifier())
            else:
                print(f"Illegal character '{self.current_char}'")
                self.advance()

        return tokens
