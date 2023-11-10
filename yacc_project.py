import ply.yacc as yacc
from lex_project import tokens

precedence = (
    ('left', 'IDENTIFIER'),
    ('left', 'PIPE'),
)

def p_program(p):
    '''program : pipeline
               | function_declaration
               | array_declaration
               | nested_if_statement
               | expression
               | for_loop
               | list_expression
    '''
    p[0] = p[1]

# Define the grammar rules
def p_pipeline(p):
    'pipeline : IDENTIFIER PIPE IDENTIFIER '
    p[0] = {
            "type": "pipeline",
            "name": [p[1]]
        }

def p_function_declaration(p):
    '''function_declaration : IDENTIFIER LPAREN RPAREN CUR_LPAREN CUR_RPAREN'''
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
def p_array_declaration(p):
    'array_declaration : IDENTIFIER EQUALS LPAREN array_items RPAREN'

    p[0] = {
        "type": "array_declaration",
        "name": p[1],
        "items": p[4]
    }

# def p_array_items(p):
#     '''array_items : IDENTIFIER
#                    | IDENTIFIER WHITESPACE array_items
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]

def p_array_items(p):
    '''array_items : IDENTIFIER
                   | IDENTIFIER WHITESPACE array_items
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# def p_nested_if_statement(p):
#     '''nested_if_statement : IF SQR_LPAREN NON_EMPTY_STRING SQR_RPAREN THEN NON_EMPTY_STRING ELIF NON_EMPTY_STRING THEN NON_EMPTY_STRING ENDIF'''
#     print(3)
#     p[0] = {
#         "type": "nested_if_statement",
#         "condition": p[2],
#         "then_statement": p[4],
#         "else_if_statements": [
#             {
#                 "condition": p[6],
#                 "then_statement": p[8]
#             }
#         ]
#     }

def p_script(p):
    '''
    script : if_statement
           | script if_statement
    '''
    p[0] = {
        "type": "nested_if_statement"
    }

def p_if_statement(p):
    '''
    if_statement : IF condition THEN NEWLINE statements FI
                 | IF condition THEN NEWLINE statements ELSE NEWLINE statements FI
    '''

def p_condition(p):
    '''
    condition : SQR_LPAREN IDENTIFIER SQR_RPAREN
    '''

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

def p_statement(p):
    '''
    statement : IDENTIFIER NEWLINE
    '''

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

# import ply.yacc as yacc
# from lex_project import tokens

# # Define the grammar rules

# # def p_program(p):
# #     '''program : pipeline
# #                | function_declaration
# #                | array_declaration
# #                | nested_if_statement
# #                | expression
# #                | for_loop
# #                | list_expression
# #     '''
# #     p[0] = p[1]

# def p_pipeline(p):
#     'pipeline : IDENTIFIER PIPE IDENTIFIER'
#     p[0] = {
#         "type": "pipeline",
#         "source": p[1],
#         "destination": p[3]
#     }

# def p_function_declaration(p):
#     'function_declaration : IDENTIFIER LPAREN RPAREN CUR_LPAREN CUR_RPAREN'
#     p[0] = {
#         "type": "function_declaration",
#         "name": p[1],
#     }

# def p_array_declaration(p):
#     'array_declaration : IDENTIFIER EQUALS LPAREN RPAREN'
#     p[0] = {
#         "type": "array_declaration",
#         "name": p[1],
#     }

# def p_nested_if_statement(p):
#     'nested_if_statement : IF expression THEN compound_statement ELSEIF expression THEN compound_statement ENDIF'
#     p[0] = {
#         "type": "nested_if_statement",
#         "condition": p[2],
#         "then_statement": p[4],
#         "else_if_statements": [
#             {
#                 "condition": p[6],
#                 "then_statement": p[8]
#             }
#         ]
#     }

# def p_expression(p):
#     '''expression : IDENTIFIER
#                   | expression COMMA IDENTIFIER
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]

# def p_for_loop(p):
#     'for_loop : FOR IDENTIFIER IN list_expression DO compound_statement ENDFOR'
#     p[0] = {
#         "type": "for_loop",
#         "iterator": p[2],
#         "list_expression": p[4],
#         "body": p[6]
#     }

# def p_list_expression(p):
#     '''list_expression : IDENTIFIER
#                       | list_expression COMMA IDENTIFIER
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]

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
    if not s:
        continue
    result = parser.parse(s)
    print(result)

