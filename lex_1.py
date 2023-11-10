import ply.lex as lex

tokens = (
    'FUNCTION',
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'CUR_LPAREN',
    'CUR_RPAREN',
    'EQUALS',
    'COMMA',
    'PIPE',
    'ARRAY',
    'LIST',
    'IF',
    'THEN',
    'ELSEIF',
    'ENDIF',
    'FOR',
    'IN',
    'DO',
    'ENDFOR',
    'WHITESPACE'
)

t_FUNCTION = r'function'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CUR_LPAREN = r'\{'
t_CUR_RPAREN = r'\}'
t_EQUALS = r'='
t_COMMA = r','
t_WHITESPACE = r' '
t_PIPE = r'\|'
t_ARRAY = r'array'
t_LIST = r'list'
t_IF = r'if'
t_THEN = r'then'
t_ELSEIF = r'elseif'
t_ENDIF = r'end\s+if'
t_FOR = r'for'
t_IN = r'in'
t_DO = r'do'
t_ENDFOR = r'endfor'

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Example usage:
# lexer.input('function my_function()')

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
