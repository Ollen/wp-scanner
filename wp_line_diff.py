import difflib

def line_diff(fpath1, fpath2):
    """ Returns an array of unified diff between two files """
    with open(fpath1, 'r') as f1, open(fpath2, 'r') as f2:
        file_1 = f1.readlines()
        file_2 = f2.readlines()
    
    diff = difflib.unified_diff(file_1, file_2)
    diff_list = [x for x in list(diff)[2:]]
    return diff_list
