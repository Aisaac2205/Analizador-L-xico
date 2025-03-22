from antlr4 import *
from Lexer import Lexer  # Importar la clase Lexer generada por ANTLR
from ErrorTable import ErrorTable

def main():
    print("Ejecutando main.py...")

    # Cargar el archivo de prueba
    input_stream = FileStream("src/test.txt", encoding="utf-8")

    # Crear una instancia del lexer con la entrada
    lexer = Lexer(input_stream)

    # Crear un flujo de tokens a partir del lexer
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    # Tabla de errores
    error_table = ErrorTable()

    # Procesar los tokens generados por el lexer
    for token in tokens.tokens:
        if token.type == Token.EOF:
            continue  # Ignorar fin de archivo

        token_name = lexer.symbolicNames[token.type]
        print(f"Línea {token.line}: {token.text} -> Válido: {token_name}")

        # Detectar errores léxicos
        if token_name == 'ERROR':  
            error_table.add_error(f"Línea {token.line}: {token.text} -> Error léxico")

    # Mostrar la tabla de errores si existen errores
    if error_table.errors:
        print("\nTabla de errores:")
        for e in error_table.errors:
            print(" ->", e)

if __name__ == "__main__":
    main()
