import sys
import os
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
PIECE_VALUES = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9
}

def debug_log(message):
    if os.environ.get('DEBUG') == "true":
        print(message)

def find_first(values, predicate):
  return next((value for value in values if predicate(value)), None)

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

def parse_position_str(_position_str):
    letter = _position_str[0].upper()
    column = LETTERS.index(letter)
    row = int(_position_str[1]) - 1
    return (column, row)

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

def get_move(position, _new_position):
    return (_new_position[0] - position[0], _new_position[1] - position[1])

def new_position(position, move):
    return (position[0] + move[0], position[1] + move[1])

def new_positions(position, moves):
    return [new_position(position, move) for move in moves]

def other_turn(turn):
    return "black" if turn == "white" else "white"

def count_column_pieces(column):
    return len([piece for piece in column if piece is not None])

def count_pieces(board):
    return sum([count_column_pieces(column) for column in board])

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

# How castling works: https://support.chess.com/article/266-how-do-i-castle
def king_castle_moves(position, board):
    # TODO: strictly speaking we would need to check the king and rooks have never moved
    # We could use a move_history variable for that
    moves = []
    piece = get_piece(position, board)
    turn = piece[0]
    king_row = 0 if turn == "white" else 7
    king_column = 4
    king_position = (king_column, king_row)
    king_in_position = position == king_position
    if is_check(turn, board) or not king_in_position:
        # Cannot castle if in check or king not in start position
        return []
    left_rook_in_position = get_piece((0, king_row), board) == (turn, "rook")
    left_positions = [(1, king_row), (king_column - 2, king_row), (king_column - 1, king_row)]
    left_open = len([p for p in left_positions if get_piece(p, board) != None]) == 0
    left_board = make_move(king_position, (-1, 0), board)
    left_not_chess = not is_check(turn, left_board)
    if left_rook_in_position and left_open and left_not_chess:
        moves.append((-2, 0))
    right_rook_in_position = get_piece((7, king_row), board) == (turn, "rook")
    right_positions = [(6, king_row), (king_column + 2, king_row), (king_column + 1, king_row)]
    right_open = len([p for p in right_positions if get_piece(p, board) != None]) == 0
    right_board = make_move(king_position, (1, 0), board)
    right_not_chess = not is_check(turn, right_board)
    if right_rook_in_position and right_open and right_not_chess:
        moves.append((2, 0))
    return moves
   
def king_moves(position, board):
    piece = get_piece(position, board)
    moves = []
    for move in ALL_DIRECTIONS:
        _new_position = new_position(position, move)
        take_piece = get_piece(_new_position, board)
        if is_in_range(_new_position) and (not take_piece or take_piece[0] != piece[0]):
            moves.append(move)
    moves.extend(king_castle_moves(position, board))
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
                    _new_position = new_position(position, move)
                    board_after_move = make_move(position, move, board)
                    _is_check = is_check(turn, board_after_move)
                    king_position = get_position((turn, "king"), board_after_move)
                    other_king_position = get_position((other_turn(turn), "king"), board_after_move)
                    is_king_threat = king_position in new_positions(other_king_position, king_moves(other_king_position, board_after_move))
                    take_piece = get_piece(new_position(position, move), board)
                    move_takes_king = bool(take_piece and take_piece[1] == "king")
                    # NOTE: you cannot move into check
                    move_is_valid = not _is_check and not is_king_threat and not move_takes_king
                    debug_log(f"{turn} all moves {piece[1]} {position_str(position)} -> {position_str(_new_position)} {move} move_is_valid={move_is_valid} is_check={_is_check} is_king_threat={is_king_threat} move_takes_king={move_takes_king}")
                    if move_is_valid:
                        result.append((position, move))                    
    return result

def should_promote_pawn(position, piece):
    promote_row = 0 if piece[0] == "black" else 7
    return piece[1] == "pawn" and promote_row == position[1]

def make_move(position, move, board):
    piece = get_piece(position, board)
    turn = piece[0]
    new_board = [column.copy() for column in board]
    _new_position = new_position(position, move)
    new_board[_new_position[0]][_new_position[1]] = new_board[position[0]][position[1]]
    new_board[position[0]][position[1]] = None
    if piece[1] == "king" and abs(_new_position[0] - position[0]) > 1:
        # It's a castling move, we also need to move the rook
        castle_row = 0 if turn == "white" else 7
        rook_column = 0 if (_new_position[0] - position[0]) < 0 else 7
        direction = -1 if (_new_position[0] - position[0]) < 0 else 1
        new_board[position[0] + direction][position[1]] = new_board[rook_column][castle_row]
        new_board[rook_column][castle_row] = None
    elif should_promote_pawn(_new_position, piece):
        new_board[_new_position[0]][_new_position[1]] = (piece[0], "queen")
    return new_board

def is_threatened(position, board):
    piece = get_piece(position, board)
    turn = piece[0]
    for (other_position, other_move) in all_position_moves(other_turn(turn), board):
        _new_position = new_position(other_position, other_move)
        if _new_position == position:
            return True
    return False

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

def is_check_mate_move(position, move, board):
    piece = get_piece(position, board)
    turn = piece[0]
    new_board = make_move(position, move, board)
    new_is_check = is_check(other_turn(turn), new_board)
    if not new_is_check:
        return False
    new_position_moves = all_position_moves(other_turn(turn), new_board)
    return new_is_check and not new_position_moves

def engine_random(position_moves, board):
    return random.choice(position_moves)

def engine_material(position_moves, board):
    max_value = 0
    max_value_position_move = None
    max_threat = False
    for (position, move) in position_moves:
        # make chess mate move if possible (duh)
        if is_check_mate_move(position, move, board):
            debug_log(f"engine_material returning check mate move position={position} move={move}")
            return (position, move)
        _new_position = new_position(position, move)
        take_piece = get_piece(_new_position, board)
        if take_piece:
            take_piece_value = PIECE_VALUES[take_piece[1]]
            new_board = make_move(position, move, board)
            value = take_piece_value
            threat = False
            if is_threatened(_new_position, new_board):
                piece = get_piece(position, board)
                piece_value = PIECE_VALUES[piece[1]]
                value = take_piece_value - piece_value
                threat = True
            if value > max_value:
                max_value = value
                max_value_position_move = (position, move)
                max_threat = threat
    if max_value_position_move:
        debug_log(f"engine_material returning max_value={max_value} max_threat={max_threat} max_value_position_move={max_value_position_move}")
        return max_value_position_move
    # TODO: move away threatened pieces (i.e. consider defense and not just offense)
    # TODO: castle when you can

    # Use random move as fallback
    return random.choice(position_moves)

def engine_user(position_moves, board):
    try:
        move_str = input("Select your move (i.e. e2 e4) ")
        (position_str, new_position_str) = move_str.split(" ")
        position = parse_position_str(position_str)
        _new_position = parse_position_str(new_position_str)
        move = get_move(position, _new_position)
        return (position, move)
    except:
        return ((0, 0), (0, 0))

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

def get_player(player_name):
    PLAYERS = {
        'random': engine_random,
        'material': engine_material,
        'user': engine_user,
    }
    return PLAYERS[player_name]

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

def print_move(turn, position, move, board):
    _new_position = new_position(position, move)
    piece = get_piece(position, board)
    take_piece = get_piece(_new_position, board)
    take_string = f"takes {take_piece}" if take_piece else ""
    promote_string = f"promotes pawn to queen" if should_promote_pawn(_new_position, piece) else ""    
    castle_string = f"castles" if (piece[1] == "king" and abs(_new_position[0] - position[0]) > 1) else ""
    messages = [
            f"{turn} move: {piece[1]} {position_str(position)} -> {position_str(_new_position)} {move}",
            take_string,
            promote_string,
            castle_string
    ]
    message = ", ".join([m for m in messages if m])
    print(message)

def play_game(player1, player2):
    board = init_board()
    turn = "white"
    move_number = 1
    while True:
        print_board(board)
        position_moves = all_position_moves(turn, board)
        _is_check = is_check(turn, board)
        print(f"{turn} turn to move #{move_number}, possible moves: {len(position_moves)}, is check: {_is_check}")
        if count_pieces(board) == 2:
            print(f"Only the kings left - draw!")
            return "draw"
        elif not position_moves:
            if _is_check:
                print(f"No possible moves for {turn} - check mate - {other_turn(turn)} wins!")
                return other_turn(turn)
            else:
                print(f"No possible moves for {turn} - stale mate - draw!")
                return "draw"
        player = player1 if turn == "white" else player2
        attempts = 1
        got_valid_move = False
        while attempts < 4:
            (position, move) = player(position_moves, board)
            if (position, move) in position_moves:
                got_valid_move = True
                break
            attempts += 1
        if not got_valid_move:
            sys.exit(f"Never got a valid move from player {player.__name__} - exiting")
        print_move(turn, position, move, board)
        board = make_move(position, move, board)
        turn = other_turn(turn)
        move_number += 1

def main():
    print(sys.argv)
    player1 = get_player(sys.argv[1])
    player2 = get_player(sys.argv[2])
    n_games = int(os.environ.get('N_GAMES', '1'))
    stats = {
        'white': 0,
        'black': 0,
        'draw': 0
    }
    for game_index in range(0, n_games):
        print("\n###########################")
        print(f"### Game #{game_index + 1}")
        print("###########################\n")
        result = play_game(player1, player2)
        stats[result] += 1
    if n_games > 1:
        print("stats:", stats)
    
if __name__ == "__main__":
    main()
