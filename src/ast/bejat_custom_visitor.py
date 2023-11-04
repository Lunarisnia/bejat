from grammar.BejatParser import BejatParser
from grammar.BejatVisitor import BejatVisitor
from src.memory.variables import variable_notekeeper


class BejatCustomVisitor(BejatVisitor):
    def visitStart(self, ctx: BejatParser.StartContext):
        return super().visitStart(ctx)

    def visitProgram(self, ctx: BejatParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitVariable(self, ctx: BejatParser.VariableContext):
        if ctx.atom():
            atom_context: BejatParser.AtomContext = ctx.atom()
            value = None
            if atom_context.STRING():
                value = atom_context.STRING().__str__()
            elif atom_context.BOOLEAN():
                value = atom_context.BOOLEAN().__str__()
            elif atom_context.NUMBER():
                value = atom_context.NUMBER().__str__()
            else:
                print("Yang bener lah tolol")
                exit(1)

            variable_notekeeper.declareVariable(ctx.IDENTIFIER(0).__str__(),
                                                ctx.DATATYPES().__str__(),
                                                value, BejatParser.AtomContext)
        elif ctx.IDENTIFIER().__len__() > 1:
            variable_notekeeper.declareVariable(ctx.IDENTIFIER(1).__str__(),
                                                ctx.DATATYPES().__str__(),
                                                ctx.IDENTIFIER(0).__str__(),
                                                BejatParser.IDENTIFIER)
        elif ctx.expression():
            expression_result = self.visitExpression(ctx.expression())
            variable_notekeeper.declareVariable(ctx.IDENTIFIER(0).__str__(),
                                                ctx.DATATYPES().__str__(),
                                                expression_result, BejatParser.ExpressionContext)
        else:
            print("Lu mau ngapain cok?")
            exit(1)
        return 0

    def visitAtom(self, ctx: BejatParser.AtomContext):
        return super().visitAtom(ctx)
    
    def visitExpression(self, ctx: BejatParser.ExpressionContext):
        if ctx.MATHOPERATORS():
            # Allowed types
            # String + String = String
            # Number + or - or / or * Number = Number
            # Number + or - or / or * Boolean(0 or 1) = Number
            # TODO: Continue This
            # TODO: Consider Modulo
            operator = ctx.MATHOPERATORS().__str__()
            print(operator)
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