# ================================================
# Color Utils
# ================================================

from strbase import StrBaseUtils as su

class ColorUtils(object):
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

    @staticmethod
    def get_a_color():
        """Cycle through COL_FG."""
        ColorUtils.COL_CYC_CNT = (ColorUtils.COL_CYC_CNT + 1) % len(ColorUtils.COL_FG_LIST)
        return ColorUtils.COL_FG_LIST[ColorUtils.COL_CYC_CNT]

    @staticmethod
    def get_str_color(a_str=''):
        if not a_str in ColorUtils.COL_STR_MAP:
            ColorUtils.COL_STR_MAP[a_str] = ColorUtils.get_a_color()
        return ColorUtils.COL_STR_MAP[a_str]

    @staticmethod
    def black  (a_str): return ColorUtils.COL_FG_BLACK   + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def red    (a_str): return ColorUtils.COL_FG_RED     + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def green  (a_str): return ColorUtils.COL_FG_GREEN   + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def yellow (a_str): return ColorUtils.COL_FG_YELLOW  + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def blue   (a_str): return ColorUtils.COL_FG_BLUE    + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def magenta(a_str): return ColorUtils.COL_FG_MAGENTA + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def cyan   (a_str): return ColorUtils.COL_FG_CYAN    + su.mk_str(a_str) + ColorUtils.COL_RESET
    @staticmethod
    def white  (a_str): return ColorUtils.COL_FG_WHITE   + su.mk_str(a_str) + ColorUtils.COL_RESET
