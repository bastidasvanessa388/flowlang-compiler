# Generated from FlowLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,3,4,47,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,5,1,5,1,5,0,1,8,6,0,2,4,
        6,8,10,0,1,1,0,3,8,70,0,13,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,39,
        1,0,0,0,8,46,1,0,0,0,10,65,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,
        15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,
        1,18,1,1,0,0,0,19,20,5,9,0,0,20,29,5,1,0,0,21,22,5,10,0,0,22,23,
        5,17,0,0,23,24,5,2,0,0,24,25,3,8,4,0,25,26,5,1,0,0,26,29,1,0,0,0,
        27,29,3,4,2,0,28,19,1,0,0,0,28,21,1,0,0,0,28,27,1,0,0,0,29,3,1,0,
        0,0,30,31,5,11,0,0,31,32,3,6,3,0,32,33,5,2,0,0,33,37,3,2,1,0,34,
        35,5,12,0,0,35,36,5,2,0,0,36,38,3,2,1,0,37,34,1,0,0,0,37,38,1,0,
        0,0,38,5,1,0,0,0,39,40,3,8,4,0,40,41,3,10,5,0,41,42,3,8,4,0,42,7,
        1,0,0,0,43,44,6,4,-1,0,44,47,5,17,0,0,45,47,5,18,0,0,46,43,1,0,0,
        0,46,45,1,0,0,0,47,62,1,0,0,0,48,49,10,6,0,0,49,50,5,15,0,0,50,61,
        3,8,4,7,51,52,10,5,0,0,52,53,5,16,0,0,53,61,3,8,4,6,54,55,10,4,0,
        0,55,56,5,13,0,0,56,61,3,8,4,5,57,58,10,3,0,0,58,59,5,14,0,0,59,
        61,3,8,4,4,60,48,1,0,0,0,60,51,1,0,0,0,60,54,1,0,0,0,60,57,1,0,0,
        0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,9,1,0,0,0,64,62,1,
        0,0,0,65,66,7,0,0,0,66,11,1,0,0,0,6,15,28,37,46,60,62
    ]

class FlowLangParser ( Parser ):

    grammarFileName = "FlowLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'Inicio'", "'Proceso'", "'Si'", "'Sino'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INICIO", "PROCESO", "SI", "SINO", "PLUS", 
                      "MINUS", "TIMES", "DIVIDE", "ID", "NUMBER", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_step = 1
    RULE_control = 2
    RULE_condition = 3
    RULE_expression = 4
    RULE_comparator = 5

    ruleNames =  [ "program", "step", "control", "condition", "expression", 
                   "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INICIO=9
    PROCESO=10
    SI=11
    SINO=12
    PLUS=13
    MINUS=14
    TIMES=15
    DIVIDE=16
    ID=17
    NUMBER=18
    WS=19
    COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FlowLangParser.EOF, 0)

        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.StepContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.StepContext,i)


        def getRuleIndex(self):
            return FlowLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FlowLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.step()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    break

            self.state = 17
            self.match(FlowLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FlowLangParser.RULE_step

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InicioStepContext(StepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.StepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INICIO(self):
            return self.getToken(FlowLangParser.INICIO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicioStep" ):
                listener.enterInicioStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicioStep" ):
                listener.exitInicioStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicioStep" ):
                return visitor.visitInicioStep(self)
            else:
                return visitor.visitChildren(self)


    class ControlStepContext(StepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.StepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def control(self):
            return self.getTypedRuleContext(FlowLangParser.ControlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlStep" ):
                listener.enterControlStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlStep" ):
                listener.exitControlStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlStep" ):
                return visitor.visitControlStep(self)
            else:
                return visitor.visitChildren(self)


    class ProcesoStepContext(StepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.StepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PROCESO(self):
            return self.getToken(FlowLangParser.PROCESO, 0)
        def ID(self):
            return self.getToken(FlowLangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(FlowLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcesoStep" ):
                listener.enterProcesoStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcesoStep" ):
                listener.exitProcesoStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcesoStep" ):
                return visitor.visitProcesoStep(self)
            else:
                return visitor.visitChildren(self)



    def step(self):

        localctx = FlowLangParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_step)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = FlowLangParser.InicioStepContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(FlowLangParser.INICIO)
                self.state = 20
                self.match(FlowLangParser.T__0)
                pass
            elif token in [10]:
                localctx = FlowLangParser.ProcesoStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(FlowLangParser.PROCESO)
                self.state = 22
                self.match(FlowLangParser.ID)
                self.state = 23
                self.match(FlowLangParser.T__1)
                self.state = 24
                self.expression(0)
                self.state = 25
                self.match(FlowLangParser.T__0)
                pass
            elif token in [11]:
                localctx = FlowLangParser.ControlStepContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.control()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(FlowLangParser.SI, 0)

        def condition(self):
            return self.getTypedRuleContext(FlowLangParser.ConditionContext,0)


        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.StepContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.StepContext,i)


        def SINO(self):
            return self.getToken(FlowLangParser.SINO, 0)

        def getRuleIndex(self):
            return FlowLangParser.RULE_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl" ):
                listener.enterControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl" ):
                listener.exitControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = FlowLangParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(FlowLangParser.SI)
            self.state = 31
            self.condition()
            self.state = 32
            self.match(FlowLangParser.T__1)
            self.state = 33
            self.step()
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 34
                self.match(FlowLangParser.SINO)
                self.state = 35
                self.match(FlowLangParser.T__1)
                self.state = 36
                self.step()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(FlowLangParser.ComparatorContext,0)


        def getRuleIndex(self):
            return FlowLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = FlowLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.expression(0)
            self.state = 40
            self.comparator()
            self.state = 41
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FlowLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FlowLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.ExpressionContext,i)

        def TIMES(self):
            return self.getToken(FlowLangParser.TIMES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.ExpressionContext,i)

        def DIVIDE(self):
            return self.getToken(FlowLangParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class MinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.ExpressionContext,i)

        def MINUS(self):
            return self.getToken(FlowLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpr" ):
                listener.enterMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpr" ):
                listener.exitMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusExpr" ):
                return visitor.visitMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FlowLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FlowLangParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(FlowLangParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusExpr" ):
                listener.enterPlusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusExpr" ):
                listener.exitPlusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusExpr" ):
                return visitor.visitPlusExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FlowLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FlowLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = FlowLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(FlowLangParser.ID)
                pass
            elif token in [18]:
                localctx = FlowLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(FlowLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = FlowLangParser.MulExprContext(self, FlowLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 49
                        self.match(FlowLangParser.TIMES)
                        self.state = 50
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = FlowLangParser.DivExprContext(self, FlowLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 52
                        self.match(FlowLangParser.DIVIDE)
                        self.state = 53
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = FlowLangParser.PlusExprContext(self, FlowLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 55
                        self.match(FlowLangParser.PLUS)
                        self.state = 56
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = FlowLangParser.MinusExprContext(self, FlowLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 58
                        self.match(FlowLangParser.MINUS)
                        self.state = 59
                        self.expression(4)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FlowLangParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = FlowLangParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




