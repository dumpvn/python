# coding=utf-8

"""
main module for testing python packages
"""

def TestCustomLogger():
    from logger.custom_logger import MyLogger
    MyLogger.info("system starting....")

def TestSimpleLogger():
    from logger.simple_log import get_logger
    logger = get_logger(__name__)
    logger.debug("executing test case")
    logger.info("this is just a simple logger")
    logger.warning("nearly finish")
    logger.error("faked error")
    
if __name__ == "__main__":
    TestCustomLogger()
    TestSimpleLogger()
    