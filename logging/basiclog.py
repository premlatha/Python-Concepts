import logging

#DEBUG:Detailed information,typically of interest only when diagnosing problems.
#INFO: Confirmation that things are owrking as expected.
#WARNING: An indication that something unexpected happenend, or indicative of some problem in the near future.
#ERROR: Due to a more serious problem, the software has not been able to perfomr some function.
#CRITICAL: A serious error, indication that the program itself may be unable to continue running.

#Configure the logging level to DEBUG and save in file
#Log attributes can be found at 'https://docs.python.org/3/library/logging.html#logrecord-attributes'
logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


def add(x,y):
    """Add Function"""
    return x+y

def subtract(x,y):
    """Subtraction Function"""
    return x-y

def multiply(x,y):
    """Multiplication Function"""
    return x*y

def divide(x,y):
    """Division Function"""
    return x/y

input1=20
input2=10

result=add(input1,input2)
logging.debug('Add: {} + {} = {}'.format(input1,input2,result))

result=subtract(input1,input2)
logging.debug('Subtraction: {} + {} = {}'.format(input1,input2,result))

result=multiply(input1,input2)
logging.debug('Multiplication: {} + {} = {}'.format(input1,input2,result))

result=divide(input1,input2)
logging.debug('Division: {} + {} = {}'.format(input1,input2,result))