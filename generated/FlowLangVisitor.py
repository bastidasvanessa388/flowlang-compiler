# Generated from FlowLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FlowLangParser import FlowLangParser
else:
    from FlowLangParser import FlowLangParser

# This class defines a complete generic visitor for a parse tree produced by FlowLangParser.

class FlowLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FlowLangParser#program.
    def visitProgram(self, ctx:FlowLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#inicioStep.
    def visitInicioStep(self, ctx:FlowLangParser.InicioStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#procesoStep.
    def visitProcesoStep(self, ctx:FlowLangParser.ProcesoStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#controlStep.
    def visitControlStep(self, ctx:FlowLangParser.ControlStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#control.
    def visitControl(self, ctx:FlowLangParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#exprComp.
    def visitExprComp(self, ctx:FlowLangParser.ExprCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#exprNum.
    def visitExprNum(self, ctx:FlowLangParser.ExprNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#comparator.
    def visitComparator(self, ctx:FlowLangParser.ComparatorContext):
        return self.visitChildren(ctx)



del FlowLangParser