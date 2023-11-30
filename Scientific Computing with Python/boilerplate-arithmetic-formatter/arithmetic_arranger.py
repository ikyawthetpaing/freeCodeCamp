BLANK = " "
NEW_LINE = "\n"
GAP = BLANK * 4

def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    bottom_line = ""
    separator_line = ""
    result_line = ""

    for problem in problems:
        [first_number, operator, second_number] = problem.split()

        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."

        result_number = ""

        match operator:
            case "+":
                result_number = str(int(first_number) + int(second_number))
            case "-":
                result_number = str(int(first_number) - int(second_number))
            case _:
                return "Error: Operator must be '+' or '-'."

        f_num_len = len(first_number)
        s_num_len = len(second_number)

        if f_num_len > 4 or s_num_len > 4:
            return "Error: Numbers cannot be more than four digits."

        rs_num_len = len(str(result_number))
        max_len = max(f_num_len, s_num_len)
        total_len = max_len + 2

        gap = GAP if problem != problems[-1] else ""

        top_line += (BLANK * (total_len - f_num_len)) + first_number + gap
        bottom_line += operator + BLANK + (BLANK * (max_len - s_num_len)) + second_number + gap
        separator_line += ("-" * total_len) + gap
        result_line += (BLANK * (total_len - rs_num_len)) + result_number + gap

    return (top_line + NEW_LINE +
            bottom_line + NEW_LINE +
            separator_line + (NEW_LINE +result_line if show_result else ""))