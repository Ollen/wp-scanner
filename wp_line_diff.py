""" Detect line diff between two files """
from difflib import Differ

def diff_filter(diff):
    """ Only returns line changes from the right hand side (+) """
    lineNum = 0
    diff_list = []
    for line in diff:
        # split off the code
        code = line[:2]
        # if the  line is in both files or just b, increment the line number.
        if code in ("  ", "+ "):
            lineNum += 1
        # if this line is only in b, print the line number and the text on the line
        if code == "+ ":
            diff_list.append('{}: {}'.format(lineNum, line[2:].strip()))
    
    return diff_list

def file_line_diff(fpath1, fpath2):
    """ Returns an array of unified diff between two files """
    with open(fpath1, 'r') as f1, open(fpath2, 'r') as f2:
        file_1 = f1.readlines()
        file_2 = f2.readlines()
    
    diff = Differ().compare(file_1, file_2)
    return diff_filter(diff)
