import logging
import logging.handlers

logger = logging.getLogger('traffic-light')
logger.setLevel(logging.DEBUG)

syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
stderr_handler = logging.StreamHandler(stream=None)

logger.addHandler(syslog_handler)
logger.addHandler(stderr_handler)

formatter = logging.Formatter('%(processName)s: %(name)s: %(levelname)s: %(message)s')
syslog_handler.setFormatter(formatter)