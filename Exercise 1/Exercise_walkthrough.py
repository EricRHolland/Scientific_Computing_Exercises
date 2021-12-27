def arithmetic_arranger(problems, calc=False):
    """
        problems (list[str]): Input list with problems
        calculate_solution Defaults to False.
    """

    ##Step 1: Create the error messages
    # I knew immediately that I would want to break these messages out into variable names because of my training
    import re

    ERR_SIZE = "Error: Too many problems."
    ERR_OP = "Error: Operator must be '+' or '-'."
    ERR_NUM = "Error: Numbers must only contain digits."
    ERR_LEN = "Error: Numbers cannot be more than four digits."


# Next, I wanted to think about the end product? What are the maximum number of characters I would have in a solution?
# 4 is the max so you want 5 max characters for the solution, but what about the operator +-?
# we need to add 2 spaces to the bottom row to account for the operator and the space between the +- and the number
#Right now, I just want 4 spaces and creating a full output of the rows and results.

    SPACE = " " * 4
    top_row = ""
    bot_row = ""
    spacers = ""
    results = ""


# Before we convert anything to int, take advantage of string and list properties, like len, to get stuff that will give errors.
This means grabbing stuff that
    if len(problems) > 5:
        return ERR_SIZE

    # loop through the list of problems and apply every operation seperately
    # So this problem requires me to solve many different +- operations at once, which means we have to split out the values from the tuple
    # it is some tuples within a list as the input according to the sample input from the .readme.

    for problem in problems:
        active_problem = problem.split()
        # Now that its been split, it appears as a list of a, operator, b, and a calc boolean
        # Honestly not quite sure how the calc thing works if it's being passed through this split function or not.
        # With that done, now we have a,operator, b that are still strings!
        #use these strings to get the error messages to work.
        a = active_problem[0]
        operator = active_problem[1]
        b = active_problem[2]

        if operator != "+" and operator != "-":
            return ERR_OP


        # cool way of checking if it is a number without using regex like in my commented out example. The previous way to do this is as follows:
        # PROBLEM STATEMENTS IF SOMETHING GOES WRONG
        # if regex.match(a) is None or regex.match(b) is None:
        # return ERR_LEN
        # In this case, the regex is defined:
        # regex = re.compile(r'^[0-9]{1,4}$')
        if not (a.isdecimal() and b.isdecimal()):
            return ERR_NUM

        # Takes advantage of a and b still being strings so we can see if they are less than 5 integers

        if (len(a) and len(b)) > 4:
            return ERR_LEN

        ## All errors that are required are covered now.
        ## Onto the fun stuff!

        # calculate the length of the longest operand and add 2
        # because of the operator and to separate the number and operator
        # .rjust is justifing the text, overall thing gives a list of the 3 lines you need for every calculation
        # The + 2 as discussed earlier is for the space and the +-
        length = max(len(a), len(b)) + 2
        #This will give you max 6 character right justified top part
        top = a.rjust(length)


        # subtract 1 from the length to account for the operator being there, otherwise the numbers lag
        # making it look weird.
        # Why the -1? Because it would otherwise justify a max 6 char bot part with 7 characters on a line if the length isnt modified.
        bot = operator + b.rjust(length - 1)

        # The spacer needs to be length max 6 char like before otherwise the top part wont match.
        # creating an empty string for the result so we can abuse the str methods to align our result.
        spacer = "-" * length
        result = "".rjust(length)


        if calc:
            # Honestly not quite sure how this variable is assigned either inside or outside the tuple still? Could be wrong though
            # convert the strs to ints and add or sub the operated stuff
            # convert the result back to str so it's easier to handle with our len and .rjust
            #only need the + part since there are only two options and any exceptions to this are caught earlier.
            if operator == "+":
                result = str(int(a) + int(b)).rjust(length)
            else:
                result = str(int(a) - int(b)).rjust(length)

        if problem == problems[-1]:
            #This could also be done by doing a len(problems) - 1 and assigning that to a var and calling it in the bracket.
            # Did it this way because its faster to reference the end of a list with the -1 part

            top_row += top
            bot_row += bot
            spacers += spacer
            results += result
            # So this part is fun because it is stops the writing of the loop to the lines.
            # This will close it and not add any more space to the end of the lines.
            # Instead of creating one individual box with arithmetic, I put them all into strings and print the strings in order

        else:
            # This says: If the problem we are working on is NOT the last, add it to the 4 strings and add more space after it
            # This will let us keep building the lines since it isn't the last one in the list we defined earlier.
            top_row += top + SPACE
            bot_row += bot + SPACE
            spacers += spacer + SPACE
            results += result + SPACE


    # This line finally shows the difference in the calc T/F cases. If it stays false, it will only return whitespace as the results lines
    # If it is changed to true, it will not show the results and instead give us the spacers (blank space created earlier)

    if calc:
        arranged_problems = (
            top_row + "\n" + bot_row + "\n" + spacers + "\n" + results
        )
    else:
        arranged_problems = top_row + "\n" + bot_row + "\n" + spacers

    return arranged_problems

    # This passes all the tests that the replit autograder uses. Woohoo!

#Summary thought process and breakthroughs
# 1) Definitely a list iteration problem since it has multiple problems, so we need to know how to split a tuple
# 2) Need to know how to iterate through a list using for loops
# 3) Realized it was much easier to create a string readout of the 4 lines that is justified instead of doing max 5 separate iterations with space.
# 4) created spacers and used logic to decide the length between problems, and this ties our approach together.
# 5) Used the spacers to give blank space if calc boolean variable is not touched by input. Then it's solved!
