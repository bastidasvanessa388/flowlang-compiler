import sys

sys.path.insert(0, "generated")

from antlr4 import *

from FlowLangLexer import FlowLangLexer
from FlowLangParser import FlowLangParser

from codegen.CodeGenerator import CodeGenerator

# ==========================================
# Leer archivo
# ==========================================

entrada = FileStream("input.txt", encoding="utf-8")

# ==========================================
# Lexer
# ==========================================

lexer = FlowLangLexer(entrada)

# ==========================================
# Tokens
# ==========================================

tokens = CommonTokenStream(lexer)

# ==========================================
# Parser
# ==========================================

parser = FlowLangParser(tokens)

# ==========================================
# Árbol
# ==========================================

tree = parser.program()

# ==========================================
# Generador de código
# ==========================================

generator = CodeGenerator()

generator.visit(tree)

python_code = generator.get_code()

# ==========================================
# Mostrar resultado
# ==========================================

print("=== CODIGO PYTHON GENERADO ===\n")

print(python_code)

# ==========================================
# Guardar archivo
# ==========================================

with open("output_program.py", "w", encoding="utf-8") as f:
    f.write(python_code)

print("\n=== ARCHIVO output_program.py GENERADO ===")
