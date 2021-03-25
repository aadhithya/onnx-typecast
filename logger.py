import logging

from colorlog import ColoredFormatter

LOG_LEVEL = logging.INFO
LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s| %(name)s | %(log_color)s%(message)s%(reset)s | (%(filename)s:%(lineno)d)"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger("onnx-typecast")
log.setLevel(LOG_LEVEL)
log.addHandler(stream)
