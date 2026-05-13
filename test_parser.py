import sys
sys.path.insert(0, "generated")

from antlr4 import *
from FlowLangLexer import FlowLangLexer
from FlowLangParser import FlowLangParser

# Leer archivo de entrada
entrada = FileStream("input.txt", encoding="utf-8")

# Crear lexer
lexer = FlowLangLexer(entrada)

# Convertir tokens
tokens = CommonTokenStream(lexer)

# Crear parser
parser = FlowLangParser(tokens)

print("=== INICIANDO ANALISIS SINTACTICO ===")

# Regla inicial del parser
tree = parser.program()

print("=== ANALISIS COMPLETADO ===")

# Mostrar árbol sintáctico
print("\n=== ARBOL SINTACTICO ===")
print(tree.toStringTree(recog=parser))

print("\n=== FIN ===")
