import sys

# ==========================================
# Agregar carpeta generated al path
# ==========================================

sys.path.insert(0, "generated")

# ==========================================
# Imports ANTLR
# ==========================================

from antlr4 import *

from FlowLangLexer import FlowLangLexer
from FlowLangParser import FlowLangParser

# ==========================================
# Semantic Analyzer
# ==========================================

from semantic_analyzer.SemanticAnalyzer import SemanticAnalyzer

# ==========================================
# Code Generator
# ==========================================

from codegen.CodeGenerator import CodeGenerator

# ==========================================
# Leer archivo de entrada
# ==========================================

print("=== FLOWLANG COMPILER ===\n")

input_file = "input.txt"

entrada = FileStream(input_file, encoding="utf-8")

print(f"Leyendo archivo: {input_file}")

# ==========================================
# ANALISIS LEXICO
# ==========================================

print("\n[1] Analisis Lexico")

lexer = FlowLangLexer(entrada)

tokens = CommonTokenStream(lexer)

print("Lexer completado correctamente")

# ==========================================
# ANALISIS SINTACTICO
# ==========================================

print("\n[2] Analisis Sintactico")

parser = FlowLangParser(tokens)

tree = parser.program()

print("Parser completado correctamente")

# ==========================================
# ANALISIS SEMANTICO
# ==========================================

print("\n[3] Analisis Semantico")

semantic = SemanticAnalyzer()

semantic.visit(tree)

errors = semantic.validate()

# ==========================================
# Verificar errores
# ==========================================

if len(errors) > 0:

    print("\nErrores semanticos encontrados:\n")

    for error in errors:
        print(f"- {error}")

    print("\nCompilacion detenida")

    sys.exit(1)

print("Analisis semantico correcto")

# ==========================================
# GENERACION DE CODIGO
# ==========================================

print("\n[4] Generacion de Codigo Python")

generator = CodeGenerator()

generator.visit(tree)

python_code = generator.get_code()

# ==========================================
# Guardar output
# ==========================================

output_file = "output_program.py"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(python_code)

print(f"Archivo generado: {output_file}")

# ==========================================
# Mostrar código generado
# ==========================================

print("\n=== CODIGO GENERADO ===\n")

print(python_code)

print("\n=== COMPILACION EXITOSA ===")
