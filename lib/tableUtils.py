# UNTESTED

header_top_spacer        = '─'
header_top_col_spacer    = '┬'
col_spacer               = '│'
header_bottom_col_spacer = '┼'
footer_top_col_spacer    = '┴'

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Get dashes used in result table header
# ─────────────────────────────────────────────────────────────────────────────
def header_column_border(length):
    return((header_top_spacer * (length + 1)))

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Print dividing line used in result table header
# ─────────────────────────────────────────────────────────────────────────────
def header_line(spc, col_length_array):
    output = ''

    output += header_column_border(col_length_array[0]) + spc

    for col_length in col_length_array[1:-1]:
        output += header_column_border(col_length + 1) + spc

    output += header_column_border(col_length_array[-1] + 2)

    return output

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Create an enumerable array from an unknown list of parameters
# ─────────────────────────────────────────────────────────────────────────────
def params_to_array(params):
    array = []
    for param in params:
        array.append(param)
    return array

# ═════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════
# PUBIC API
# ═════════════════════════════════════════════════════════════════════════════
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Print result table row with column spacers
# ─────────────────────────────────────────────────────────────────────────────
def table_row(*values):
    output = ''
    value_array = params_to_array(values)

    for value in value_array[:-1]:
        output += str(value) + col_spacer.center(3, ' ')

    output += str(value_array[-1])
    return output

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Print top border used in result table header
# ─────────────────────────────────────────────────────────────────────────────
def table_header_top_line(*col_lengths):
    col_length_array = params_to_array(col_lengths)
    hl = header_line(header_top_col_spacer, col_length_array)
    return hl

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Print bottom border used in result table header
# ─────────────────────────────────────────────────────────────────────────────
def table_header_bottom_line(*col_lengths):
    col_length_array = params_to_array(col_lengths)
    hl = header_line(header_bottom_col_spacer, col_length_array)
    return hl

# ─────────────────────────────────────────────────────────────────────────────
# Purpose: Print table footer border
# ─────────────────────────────────────────────────────────────────────────────
def table_footer(*col_lengths):
    col_length_array = params_to_array(col_lengths)
    hl = header_line(footer_top_col_spacer, col_length_array)
    return hl