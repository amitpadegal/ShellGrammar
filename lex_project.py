# import ply.lex as lex

# # List of token names.   This is always required
# tokens = (
#     'FUNCTION',
#     'IDENTIFIER',
#     'ARGUMENTS',
#     'ARGUMENT_LIST',
#     'LPAREN',
#     'RPAREN',
#     'COMMA',
#     'PIPE',
#     'ARRAY',
#     'ARRAY_DECLARATION',
#     'LIST',
#     'IF',
#     'THEN',
#     'ELSEIF',
#     'ENDIF',
#     'FOR',
#     'IN',
#     'DO',
#     'ENDFOR',
#     'compound_statement',
#     'COMMAND',
#     'CUR_LPAREN',
#     'CUR_RPAREN',
#     'NON_NULL',
#     'EQUALS',
#     'SQR_RPAREN',
#     'SQR_LPAREN',
#     'ELIF',
#     'NON_EMPTY_STRING'
# )

# # Regular expression rules for simple tokens
# t_FUNCTION      = r'function'
# t_IDENTIFIER    = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_LPAREN       = r'\('
# t_RPAREN       = r'\)'
# t_CUR_LPAREN   = r'\{'
# t_CUR_RPAREN   = r'\}'
# t_SQR_LPAREN   = r'\['
# t_SQR_RPAREN   = r'\]'
# t_EQUALS       = r'='
# t_COMMA        = r','
# # t_WHITESPACE   = r's+'
# t_PIPE          = r'\|'
# t_ARRAY         = r'array'
# t_LIST          = r'list'
# t_IF            = r'if'
# t_THEN          = r'then'
# t_ELIF        = r'elif'
# t_ENDIF         = r'end\s+if'
# t_FOR           = r'for'
# t_IN            = r'in'
# t_DO            = r'do'
# t_ENDFOR        = r'end\s+for'
# # t_NOT_EMPTY_STRING      = r'.+'

# # A string containing ignored characters (spaces and tabs)
# t_ignore  = ' \t'

# # Error handling rule
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)


# # Build the lexer
# lexer = lex.lex()

# data = 'function hi()'

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)


import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'FUNCTION',
    'IDENTIFIER',
    'ARGUMENTS',
    'ARGUMENT_LIST',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'PIPE',
    'ARRAY',
    'ARRAY_DECLARATION',
    'LIST',
    'IF',
    'THEN',
    'ELSEIF',
    'ENDIF',
    'FOR',
    'IN',
    'DO',
    'ENDFOR',
    'compound_statement',
    'COMMAND',
    'CUR_LPAREN',
    'CUR_RPAREN',
    'NON_NULL',
    'EQUALS',
    'WHITESPACE'
)

# Regular expression rules for simple tokens
t_FUNCTION      = r'function'
t_IDENTIFIER    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
# t_NON_NULL      = r'.?'
t_CUR_LPAREN       = r'\{'
t_CUR_RPAREN       = r'\}'
t_EQUALS           = r'='
t_COMMA        = r','
t_WHITESPACE       = r' [ \t]+'
t_PIPE          = r'\|'
t_ARRAY         = r'array'
t_LIST          = r'list'
t_IF            = r'if'
t_THEN          = r'then'
t_ELSEIF        = r'else\s+if'
t_ENDIF         = r'end\s+if'
t_FOR           = r'for'
t_IN            = r'in'
t_DO            = r'do'
t_ENDFOR        = r'end\s+for'
# t_EMPTY         = r''

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

data = 'function hi()'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)