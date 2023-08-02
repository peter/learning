import random

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]
SQUARE_LENGTH = 8
BOARD_END = " | "
ALL_DIRECTIONS = [
        (-1, -1), # left, down
        (-1, 0), # left
        (-1, 1), # left, up
        (0, 1), # up
        (1, 1), # right, up
        (1, 0), # right
        (1, -1), # right, down
        (0, -1) # down
]


def empty_row():
    return [None for _ in range(0, 8)]

def square_str(label):
    return str(label).ljust(SQUARE_LENGTH)[0:SQUARE_LENGTH]

def piece_str(piece):
    if piece == None:
        return ""
    else:
        return f"{piece[0][0]} {piece[1]}"

def position_str(position):
    pretty_column = LETTERS[position[0]]
    pretty_row = position[1] + 1
    return f"{pretty_column}{pretty_row}"

def is_in_range(position):
    return position[0] >= 0 and position[0] <= 7 and position[1] >= 0 and position[1] <= 7

def get_piece(position, board):
    if not is_in_range(position):
        return None
    return board[position[0]][position[1]]

def get_position(piece, board):
    for column in range(0, 8):
        for row in range(0, 8):
            if board[column][row] == piece:
                return (column, row)
    return None

def new_position(position, move):
    return (position[0] + move[0], position[1] + move[1])

def new_positions(position, moves):
    return [new_position(position, move) for move in moves]

def other_turn(turn):
    return "black" if turn == "white" else "white"

# Helper function for pieces that move one or more steps in different
# directions (rook, bishop, queen)
def get_moves_from_directions(position, directions, board):
    moves = []
    piece = get_piece(position, board)
    for step in directions:
        n_steps = 1
        while True:
            move = (n_steps * step[0], n_steps * step[1])
            _new_position = new_position(position, move)
            take_piece = get_piece(_new_position, board)
            if not is_in_range(_new_position) or (take_piece and take_piece[0] == piece[0]):
                # we are outside the board or we have hit one of our own pieces (same color)
                break
            elif take_piece and take_piece[0] != piece[0]:
                # different color piece we can take, but we can't proceed
                moves.append(move)
                break
            else:
                # empty square so we can proceeed
                moves.append(move)
            n_steps += 1            
    return moves

def pawn_moves(position, board):
    piece = get_piece(position, board)
    moves = []
    direction = (1 if piece[0] == "white" else -1)
    is_start_position = (piece[0] == "white" and position[1] == 1) or (piece[0] == "black" and position[1] == 6)
    # Can move one step if no piece in that square
    one_move = (0, direction)
    if not get_piece(new_position(position, one_move), board):
        moves.append(one_move)
        # Can move two steps if in start position and no pieces in the way
        two_move = (0, direction * 2)
        if is_start_position and not get_piece(new_position(position, two_move), board):
            moves.append(two_move)
    # Can take diagonal left if opponent piece there
    left_move = (-1, direction)
    left_move_piece = get_piece(new_position(position, left_move), board)
    if left_move_piece and left_move_piece[0] != piece[0]:
        moves.append(left_move)
    # Can take diagonal right if opponent piece there
    right_move = (1, direction)
    right_move_piece = get_piece(new_position(position, right_move), board)
    if right_move_piece and right_move_piece[0] != piece[0]:
        moves.append(right_move)
    # TODO: en passant
    return [m for m in moves if is_in_range(new_position(position, m))]

def knight_moves(position, board):
    piece = get_piece(position, board)
    moves = []
    all_moves = [
        # Moving up (positive row movement)
        (-1, 2),
        (-2, 1),
        (1, 2),
        (2, 1),
        # Moving down (negative row movement)
        (-1, -2),
        (-2, -1),
        (1, -2),
        (2, -1)
    ]
    for move in all_moves:
        _new_position = new_position(position, move)
        take_piece = get_piece(_new_position, board)
        if is_in_range(_new_position) and (not take_piece or (take_piece[0] != piece[0])):
            moves.append(move)
    return moves

def bishop_moves(position, board):
    directions = [
        (-1, -1), # left, down
        (-1, 1), # left, up
        (1, 1), # right, up
        (1, -1) # right, down
    ]
    return get_moves_from_directions(position, directions, board)

def rook_moves(position, board):
    directions = [
        (-1, 0), # left
        (1, 0), # right
        (0, 1), # up
        (0, -1) # down
    ]
    return get_moves_from_directions(position, directions, board)

def queen_moves(position, board):
    return get_moves_from_directions(position, ALL_DIRECTIONS, board)

def king_moves(position, board):
    piece = get_piece(position, board)
    moves = []
    for move in ALL_DIRECTIONS:
        _new_position = new_position(position, move)
        take_piece = get_piece(_new_position, board)
        if is_in_range(_new_position) and (not take_piece or take_piece[0] != piece[0]):
            moves.append(move)
    return moves

def get_moves(position, board):
    piece = get_piece(position, board)
    if piece == None:
        return []
    elif piece[1] == "pawn":
        return pawn_moves(position, board)
    elif piece[1] == "knight":
        return knight_moves(position, board)
    elif piece[1] == "bishop":
        return bishop_moves(position, board)
    elif piece[1] == "rook":
        return rook_moves(position, board)
    elif piece[1] == "queen":
        return queen_moves(position, board)
    elif piece[1] == "king":
        return king_moves(position, board)
    else:
        raise(f"Unknown piece={piece[1]}")

def all_position_moves(turn, board):
    result = []
    for row in range(0, 8):
        for column in range(0, 8):
            position = (column, row)
            piece = get_piece(position, board)            
            if piece and piece[0] == turn:
                moves = get_moves(position, board)
                for move in moves:
                    board_after_move = make_move(position, move, board)
                    _is_check = is_check(turn, board_after_move)
                    king_position = get_position((turn, "king"), board_after_move)
                    other_king_position = get_position((other_turn(turn), "king"), board_after_move)
                    is_king_threat = king_position in new_positions(other_king_position, king_moves(other_king_position, board_after_move))
                    take_piece = get_piece(new_position(position, move), board)
                    move_takes_king = take_piece and take_piece[1] == "king"
                    # NOTE: you cannot move into check
                    if not _is_check and not is_king_threat and not move_takes_king:
                        result.append((position, move))                    
    return result

def should_promote_pawn(position, board):
    piece = get_piece(position, board)
    promote_row = 0 if piece[0] == "black" else 7
    return piece[1] == "pawn" and promote_row == position[1]

def make_move(position, move, board):
    piece = get_piece(position, board)
    new_board = [column.copy() for column in board]
    _new_position = new_position(position, move)
    new_board[_new_position[0]][_new_position[1]] = new_board[position[0]][position[1]]
    new_board[position[0]][position[1]] = None
    if should_promote_pawn(_new_position, new_board):
        # print(f"would promote {piece[0]} pawn to queen at position {position_str(_new_position)}")
        new_board[_new_position[0]][_new_position[1]] = (piece[0], "queen")
    return new_board

def is_check(turn, board):
    king_position = get_position((turn, "king"), board)
    for column in range(0, 8):
        for row in range(0, 8):
            position = (column, row)
            piece = get_piece(position, board)
            if not piece or piece[0] == turn:
                continue
            if piece[1] == "pawn" and king_position in new_positions(position, pawn_moves(position, board)):
                return True
            elif piece[1] == "knight" and king_position in new_positions(position, knight_moves(position, board)):
                return True
            elif piece[1] == "bishop" and king_position in new_positions(position, bishop_moves(position, board)):
                return True
            elif piece[1] == "rook" and king_position in new_positions(position, rook_moves(position, board)):
                return True
            elif piece[1] == "queen" and king_position in new_positions(position, queen_moves(position, board)):
                return True
    return False

# Board is organized so we can index it by (x, y) coordinates
# where x is column 0-7 (A-H in letters) and y is row 0-7 (1-7 in numbers on the board)
def init_board():
    board = []
    board.append([
        ("white", "rook"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "rook")
    ])
    board.append([
        ("white", "knight"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "knight")
    ])
    board.append([        
        ("white", "bishop"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "bishop")
    ])
    board.append([        
        ("white", "queen"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "queen")
    ])
    board.append([        
        ("white", "king"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "king")
    ])
    board.append([        
        ("white", "bishop"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "bishop")
    ])
    board.append([        
        ("white", "knight"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "knight")
    ])
    board.append([        
        ("white", "rook"),
        ("white", "pawn"),
        None,
        None,
        None,
        None,
        ("black", "pawn"),
        ("black", "rook")
    ])
    return board

def print_letters():
    print(square_str(""), end=BOARD_END)
    for letter in LETTERS:
        print(square_str(letter), end=BOARD_END)

def print_board(board):
    for row in range(7, -1, -1):
        print(square_str(row + 1), end=BOARD_END)
        for column in range(0, 8):
            position = (column, row)
            piece = get_piece(position, board)
            print(square_str(piece_str(piece)), end=BOARD_END)
        print()
    print_letters()
    print()

def print_moves(position_moves, board):
    for (position, moves) in position_moves:
        if moves:
            piece = get_piece(position, board)
            moves = get_moves(position, board)
            print('pm debug moves', position, piece, moves)

def print_move(turn, position, move, board):
    _new_position = new_position(position, move)
    piece = get_piece(position, board)
    take_piece = get_piece(_new_position, board)
    take_string = f"takes {take_piece}" if take_piece else ""
    print(f"{turn} move: {piece[1]} {position_str(position)} -> {position_str(_new_position)} {move}  {take_string}")

def main():
    board = init_board()
    turn = "white"
    move_number = 1
    while True:
        print_board(board)
        position_moves = all_position_moves(turn, board)
        _is_check = is_check(turn, board)
        print(f"{turn} turn to move #{move_number}, possible moves: {len(position_moves)}, is check: {_is_check}")
        if not position_moves:
            if _is_check:
                print(f"No possible moves for {turn} - check mate - {other_turn(turn)} wins!")
            else:
                print(f"No possible moves for {turn} - stale mate - draw!")
            break
        # print_moves(position_moves, board)
        (position, move) = random.choice(position_moves)
        print_move(turn, position, move, board)
        board = make_move(position, move, board)
        turn = other_turn(turn)
        move_number += 1
    
if __name__ == "__main__":
    main()
