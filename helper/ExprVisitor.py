#
# # Generated from Expr.g4 by ANTLR 4.12.0
# from antlr4 import *
# if __name__ is not None and "." in __name__:
#     from dist.ExprParser import ExprParser
# else:
#     from ExprParser import ExprParser
#
# # This class defines a complete generic visitor for a parse tree produced by ExprParser.
#
# class ExprVisitor(ParseTreeVisitor):
#
#     def __init__(self):
#         self.f = open("output_file", "w")
#         self.f.write("#include <iostream> \nusing namespace std;\n\n")
#
#
#     # Visit a parse tree produced by ExprParser#prog.
#     def visitProg(self, ctx:ExprParser.ProgContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#expr.
#     # TODO
#     def visitExpr(self, ctx:ExprParser.ExprContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#variable.
#     # TODO
#     def visitVariable(self, ctx:ExprParser.VariableContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#variable_declaration.
#     # TODO NIE TYKAj
#     def visitVariable_declaration(self, ctx: ExprParser.Variable_declarationContext):
#         typ = self.visitTyp(ctx.typ())
#         name = ctx.IDENTIFIER().getText()
#         value = None
#         if ctx.EQ():
#             value = " = " + ctx.literals().getText() + ";\n"
#         self.f.write(typ + ' ' + name + value)
#         print("var declar", ctx.getText())
#
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#variable_assign.
#     # TODO
#     def visitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#parameter.
#     # zwraca pojedynczy parametr bez srednika
#
#     def visitParameter(self, ctx:ExprParser.ParameterContext):
#         typ = self.visitTyp(ctx.typ())
#         name = ctx.IDENTIFIER().getText()
#         print("paramterer", ctx.getText())
#         return typ + " " + name
#
#
#     # Visit a parse tree produced by ExprParser#unary_operator.
#     def visitUnary_operator(self, ctx:ExprParser.Unary_operatorContext):
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#unary.
#     def visitUnary(self, ctx:ExprParser.UnaryContext):
#         self.f.write(ctx.getText() + ";" + "\n")
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#operators.
#     # zrobione
#     def visitOperators(self, ctx:ExprParser.OperatorsContext):
#         self.f.write(" " + ctx.getText() + " ")
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#logic_operators.
#     # zrobione
#     #TODO
#     def visitLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
#         self.f.write(" " + ctx.getText() + " ")
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#numeric_literals.
#     def visitNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
#         # self.f.write(" " + ctx.getText() + " ")
#         # return self.visitChildren(ctx)
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#text_type.
#     def visitText_type(self, ctx:ExprParser.Text_typeContext):
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#numeric_type.
#     def visitNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#literals.
#     def visitLiterals(self, ctx:ExprParser.LiteralsContext):
#         if ctx.getText() == "null":
#             self.f.write(" " + "NULL" + "\n")
#             pass
#         self.f.write(" " + ctx.getText() + ";\n")
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#assignment_type.
#     def visitAssignment_type(self, ctx:ExprParser.Assignment_typeContext):
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#assignment.
#     def visitAssignment(self, ctx:ExprParser.AssignmentContext):
#         self.f.write(" " + ctx.getText() + ";\n")
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#comparisson_type.
#     def visitComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
#         self.f.write(" " + ctx.getText() + " ")
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#typ.
#     def visitTyp(self, ctx:ExprParser.TypContext):
#         return ctx.getText().lower()
#
#
#     # Visit a parse tree produced by ExprParser#if_statement.
#     def visitIf_statement(self, ctx:ExprParser.If_statementContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#if_body.
#     def visitIf_body(self, ctx:ExprParser.If_bodyContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#func_declaration.
#     def visitFunc_declaration(self, ctx:ExprParser.Func_declarationContext):
#         return_type = "void"
#         if ctx.typ():
#             return_type = ctx.typ().getText()
#         name = ctx.IDENTIFIER().getText()
#
#
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#for_loop_condition.
#     def visitFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#for_loop.
#     def visitFor_loop(self, ctx:ExprParser.For_loopContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#while_loop.
#     def visitWhile_loop(self, ctx:ExprParser.While_loopContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#while_condition.
#     def visitWhile_condition(self, ctx:ExprParser.While_conditionContext):
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#visibility_modifier.
#     def visitVisibility_modifier(self, ctx:ExprParser.Visibility_modifierContext):
#         return ctx.getText()
#         pass
#
#
#     # Visit a parse tree produced by ExprParser#class_or_func_body.
#     #zwraca liste parametrow w postaci c++ ( bez srednika )
#     def visitClass_or_func_body(self, ctx:ExprParser.Class_or_func_bodyContext):
#         parameters = []
#         if ctx.parameter():
#             for i in ctx.parameter():
#                 parameters.append(self.visitParameter(i))
#         return parameters
#
#
#     # Visit a parse tree produced by ExprParser#class_declaration.
#     def visitClass_declaration(self, ctx:ExprParser.Class_declarationContext):
#         # class_modifier = ctx.class_visibility_modifier().getText() if ctx.class_visibility_modifier() is not None else None
#         # # print(class_modifier)
#         # # print(modifier)
#         # name = ctx.IDENTIFIER().getText()
#         # constructor_body = self.visitClass_or_func_body(ctx.class_or_func_body())
#         # paramteters_modifiers = [self.visitParameter_visibility_modifier(i) for i in ctx.parameter_visibility_modifier()] if ctx.parameter_visibility_modifier() is not None else None
#         # func_modifiers = [self.visitFunc_visibility_modifier(i) for i in ctx.func_visibility_modifier()] if ctx.func_visibility_modifier() is not None else None
#         # parameters = ctx.variable_declaration()
#         #
#         # body = None
#
#         # self.f.write(class_modifier + " " + name + "{" + "\n")\
#
#         return self.visitChildren(ctx)
#
#
#     # Visit a parse tree produced by ExprParser#func_or_class_call.
#     def visitFunc_or_class_call(self, ctx:ExprParser.Func_or_class_callContext):
#
#         return ctx.getText()
#         # Visit a parse tree produced by ExprParser#class_visibility_modifier.
#
#     def visitClass_visibility_modifier(self, ctx: ExprParser.Class_visibility_modifierContext):
#         print("class modifier", ctx.getText())
#         self.f.write(ctx.getText() + ' class ')
#         return ctx.getText()
#
#         # Visit a parse tree produced by ExprParser#parameter_visibility_modifier.
#
#     def visitParameter_visibility_modifier(self, ctx: ExprParser.Parameter_visibility_modifierContext):
#         print("paramtere modifier", ctx.getText())
#         self.f.write(ctx.getText() + ' ')
#         return ctx.getText()
#
#         # Visit a parse tree produced by ExprParser#func_visibility_modifier.
#
#     def visitFunc_visibility_modifier(self, ctx: ExprParser.Func_visibility_modifierContext):
#         print("func modifier", ctx.getText())
#         self.f.write(ctx.getText() + ' ')
#         return ctx.getText()
#
#
#
# del ExprParser