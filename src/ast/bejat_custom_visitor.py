from grammar.BejatParser import BejatParser
from grammar.BejatVisitor import BejatVisitor
from src.memory.variables import variable_notekeeper
from src.memory.to_number import toNumber, ParsingException


class BejatCustomVisitor(BejatVisitor):
    def visitStart(self, ctx: BejatParser.StartContext):
        return super().visitStart(ctx)

    def visitProgram(self, ctx: BejatParser.ProgramContext):
        return super().visitProgram(ctx)
    
    def visitIdentifier(self, ctx: BejatParser.IdentifierContext):
        return ctx.IDENTIFIER().__str__()

    def visitVariable(self, ctx: BejatParser.VariableContext):
        if ctx.atom():
            value = self.visit(ctx.atom())
            variable_notekeeper.declareVariable(self.visit(ctx.identifier(0)),
                                                ctx.DATATYPES().__str__(),
                                                value, BejatParser.AtomContext)
        elif ctx.identifier().__len__() > 1:
            variable_notekeeper.declareVariable(self.visit(ctx.identifier(1)),
                                                ctx.DATATYPES().__str__(),
                                                self.visit(ctx.identifier(0)),
                                                BejatParser.IdentifierContext)
        elif ctx.expression():
            expression_result = self.visit(ctx.expression())
            variable_notekeeper.declareVariable(self.visit(ctx.identifier(0)),
                                                ctx.DATATYPES().__str__(),
                                                expression_result, BejatParser.ExpressionContext)
        else:
            print("Lu mau ngapain cok?")
            exit(1)
        return 0

    def visitAtom(self, ctx: BejatParser.AtomContext):
        value = None
        if ctx.STRING():
            value = ctx.STRING().__str__()
        elif ctx.BOOLEAN():
            value = True if value == ctx.BOOLEAN().__str__() else False
        elif ctx.NUMBER():
            value = ctx.NUMBER().__str__()
            try:
                value = toNumber(value)
            except ParsingException:
                print("what the fuck is wrong with you?")
                exit(1)
        else:
            print("Yang bener lah tolol")
            exit(1)
        return value
    
    def visitExpression(self, ctx: BejatParser.ExpressionContext):
        if ctx.MATHOPERATORS():
            # Allowed types
            # String + String = String
            # Number + or - or / or * Number = Number
            # Number + or - or / or * Boolean(0 or 1) = Number
            # TODO: Continue This
            # TODO: Consider Modulo
            operator = ctx.MATHOPERATORS().__str__()
            if operator == "ditambah":
                allowed_mix = {
                    "str": "str",
                    "num": "num"
                }
                # We cannot know which one is left/right value this way
                print(self.visit(ctx.getChild(0)))
                

                # # String + String
                # # Not String + Num / Num + String
                # left_value = None
                # right_value = None
                # if ctx.atom().__len__() > 0:
                #     if ctx.atom(0).STRING():
                #         left_value = ctx.atom(0).STRING().__str__()
                #     if ctx.atom(1) and 
                # if ctx.IDENTIFIER().__len__() > 0:
                #     pass

                # if ctx.callFunction().__len__() > 0:
                #     pass
                # # else:
                # #     print("Gimana ceritanya?")
                # #     exit(1)
            elif operator == "dikurang":
                pass
            elif operator == "dibagi":
                pass
            elif operator == "dikali":
                pass
            else:
                print("impossible")
                exit(1)
            # print(operator)
            pass
        elif ctx.COMPARISONOPERATORS():
            # Allowed types
            # String == | != String = String
            # Number > | >= | < | <= | == | != Number = Number
            # Number > | >= | < | <= | == | != Boolean(0 or 1) = Number
            pass
        else:
            print('Gimana ceritanya bisa sampe sini.')
            exit(1)
        return True # TODO: Return the result of the calculation