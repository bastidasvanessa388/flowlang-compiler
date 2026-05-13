# Generated from FlowLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FlowLangParser import FlowLangParser
else:
    from FlowLangParser import FlowLangParser

# This class defines a complete listener for a parse tree produced by FlowLangParser.
class FlowLangListener(ParseTreeListener):

    # Enter a parse tree produced by FlowLangParser#program.
    def enterProgram(self, ctx:FlowLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by FlowLangParser#program.
    def exitProgram(self, ctx:FlowLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by FlowLangParser#inicioStep.
    def enterInicioStep(self, ctx:FlowLangParser.InicioStepContext):
        pass

    # Exit a parse tree produced by FlowLangParser#inicioStep.
    def exitInicioStep(self, ctx:FlowLangParser.InicioStepContext):
        pass


    # Enter a parse tree produced by FlowLangParser#procesoStep.
    def enterProcesoStep(self, ctx:FlowLangParser.ProcesoStepContext):
        pass

    # Exit a parse tree produced by FlowLangParser#procesoStep.
    def exitProcesoStep(self, ctx:FlowLangParser.ProcesoStepContext):
        pass


    # Enter a parse tree produced by FlowLangParser#controlStep.
    def enterControlStep(self, ctx:FlowLangParser.ControlStepContext):
        pass

    # Exit a parse tree produced by FlowLangParser#controlStep.
    def exitControlStep(self, ctx:FlowLangParser.ControlStepContext):
        pass


    # Enter a parse tree produced by FlowLangParser#control.
    def enterControl(self, ctx:FlowLangParser.ControlContext):
        pass

    # Exit a parse tree produced by FlowLangParser#control.
    def exitControl(self, ctx:FlowLangParser.ControlContext):
        pass


    # Enter a parse tree produced by FlowLangParser#condition.
    def enterCondition(self, ctx:FlowLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by FlowLangParser#condition.
    def exitCondition(self, ctx:FlowLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by FlowLangParser#numberExpr.
    def enterNumberExpr(self, ctx:FlowLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#numberExpr.
    def exitNumberExpr(self, ctx:FlowLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#mulExpr.
    def enterMulExpr(self, ctx:FlowLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#mulExpr.
    def exitMulExpr(self, ctx:FlowLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#divExpr.
    def enterDivExpr(self, ctx:FlowLangParser.DivExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#divExpr.
    def exitDivExpr(self, ctx:FlowLangParser.DivExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#minusExpr.
    def enterMinusExpr(self, ctx:FlowLangParser.MinusExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#minusExpr.
    def exitMinusExpr(self, ctx:FlowLangParser.MinusExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#plusExpr.
    def enterPlusExpr(self, ctx:FlowLangParser.PlusExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#plusExpr.
    def exitPlusExpr(self, ctx:FlowLangParser.PlusExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#idExpr.
    def enterIdExpr(self, ctx:FlowLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by FlowLangParser#idExpr.
    def exitIdExpr(self, ctx:FlowLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by FlowLangParser#comparator.
    def enterComparator(self, ctx:FlowLangParser.ComparatorContext):
        pass

    # Exit a parse tree produced by FlowLangParser#comparator.
    def exitComparator(self, ctx:FlowLangParser.ComparatorContext):
        pass



del FlowLangParser