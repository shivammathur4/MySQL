import logging

logger = logging
   

logger.basicConfig(filename='mysql.log', level=logging.ERROR,
format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')
