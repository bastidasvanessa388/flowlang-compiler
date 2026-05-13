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
        4,1,20,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,3,
        3,43,8,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,3,8,46,0,11,1,0,0,0,
        2,26,1,0,0,0,4,28,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,12,3,2,1,
        0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,
        1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,5,9,0,0,18,27,5,1,0,0,19,
        20,5,10,0,0,20,21,5,17,0,0,21,22,5,2,0,0,22,23,3,6,3,0,23,24,5,1,
        0,0,24,27,1,0,0,0,25,27,3,4,2,0,26,17,1,0,0,0,26,19,1,0,0,0,26,25,
        1,0,0,0,27,3,1,0,0,0,28,29,5,11,0,0,29,30,3,6,3,0,30,31,5,2,0,0,
        31,35,3,2,1,0,32,33,5,12,0,0,33,34,5,2,0,0,34,36,3,2,1,0,35,32,1,
        0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,38,5,17,0,0,38,39,3,8,4,0,39,
        40,5,18,0,0,40,43,1,0,0,0,41,43,5,18,0,0,42,37,1,0,0,0,42,41,1,0,
        0,0,43,7,1,0,0,0,44,45,7,0,0,0,45,9,1,0,0,0,4,13,26,35,42
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
    RULE_expr = 3
    RULE_comparator = 4

    ruleNames =  [ "program", "step", "control", "expr", "comparator" ]

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.step()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    break

            self.state = 15
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
        def expr(self):
            return self.getTypedRuleContext(FlowLangParser.ExprContext,0)


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
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = FlowLangParser.InicioStepContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(FlowLangParser.INICIO)
                self.state = 18
                self.match(FlowLangParser.T__0)
                pass
            elif token in [10]:
                localctx = FlowLangParser.ProcesoStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(FlowLangParser.PROCESO)
                self.state = 20
                self.match(FlowLangParser.ID)
                self.state = 21
                self.match(FlowLangParser.T__1)
                self.state = 22
                self.expr()
                self.state = 23
                self.match(FlowLangParser.T__0)
                pass
            elif token in [11]:
                localctx = FlowLangParser.ControlStepContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
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

        def expr(self):
            return self.getTypedRuleContext(FlowLangParser.ExprContext,0)


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
            self.state = 28
            self.match(FlowLangParser.SI)
            self.state = 29
            self.expr()
            self.state = 30
            self.match(FlowLangParser.T__1)
            self.state = 31
            self.step()
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 32
                self.match(FlowLangParser.SINO)
                self.state = 33
                self.match(FlowLangParser.T__1)
                self.state = 34
                self.step()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FlowLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprCompContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FlowLangParser.ID, 0)
        def comparator(self):
            return self.getTypedRuleContext(FlowLangParser.ComparatorContext,0)

        def NUMBER(self):
            return self.getToken(FlowLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComp" ):
                listener.enterExprComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComp" ):
                listener.exitExprComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComp" ):
                return visitor.visitExprComp(self)
            else:
                return visitor.visitChildren(self)


    class ExprNumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FlowLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FlowLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNum" ):
                listener.enterExprNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNum" ):
                listener.exitExprNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNum" ):
                return visitor.visitExprNum(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = FlowLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = FlowLangParser.ExprCompContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(FlowLangParser.ID)
                self.state = 38
                self.comparator()
                self.state = 39
                self.match(FlowLangParser.NUMBER)
                pass
            elif token in [18]:
                localctx = FlowLangParser.ExprNumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(FlowLangParser.NUMBER)
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
        self.enterRule(localctx, 8, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
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





