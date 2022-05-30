import logging
from pathlib import Path

# DEBUG: Detailed information, typically of interest only when diagnosing the problem.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is stll working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function. 

# CRITICAL: A serious error, indicating that the program itsef may be unable to continue running. 

logging.basicConfig(filename= f'{Path(__file__).parent}/test.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
# logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result)) # doesn't print anything without logging.basicConfig
# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result)) # prints it out regardless if basicConfig is set or not because default for basicConfig is warning
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Multiply: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_result))




