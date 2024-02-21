import ply.lex as lex

# Lista para guardar mensajes de error
errores_lexicos = []

tokens = (
    'LBRACE', 'RBRACE', 'VAR', 'TYPE', 'VARIABLE',
    'EQUALS', 'FUNCTION', 'PARENTHESIS'
)

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='

# Definir explícitamente "takeData" como una función
def t_FUNCTION(t):
    r'takeData'
    return t

# Luego definir el token para variables y tipos
def t_VARIABLE(t):
    r'[a-z]+'
    if t.value == 'var':
        t.type = 'VAR'
    elif t.value in ['int', 'float', 'string']:
        t.type = 'TYPE'
    return t

def t_PARENTHESIS(t):
    r'\(\s*\)'
    return t

t_ignore = ' \t'

def t_error(t):
    global errores_lexicos
    error_msg = f"Illegal character '{t.value[0]}' at position {t.lexpos}"
    errores_lexicos.append(error_msg)
    t.lexer.skip(1)

lexer = lex.lex()