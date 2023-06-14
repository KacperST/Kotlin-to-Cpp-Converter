# Generated from Expr.g4 by ANTLR 4.12.0
from antlr4 import *

import dist.ExprParser

if __name__ is not None and "." in __name__:
    from dist.ExprParser import ExprParser
else:
    from ExprParser import ExprParser


# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):
    indent = 0

    def __init__(self):
        self.f = open("output_file", "w")
        self.f.write("#include <iostream> \nusing namespace std;\n\n")

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#expr.
    # TODO
    def visitExpr(self, ctx: ExprParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#variable.
    # TODO
    def visitVariable(self, ctx: ExprParser.VariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#variable_declaration.
    # TODO NIE TYKAj
    def visitVariable_declaration(self, ctx: ExprParser.Variable_declarationContext):
        typ = self.visitTyp(ctx.typ())
        name = ctx.IDENTIFIER().getText()
        const = "const " if ctx.VAL() else ""

        value = None
        if ctx.EQ():
            value = " = " + ctx.literals().getText() + ";\n"
        self.f.write('\t' * self.indent + const + typ + ' ' + name + value)
        pass

    # Visit a parse tree produced by ExprParser#variable_assign.
    # TODO
    def visitVariable_assign(self, ctx: ExprParser.Variable_assignContext):
        const = "const " if ctx.VAL() else ""
        name = ctx.IDENTIFIER().getText()
        value = " = " + ctx.literals().getText().replace('\n', '') + ";\n"
        print(ctx.literals().getText())
        self.f.write('\t' * self.indent + const + name + value)
        pass

    # Visit a parse tree produced by ExprParser#parameter.
    # zwraca pojedynczy parametr bez srednika

    def visitParameter(self, ctx: ExprParser.ParameterContext):
        typ = self.visitTyp(ctx.typ())
        name = ctx.IDENTIFIER().getText()
        return typ + " " + name, name

    # Visit a parse tree produced by ExprParser#unary_operator.
    def visitUnary_operator(self, ctx: ExprParser.Unary_operatorContext):
        pass

    # Visit a parse tree produced by ExprParser#unary.
    def visitUnary(self, ctx: ExprParser.UnaryContext):
        self.f.write('\t' * self.indent + ctx.getText() + ";" + "\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#operators.
    # zrobione
    def visitOperators(self, ctx: ExprParser.OperatorsContext):
        self.f.write(" " + ctx.getText() + " ")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#logic_operators.
    # zrobione
    # TODO
    def visitLogic_operators(self, ctx: ExprParser.Logic_operatorsContext):
        self.f.write(" " + ctx.getText() + " ")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#numeric_literals.
    def visitNumeric_literals(self, ctx: ExprParser.Numeric_literalsContext):
        # self.f.write(" " + ctx.getText() + " ")
        # return self.visitChildren(ctx)
        pass

    # Visit a parse tree produced by ExprParser#text_type.
    def visitText_type(self, ctx: ExprParser.Text_typeContext):
        pass

    # Visit a parse tree produced by ExprParser#numeric_type.
    def visitNumeric_type(self, ctx: ExprParser.Numeric_typeContext):
        pass

    # Visit a parse tree produced by ExprParser#literals.
    def visitLiterals(self, ctx: ExprParser.LiteralsContext):
        if ctx.getText() == "null":
            self.f.write(" " + "NULL" + "\n")
            pass
        self.f.write(" " + ctx.getText() + ";\n")
        pass

    # Visit a parse tree produced by ExprParser#assignment_type.
    def visitAssignment_type(self, ctx: ExprParser.Assignment_typeContext):
        pass

    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        self.f.write('\t' * self.indent + " " + ctx.getText() + ";\n")
        pass

    # Visit a parse tree produced by ExprParser#comparisson_type.
    def visitComparisson_type(self, ctx: ExprParser.Comparisson_typeContext):
        self.f.write(" " + ctx.getText() + " ")
        pass

    # Visit a parse tree produced by ExprParser#typ.
    def visitTyp(self, ctx: ExprParser.TypContext):
        return ctx.getText().lower()

    # Visit a parse tree produced by ExprParser#if_statement.
    def visitIf_statement(self, ctx: ExprParser.If_statementContext):
        self.f.write('\t' * self.indent + f"if({ctx.if_body().getText()})" + '{\n')
        self.indent += 1
        for i in ctx.expr():
            self.visit(i)
        self.indent -= 1
        self.f.write('\t' * self.indent + "}\n")
        pass

    # Visit a parse tree produced by ExprParser#if_body.
    def visitIf_body(self, ctx: ExprParser.If_bodyContext):
        pass

    # Visit a parse tree produced by ExprParser#func_declaration.
    def visitFunc_declaration(self, ctx: ExprParser.Func_declarationContext):
        return_type = self.visitTyp(ctx.typ()) if ctx.typ() else '\t' * self.indent + 'void'
        parameters = self.visit(ctx.class_or_func_body())
        name = ctx.IDENTIFIER().getText()
        self.f.write(f"{return_type} {name}(")
        new_parameters = list(zip(*parameters[:]))
        if new_parameters:
            self.f.write(', '.join(new_parameters[0]) + ') {\n')
        else:
            self.f.write(') {\n')
        self.indent += 1
        for e in ctx.expr():
            self.visitExpr(e)
        if 'void' not in return_type:
            self.f.write('\t' * self.indent + f'return {ctx.literals().getText()};\n')
        self.indent -= 1
        self.f.write('\t' * self.indent + '}\n')

        # return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#for_loop_condition.
    def visitFor_loop_condition(self, ctx: ExprParser.For_loop_conditionContext):
        compare = "<"
        if ctx.DOWNTO():
            compare = ">"

        if not ctx.STEP() and compare == ">":
            return "int i = " + ctx.INTLITERAL()[0] \
                .getText() + ";" + f' i {compare} {ctx.INTLITERAL()[1].getText()}; i--'
        elif not ctx.STEP() and compare == "<":
            return "int i = " + ctx.INTLITERAL()[0] \
                .getText() + ";" + f' i {compare} {ctx.INTLITERAL()[1].getText()}; i++'
        elif compare == "<":
            return "int i = " + ctx.INTLITERAL()[0] \
                .getText() + ";" + f' i {compare} {ctx.INTLITERAL()[1].getText()}; i += {ctx.INTLITERAL()[2].getText()}'
        if compare == ">":
            return "int i = " + ctx.INTLITERAL()[0] \
                .getText() + ";" + f' i {compare} {ctx.INTLITERAL()[1].getText()}; i -= {ctx.INTLITERAL()[2].getText()}'

        pass

    # Visit a parse tree produced by ExprParser#for_loop.
    def visitFor_loop(self, ctx: ExprParser.For_loopContext):
        condition = self.visit(ctx.for_loop_condition())
        self.f.write('\t' * self.indent + f'for({condition})' + '{\n')
        self.indent += 1
        for i in ctx.expr():
            self.visit(i)
        self.indent -= 1
        self.f.write('\t' * self.indent + "}\n")
        pass

    # Visit a parse tree produced by ExprParser#while_loop.
    def visitWhile_loop(self, ctx: ExprParser.While_loopContext):
        self.f.write('\t' * self.indent + f'while( {ctx.while_condition().getText()} )' + "{\n")
        self.indent += 1
        for i in ctx.expr():
            self.visit(i)
        self.indent -= 1
        self.f.write('\t' * self.indent + "}\n")
        pass

    # Visit a parse tree produced by ExprParser#while_condition.
    def visitWhile_condition(self, ctx: ExprParser.While_conditionContext):
        pass

    # Visit a parse tree produced by ExprParser#visibility_modifier.
    def visitVisibility_modifier(self, ctx: ExprParser.Visibility_modifierContext):
        self.f.write(f'{ctx[0].getText()} ')

    # Visit a parse tree produced by ExprParser#class_or_func_body.
    # zwraca liste parametrow w postaci c++ ( bez srednika )
    def visitClass_or_func_body(self, ctx: ExprParser.Class_or_func_bodyContext):
        parameters = []
        if ctx.parameter():
            for i in ctx.parameter():
                parameters.append(self.visitParameter(i))
        return parameters

    # Visit a parse tree produced by ExprParser#class_declaration.
    def visitClass_declaration(self, ctx: ExprParser.Class_declarationContext):
        keywords = ('public', 'private', 'protected')
        active_keyword = 'public'
        children = list(ctx.getChildren())
        name = ctx.IDENTIFIER()
        parameter = self.visitClass_or_func_body(ctx.class_or_func_body())
        variables = ctx.variable_declaration()
        functions = ctx.func_declaration()
        self.f.write('\t' * self.indent + f'{ctx.CLASS()} {name}' + ' {\n')
        self.indent += 1

        new_parameters = list(zip(*parameter[:]))

        constructor_dict = {}
        for x in new_parameters[1]:
            constructor_dict[x] = x
        for v in variables:
            splited = v.getText().split('=')
            if splited[1] in new_parameters[1]:
                name2 = v.IDENTIFIER().getText()
                constructor_dict[splited[1]] = name2

        for i in parameter:
            if constructor_dict[i[1]] == i[1]:
                self.f.write('\t' * self.indent + i[0] + ";\n")

        for v in variables:
            index = children.index(v)
            if children[index - 1].getText() in keywords:
                self.f.write(f"{children[index - 1].getText()}:\n")
            if v.IDENTIFIER().getText() not in constructor_dict.values():
                self.visitVariable_declaration(v)

        if new_parameters:
            self.f.write('\t' * self.indent + f'{name}({", ".join(new_parameters[0])})' + " {\n")
        else:
            self.f.write('\t' * self.indent + f'{name}()' + " {\n")
        self.indent += 1
        for i in parameter:
            self.f.write('\t' * self.indent + f"this.{constructor_dict[i[1]]} = {i[1]};\n")
        self.indent -= 1
        self.f.write('\t' * self.indent + '}\n')

        for f in functions:
            index = functions.index(f)
            if functions[index - 1].getText() in keywords:
                self.f.write('\t' * self.indent + f"{functions[index - 1].getText()}:\n")
            self.visitFunc_declaration(f)
        self.indent -= 1
        self.f.write('\t' * self.indent + '}\n')

        # return self.visitChildren(ctx)
        # for i in ctx.children:
        #     print(i," ", type(i))
        #     if isinstance(i,TerminalNode):
        #         print("adw" ,i)
        #         self.f.write(str(i) + " ")
        #     elif isinstance(i,dist.ExprParser.ExprParser.Class_or_func_bodyContext):
        #         parameter = self.visit(i)
        #         print("parameter",parameter)
        #     elif isinstance(i,dist.ExprParser.ExprParser.Func_declarationContext) and not constructor_created:
        #         self.f.write(str(i) + " ")
        #     else:
        #         if isinstance(i, dist.ExprParser.ExprParser.Visibility_modifierContext):
        #             continue
        #         self.visit(i)
        # class_modifier = ctx.class_visibility_modifier().getText() if ctx.class_visibility_modifier() is not None else None
        # # print(class_modifier)
        # # print(modifier)
        # name = ctx.IDENTIFIER().getText()
        # constructor_body = self.visitClass_or_func_body(ctx.class_or_func_body())
        # paramteters_modifiers = [self.visitParameter_visibility_modifier(i) for i in ctx.parameter_visibility_modifier()] if ctx.parameter_visibility_modifier() is not None else None
        # func_modifiers = [self.visitFunc_visibility_modifier(i) for i in ctx.func_visibility_modifier()] if ctx.func_visibility_modifier() is not None else None
        # parameters = ctx.variable_declaration()
        #
        # body = None

        # self.f.write(class_modifier + " " + name + "{" + "\n")\
        # print(self.visitChildren(ctx))
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#func_or_class_call.
    def visitFunc_or_class_call(self, ctx: ExprParser.Func_or_class_callContext):
        if ctx.IDENTIFIER().getText() == 'print':
            self.f.write('\t' * self.indent + "cout")
            for i in ctx.literals():
                self.f.write(" << " + i.getText())
            self.f.write(" << endl;\n")

        else:
            self.f.write('\t' * self.indent + ctx.getText().replace('\n', '') + ";\n")
        pass
        # Visit a parse tree produced by ExprParser#class_visibility_modifier.


del ExprParser
