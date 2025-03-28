import logging

COLORS = {
    'DEBUG': '\033[94m',          #Blue
    'INFO': '\033[90m',           #Gray
    'WARNING': '\033[93m',        #Yellow
    'ERROR': '\033[91m',          #Red
    'CRITICAL': '\033[38;5;88m',  #Dark Red
    'RESET': '\033[0m',           #Reset
    'BOLD': '\033[1m',            #Bold
}

RAINBOW_COLORS = [
    '\033[31m',     #Red
    '\033[33m',     #Orange
    '\033[93m',     #Yellow
    '\033[32m',     #Green
    '\033[34m',     #Blue
    '\033[36m',     #Cyan
    '\033[35m',     #Pink
    '\033[38;5;93m' #Violet
]

class CustomFormatter(logging.Formatter):
    def format(self, record):
        baseColor = COLORS.get(record.levelname, COLORS['RESET'])
        reset = COLORS['RESET']
        bold = COLORS['BOLD']
        message = record.getMessage()

        if record.levelname == 'CRITICAL':
            editedMessage = ''.join(
                f"{RAINBOW_COLORS[i % len(RAINBOW_COLORS)]}{char}"
                for i, char in enumerate(message)
            )
            message = f"{editedMessage}{reset}"
        else:
            message = f"{baseColor}{bold}{message}{reset}"

        format = f"{bold}{baseColor}%(asctime)s - %(levelname)s - {message}{reset}"
        formatter = logging.Formatter(format, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def newLogger(name):
    '''
    Creates a new logger
    :param name: Str
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    formatter = CustomFormatter()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    return logger

if __name__ == "__main__":
    logger = newLogger("testlogger")
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")