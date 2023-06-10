import logging
logging.basicConfig(filename="logging.log",level=logging.ERROR)
try:
    a = 99/0
except ZeroDivisionError as e:
    logging.error(f"I am trying to handle a zero division error: {e}")

