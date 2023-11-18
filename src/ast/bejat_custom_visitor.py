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
            if type(value) == bool:
                return "bener" if value else "salah"
            return value
        else:
            print("Variabelnya belom dibuat bang.")
            exit(1)

    def visitIdentifier(self, ctx: BejatParser.IdentifierContext):
        return ctx.IDENTIFIER().__str__()

    def visitVariable(self, ctx: BejatParser.VariableContext):
        if ctx.atom():
            value = self.visit(ctx.atom())
            variable_notekeeper.declareVariable(
                self.visit(ctx.identifier(0)),
                ctx.DATATYPES().__str__(),
                value,
                BejatParser.AtomContext,
            )
        elif ctx.identifier().__len__() > 1:
            variable_notekeeper.declareVariable(
                self.visit(ctx.identifier(1)),
                ctx.DATATYPES().__str__(),
                self.visit(ctx.identifier(0)),
                BejatParser.IdentifierContext,
            )
        elif ctx.expression():
            expression_result = self.visit(ctx.expression())
            variable_notekeeper.declareVariable(
                self.visit(ctx.identifier(0)),
                ctx.DATATYPES().__str__(),
                expression_result,
                BejatParser.ExpressionContext,
            )
        elif ctx.callFunction():
            function_result = self.visit(ctx.callFunction())
            variable_notekeeper.declareVariable(
                self.visit(ctx.identifier(0)),
                ctx.DATATYPES().__str__(),
                function_result,
                BejatParser.CallFunctionContext,
            )
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

    def visitCallFunction(self, ctx: BejatParser.CallFunctionContext):
        func_id = self.visit(ctx.identifier(0))
        if func_id == "bilang":
            text = self.visit(ctx.getChild(3))
            if type(ctx.getChild(3)) == BejatParser.IdentifierContext:
                text = self.identifierValue(ctx.getChild(3))
            print(text)
        elif func_id == "gaguna":
            return "Gaguna"
        
        else:
            print(f"{func_id} kaga ada. yang bener lah")

    def visitVariableReassignment(self, ctx: BejatParser.VariableReassignmentContext):
        result = self.visit(ctx.getChild(0))
        key = self.visitIdentifier(ctx.identifier()[-1])
        variable = self.identifierValue(ctx.identifier()[-1])

        if type(result) == type(variable):
            variable_notekeeper.updateValue(key, result)
        else:
            print(
                f"{result} typenya beda sama {self.visitIdentifier(ctx.identifier()[-1])} yang bener dong"
            )
            exit(1)

    def visitIfStatement(self, ctx: BejatParser.IfStatementContext):
        expression = self.visitExpression(ctx.expression())
        if expression:
            self.visit(ctx.program())
        else:
            if ctx.elseIfStatement().__len__() > 0:
                for elifstatement in ctx.elseIfStatement():
                    expression = self.visitExpression(
                        elifstatement.expression())
                    if expression:
                        self.visitElseIfStatement(elifstatement)
                        break
            if ctx.elseStatement() and not (expression):
                self.visit(ctx.elseStatement())

    def visitElseIfStatement(self, ctx: BejatParser.ElseIfStatementContext):
        return self.visit(ctx.program())

    def visitElseStatement(self, ctx: BejatParser.ElseStatementContext):
        return self.visit(ctx.program())

    def visitStatement(self, ctx: BejatParser.StatementContext):
        return self.visit(ctx.ifStatement())

    def visitExpression(self, ctx: BejatParser.ExpressionContext):
        left = None
        right = None

        if type(ctx.getChild(0)) == BejatParser.IdentifierContext:
            left = self.identifierValue(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))

        if type(ctx.getChild(2)) == BejatParser.IdentifierContext:
            right = self.identifierValue(ctx.getChild(2))
        else:
            right = self.visit(ctx.getChild(2))

        if ctx.MATHOPERATORS():
            operator = ctx.MATHOPERATORS().__str__()
            if operator == "ditambah":
                if type(left) == str and type(right) == str:
                    return left + right
                elif (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left + right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dikurang":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left - right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dibagi":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left / right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "dikali":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left * right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            elif operator == "sisa bagi":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left % right
                else:
                    print(f"{left} {operator} {right}????? Mana bisa bang")
                    exit(1)
            else:
                print("impossible")
                exit(1)
        elif ctx.COMPARISONOPERATORS():
            operator = ctx.COMPARISONOPERATORS().__str__()
            if operator == "sama ama":
                return left == right
            elif operator == "ga sama ama":
                return left != right
            elif operator == "lebih dari":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left > right
            elif operator == "lebih ato sama ama":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left >= right
            elif operator == "kurang dari":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left < right
            elif operator == "kurang ato sama ama":
                if (
                    type(left) == int or type(
                        left) == float or type(left) == bool
                ) and (
                    type(right) == int or type(
                        right) == float or type(right) == bool
                ):
                    return left <= right
            else:
                print("gamungkin kesini lah aneh lu")
                exit(1)
        else:
            print("Gimana ceritanya bisa sampe sini.")
            exit(1)
        return None
