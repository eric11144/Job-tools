import logging
import time
from datetime import datetime

from logging.handlers import RotatingFileHandler

#----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    a = []
    dt = datetime.now()
    
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=1*1024*1024*1024,
                                  backupCount=10)
    logger.addHandler(handler)
    
    for i in range(130000):
        a.append("a")
        print(i)

    while True:
        logger.info(a)
        print("Date and time is:", dt)
    
    # while 1==1:
    #     logger.info("")        
#----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "/mnt/logs/test.log"
    create_rotating_log(log_file)
