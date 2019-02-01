# import io
#
# s = io.StringIO ()
# s.write ('Hello World\n')
# print ('this is a test\n', file=s)
# print (s.getvalue ())
#
# s = io.StringIO ('Hello World\n')
# print (s.read (4))
# print (s.read ())


import io

s = io.StringIO ()
s.write ('Hello World\n')
print ('this is a test\n', file=s)
print (s.getvalue ())

s = io.StringIO ('Hello World\n')
print (s.read (4))
print (s.read ())

import logging
import sys


def test_log_level():
    # set default logging configuration
    logger = logging.getLogger()  # initialize logging class
    logger.setLevel(logging.DEBUG)  # default log level
    format = logging.Formatter("%(asctime)s - %(message)s")  # output format
    sh = logging.StreamHandler(stream=sys.stdout)  # output to standard output
    sh.setFormatter(format)
    logger.addHandler(sh)

    # use logging to generate log ouput
    logger.info("this is info")
    logger.debug("this is debug")
    logger.warning("this is warning")
    logging.error("this is error")
    logger.critical("this is critical")


test_log_level()