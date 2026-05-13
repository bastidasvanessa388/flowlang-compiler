import sys

sys.path.insert(0, "generated")

from FlowLangVisitor import FlowLangVisitor


class CodeGenerator(FlowLangVisitor):

    def __init__(self):

        # Código Python generado
        self.code = []

        # Nivel de indentación
        self.indent = 0

    # ==========================================
    # Ayuda para indentación
    # ==========================================

    def add_line(self, text):

        spaces = "    " * self.indent

        self.code.append(f"{spaces}{text}")

    # ==========================================
    # Inicio
    # ==========================================

    def visitInicioStep(self, ctx):

        # Inicio no genera código Python
        return None

    # ==========================================
    # Proceso
    # ==========================================

    def visitProcesoStep(self, ctx):

        variable = ctx.ID().getText()

        expression = self.visit(ctx.expression())

        self.add_line(f"{variable} = {expression}")

        return None

    # ==========================================
    # If / Else
    # ==========================================

    def visitControl(self, ctx):

        condition = self.visit(ctx.condition())

        # IF
        self.add_line(f"if {condition}:")

        self.indent += 1

        self.visit(ctx.step(0))

        self.indent -= 1

        # ELSE opcional
        if ctx.SINO():

            self.add_line("else:")

            self.indent += 1

            self.visit(ctx.step(1))

            self.indent -= 1

        return None

    # ==========================================
    # Condición
    # ==========================================

    def visitCondition(self, ctx):

        left = self.visit(ctx.expression(0))

        operator = ctx.comparator().getText()

        right = self.visit(ctx.expression(1))

        return f"{left} {operator} {right}"

    # ==========================================
    # Expresiones matemáticas
    # ==========================================

    def visitNumberExpr(self, ctx):

        return ctx.getText()

    def visitIdExpr(self, ctx):

        return ctx.getText()

    def visitPlusExpr(self, ctx):

        left = self.visit(ctx.expression(0))

        right = self.visit(ctx.expression(1))

        return f"{left} + {right}"

    def visitMinusExpr(self, ctx):

        left = self.visit(ctx.expression(0))

        right = self.visit(ctx.expression(1))

        return f"{left} - {right}"

    def visitMulExpr(self, ctx):

        left = self.visit(ctx.expression(0))

        right = self.visit(ctx.expression(1))

        return f"{left} * {right}"

    def visitDivExpr(self, ctx):

        left = self.visit(ctx.expression(0))

        right = self.visit(ctx.expression(1))

        return f"{left} / {right}"

    # ==========================================
    # Obtener código final
    # ==========================================

    def get_code(self):

        return "\n".join(self.code)
