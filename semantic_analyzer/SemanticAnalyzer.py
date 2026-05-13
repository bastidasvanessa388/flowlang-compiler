import sys

sys.path.insert(0, "generated")

from FlowLangVisitor import FlowLangVisitor
from FlowLangParser import FlowLangParser


class SemanticAnalyzer(FlowLangVisitor):

    def __init__(self):
        # Tabla de símbolos
        self.variables = set()

        # Lista de errores semánticos
        self.errors = []

        # Verificar si existe Inicio
        self.has_inicio = False

    # ==========================================
    # Inicio
    # ==========================================

    def visitInicioStep(self, ctx):
        self.has_inicio = True
        return self.visitChildren(ctx)

    # ==========================================
    # Proceso
    # ==========================================

    def visitProcesoStep(self, ctx):

        variable = ctx.ID().getText()

        # Registrar variable como definida
        self.variables.add(variable)

        # Visitar expresión
        self.visit(ctx.expression())

        return None

    # ==========================================
    # Variables en expresiones
    # ==========================================

    def visitIdExpr(self, ctx):

        variable = ctx.getText()

        if variable not in self.variables:
            self.errors.append(
                f"Variable no definida: {variable}"
            )

        return None

    # ==========================================
    # Verificación final
    # ==========================================

    def validate(self):

        if not self.has_inicio:
            self.errors.append(
                "El programa debe comenzar con Inicio;"
            )

        return self.errors
