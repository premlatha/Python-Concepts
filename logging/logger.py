import logging

#DEBUG:Detailed information,typically of interest only when diagnosing problems.
#INFO: Confirmation that things are owrking as expected.
#WARNING: An indication that something unexpected happenend, or indicative of some problem in the near future.
#ERROR: Due to a more serious problem, the software has not been able to perfomr some function.
#CRITICAL: A serious error, indication that the program itself may be unable to continue running.

#Log attributes can be found at 'https://docs.python.org/3/library/logging.html#logrecord-attributes'

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(levelname)s:%(message)s')

file_handler=logging.FileHandler('employee.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Employee:
    """A Sample Employee class"""

    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last

        #print('New Employee: {} with {}'.format(self.fullname,self.email))
        logger.info('New Employee: {} with {}'.format(self.fullname,self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstname,self.lastname)


emp_1=Employee('Alex','Smith')
emp_2=Employee('Sriene','Mathew')