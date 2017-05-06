from context import wau
from wau import *

import unittest

def test_helper_gen_a_tree():
    root = su.TreeNode("root")
    child0 = su.TreeNode("child0", root)
    child1 = su.TreeNode("child1", root)
    child2 = su.TreeNode("child2", root)
    grandchild00 = su.TreeNode("grandchild00", child0)
    grandchild10 = su.TreeNode("grandchild10", child1)
    grandchild11 = su.TreeNode("grandchild11", child1)
    grandchild20 = su.TreeNode("grandchild20", child2)
    grandchild21 = su.TreeNode("grandchild21", child2)
    grandchild22 = su.TreeNode("grandchild22", child2)
    grandchild23 = su.TreeNode("grandchild23", child2)
    greatgrandchild220 = su.TreeNode("greatgrandchild220", grandchild22)
    greatgrandchild221 = su.TreeNode("greatgrandchild221", grandchild22)
    greatgrandchild222 = su.TreeNode("greatgrandchild222", grandchild22)
    greatgrandchild223 = su.TreeNode("greatgrandchild223", grandchild22)
    return root

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    # The very first test.
    def test_import(self):
        assert(cu.green('green') == '\033[0;32mgreen\033[0;00m')

    # Test gu
    def test_sanity_gu(self):
        assert(gu.check_equal([]) == True)
        assert(gu.check_equal([1]) == True)
        assert(gu.check_equal([1,1,1]) == True)
        assert(gu.check_equal([1,0]) == False)

    # Test su
    def test_sanity_su(self):
        # insert_str()
        assert(su.insert_str("1256", "34", 2) == "123456")
        # mk_str()
        assert(su.mk_str(None) == '')
        assert(su.mk_str('') == '')
        assert(su.mk_str('abc') == 'abc')
        # is_visible()
        assert(su.is_visible(None) == False)
        assert(su.is_visible('') == False)
        assert(su.is_visible('  ') == False)
        assert(su.is_visible(' a ') == True)
        # suffix()
        assert(su.suffix('','nothing') == '')
        assert(su.suffix(' ','nothing') == '')
        assert(su.suffix(None,'nothing') == '')
        assert(su.suffix(":",')') == ':)')
        # prefix()
        assert(su.prefix('','nothing') == '')
        assert(su.prefix(' ','nothing') == '')
        assert(su.prefix(None,'nothing') == '')
        assert(su.prefix(":",'(') == '(:')
        # gen_tree(), TreeNode and TreeIndent
        test_root = test_helper_gen_a_tree()
        exp_tree_str = """root
 +- child0
 |   `- grandchild00
 +- child1
 |   +- grandchild10
 |   `- grandchild11
 `- child2
     +- grandchild20
     +- grandchild21
     +- grandchild22
     |   +- greatgrandchild220
     |   +- greatgrandchild221
     |   +- greatgrandchild222
     |   `- greatgrandchild223
     `- grandchild23
"""
        assert(su.gen_tree(test_root) == exp_tree_str)

    # Test cu
    def test_sanity_cu(self):
        # the colors()
        assert(cu.black  ('black  ') == '\033[0;30mblack  \033[0;00m')
        assert(cu.red    ('red    ') == '\033[0;31mred    \033[0;00m')
        assert(cu.green  ('green  ') == '\033[0;32mgreen  \033[0;00m')
        assert(cu.yellow ('yellow ') == '\033[0;33myellow \033[0;00m')
        assert(cu.blue   ('blue   ') == '\033[0;34mblue   \033[0;00m')
        assert(cu.magenta('magenta') == '\033[0;35mmagenta\033[0;00m')
        assert(cu.cyan   ('cyan   ') == '\033[0;36mcyan   \033[0;00m')
        assert(cu.white  ('white  ') == '\033[0;37mwhite  \033[0;00m')
        # get_a_color()
        assert(cu.get_a_color() == cu.COL_FG_RED)
        assert(cu.get_a_color() == cu.COL_FG_GREEN)
        assert(cu.get_a_color() == cu.COL_FG_YELLOW)
        assert(cu.get_a_color() == cu.COL_FG_BLUE)
        assert(cu.get_a_color() == cu.COL_FG_MAGENTA)
        assert(cu.get_a_color() == cu.COL_FG_CYAN)
        assert(cu.get_a_color() == cu.COL_BFG_RED)
        assert(cu.get_a_color() == cu.COL_BFG_GREEN)
        assert(cu.get_a_color() == cu.COL_BFG_YELLOW)
        assert(cu.get_a_color() == cu.COL_BFG_BLUE)
        assert(cu.get_a_color() == cu.COL_BFG_MAGENTA)
        assert(cu.get_a_color() == cu.COL_BFG_CYAN)
        # get_str_color()
        assert(cu.get_str_color('0') == cu.COL_FG_RED)
        assert(cu.get_str_color('1') == cu.COL_FG_GREEN)
        assert(cu.get_str_color('2') == cu.COL_FG_YELLOW)
        assert(cu.get_str_color('3') == cu.COL_FG_BLUE)
        assert(cu.get_str_color('4') == cu.COL_FG_MAGENTA)
        assert(cu.get_str_color('5') == cu.COL_FG_CYAN)
        assert(cu.get_str_color('6') == cu.COL_BFG_RED)
        assert(cu.get_str_color('7') == cu.COL_BFG_GREEN)
        assert(cu.get_str_color('8') == cu.COL_BFG_YELLOW)
        assert(cu.get_str_color('9') == cu.COL_BFG_BLUE)
        assert(cu.get_str_color('10') == cu.COL_BFG_MAGENTA)
        assert(cu.get_str_color('11') == cu.COL_BFG_CYAN)
        assert(cu.get_str_color('0') == cu.COL_FG_RED)
        assert(cu.get_str_color('1') == cu.COL_FG_GREEN)
        assert(cu.get_str_color('2') == cu.COL_FG_YELLOW)
        assert(cu.get_str_color('3') == cu.COL_FG_BLUE)
        assert(cu.get_str_color('4') == cu.COL_FG_MAGENTA)
        assert(cu.get_str_color('5') == cu.COL_FG_CYAN)
        assert(cu.get_str_color('6') == cu.COL_BFG_RED)
        assert(cu.get_str_color('7') == cu.COL_BFG_GREEN)
        assert(cu.get_str_color('8') == cu.COL_BFG_YELLOW)
        assert(cu.get_str_color('9') == cu.COL_BFG_BLUE)
        assert(cu.get_str_color('10') == cu.COL_BFG_MAGENTA)
        assert(cu.get_str_color('11') == cu.COL_BFG_CYAN)

if __name__ == '__main__':
    unittest.main()
