# 📌 Analizador Léxico

Este repositorio contiene un **analizador léxico** desarrollado en Python con ANTLR. El programa procesa un archivo de entrada, detecta tokens válidos y errores léxicos, y los muestra en una tabla.

## 📂 Estructura del Proyecto
```
Analizador-Lexico/
│── lib/                           # Librerías externas
│── src/                           # Código fuente
│   ├── __pycache__/               # Caché de Python (se ignora en Git)
│   ├── antlr/                     # Archivos de ANTLR (si los usas)
│   ├── ErrorTable.py              # Módulo para manejar errores
│   ├── Lexer.g4                   # Definición de reglas léxicas
│   ├── Lexer.interp               # Archivo generado por ANTLR
│   ├── Lexer.tokens               # Archivo generado por ANTLR
│   ├── Lexer.py                    # Código del analizador léxico
│   ├── SymbolTable.py             # Manejo de tabla de símbolos
│   ├── main.py                     # Archivo principal
│── test/                          # Casos de prueba
│   ├── test.txt                   # Archivo de prueba de entrada
│── README.md                      # Documentación del proyecto
│── .gitignore                      # Archivos a ignorar en Git
```

## 🔹 Expresiones Regulares Implementadas

| # | Expresión Regular | Descripción |
|---|------------------|-------------|
| 1 | `/^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$/` | Contraseñas seguras |
| 2 | `/^[a-z0-9_-]{3,16}$/` | Nombre de usuario válido |
| 3 | `/^-?\d*(\.\d+)?$/` | Números enteros o decimales |
| 4 | `/^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+$/` | Solo letras (incluyendo acentos y ñ) |
| 5 | `/^[0-9]+[.,]{1,1}\[0]{2,2}$/` | Números con dos ceros decimales |

## 🛠️ Instalación y Uso

1. **Clona el repositorio**
   ```sh
   git clone https://github.com/Aisaac2205/Analizador-L-xico.git
   ```
2. **Ingresa a la carpeta del proyecto**
   ```sh
   cd Analizador-L-xico/src
   ```
3. **Ejecuta el analizador léxico**
   ```sh
   python main.py
   ```
4. **Revisa la salida en la terminal**

## 📜 Licencia
Este proyecto es de uso educativo. Puedes modificarlo y compartirlo libremente.

