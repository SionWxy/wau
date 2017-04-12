# ================================================
# String Base Utils
# ================================================

class StrBaseUtils(object):
    @staticmethod
    def insert_str(a_orig, a_new, a_pos):
       return a_orig[:a_pos] + a_new + a_orig[a_pos:]

    @staticmethod
    def mk_str(a_str):
        """Return '' for None, otherwise str()."""
        return str(a_str) if a_str != None else ''

    @staticmethod
    def is_visible(a_str):
        """If a_str is:
          1. None
          2. Empty string
          3. Contains only spaces
        Then a_str is considered invisible.
        """
        return StrBaseUtils.mk_str(a_str) != '' and (not StrBaseUtils.mk_str(a_str).isspace())

    @staticmethod
    def suffix(a_str=None, a_suffix=' '):
        """Append a_suffix if a_str is visible."""
        return StrBaseUtils.mk_str(a_str) + a_suffix if StrBaseUtils.is_visible(a_str) else ''

    @staticmethod
    def prefix(a_str=None, a_prefix=' '):
        """Prepend a_prefix if a_str is visible."""
        return a_prefix + StrBaseUtils.mk_str(a_str) if StrBaseUtils.is_visible(a_str) else ''
