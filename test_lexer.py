import sys
sys.path.insert(0, "generated")

from antlr4 import CommonTokenStream, FileStream
from FlowLangLexer import FlowLangLexer

# Leer archivo de entrada
entrada = FileStream("input.txt", encoding="utf-8")

# Crear lexer
lexer = FlowLangLexer(entrada)

# Crear stream de tokens
stream = CommonTokenStream(lexer)
stream.fill()

print("=== TOKENS DETECTADOS ===")

for token in stream.tokens:
    if token.type == -1:
        continue

    print(
        f"Linea {token.line:<3} | "
        f"Tipo {token.type:<3} | "
        f"Texto '{token.text}'"
    )

print("=== FIN ===")
