# print("I am printing this.")
import logging


# logging.basicConfig(filename=r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/file_test.log",level=logging.INFO)
# logging.info("Hello World")
# logging.debug("This is my message")
# logging.warning('It is my warning')
# logging.error('This is my Error')
# logging.critical("It's critical condition")
# logging.shutdown()


# logging.basicConfig(filename=r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/file_test_1.log", level = logging.DEBUG, format="%(asctime)s %(message)s")
# logging.info("This is my other Info")
# logging.info("This is my Error message")
# logging.critical("This is my critical file")
# logging.shutdown()


logging.basicConfig(filename=r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/file_test_2.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logging.debug("This is my debug code")

l = [1,2,3,4,["hello","a",13,292],"Anurag PAreek","L"]
integer = []
string = []
for i in l:
    logging.info("We are iterating through our list and our local variable is 'i'" + str(l))
    if type(i) == list:
        logging.info("I am inside if statement and i am trying to check list type")
        for j in p:
            logging.info("I am inside another for loop and i am trying to check integer and string type , {}".format(i))
            if type(j) == int:
                logging.info("I am inside if statement")
                integer.append(j)
            else:
                string.append(j)
    elif type(i) == int:
        integer.append(i)
    else:
        string.append(i)
logging.info(f"My final result if {integer} and {string}")