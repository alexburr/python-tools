# UNTESTED

ellipsis = '…'

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Collapse a string to a maximum length, with middle ellipsis 
# ─────────────────────────────────────────────────────────────────────────────
def truncate(input, start, end):
    str_input = str(input)
    if start == 0 and end == 0:
        return str_input
    if start != 0 and end != 0 and len(str_input) < (start + end):
        return str_input
    elif start == 0 and end != 0 and len(str_input) > 0:
        return ellipsis + str_input[-end:]
    elif end == 0 and start !=0 and len(str_input) > 0:
        return str_input[0:start] + ellipsis
    elif start != 0 and end != 0 and len(str_input) > 0:
        str_first = str(str_input[0:start])
        str_last = str(str_input[-end:])        
        return str_first + ellipsis + str_last
    else:
        return str_input

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Trim a string and left justify, with ellipsis
# ─────────────────────────────────────────────────────────────────────────────
def fitl(input, size):
    str_input = str(input)
    if len(str_input) < size:
        return str_input.ljust(size)
    elif len(str_input) > size:
        return(truncate(input, 0, size - 1))
    else:
        return str_input

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Trim a string and right justify, with ellipsis
# ─────────────────────────────────────────────────────────────────────────────
def fitr(input, size):
    str_input = str(input)
    if len(str_input) < size:
        return str_input.rjust(size)
    elif len(str_input) > size:
        return(truncate(input, 0, size - 1))
    else:
        return str_input