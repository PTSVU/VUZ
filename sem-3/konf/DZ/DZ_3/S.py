from sly import Lexer, Parser
import json


class ConfLexer(Lexer):
    tokens = {NUM, STRING, LPAREN, RPAREN, ASSIGN, NAME, LCODE, RCODE, SEMICOLON, POINTER, FOR, PATTERN}

    ignore = ' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'\#.*'

    SEMICOLON = r';'
    STRING = r'\"[\w\dа-яА-Я_\-\.\,\s]+\"'
    LPAREN = r'\('
    RPAREN = r'\)'
    ASSIGN = r'='
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]+'
    POINTER = r'&'
    LCODE = r'\{'
    RCODE = r'\}'
    NUM = r'\d+'

    NAME["for"] = FOR
    PATTERN = r'\"[\w\dа-яА-Я_\-\.\,\s]+&[\w\dа-яА-Я_\-\.\,\s]*\"'

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t


class ConfParser(Parser):
    tokens = ConfLexer.tokens

    def __init__(self):
        self.names = {}

    @_('LCODE statements RCODE object')
    def program(self, p):
        return p.object

    @_('object')
    def program(self, p):
        return p.object

    @_('LPAREN list_assign RPAREN')
    def object(self, p):
        d = {}
        d.update(p.list_assign)
        return d

    @_('assign list_assign')
    def list_assign(self, p):
        d = {}
        d.update(p.assign)
        d.update(p.list_assign)
        return d

    @_('')
    def list_assign(self, p):
        return {}

    @_('NAME ASSIGN LPAREN list_value RPAREN')
    def assign(self, p):
        d = {}
        d[p.NAME] = p.list_value
        return d

    @_('value list_value')
    def list_value(self, p):
        if (isinstance(p.list_value, list)):
            if (len(p.list_value) != 0):
                return [p.value] + p.list_value
            return p.value
        return [p.value] + [p.list_value]

    @_('')
    def list_value(self, p):
        return []

    @_('NUM')
    def value(self, p):
        return p.NUM

    @_('STRING')
    def value(self, p):
        return p.STRING[1:-1]

    @_('object')
    def value(self, p):
        return p.object

    @_('POINTER NAME')
    def value(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f'Undefined name {p.NAME!r}')
            return 0

    @_('FOR POINTER NUM NUM NUM PATTERN')
    def value(self, p):
        b = p.NUM0
        e = p.NUM1
        s = p.NUM2
        word = p.PATTERN
        word = word[1:-1]
        parts = word.split('&')
        a = {}
        try:
            for x in range(b, e+1, s):
                n = parts[0] + str(x) + parts[1]
                try:
                    a[n] = self.names[n]
                except Exception:
                    a[n] = f"Не существует переменной {n}"
            return a
        except Exception:
            print("Ошибка")
            return 0

    @_('FOR NUM NUM NUM')
    def value(self, p):
        b = p.NUM0
        e = p.NUM1
        s = p.NUM2
        a = []
        for x in range(b, e+1, s):
            a.append(x)
        return a

    @_('FOR NUM NUM NUM PATTERN')
    def value(self, p):
        b = p.NUM0
        e = p.NUM1
        s = p.NUM2
        word = p.PATTERN
        word = word[1:-1]
        parts = word.split('&')
        a = []
        for x in range(b, e+1, s):
            a.append(parts[0] + str(x) + parts[1])
        return a

    @_('FOR PATTERN NUM NUM NUM PATTERN')
    def value(self, p):
        b = p.NUM0
        e = p.NUM1
        s = p.NUM2
        word0 = p.PATTERN0
        word0 = word0[1:-1]
        parts0 = word0.split('&')
        word1 = p.PATTERN1
        word1 = word1[1:-1]
        parts1 = word1.split('&')
        a = {}
        for x in range(b, e+1, s):
            n1 = parts0[0] + str(x) + parts0[1]
            n2 = parts1[0] + str(x) + parts1[1]
            try:
                a[n1] = self.names[n2]
            except Exception:
                a[n1] = n2
        return a

    @_('statement statements')
    def statements(self, p):
        p.statement
        p.statements

    @_('')
    def statements(self, p):
        pass

    # statement ::= NAME=list_value;
    @_('NAME ASSIGN list_value SEMICOLON')
    def statement(self, p):
        self.names[p.NAME] = p.list_value


if __name__ == "__main__":
    name = input("Введите название файла конфигурации: ")
    try:
        data = open(name, "r").read()
        lexer = ConfLexer()
        parser = ConfParser()
        result = parser.parse(lexer.tokenize(data))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception:
        print("Ошибка")


# БНФ
# <s-выражение> ::= "{" <список-атрибутов> "}"
# <список-атрибутов> ::= <атрибут> <список-атрибутов> | ε
# <атрибут> ::= "#" <комментарий> | <присвоение> | <присвоение-объекта> | <присвоение-массива>
# <комментарий> ::= "комментарий" "=" <строка> ";"
# <присвоение> ::= <имя> "=" <значение> ";"
# <присвоение-объекта> ::= <имя> "=" "(" <список-присвоений> ")" ";"
# <присвоение-массива> ::= <имя> "=" "(" <список-значений> ")" ";"
# <список-присвоений> ::= <присвоение> <список-присвоений> | ε
# <список-значений> ::= <значение> <список-значений> | ε
# <значение> ::= <число> | <строка> | <ссылка> | <цикл> | <паттерн>
# <число> ::= ...  # Здесь описывается формат числа
# <строка> ::= ...  # Здесь описывается формат строки
# <ссылка> ::= "&" <имя>
# <цикл> ::= "for" <число> <число> <число> <строка> | "for" <строка> <число> <число> <число> <строка>
# <паттерн> ::= <строка> "&" <строка>
