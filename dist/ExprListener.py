# Generated from Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_assign.
    def enterVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_assign.
    def exitVariable_assign(self, ctx:ExprParser.Variable_assignContext):
        pass


    # Enter a parse tree produced by ExprParser#parameter.
    def enterParameter(self, ctx:ExprParser.ParameterContext):
        pass

    # Exit a parse tree produced by ExprParser#parameter.
    def exitParameter(self, ctx:ExprParser.ParameterContext):
        pass


    # Enter a parse tree produced by ExprParser#unary_operator.
    def enterUnary_operator(self, ctx:ExprParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#unary_operator.
    def exitUnary_operator(self, ctx:ExprParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#unary.
    def enterUnary(self, ctx:ExprParser.UnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#unary.
    def exitUnary(self, ctx:ExprParser.UnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#operators.
    def enterOperators(self, ctx:ExprParser.OperatorsContext):
        pass

    # Exit a parse tree produced by ExprParser#operators.
    def exitOperators(self, ctx:ExprParser.OperatorsContext):
        pass


    # Enter a parse tree produced by ExprParser#logic_operators.
    def enterLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        pass

    # Exit a parse tree produced by ExprParser#logic_operators.
    def exitLogic_operators(self, ctx:ExprParser.Logic_operatorsContext):
        pass


    # Enter a parse tree produced by ExprParser#numeric_literals.
    def enterNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
        pass

    # Exit a parse tree produced by ExprParser#numeric_literals.
    def exitNumeric_literals(self, ctx:ExprParser.Numeric_literalsContext):
        pass


    # Enter a parse tree produced by ExprParser#text_type.
    def enterText_type(self, ctx:ExprParser.Text_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#text_type.
    def exitText_type(self, ctx:ExprParser.Text_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#numeric_type.
    def enterNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#numeric_type.
    def exitNumeric_type(self, ctx:ExprParser.Numeric_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#literals.
    def enterLiterals(self, ctx:ExprParser.LiteralsContext):
        pass

    # Exit a parse tree produced by ExprParser#literals.
    def exitLiterals(self, ctx:ExprParser.LiteralsContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_type.
    def enterAssignment_type(self, ctx:ExprParser.Assignment_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_type.
    def exitAssignment_type(self, ctx:ExprParser.Assignment_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#comparisson_type.
    def enterComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#comparisson_type.
    def exitComparisson_type(self, ctx:ExprParser.Comparisson_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#typ.
    def enterTyp(self, ctx:ExprParser.TypContext):
        pass

    # Exit a parse tree produced by ExprParser#typ.
    def exitTyp(self, ctx:ExprParser.TypContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_body.
    def enterIf_body(self, ctx:ExprParser.If_bodyContext):
        pass

    # Exit a parse tree produced by ExprParser#if_body.
    def exitIf_body(self, ctx:ExprParser.If_bodyContext):
        pass


    # Enter a parse tree produced by ExprParser#func_declaration.
    def enterFunc_declaration(self, ctx:ExprParser.Func_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#func_declaration.
    def exitFunc_declaration(self, ctx:ExprParser.Func_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#for_loop_condition.
    def enterFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
        pass

    # Exit a parse tree produced by ExprParser#for_loop_condition.
    def exitFor_loop_condition(self, ctx:ExprParser.For_loop_conditionContext):
        pass


    # Enter a parse tree produced by ExprParser#for_loop.
    def enterFor_loop(self, ctx:ExprParser.For_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#for_loop.
    def exitFor_loop(self, ctx:ExprParser.For_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#while_loop.
    def enterWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass

    # Exit a parse tree produced by ExprParser#while_loop.
    def exitWhile_loop(self, ctx:ExprParser.While_loopContext):
        pass


    # Enter a parse tree produced by ExprParser#while_condition.
    def enterWhile_condition(self, ctx:ExprParser.While_conditionContext):
        pass

    # Exit a parse tree produced by ExprParser#while_condition.
    def exitWhile_condition(self, ctx:ExprParser.While_conditionContext):
        pass


    # Enter a parse tree produced by ExprParser#visibility_modifier.
    def enterVisibility_modifier(self, ctx:ExprParser.Visibility_modifierContext):
        pass

    # Exit a parse tree produced by ExprParser#visibility_modifier.
    def exitVisibility_modifier(self, ctx:ExprParser.Visibility_modifierContext):
        pass


    # Enter a parse tree produced by ExprParser#class_or_func_body.
    def enterClass_or_func_body(self, ctx:ExprParser.Class_or_func_bodyContext):
        pass

    # Exit a parse tree produced by ExprParser#class_or_func_body.
    def exitClass_or_func_body(self, ctx:ExprParser.Class_or_func_bodyContext):
        pass


    # Enter a parse tree produced by ExprParser#class_declaration.
    def enterClass_declaration(self, ctx:ExprParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#class_declaration.
    def exitClass_declaration(self, ctx:ExprParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#func_or_class_call.
    def enterFunc_or_class_call(self, ctx:ExprParser.Func_or_class_callContext):
        pass

    # Exit a parse tree produced by ExprParser#func_or_class_call.
    def exitFunc_or_class_call(self, ctx:ExprParser.Func_or_class_callContext):
        pass



del ExprParser