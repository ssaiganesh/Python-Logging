import logging
import employee
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(f'{Path(__file__).parent}/sample.log')
file_handler.setLevel(logging.ERROR) # setting a different logging level for file as compared to formatter
file_handler.setFormatter(formatter) 

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter) 


logger.addHandler(file_handler)
logger.addHandler(stream_handler) # prints it in console not just file and also includes debug statements


# logging.basicConfig(filename= f'{Path(__file__).parent}/test.log', level=logging.DEBUG,
#     format='%(asctime)s:%(levelname)s:%(message)s') 

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
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero') # Includes traceback unlike logger.error
    else:
        return result

num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
# logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result)) # doesn't print anything without logging.basicConfig
# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result)) # prints it out regardless if basicConfig is set or not because default for basicConfig is warning
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Multiply: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_result))




