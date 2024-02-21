import re

tabla_analisis_predictivo = {
    ('S', '{'): ['I', 'V', 'F'],
    ('I', '{'): ['{'],
    ('V', 'var'): ['var', 'T', 'G'],
    ('T', 'int'): ['int'],
    ('T', 'float'): ['float'],
    ('T', 'string'): ['string'],
    ('G', r'[a-z]'): ['N', '=', 'O'],
    ('N', r'[a-z]'): ['L', 'R'],
    ('R', r'[a-z]'): ['L', 'R'],
    ('R', '='): ['ε'],
    ('O', 'takeData'): ['takeData', 'P'],
    ('P', '()'): ['()'],
    ('F', '}'): ['}'],
    ('L', r'[a-z]'): [r'[a-z]']
}

terminales = ['{', 'var', 'int', 'float', 'string', '}', 'takeData', '()', '=', '}']
no_terminales = ['S', 'I', 'V', 'T', 'G', 'N', 'R', 'O', 'P', 'F', 'L']

def coincide_expresion(caracter, expresion):
    return re.match(expresion, caracter) is not None

def obtener_produccion(tabla, no_terminal, simbolo_entrada):
    # Verifica directamente para símbolos específicos
    if (no_terminal, simbolo_entrada) in tabla:
        return tabla[(no_terminal, simbolo_entrada)]
    
    # Verifica para coincidencias con expresiones regulares
    for (nt, regex), produccion in tabla.items():
        if nt == no_terminal and re.match(regex, simbolo_entrada):
            return produccion
    
    # Si no se encuentra una producción adecuada
    return None

def anadir_invertido(a, b):
    # Extiende la lista 'a' con los elementos de 'b' en orden inverso
    a.extend(reversed(b))
    return a

def parser(tokens):
    pila = ['$', 'S']
    indice_entrada = 0
    while pila[-1] != '$':
        tope_pila = pila[-1]
        try:
            simbolo_actual = tokens[indice_entrada]     
        except IndexError as _:
            break
        
        if tope_pila in terminales or tope_pila == '$':
            if tope_pila == simbolo_actual:
                pila.pop()  # Elimina el elemento de la pila
                indice_entrada += 1  # Avanza en la entrada
            else:
                print("Error: símbolo de entrada no coincide con el esperado")
                return
        # Revisa si el tope de la pila es una expresión regular
        elif any(tope_pila == regex for regex in [r'[a-z]']):
            if coincide_expresion(simbolo_actual, tope_pila):
                pila.pop()  # Elimina el elemento de la pila
                indice_entrada += 1  # Avanza en la entrada
            else:
                print("Error: símbolo de entrada no coincide con el esperado")
                return
        # Revisa si el tope de la pila es un no terminal
        elif tope_pila in no_terminales:
            produccion = obtener_produccion(tabla_analisis_predictivo, tope_pila, simbolo_actual)
            if produccion is not None:
                pila.pop()  # Elimina el no terminal de la pila
                if produccion != ['ε']:
                    pila.extend(reversed(produccion))
            else:
                print("Error: producción no encontrada para el no terminal")
                return
        else:
            print("Error: símbolo desconocido")
            return
        
    # Al finalizar el bucle, verifica si la entrada se ha consumido completamente
    if len(pila) == 1:
        return "Análisis completado exitosamente."
    
    return "La entrada no coincide con la gramática."

# Asegúrate de que tokens sea una lista de tokens reconocibles, no caracteres individuales
tokens = ['{', 'var', 'float', 'v','a','r','i','a','b','l','e', '=', 'takeData', '()', '}']
datos = parser(tokens)