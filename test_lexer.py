import sys
sys.path.insert(0, "generated")

from antlr4 import CommonTokenStream, FileStream
from FlowLangLexer import FlowLangLexer

entrada = FileStream("input.txt", encoding="utf-8")
lexer   = FlowLangLexer(entrada)
stream  = CommonTokenStream(lexer)
stream.fill()

sim = FlowLangLexer.symbolicNames
lit = FlowLangLexer.literalNames

def nombre(tipo):
    if tipo <= 0: return "EOF"
    if tipo < len(sim) and sim[tipo] not in (None,"<INVALID>"): return sim[tipo]
    if tipo < len(lit) and lit[tipo] not in (None,"<INVALID>"): return lit[tipo]
    return f"T{tipo}"

print("=== TOKENS DETECTADOS ===")
print("  " + "-"*40)
for t in stream.tokens:
    if t.type == -1: continue
    n = nombre(t.type)
    if n != "EOF":
        print(f"  Linea {t.line:<4} | {n:<15} | {repr(t.text)}")
print("\n=== FIN ===")
