def arithmetic_arranger(arithmetic_problems:list, answers=False):
    """Format output of a list of addition and subtraction problems.
    
    Args:
        a (list): a list of arithmetic addition and subtraction problems
        answers(bool): Optional, False by default;\
            Set to True to display answers
    """
    # Check whether maximum problem limit is exceeded
    while len(arithmetic_problems) > 5:
        problemError = 'Error: Too many problems.'
        return problemError
        quit()
    
    # Lists to hold values that will be printed
    first_number_list = []
    second_number_list = []
    operator_list = []
    answers_list = []
    width_list = []
     
    #loop through the different problems to pick numbers and check for errors
    for problem in arithmetic_problems:
        
        problem = problem.replace(' ','') # Remove any whitespace
    
    # Check whether operand other than - or + used    
        while '-' not in problem and '+' not in problem:
            operatorError = 'Error: Operator must be \'+\' or \'-\'.'
            return operatorError
            quit()
        
        # Check whether numbers contain only digits    
        for character in problem:
            if character not in ('0,1,2,3,4,5,6,7,8,9,+,-'):
                numberError = "Error: Numbers must only contain digits."
                return numberError
                quit()
            
        # select numbers and operand from problem
        try:
            problem_breakdown = problem.split('+')
            first_number = problem_breakdown[0]
            second_number = problem_breakdown[1]
            
            answer = int(first_number) + int(second_number) #answer to operation
            operator = '+'
        
        except IndexError:
            problem_breakdown = problem.split('-')
            first_number = problem_breakdown[0]
            second_number = problem_breakdown[1]
            
            answer = int(first_number) - int(second_number) #answer to operation
            operator = '-'
            
        #Check whether digit count in numbers exceeds maximum digit limit (4 digits max)
        digit_count = len(first_number) if len(first_number) > len(second_number)\
            else len(second_number)
            
        while digit_count > 4:
            digitError = "Error: Numbers cannot be more than four digits."
            return digitError
            quit()
            
        # Define minimum width for string output
            # Add +2 for "+ " or "- " that comes before second_number
        width = digit_count + 2 
        
        # Append to lists    
        first_number_list.append(first_number)
        second_number_list.append(second_number)
        operator_list.append(operator)
        answers_list.append(answer)
        width_list.append(width)
        
    # Print out first numbers in each problem first    
    count = 0
    first_line = ''
    for number in first_number_list:
        index = count
        width = width_list[index]
        number = str(number).strip()
        if index == 0:
            first_line += f"{number:>{width}.{width}}"
        else:
            first_line += f"    {number:>{width}.{width}}"
        count += 1
    
    # Print out second number preceeded by operator i.e."+" or "-"
    # Remember we added 2 for operator to width (line 63). \
        # Must subtract the 2 as the preceding sign and ASCII space take those positions  
        
    count = 0     
    second_line = ''   
    for number in second_number_list:
        index = count
        width = width_list[index] - 2
        number = str(number).strip()
        if index == 0:
            second_line += f"{operator_list[index]} {number:>{width}.{width}}"
        else:
            second_line += f"    {operator_list[index]} {number:>{width}.{width}}"
        count += 1
        
    # Print dashes that separates  problem above from answer below
    count = 0
    dash = ''    
    for number in second_number_list:
        index = count
        width = width_list[index]
        line = '-' * width
        if index == 0:
            dash += f'{line}'
        else:    
            dash += f'    {line}'
        count += 1
    count = 0 
    answer_line = ''       
    for answer in answers_list:
        index = count
        width = width_list[index]
        number = str(answer).strip()
        
        if index == 0:
            answer_line += f"{number:>{width}.{width}}"
        else:
            answer_line += f"    {number:>{width}.{width}}"
        count += 1
        
    # Print answer when answers == True        
    if answers != True:
        arranged_problems = f'{first_line}\n{second_line}\n{dash}'
    else:
        arranged_problems = f'{first_line}\n{second_line}\n{dash}\n{answer_line}'
            
    return arranged_problems

if __name__ == '__main__':       
    print(arithmetic_arranger(["3299 - 6998", "1999 - 3801", "4995 + 4993", "1293 + 4999"], True))