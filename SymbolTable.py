class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, token_type, scope):
        """
        Agrega un símbolo a la tabla.
        """
        self.symbols[name] = {"type": token_type, "scope": scope}

    def print_symbols(self):
        print("\nTabla de Símbolos:")
        for name, data in self.symbols.items():
            print(f"Símbolo: {name}, Tipo: {data['type']}, Alcance: {data['scope']}")
