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

    #create your list
    listref = []

    #define the for loop to go through your stuff.
    for problem in problems:

        [a, op, b] = problem.split()
        if op != "+" or op != "-":
            return ERR_OP
        
        listref.append((a,op,b))










def cleaner(a,op,b,calc):
    x = int(a)
    y = int(b)

