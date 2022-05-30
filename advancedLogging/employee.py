import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(f'{Path(__file__).parent}/employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename=f'{Path(__file__).parent}/employee.log', level=logging.INFO,
#     format='%(levelname)s:%(name)s:%(message)s')

class Employee:
    """ A Sample Employee Class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
