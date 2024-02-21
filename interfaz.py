import tkinter as tk
from tkinter import scrolledtext
from lexer import lexer, errores_lexicos
from parser_algortimo import parser

def procesar_entrada():
    global errores_lexicos
    errores_lexicos.clear()  # Limpia la lista de errores para cada procesamiento
    entrada = entrada_txt.get("1.0", tk.END).strip()
    lexer.input(entrada)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok.value)
    
    mensaje = f'Tokens: {tokens}'
    result = parser(tokens)
    if result == None:
        result = "La entrada no coincide con la gramática."
        
    if errores_lexicos:
        mensaje += "\n\nErrores:\n" + "\n".join(errores_lexicos)
    mensaje += f"\n\nResultado Algoritmo: {result}"
    
    salida_txt.configure(state='normal')
    salida_txt.delete("1.0", tk.END)
    salida_txt.insert(tk.INSERT, mensaje)
    salida_txt.configure(state='disabled')

ventana = tk.Tk()
ventana.title("Analizador Léxico con Interfaz Gráfica")

frame_entrada = tk.Frame(ventana, padx=10, pady=10)
frame_entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

entrada_txt = scrolledtext.ScrolledText(frame_entrada, wrap=tk.WORD)
entrada_txt.pack(fill=tk.BOTH, expand=True)

frame_salida = tk.Frame(ventana, padx=10, pady=10)
frame_salida.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

salida_txt = scrolledtext.ScrolledText(frame_salida, wrap=tk.WORD, state='disabled')
salida_txt.pack(fill=tk.BOTH, expand=True)

btn_procesar = tk.Button(frame_entrada, text="Procesar", command=procesar_entrada)
btn_procesar.pack(side=tk.BOTTOM, pady=(5,0))

ventana.mainloop()
