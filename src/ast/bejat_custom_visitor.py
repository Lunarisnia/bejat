from grammar.BejatParser import BejatParser
from grammar.BejatVisitor import BejatVisitor
from src.memory.variables import variable_notekeeper
from src.memory.to_number import toNumber, ParsingException


class BejatCustomVisitor(BejatVisitor):
    def visitStart(self, ctx: BejatParser.StartContext):
        return super().visitStart(ctx)

    def visitProgram(self, ctx: BejatParser.ProgramContext):
        return super().visitProgram(ctx)

    def identifierValue(self, ctx: BejatParser.IdentifierContext):
        value = variable_notekeeper.getVariable(ctx.IDENTIFIER().__str__())
        if value != None:
            return value
        else:
            print("Variabelnya belom dibuat bang.")
            exit(1)

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
            value = True if ctx.BOOLEAN().__str__() == "bener" else False
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
    
    def visitFunctionBody(self, ctx: BejatParser.FunctionBodyContext):
        return self.visit(ctx.program())

    def visitCallFunction(self, ctx: BejatParser.CallFunctionContext):
        func_id = self.visit(ctx.identifier(0))
        if func_id == "bilang":
            text = self.visit(ctx.getChild(3))
            if type(ctx.getChild(3)) == BejatParser.IdentifierContext:
                text = self.identifierValue(ctx.getChild(3))
            print(text)
        else:
            function_id = ctx.identifier(0)
            # check the type of self.identifierValue(function_id) if confused
            self.visitFunctionBody(self.identifierValue(function_id)())

    # TODO: Might want to consider removing the ability to declare function
    # TODO: support for parameter
    # TODO: Support for local variable
    # TODO: Support return
    # TODO: Fuck me
    def visitDefineFunction(self, ctx: BejatParser.DefineFunctionContext):
        variable_notekeeper.declareVariable(self.visit(ctx.identifier(0)),
                                            ctx.DATATYPES().__str__(),
                                            ctx.functionBody,
                                            BejatParser.DefineFunctionContext)

    def visitExpression(self, ctx: BejatParser.ExpressionContext):
        left = None
        right = None
        # TODO: Do Function call
        if type(ctx.getChild(0)) == BejatParser.IdentifierContext:
            left = self.identifierValue(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))

        if type(ctx.getChild(2)) == BejatParser.IdentifierContext:
            right = self.identifierValue(ctx.getChild(2))
        else:
            right = self.visit(ctx.getChild(2))
        # print(f"Left: {left}, Right: {right}")

        if ctx.MATHOPERATORS():
            operator = ctx.MATHOPERATORS().__str__()
            if operator == "ditambah":
                if type(left) == str and type(right) == str:
                    return left + right
                elif (type(left) == int or type(left) == float or type(left) == bool) and (type(right) == int or type(right) == float or type(right) == bool):
                    return left + right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dikurang":
                if (type(left) == int or type(left) == float or type(left) == bool) and (type(right) == int or type(right) == float or type(right) == bool):
                    return left - right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dibagi":
                if (type(left) == int or type(left) == float or type(left) == bool) and (type(right) == int or type(right) == float or type(right) == bool):
                    return left / right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dikali":
                if (type(left) == int or type(left) == float or type(left) == bool) and (type(right) == int or type(right) == float or type(right) == bool):
                    return left * right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "sisa bagi":
                if (type(left) == int or type(left) == float or type(left) == bool) and (type(right) == int or type(right) == float or type(right) == bool):
                    return left % right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            else:
                print("impossible")
                exit(1)
        elif ctx.COMPARISONOPERATORS():
            # Allowed types
            # String == | != String = String
            # Number > | >= | < | <= | == | != Number = Number
            # Number > | >= | < | <= | == | != Boolean(0 or 1) = Number
            pass
        else:
            print('Gimana ceritanya bisa sampe sini.')
            exit(1)
        return None
