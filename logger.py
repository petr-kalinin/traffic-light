import os.path
import sys
import logging
import logging.handlers

logger = logging.getLogger('traffic-light')
logger.setLevel(logging.DEBUG)

syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
stderr_handler = logging.StreamHandler(stream=None)
file_handler = logging.handlers.RotatingFileHandler(os.path.join(os.path.dirname(sys.argv[0]), "log"), maxBytes=1000000, backupCount=7)

logger.addHandler(syslog_handler)
logger.addHandler(stderr_handler)
logger.addHandler(file_handler)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
for handler in [syslog_handler, stderr_handler, file_handler]:
    handler.setFormatter(formatter)