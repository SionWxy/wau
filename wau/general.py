# ================================================
# General utils
# ================================================

class GeneralUtils(object):
    @staticmethod
    def check_equal(iterator):
        return len(set(iterator)) <= 1
