# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:46:41 2021

@author: EricH
"""
import re

ERR_SIZE = "Error: Too many problems."
ERR_OP = "Error: Operator must be '+' or '-'."
ERR_NUM = "Error: Numbers must only contain digits."
ERR_LEN = "Error: Numbers cannot be more than four digits."


def arithmetic_arranger(problems, calc=False):

    if len(problems) > 5:
        return ERR_SIZE

    #set out the regex for later
    regex = re.compile(problems, r'^[0-9]{1,4}$')
    #create your list
    listref = []

    #define the for loop to go through your stuff.
    for problem in problems:

        [a, op, b] = problem.split()

        ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
        if op != "+" or op != "-":
            return ERR_OP
        ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
        if len(a) > 4 or len(b) > 4:
            return ERR_LEN
        ##PROBLEM STATEMENTS IF SOMETHING GOES WRONG
        if regex.match(a) is None or regex.match(b) is None:
            return ERR_LEN

        ## All errors that are required are covered now.
        ## Onto the fun stuff!
        listref.append(cleaner(a,op,b,calc))













def cleaner(a,op,b,calc):
    x = int(a)
    y = int(b)
    result = x+y if op == '+' else x-y
    sign_shift = result if result > 0 else 0-result
    column_width = max(len(a),len(b), len(str(result))) if calc is True else max(len(a),len(b))
    result = str(result)
    column_width = column_width + 2
    ##.rjust is justifing the text, overall thing gives a list of the 3 lines you need for every calculation
    fin_result = [a.rjust(column_width), op + " " + b.rjust(column_width - 2), '-' * column_width]
    if calc is True:
        fin_result.append(result.rjust(column_width))
    return fin_result

