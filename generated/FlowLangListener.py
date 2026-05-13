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


    # Enter a parse tree produced by FlowLangParser#exprComp.
    def enterExprComp(self, ctx:FlowLangParser.ExprCompContext):
        pass

    # Exit a parse tree produced by FlowLangParser#exprComp.
    def exitExprComp(self, ctx:FlowLangParser.ExprCompContext):
        pass


    # Enter a parse tree produced by FlowLangParser#exprNum.
    def enterExprNum(self, ctx:FlowLangParser.ExprNumContext):
        pass

    # Exit a parse tree produced by FlowLangParser#exprNum.
    def exitExprNum(self, ctx:FlowLangParser.ExprNumContext):
        pass


    # Enter a parse tree produced by FlowLangParser#comparator.
    def enterComparator(self, ctx:FlowLangParser.ComparatorContext):
        pass

    # Exit a parse tree produced by FlowLangParser#comparator.
    def exitComparator(self, ctx:FlowLangParser.ComparatorContext):
        pass



del FlowLangParser