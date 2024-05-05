import re

patterns = {
 'IMPORTS' : r'<stdio.h>|<conio.h>|<stdlib.h>',
 'STRING' : r'\".*\"',
 'KEYWORD' : r'#include|if|else|for|break|int|float|void|String|char|double',
 'FUNCTION' : r'printf|scanf|clrscr|getch',
 'FLOAT' : r'\d+\.\d+',
 'INT' : r'\d+',
 'OPERATOR' : r'\+?\+|-|\*|/|=|==|<|>',
 'ID' : r'[a-zA-z_][a-zA-Z0-9_]*',
 'LPARAN' : r'\(',
 'RPARAN' : r'\)',
 'SEPRATOR' : r'[;:,]',
 'LBRACE' : r'\{',
 'RBRACE' : r'\}',
}
def lex_anz(input):
    tokens = []
    regex_patt = '|'.join(f'(?P<{tok}>{patterns[tok]})' for tok in patterns)
    for match in re.finditer(regex_patt, input):
       tok_type = match.lastgroup
       tok_val = match.group()
       tokens.append((tok_type, tok_val))
    return tokens

code = ("#include<stdio.h> int main() {} int x = 3; if ( x < 10 ) { printf(Hello World)return 0;}}") 
#code = open('text.cpp').read()
result = lex_anz(code)
for t, v in result: print(f'{v} -> {t}')

