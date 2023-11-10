import ply.yacc as yacc

# Import tokens from the lexer
from lex_project import tokens

# Parser code
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

def p_pipeline(p):
    'pipeline : IDENTIFIER PIPE IDENTIFIER'
    p[0] = {
        "type": "pipeline",
        "source": p[1],
        "destination": p[3]
    }

def p_function_declaration(p):
    '''function_declaration : IDENTIFIER LPAREN RPAREN CUR_LPAREN CUR_RPAREN'''
    p[0] = {
        "type": "function_declaration",
        "name": p[1],
    }

def p_array_declaration(p):
    'array_declaration : IDENTIFIER EQUALS LPAREN array_items RPAREN'
    p[0] = {
        "type": "array_declaration",
        "name": p[1],
        "items": p[4]
    }

def p_array_items(p):
    '''array_items : IDENTIFIER array_items
                   | IDENTIFIER WHITESPACE IDENTIFIER
                   | IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1], p[3]]
    else:
        p[0] = [p[1]] + p[2]



def p_nested_if_statement(p):
    'nested_if_statement : IF expression THEN block ELSEIF expression THEN block ENDIF'
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
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_for_loop(p):
    '''for_loop :  IDENTIFIER LPAREN IDENTIFIER'''
    print(1)
    p[0] = {
        "type": "for_loop",
        "iterator": p[1],
    }


def p_list_expression(p):
    '''list_expression : IDENTIFIER
                      | list_expression COMMA IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_block(p):
    '''block : CUR_LPAREN program CUR_RPAREN
             | statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_statement(p):
    '''statement : expression
                 | nested_if_statement
                 | for_loop
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

# Example usage:
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
