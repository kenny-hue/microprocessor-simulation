from operator import neg

def Calculation_func(operator, *arguments):
    
    if operator == 'add':
        return sum(arguments)

    elif operator == 'mul':

        if len(arguments) != 2:
            if len(arguments) < 2:
                return f'invalid operation {operator} {arguments[0]}'
            else:
                return f'invalid operation {operator} {arguments[0]} {arguments[1]} {arguments[2]}'
            
        return arguments[0] * arguments[1]

    elif operator == 'or':
        if len(arguments) != 2:
            if len(arguments) < 2:
                return f'invalid operation {operator} {arguments[0]}'
            else:
                return f'invalid operation {operator} {arguments[0]} {arguments[1]} {arguments[2]}'
        
        return int(bool(0 or (arguments[0] or arguments[1])))


    elif operator == 'nand':

        if len(arguments) != 2:
            if len(arguments) < 2:
                return f'invalid operation {operator} {arguments[0]}'
            else:
                return f'invalid operation {operator} {arguments[0]} {arguments[1]} {arguments[2]}'
            
        return int(not (arguments[0] and arguments[1]))

    elif operator == 'noop':

        if any(arg > 0 for arg in arguments):
            if len(arguments) < 2:
                return f'invalid operation {operator} {arguments[0]}'
            else:
                return f'invalid operation {operator} {arguments[0]} {arguments[1]}'
        else:
            return ""

    elif operator == 'gt':

        if len(arguments) != 2:
            if len(arguments) < 2:
                return f'invalid operation {operator} {arguments[0]}'
            else:
                return f'invalid operation {operator} {arguments[0]} {arguments[1]} {arguments[2]}'
            
        return int(arguments[0] > arguments[1])

    elif operator == 'shift':
        
        if arguments[0] <= 0 or arguments[1] <= 0:
            return f'invalid operation {operator} {arguments[0]} {arguments[1]}'
        else:
            return arguments[0] << arguments[1]

    elif operator == 'min':
        return min(arguments)