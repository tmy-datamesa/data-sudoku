# pylint: disable=missing-docstring

def sudoku_validator(grid):
    VALID = set(range(1, 10))

    def is_valid_group(group):
        return set(group) == VALID

    # rows
    for row in grid:
        if not is_valid_group(row):
            return False

    # cols
    for j in range(9):
        col = [grid[i][j] for i in range(9)]
        if not is_valid_group(col):
            return False

    # 3x3 boxes
    for box_row in (0, 3, 6):
        for box_col in (0, 3, 6):
            box = []
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    box.append(grid[i][j])
            if not is_valid_group(box):
                return False

    return True
