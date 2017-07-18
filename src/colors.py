class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def title(string):
    return bold(underline(string))

def red(string):
    return color.FAIL + str(string) + color.ENDC

def green(string):
    return color.OKGREEN + str(string) + color.ENDC

def blue(string):
    return color.OKBLUE + str(string) + color.ENDC

def yellow(string):
    return color.WARNING + str(string) + color.ENDC

def header(string):
    return color.HEADER + str(string) + color.ENDC

def bold(string):
    return color.BOLD + str(string) + color.ENDC

def underline(string):
    return color.UNDERLINE + str(string) + color.ENDC

def error(string):
    return color.FAIL + "[ERROR] " + color.ENDC + str(string)

def success(string):
    return color.OKGREEN + "[OK] " + color.ENDC + str(string)

def warning(string):
    return color.WARNING + "[WARNING] " + color.ENDC + str(string)

def info(string):
    return color.OKBLUE + "[INFO] " + color.ENDC + str(string)
