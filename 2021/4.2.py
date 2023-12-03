def check_row(row):
    return all(row)

def check_column(board, column):
    column = []

    for row in board:
        column.append(row[c])
    
    return all(column)

def calculate_score(board, marked_board, winning_number):
    sum = 0

    for r in range(len(board)):
            for c  in range(len(board[r])):
                if not marked_board[r][c]:
                    sum = sum + int(board[r][c])

    return sum * int(winning_number)


with open('4.txt') as f:
    data = f.read().splitlines()

pickable_numbers = data[0].split(',')

boards = []
marked_boards = []
board = []
marked_board = []
for line in data[2:]:
    if not line:
        boards.append(board)
        marked_boards.append(marked_board)
        board = []
        marked_board = []
    else:
        clean_line = list(filter(lambda x: x, line.split(' ')))
        board.append(clean_line)
        marked_board.append(list(map(lambda x: None, clean_line)))

pick_index = -1
last_board_winner = False
while not last_board_winner and pick_index < len(pickable_numbers):
    pick_index = pick_index + 1

    boards_that_won = []
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c  in range(len(boards[b][r])):
                if boards[b][r][c] == pickable_numbers[pick_index]:
                    marked_boards[b][r][c] = pickable_numbers[pick_index]

                    if check_row(marked_boards[b][r]) or check_column(marked_boards[b], c):
                        boards_that_won.append(b)

    if len(boards) == 1 and len(boards_that_won) == 1:
        last_board_winner = True
    else:
        boards_that_won.reverse()
        for board_that_won in boards_that_won:
            boards.pop(board_that_won)
            marked_boards.pop(board_that_won)

print(f'Last board score: {calculate_score(boards[0], marked_boards[0], pickable_numbers[pick_index])}')
