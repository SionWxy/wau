# ================================================
# String Base Utils
# ================================================

def insert_str(a_orig, a_new, a_pos):
   return a_orig[:a_pos] + a_new + a_orig[a_pos:]

def mk_str(a_str):
    """Return '' for None, otherwise str()."""
    return str(a_str) if a_str != None else ''

def is_visible(a_str):
    """If a_str is:
      1. None
      2. Empty string
      3. Contains only spaces
    Then a_str is considered invisible.
    """
    return mk_str(a_str) != '' and (not mk_str(a_str).isspace())

def suffix(a_str=None, a_suffix=' '):
    """Append a_suffix if a_str is visible."""
    return mk_str(a_str) + a_suffix if is_visible(a_str) else ''

def prefix(a_str=None, a_prefix=' '):
    """Prepend a_prefix if a_str is visible."""
    return a_prefix + mk_str(a_str) if is_visible(a_str) else ''

# ================================================
# String Tree Utils
# ================================================

def gen_tree(a_root, a_tree_indent=None,
             a_get_children_func=lambda x: x._children,
             a_mk_str_func=lambda x: mk_str(x)):
    """Generate a tree string.
    a_tree_indent: is the tree indent. A TreeIndent instance.
    a_get_children_func: is a lambda function that returns a list of children nodes.
    a_mk_str_func: is the labmda function that converts a_root into string.
    """
    tree_str = ''
    tree_indent = TreeIndent() if a_tree_indent == None else a_tree_indent
    # Check out one leaf count
    tree_indent.decrement()
    # Print root line
    tree_str += str(tree_indent) + a_mk_str_func(a_root) + '\n'
    # Handle all children recursively
    children = a_get_children_func(a_root)
    tree_indent.append(len(children))
    for c in children:
        tree_str += gen_tree(c, tree_indent, a_get_children_func, a_mk_str_func)
    tree_indent.pop()
    return tree_str

class TreeIndent(object):
    """
    A util to help generate tree indents.
    Four types of output patterns:
      'fork'   : ' |  '
      'break'  : '    '
      'branch' : ' +- '
      'leaf'   : ' `- '

    _track: is a list of counts of remaining elements in each branches.
    """
    TAG_FORK   = 'fork'
    TAG_BREAK  = 'break'
    TAG_BRANCH = 'branch'
    TAG_LEAF   = 'leaf'
    def __init__(self, a_fork=' |  ', a_break='    ', a_branch=' +- ', a_leaf=' `- '):
        self._track = []
        self._symbols = {}
        self._symbols[TreeIndent.TAG_FORK]   = a_fork
        self._symbols[TreeIndent.TAG_BREAK]  = a_break
        self._symbols[TreeIndent.TAG_BRANCH] = a_branch
        self._symbols[TreeIndent.TAG_LEAF]   = a_leaf
    def append(self, a_count=1):
        self._track.append(a_count)
    def decrement(self):
        if len(self._track) > 0: self._track[-1] -= 1
    def pop(self):
        """Remove the last counter in the _track. Used when all children has
        finished their printing and is about to return to the object's parent."""
        assert(self._track[-1] == 0)
        self._track.pop()

    def gen_symbol(self, a_count, a_isLast):
        token = TreeIndent.TAG_FORK
        if a_count >  0 and not a_isLast: token = TreeIndent.TAG_FORK
        if a_count <= 0 and not a_isLast: token = TreeIndent.TAG_BREAK
        if a_count >  0 and a_isLast: token = TreeIndent.TAG_BRANCH
        if a_count <= 0 and a_isLast: token = TreeIndent.TAG_LEAF
        return self._symbols[token]

    def __repr__(self):
        if len(self._track) == 0: return ''
        ret = ''
        for n in self._track[:-1]: ret += self.gen_symbol(n, False)
        ret += self.gen_symbol(self._track[-1], True)
        return ret
