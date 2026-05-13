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


    # Visit a parse tree produced by FlowLangParser#condition.
    def visitCondition(self, ctx:FlowLangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#numberExpr.
    def visitNumberExpr(self, ctx:FlowLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#mulExpr.
    def visitMulExpr(self, ctx:FlowLangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#divExpr.
    def visitDivExpr(self, ctx:FlowLangParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#minusExpr.
    def visitMinusExpr(self, ctx:FlowLangParser.MinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#plusExpr.
    def visitPlusExpr(self, ctx:FlowLangParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#idExpr.
    def visitIdExpr(self, ctx:FlowLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#comparator.
    def visitComparator(self, ctx:FlowLangParser.ComparatorContext):
        return self.visitChildren(ctx)



del FlowLangParser