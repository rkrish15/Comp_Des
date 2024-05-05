import ply.lex as lex

tokens = (
    'NUMBER',
    'KEYWORD',
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'STRING',
    'OPERATOR',
)

t_KEYWORD = r'if|else|while|for|int|float|char|return'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9]*'
t_OPERATOR = r'\+|-|\*|/|===|<|>|<=|>='
t_STRING = r'"([^"]*)"'
t_LPAREN = r'\('
t_RPAREN = r'\)'

print("Enter the expression")

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = input()
lexer.input(data)

for tok in lexer:
    print(tok)
