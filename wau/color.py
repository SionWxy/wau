# ================================================
# Color Utils
# ================================================

import strbase as su

"""
ANSI color code.
\033 === \x1b === 'd27, which is ESC.
All codes here are made equal length to support alignment.
"""
COL_RESET       = '\033[0;00m'
COL_FG_BLACK    = '\033[0;30m'
COL_FG_RED      = '\033[0;31m'
COL_FG_GREEN    = '\033[0;32m'
COL_FG_YELLOW   = '\033[0;33m'
COL_FG_BLUE     = '\033[0;34m'
COL_FG_MAGENTA  = '\033[0;35m'
COL_FG_CYAN     = '\033[0;36m'
COL_FG_WHITE    = '\033[0;37m'
COL_BFG_BLACK   = '\033[1;30m'
COL_BFG_RED     = '\033[1;31m'
COL_BFG_GREEN   = '\033[1;32m'
COL_BFG_YELLOW  = '\033[1;33m'
COL_BFG_BLUE    = '\033[1;34m'
COL_BFG_MAGENTA = '\033[1;35m'
COL_BFG_CYAN    = '\033[1;36m'
COL_BFG_WHITE   = '\033[1;37m'
COL_FG_LIST = [
    # COL_FG_BLACK,
    COL_FG_RED,
    COL_FG_GREEN,
    COL_FG_YELLOW,
    COL_FG_BLUE,
    COL_FG_MAGENTA,
    COL_FG_CYAN,
    # COL_FG_WHITE,
    # COL_BFG_BLACK,
    COL_BFG_RED,
    COL_BFG_GREEN,
    COL_BFG_YELLOW,
    COL_BFG_BLUE,
    COL_BFG_MAGENTA,
    COL_BFG_CYAN,
    # COL_BFG_WHITE,
]
# Color cyclical counter, used by get_a_color().
COL_CYC_CNT = -1
# Dict mapping a string with a color.
COL_STR_MAP = {}

def get_a_color():
    """Cycle through COL_FG."""
    global COL_CYC_CNT, COL_FG_LIST
    COL_CYC_CNT = (COL_CYC_CNT + 1) % len(COL_FG_LIST)
    return COL_FG_LIST[COL_CYC_CNT]

def get_str_color(a_str=''):
    global COL_STR_MAP
    if not a_str in COL_STR_MAP:
        COL_STR_MAP[a_str] = get_a_color()
    return COL_STR_MAP[a_str]

def black  (a_str): return COL_FG_BLACK   + su.mk_str(a_str) + COL_RESET
def red    (a_str): return COL_FG_RED     + su.mk_str(a_str) + COL_RESET
def green  (a_str): return COL_FG_GREEN   + su.mk_str(a_str) + COL_RESET
def yellow (a_str): return COL_FG_YELLOW  + su.mk_str(a_str) + COL_RESET
def blue   (a_str): return COL_FG_BLUE    + su.mk_str(a_str) + COL_RESET
def magenta(a_str): return COL_FG_MAGENTA + su.mk_str(a_str) + COL_RESET
def cyan   (a_str): return COL_FG_CYAN    + su.mk_str(a_str) + COL_RESET
def white  (a_str): return COL_FG_WHITE   + su.mk_str(a_str) + COL_RESET
