import ply.yacc as yacc
from lex_project import tokens

precedence = (
    ('left', 'IDENTIFIER'),
    ('left', 'PIPE'),
)

# Define the grammar rules

def p_function_declaration(p):
    '''function_declaration : IDENTIFIER LPAREN RPAREN CUR_LPAREN CUR_RPAREN'''
    print("hi")
    p[0] = {
        "type": "function_declaration",
        "name": p[1],
    }

# def p_arguments(p):
#     "arguments : EMPTY PIPE ARGUMENT_LIST"
#     if p[1] is None:
#         p[0] = []
#     else:
#         p[0] = p[1]

# def p_argument_list(p):
#     '''argument_list : IDENTIFIER PIPE argument_list COMMA IDENTIFIER
#                         | IDENTIFIER
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]

# def p_list_declaration(p):
#     'list_declaration : LIST IDENTIFIER LPAREN RPAREN'
#     p[0] = {
#         "type": "list_declaration",
#         "name": p[2]
#     }

#for now let's make command as identifier
def p_pipeline(p):
    'pipeline : IDENTIFIER PIPE IDENTIFIER '
    print(1)
    p[0] = {
            "type": "pipeline",
            "name": [p[1]]
        }
    

def p_array_declaration(p):
    'array_declaration : IDENTIFIER EQUALS LPAREN RPAREN'
    print(2)
    p[0] = {
        "type": "array_declaration",
        "name": p[2]
    }

def array_items(p):
    '''array_items :IDENTIFIER WHITESPACE IDENTIFIER
                    | IDENTIFIER
    '''

def p_nested_if_statement(p):
    'nested_if_statement : IF expression THEN compound_statement ELSEIF expression THEN compound_statement ENDIF'
    print(3)
    p[0] = {
        "type": "nested_if_statement",
        "condition": p[2],
        "then_statement": p[4],
        "else_if_statements": [
            {
                "condition": p[6],
                "then_statement": p[8]
            }
        ]
    }

def p_expression(p):
    '''expression : IDENTIFIER
                          | expression COMMA IDENTIFIER

    '''
    print(4)
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]



def p_for_loop(p):
    'for_loop : FOR IDENTIFIER IN list_expression DO compound_statement ENDFOR'
    print(5)
    p[0] = {
        "type": "for_loop",
        "iterator": p[2],
        "list_expression": p[4],
        "body": p[6]
    }

def p_list_expression(p):
    '''list_expression : IDENTIFIER
                      | list_expression COMMA IDENTIFIER
    '''
    print(6)
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
