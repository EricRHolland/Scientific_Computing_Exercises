# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:46:41 2021

@author: EricH
"""

def arithmetic_arranger(problems, calc=False):
    """
        problems (list[str]): Input list with problems
        calculate_solution Defaults to False.
    """
    import re

    ERR_SIZE = "Error: Too many problems."
    ERR_OP = "Error: Operator must be '+' or '-'."
    ERR_NUM = "Error: Numbers must only contain digits."
    ERR_LEN = "Error: Numbers cannot be more than four digits."

    SPACE = " " * 4
    top_row = ""
    bot_row = ""
    spacers = ""
    results = ""

    if len(problems) > 5:
        return ERR_SIZE

    # loop through the list of problems and apply every operation seperatly
    for problem in problems:
        active_problem = problem.split()
        a = active_problem[0]
        operator = active_problem[1]
        b = active_problem[2]

        if operator != "+" and operator != "-":
            return ERR_OP

        if not (a.isdecimal() and b.isdecimal()):
            return ERR_NUM

        if (len(a) and len(b)) > 4:
            return ERR_LEN

        ## All errors that are required are covered now.
        ## Onto the fun stuff!

        # calculate the length of the longest operand and add 2
        # because of the operator and to separate the number and operator
        # .rjust is justifing the text, overall thing gives a list of the 3 lines you need for every calculation
        length = max(len(a), len(b)) + 2
        top = a.rjust(length)
        # subtract 1 from the length to account for the operator being there, otherwise the numbers lag
        #making it look weird.
        bot = operator + b.rjust(length - 1)
        spacer = "-" * length
        result = "".rjust(length)

        if calc:
            # convert the strs to ints and add or sub the operated stuff
            # convert the result back to str so it's easier to handle with
            if operator == "+":
                result = str(int(a) + int(b)).rjust(length)
            else:
                result = str(int(a) - int(b)).rjust(length)

        if problem == problems[-1]:
            top_row += top
            bot_row += bot
            spacers += spacer
            results += result
        else:
            top_row += top + SPACE
            bot_row += bot + SPACE
            spacers += spacer + SPACE
            results += result + SPACE

    if calc:
        arranged_problems = (
            top_row + "\n" + bot_row + "\n" + spacers + "\n" + results
        )
    else:
        arranged_problems = top_row + "\n" + bot_row + "\n" + spacers

    return arranged_problems


# import re
#
# ERR_SIZE = "Error: Too many problems."
# ERR_OP = "Error: Operator must be '+' or '-'."
# ERR_NUM = "Error: Numbers must only contain digits."
# ERR_LEN = "Error: Numbers cannot be more than four digits."
#
#
# def arithmetic_arranger(problems, calc=False):
#
#     if len(problems) > 5:
#         return ERR_SIZE
#
#     #set out the regex for later
#     regex = re.compile(r'^[0-9]{1,4}$')
#     #create your list
#     listref = []
#
#     #define the for loop to go through your stuff.
#     for problem in problems:
#
#         [a, op, b] = problem.split()
#
#         ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
#         if op != "+" or op != "-":
#             return ERR_OP
#         ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
#         if len(a) > 4 or len(b) > 4:
#             return ERR_LEN
#         ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
#         if regex.match(a) is None or regex.match(b) is None:
#             return ERR_LEN
#
#         ## All errors that are required are covered now.
#         ## Onto the fun stuff!
#         listref.append(cleaner(a,op,b,calc))
#     first_problem = listref[0]
#     format_spaces = " " * 4
#     for problem in listref[1:]:
#         for i in range(0, len(first_problem)):
#             first_problem[i] = first_problem[i] + format_spaces + problem[i]
#     if not calc:
#         first_problem = first_problem[0:3]
#     return '\n'.join(first_problem)


# def cleaner(a,op,b,calc):
#     x = int(a)
#     y = int(b)
#     result = x+y if op == '+' else x-y
#     sign_shift = result if result > 0 else 0-result
#     column_width = max(len(a),len(b), len(str(result))) if calc is True else max(len(a),len(b))
#     result = str(result)
#     column_width = column_width + 2
#     ##.rjust is justifing the text, overall thing gives a list of the 3 lines you need for every calculation
#     fin_result = [a.rjust(column_width), op + " " + b.rjust(column_width - 2), '-' * column_width]
#     if calc is True:
#         fin_result.append(result.rjust(column_width))
#     # return fin_result