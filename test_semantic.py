import sys

sys.path.insert(0, "generated")

from antlr4 import *

from FlowLangLexer import FlowLangLexer
from FlowLangParser import FlowLangParser

from semantic_analyzer.SemanticAnalyzer import SemanticAnalyzer

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
# Árbol sintáctico
# ==========================================

tree = parser.program()

# ==========================================
# Semantic Analyzer
# ==========================================

semantic = SemanticAnalyzer()

semantic.visit(tree)

errors = semantic.validate()

# ==========================================
# Resultado
# ==========================================

print("=== ANALISIS SEMANTICO ===")

if len(errors) == 0:
    print("Programa semanticamente correcto")
else:
    print("Errores encontrados:\n")

    for error in errors:
        print(f"- {error}")

print("\n=== FIN ===")
