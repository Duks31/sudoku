from pprint import pprint 


def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet --> replace with -1
    # return row, col tuple or None if not 
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # no space in the puzzle 

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if is valid

    # check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.apennd(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False 

    # Checking the Grid 
    row_start = (row // 3) *3 # 1//3 = 0, 5 // 3 = 1
    col_start = (col // 3) *3 

    for r in range( row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # if we get here,  these checks pass
    return True 
 

def solve(puzzle):
    # Solve sudoku using Backtracking
    # our puzzle is a list of list where each inner list is the row in our sudoku puzzle
    # returns whether the solution exists 
    # mutates puzzle to be the solution if it exists

    # Step 1:
    row, col = find_next_empty(puzzle)

    #Step 1a: if ghere is no row left we're done because we only allowed valid inputs 
    if row is None:
        return True 
    
    # Step 2: if there is a number space, make a guess between 1 and 9 
    for guess in range(1, 10):
        # Step 3: cheeck if it s a valid guess 
        if is_valid(puzzle, guess, row, col):
            #step3a : If is_valid is True then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # recursively call our function 
            if solve(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
        # backtrack and try a new number 

        puzzle[row][col] = -1 # reset the guess 
    
    # Step6: if none of the solutions worked, then the puzzle is Unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve(example_board))
    pprint(example_board)
