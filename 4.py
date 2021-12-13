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
winning_board = None
winning_marked_board = None
while not winning_board and pick_index < len(pickable_numbers):
    pick_index = pick_index + 1

    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c  in range(len(boards[b][r])):
                if boards[b][r][c] == pickable_numbers[pick_index]:
                    marked_boards[b][r][c] = pickable_numbers[pick_index]

                    if check_row(marked_boards[b][r]):
                        winning_board = boards[b]
                        winning_marked_board = marked_boards[b]

                    if check_column(marked_boards[b], c):
                        winning_board = boards[b]
                        winning_marked_board = marked_boards[b]

print(winning_board)
print(f'Winning board score: {calculate_score(winning_board, winning_marked_board, pickable_numbers[pick_index])}')
