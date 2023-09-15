# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys

from funct_operations import Calculation_func


# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(line):
    items = line.split()
    operator = items[0]

    arguments = []   
    invalid_argument = None

    for num in items[1:]:
        
        argument = float(num)
    
        if argument.is_integer():
            arguments.append(int(argument))
        else:
            invalid_argument = num
            break

    if invalid_argument is not None:
        print(f'invalid operation {items[0]} {" ".join(items[1:])}')
    else:
        result = Calculation_func(operator, *arguments)
        print(result)




  


# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line
def run(filename):
  with open(filename, 'r') as file:
    for operation in file.readlines():
      process(operation.strip())


# This code will call the run function with a filename, if it's provided on the
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage: python main.py [path/to/sample]")
  else:
    run(sys.argv[1])
