from tkinter import *
from PIL import ImageTk, Image
import BoardAndPieces

global white_to_move
global piece_selected
global indications
global board_map
global game_state
global possible_moves
global announcer
global announcement

announcement = "Press the Start button\n to begin the game"
piece_selected = None

white_to_move = True
move_number = 1
game_state = "PREP"

indications = []
board_map = []

root = Tk()
root.title('Chess Simulation')
root.config(bg='#404040')
# root.option_add('*Font', '19')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(int(screen_width * 0.7)) + 'x' + str(int(screen_height * 0.7)) + '+200+100')
root.resizable(False, False)

new_game_button = Button(
    master=root,
    text="Start New Game",
    relief=RAISED,
    width=20,
    height=3,
)
chess_board = BoardAndPieces.Board()

new_game_button.place(x=(screen_width * 0.7 - 300), y=40)
square_size = int(screen_height * 0.7) / 8 * root.winfo_height()
instructions = "Click the top button to start \n or reset the game.To move a piece, click it \n" + \
               "first to view its legal " + \
               "moves. \nThen click the green indicators \nto move the piece."

announcer_frame = Frame(master=root, relief=RAISED, background="white", width=24, height=3)
announcer_frame.place(x=(screen_width * 0.7 - 300) - 20, y=120)
announcer_banner = Label(announcer_frame, text=announcement, width=24, height=3, bg="#34b356")
announcer_banner.pack()
score_board = Label(master=root, text="Lorem ipsum", width=30, height=16)
score_board.place(x=(screen_width * 0.7 - 300) - 48, y=200)
instructions_card = Label(master=root, text=instructions, width=30, height=6)
instructions_card.place(x=(screen_width * 0.7 - 300) - 48, y=500)

black_color = "#b56b60"

is_white = False
# Generating the chess board appearance
for y in range(8):
    for x in range(8):
        if is_white:
            square = Frame(
                master=root,
                relief=RAISED,
                background="white",
                width=square_size,
                height=square_size
            )
            square.grid(row=7 - y, column=x)
        else:
            square = Frame(
                master=root,
                relief=RAISED,
                background=black_color,
                width=square_size,
                height=square_size
            )
            square.grid(row=7 - y, column=x)

        is_white = not is_white
        if x == 7:
            is_white = not is_white

# obtaining chess images, converting to TkImage, resizing them, putting them in Label widgets,
# and sticking the label widgets onto the board locations
black_queen_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_queen.png'
black_queen_image = Image.open(black_queen_filepath)
black_king_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_king.png'
black_king_image = Image.open(black_king_filepath)
black_bishop_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_bishop.png'
black_bishop_image = Image.open(black_bishop_filepath)
black_knight_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_knight.png'
black_knight_image = Image.open(black_knight_filepath)
black_rook_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_rook.png'
black_rook_image = Image.open(black_rook_filepath)
black_pawn_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/black_pawn.png'
black_pawn_image = Image.open(black_pawn_filepath)

# Resize the image using resize() method
resized_black_queen = black_queen_image.resize((square_size - 10, square_size - 10))
resized_black_king = black_king_image.resize((square_size - 10, square_size - 10))
resized_black_bishop = black_bishop_image.resize((square_size - 10, square_size - 10))
resized_black_knight = black_knight_image.resize((square_size - 10, square_size - 10))
resized_black_rook = black_rook_image.resize((square_size - 10, square_size - 10))
resized_black_pawn = black_pawn_image.resize((square_size - 10, square_size - 10))

tk_black_queen = ImageTk.PhotoImage(resized_black_queen)
tk_black_king = ImageTk.PhotoImage(resized_black_king)
tk_black_bishop = ImageTk.PhotoImage(resized_black_bishop)
tk_black_knight = ImageTk.PhotoImage(resized_black_knight)
tk_black_rook = ImageTk.PhotoImage(resized_black_rook)
tk_black_pawn = ImageTk.PhotoImage(resized_black_pawn)

# create label and add resize image

b_rook1 = Label(master=root, image=tk_black_rook)
b_rook1.image = tk_black_rook
b_rook1.grid(row=0, column=7)
b_rook1.config(bg=black_color)

b_knight1 = Label(master=root, image=tk_black_knight)
b_knight1.image = tk_black_knight
b_knight1.grid(row=0, column=6)
b_knight1.config(bg="white")

b_bishop1 = Label(master=root, image=tk_black_bishop)
b_bishop1.image = tk_black_bishop
b_bishop1.grid(row=0, column=5)
b_bishop1.config(bg=black_color)

b_king = Label(master=root, image=tk_black_king)
b_king.image = tk_black_king
b_king.grid(row=0, column=4)
b_king.config(bg="white")

b_queen = Label(master=root, image=tk_black_queen)
b_queen.image = tk_black_queen
b_queen.grid(row=0, column=3)
b_queen.config(bg=black_color)

b_bishop2 = Label(master=root, image=tk_black_bishop)
b_bishop2.image = tk_black_bishop
b_bishop2.grid(row=0, column=2)
b_bishop2.config(bg="white")

b_knight2 = Label(master=root, image=tk_black_knight)
b_knight2.image = tk_black_knight
b_knight2.grid(row=0, column=1)
b_knight2.config(bg=black_color)

b_rook2 = Label(master=root, image=tk_black_rook)
b_rook2.image = tk_black_rook
b_rook2.grid(row=0, column=0)
b_rook2.config(bg="white")

b_h_pawn = Label(master=root, image=tk_black_pawn)
b_h_pawn.image = tk_black_pawn
b_h_pawn.grid(row=1, column=7)
b_h_pawn.config(bg="white")

b_g_pawn = Label(master=root, image=tk_black_pawn)
b_g_pawn.image = tk_black_pawn
b_g_pawn.grid(row=1, column=6)
b_g_pawn.config(bg=black_color)

b_f_pawn = Label(master=root, image=tk_black_pawn)
b_f_pawn.image = tk_black_pawn
b_f_pawn.grid(row=1, column=5)
b_f_pawn.config(bg="white")

b_e_pawn = Label(master=root, image=tk_black_pawn)
b_e_pawn.image = tk_black_pawn
b_e_pawn.grid(row=1, column=4)
b_e_pawn.config(bg=black_color)

b_d_pawn = Label(master=root, image=tk_black_pawn)
b_d_pawn.image = tk_black_pawn
b_d_pawn.grid(row=1, column=3)
b_d_pawn.config(bg="white")

b_c_pawn = Label(master=root, image=tk_black_pawn)
b_c_pawn.image = tk_black_pawn
b_c_pawn.grid(row=1, column=2)
b_c_pawn.config(bg=black_color)

b_b_pawn = Label(master=root, image=tk_black_pawn)
b_b_pawn.image = tk_black_pawn
b_b_pawn.grid(row=1, column=1)
b_b_pawn.config(bg="white")

b_a_pawn = Label(master=root, image=tk_black_pawn)
b_a_pawn.image = tk_black_pawn
b_a_pawn.grid(row=1, column=0)
b_a_pawn.config(bg=black_color)

white_queen_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_queen.png'
white_queen_image = Image.open(white_queen_filepath)
white_king_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_king.png'
white_king_image = Image.open(white_king_filepath)
white_bishop_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_bishop.png'
white_bishop_image = Image.open(white_bishop_filepath)
white_knight_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_knight.png'
white_knight_image = Image.open(white_knight_filepath)
white_rook_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_rook.png'
white_rook_image = Image.open(white_rook_filepath)
white_pawn_filepath = '/Users/danielhuang/PycharmProjects/ChessSimulation/venv/lib/images/white_pawn.png'
white_pawn_image = Image.open(white_pawn_filepath)

# Resize the image using resize() method
resized_white_queen = white_queen_image.resize((square_size - 10, square_size - 10))
resized_white_king = white_king_image.resize((square_size - 10, square_size - 10))
resized_white_bishop = white_bishop_image.resize((square_size - 10, square_size - 10))
resized_white_knight = white_knight_image.resize((square_size - 10, square_size - 10))
resized_white_rook = white_rook_image.resize((square_size - 10, square_size - 10))
resized_white_pawn = white_pawn_image.resize((square_size - 10, square_size - 10))

tk_white_queen = ImageTk.PhotoImage(resized_white_queen)
tk_white_king = ImageTk.PhotoImage(resized_white_king)
tk_white_bishop = ImageTk.PhotoImage(resized_white_bishop)
tk_white_knight = ImageTk.PhotoImage(resized_white_knight)
tk_white_rook = ImageTk.PhotoImage(resized_white_rook)
tk_white_pawn = ImageTk.PhotoImage(resized_white_pawn)

# create label and add resize image

w_rook1 = Label(master=root, image=tk_white_rook)
w_rook1.image = tk_white_rook
w_rook1.grid(row=7, column=0)
w_rook1.config(bg=black_color)

w_knight1 = Label(master=root, image=tk_white_knight)
w_knight1.image = tk_white_knight
w_knight1.grid(row=7, column=1)
w_knight1.config(bg="white")

w_bishop1 = Label(master=root, image=tk_white_bishop)
w_bishop1.image = tk_white_bishop
w_bishop1.grid(row=7, column=2)
w_bishop1.config(bg=black_color)

w_queen = Label(master=root, image=tk_white_queen)
w_queen.image = tk_white_queen
w_queen.grid(row=7, column=3)
w_queen.config(bg="white")

w_king = Label(master=root, image=tk_white_king)
w_king.image = tk_white_king
w_king.grid(row=7, column=4)
w_king.config(bg=black_color)

w_bishop2 = Label(master=root, image=tk_white_bishop)
w_bishop2.image = tk_white_bishop
w_bishop2.grid(row=7, column=5)
w_bishop2.config(bg="white")

w_knight2 = Label(master=root, image=tk_white_knight)
w_knight2.image = tk_white_knight
w_knight2.grid(row=7, column=6)
w_knight2.config(bg=black_color)

w_rook2 = Label(master=root, image=tk_white_rook)
w_rook2.image = tk_white_rook
w_rook2.grid(row=7, column=7)
w_rook2.config(bg="white")

w_h_pawn = Label(master=root, image=tk_white_pawn)
w_h_pawn.image = tk_white_pawn
w_h_pawn.grid(row=6, column=7)
w_h_pawn.config(bg=black_color)

w_g_pawn = Label(master=root, image=tk_white_pawn)
w_g_pawn.image = tk_white_pawn
w_g_pawn.grid(row=6, column=6)
w_g_pawn.config(bg='white')

w_f_pawn = Label(master=root, image=tk_white_pawn)
w_f_pawn.image = tk_white_pawn
w_f_pawn.grid(row=6, column=5)
w_f_pawn.config(bg=black_color)

w_e_pawn = Label(master=root, image=tk_white_pawn)
w_e_pawn.image = tk_white_pawn
w_e_pawn.grid(row=6, column=4)
w_e_pawn.config(bg='white')

w_d_pawn = Label(master=root, image=tk_white_pawn)
w_d_pawn.image = tk_white_pawn
w_d_pawn.grid(row=6, column=3)
w_d_pawn.config(bg=black_color)

w_c_pawn = Label(master=root, image=tk_white_pawn)
w_c_pawn.image = tk_white_pawn
w_c_pawn.grid(row=6, column=2)
w_c_pawn.config(bg="white")

w_b_pawn = Label(master=root, image=tk_white_pawn)
w_b_pawn.image = tk_white_pawn
w_b_pawn.grid(row=6, column=1)
w_b_pawn.config(bg=black_color)

w_a_pawn = Label(master=root, image=tk_white_pawn)
w_a_pawn.image = tk_white_pawn
w_a_pawn.grid(row=6, column=0)
w_a_pawn.config(bg="white")

black_piece_images = [b_h_pawn, b_g_pawn, b_f_pawn, b_e_pawn, b_d_pawn, b_c_pawn, b_b_pawn, b_a_pawn,
                      b_rook1, b_knight1, b_bishop1, b_king, b_queen, b_bishop2, b_knight2, b_rook2]
white_piece_images = [w_a_pawn, w_b_pawn, w_c_pawn, w_d_pawn, w_e_pawn, w_f_pawn, w_g_pawn, w_h_pawn,
                      w_rook1, w_knight1, w_bishop1, w_queen, w_king, w_bishop2, w_knight2, w_rook2]

for index in range(8):
    board_map.append([None, None, None, None, None, None, None, None])


def evaluate_board():
    for x_clear in range(8):
        for y_clear in range(len(board_map)):
            board_map[x_clear][y_clear] = None
    for piece_a in chess_board.white_pieces:
        if not piece_a.captured:
            board_map[piece_a.x][piece_a.y] = piece_a
    for piece_b in chess_board.black_pieces:
        if not piece_b.captured:
            board_map[piece_b.x][piece_b.y] = piece_b


def find_checks(sides):
    checks = []
    pieces_to_check = []
    if sides:
        pieces_to_check = chess_board.black_pieces
    else:
        pieces_to_check = chess_board.white_pieces

    for piece in pieces_to_check:
        if not piece.captured:
            if piece.identity == "Queen" or piece.identity == "Rook":
                for move_right in range(1, 8):
                    if piece.x + move_right > 7:
                        break
                    given_piece = board_map[piece.x + move_right][piece.y]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":
                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_left in range(1, 8):
                    if piece.x - move_left < 0:
                        break
                    given_piece = board_map[piece.x - move_left][piece.y]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":

                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_up in range(1, 8):
                    if piece.y + move_up > 7:
                        break
                    given_piece = board_map[piece.x][piece.y + move_up]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":

                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_down in range(1, 8):
                    if piece.y - move_down < 0:
                        break
                    given_piece = board_map[piece.x][piece.y - move_down]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":

                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
            if piece.identity == "Queen" or piece.identity == "Bishop":
                for move_up_right in range(1, 8):
                    if piece.x + move_up_right > 7 or piece.y + move_up_right > 7:
                        break
                    given_piece = board_map[piece.x + move_up_right][piece.y + move_up_right]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":

                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_up_left in range(1, 8):
                    if piece.x - move_up_left < 0 or piece.y + move_up_left > 7:
                        break
                    given_piece = board_map[piece.x - move_up_left][piece.y + move_up_left]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":

                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_down_right in range(1, 8):
                    if piece.x + move_down_right > 7 or piece.y - move_down_right < 0:
                        break
                    given_piece = board_map[piece.x + move_down_right][piece.y - move_down_right]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":
                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
                for move_down_left in range(1, 8):
                    if piece.x - move_down_left < 0 or piece.y - move_down_left < 0:
                        break
                    given_piece = board_map[piece.x - move_down_left][piece.y - move_down_left]
                    if given_piece is not None:
                        if given_piece.side == sides:
                            if given_piece.identity == "King":
                                checks.append(piece)
                                break
                            else:
                                break
                        else:
                            break
            elif piece.identity == "Knight":
                jumps = [[1, 2], [-1, 2], [2, 1], [-2, 1], [2, -1], [-2, -1], [1, -2], [-1, -2]]
                for jump in jumps:
                    given_piece = None
                    if 0 <= piece.x + jump[0] <= 7 and 0 <= piece.y + jump[1] <= 7:
                        given_piece = board_map[piece.x + jump[0]][piece.y + jump[1]]
                    if given_piece is not None:
                        if given_piece.side == sides and given_piece.identity == "King":
                            checks.append(piece)
            elif piece.identity == "Pawn":
                jumps = []
                if sides:
                    jumps = [[1, -1], [-1, -1]]
                else:
                    jumps = [[1, 1], [-1, 1]]
                for jump in jumps:
                    given_piece = None
                    if 0 <= piece.x + jump[0] <= 7 and 0 <= piece.y + jump[1] <= 7:
                        given_piece = board_map[piece.x + jump[0]][piece.y + jump[1]]
                    if given_piece is not None:
                        if given_piece.side == sides and given_piece.identity == "King":
                            checks.append(piece)
    return checks


def update_board():
    # The following for loop displays all the widget pieces based on their location
    for index in range(len(chess_board.white_pieces)):
        if not chess_board.white_pieces[index].captured:
            white_piece_images[index].grid(row=7 - chess_board.white_pieces[index].y,
                                           column=chess_board.white_pieces[index].x)
        else:
            white_piece_images[index].place(x=1000, y=1000)

        if not chess_board.black_pieces[index].captured:
            black_piece_images[index].grid(row=7 - chess_board.black_pieces[index].y,
                                           column=chess_board.black_pieces[index].x)
        else:
            black_piece_images[index].place(x=4000, y=4000)

        if (chess_board.white_pieces[index].x % 2 == 1 and chess_board.white_pieces[index].y % 2 == 0) \
                or (chess_board.white_pieces[index].x % 2 == 0 and chess_board.white_pieces[index].y % 2 == 1):
            white_piece_images[index].config(bg="white")
        else:
            white_piece_images[index].config(bg=black_color)
        if (chess_board.black_pieces[index].x % 2 == 1 and chess_board.black_pieces[index].y % 2 == 0) \
                or (chess_board.black_pieces[index].x % 2 == 0 and chess_board.black_pieces[index].y % 2 == 1):
            black_piece_images[index].config(bg="white")
        else:
            black_piece_images[index].config(bg=black_color)


def find_legal_moves(given_piece):
    legal_moves = []
    if given_piece.captured:
        return legal_moves
    if given_piece.identity == "Queen" or given_piece.identity == "Rook":
        for move_right in range(1, 8):
            if given_piece.x + move_right > 7:
                break
            elif board_map[given_piece.x + move_right][given_piece.y] is None:
                legal_moves.append([move_right, 0])
            else:
                if board_map[given_piece.x + move_right][given_piece.y].side != given_piece.side:
                    legal_moves.append([move_right, 0])
                    break
                else:
                    break
        for move_left in range(1, 8):
            if given_piece.x - move_left < 0:
                break
            elif board_map[given_piece.x - move_left][given_piece.y] is None:
                legal_moves.append([move_left * -1, 0])
            else:
                if board_map[given_piece.x - move_left][given_piece.y].side != given_piece.side:
                    legal_moves.append([move_left * -1, 0])
                    break
                else:
                    break
        for move_up in range(1, 8):
            if given_piece.y + move_up > 7:
                break
            elif board_map[given_piece.x][given_piece.y + move_up] is None:
                legal_moves.append([0, move_up])
            else:
                if board_map[given_piece.x][given_piece.y + move_up].side != given_piece.side:
                    legal_moves.append([0, move_up])
                    break
                else:
                    break
        for move_down in range(1, 8):
            if given_piece.y - move_down < 0:
                break
            elif board_map[given_piece.x][given_piece.y - move_down] is None:
                legal_moves.append([0, move_down * -1])
            else:
                if board_map[given_piece.x][given_piece.y - move_down].side != given_piece.side:
                    legal_moves.append([0, move_down * -1])
                    break
                else:
                    break
    if given_piece.identity == "Queen" or given_piece.identity == "Bishop":
        for move_up_right in range(1, 8):
            if given_piece.x + move_up_right > 7 or given_piece.y + move_up_right > 7:
                break
            elif board_map[given_piece.x + move_up_right][given_piece.y + move_up_right] is None:
                legal_moves.append([move_up_right, move_up_right])
            else:
                if board_map[given_piece.x + move_up_right][given_piece.y + move_up_right].side != given_piece.side:
                    legal_moves.append([move_up_right, move_up_right])
                    break
                else:
                    break
        for move_up_left in range(1, 8):
            if given_piece.x - move_up_left < 0 or given_piece.y + move_up_left > 7:
                break
            elif board_map[given_piece.x - move_up_left][given_piece.y + move_up_left] is None:
                legal_moves.append([move_up_left * -1, move_up_left])
            else:
                if board_map[given_piece.x - move_up_left][given_piece.y + move_up_left].side != given_piece.side:
                    legal_moves.append([move_up_left * -1, move_up_left])
                    break
                else:
                    break
        for move_down_right in range(1, 8):
            if given_piece.x + move_down_right > 7 or given_piece.y - move_down_right < 0:
                break
            elif board_map[given_piece.x + move_down_right][given_piece.y - move_down_right] is None:
                legal_moves.append([move_down_right, move_down_right * -1])
            else:
                if board_map[given_piece.x + move_down_right][given_piece.y - move_down_right].side != given_piece.side:
                    legal_moves.append([move_down_right, move_down_right * -1])
                    break
                else:
                    break
        for move_down_left in range(1, 8):
            if given_piece.x - move_down_left < 0 or given_piece.y - move_down_left < 0:
                break
            elif board_map[given_piece.x - move_down_left][given_piece.y - move_down_left] is None:
                legal_moves.append([move_down_left * -1, move_down_left * -1])
            else:
                if board_map[given_piece.x - move_down_left][given_piece.y - move_down_left].side != given_piece.side:
                    legal_moves.append([move_down_left * -1, move_down_left * -1])
                    break
                else:
                    break
    elif given_piece.identity == "Knight":
        jumps = [[1, 2], [-1, 2], [2, 1], [-2, 1], [2, -1], [-2, -1], [1, -2], [-1, -2]]
        for jump in jumps:
            if 0 <= given_piece.x + jump[0] <= 7 and 0 <= given_piece.y + jump[1] <= 7:
                if board_map[given_piece.x + jump[0]][given_piece.y + jump[1]] is None:
                    legal_moves.append([jump[0], jump[1]])
                elif board_map[given_piece.x + jump[0]][given_piece.y + jump[1]] is not None and \
                        board_map[given_piece.x + jump[0]][given_piece.y + jump[1]].side != given_piece.side:
                    legal_moves.append([jump[0], jump[1]])
    elif given_piece.identity == "Pawn":
        step = 1
        if not given_piece.side:
            step = -1

        if given_piece.x - 1 >= 0:
            if board_map[given_piece.x - 1][given_piece.y + step] is not None:
                if board_map[given_piece.x - 1][given_piece.y + step].side != given_piece.side:
                    legal_moves.append([-1, step])
        if given_piece.x + 1 <= 7:
            if board_map[given_piece.x + 1][given_piece.y + step] is not None:
                if board_map[given_piece.x + 1][given_piece.y + step].side != given_piece.side:
                    legal_moves.append([1, step])
        if board_map[given_piece.x][given_piece.y + step] is None:
            legal_moves.append([0, step])
            if board_map[given_piece.x][given_piece.y + step] is None and \
                    board_map[given_piece.x][given_piece.y + step * 2] is None:
                if (given_piece.side and given_piece.y == 1) or (not given_piece.side and given_piece.y == 6):
                    legal_moves.append([0, step * 2])
    elif given_piece.identity == "King":
        if not given_piece.has_moved:
            given_rook1 = None
            given_rook2 = None
            if given_piece.side:
                given_rook1 = chess_board.rook1_white
                given_rook2 = chess_board.rook2_white
            else:
                given_rook1 = chess_board.rook1_black
                given_rook2 = chess_board.rook2_black
            if given_piece.side and not given_rook2.has_moved and board_map[given_piece.x + 1][given_piece.y] \
                    is None and board_map[given_piece.x + 2][given_piece.y] is None:
                legal_moves.append(["castle kingside"])
            elif not given_piece.side and not given_rook1.has_moved and board_map[given_piece.x + 1][given_piece.y] \
                    is None and board_map[given_piece.x + 2][given_piece.y] is None:
                legal_moves.append(["castle kingside"])

            if given_piece.side and not given_rook1.has_moved and board_map[given_piece.x - 1][given_piece.y] \
                    is None and board_map[given_piece.x - 2][given_piece.y] is None and \
                    board_map[given_piece.x - 3][given_piece.y] is None:
                legal_moves.append(["castle queenside"])
            elif not given_piece.side and not given_rook2.has_moved and board_map[given_piece.x - 1][given_piece.y] \
                    is None and board_map[given_piece.x - 2][given_piece.y] is None and \
                    board_map[given_piece.x - 3][given_piece.y] is None:
                legal_moves.append(["castle queenside"])

        jumps = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        for jump in jumps:
            if 0 <= given_piece.x + jump[0] <= 7 and 0 <= given_piece.y + jump[1] <= 7:
                if board_map[given_piece.x + jump[0]][given_piece.y + jump[1]] is None:
                    legal_moves.append([jump[0], jump[1]])
                elif board_map[given_piece.x + jump[0]][given_piece.y + jump[1]] is not None and \
                        board_map[given_piece.x + jump[0]][given_piece.y + jump[1]].side != given_piece.side:
                    legal_moves.append([jump[0], jump[1]])

    moves_to_remove = []
    if given_piece.identity == "King":
        in_check = find_checks(given_piece.side)
        if len(in_check) > 0:
            if "castle kingside" in legal_moves:
                legal_moves.remove("castle kingside")
            if "castle queenside" in legal_moves:
                legal_moves.remove("castle queenside")
        if "castle kingside" in legal_moves:
            given_piece.x += 1
            evaluate_board()
            check1 = find_checks(given_piece.side)
            if len(check1) > 0:
                legal_moves.remove("castle kingside")
            given_piece.x += 1
            evaluate_board()
            check2 = find_checks(given_piece.side)
            if len(check2) > 0 and "castle kingside" in legal_moves:
                legal_moves.remove("castle kingside")
            given_piece.x -= 2
            evaluate_board()
        if "castle queenside" in legal_moves:
            given_piece.x -= 1
            evaluate_board()
            check1 = find_checks(given_piece.side)
            if len(check1) > 0:
                legal_moves.remove("castle queenside")
            given_piece.x -= 1
            evaluate_board()
            check2 = find_checks(given_piece.side)
            if len(check2) > 0 and "castle queenside" in legal_moves:
                legal_moves.remove("castle queenside")
            given_piece.x += 2
            evaluate_board()
            pass
    has_castling = []
    if ['castle kingside'] in legal_moves:
        has_castling.append(['castle kingside'])
        legal_moves.remove(['castle kingside'])
    if ['castle queenside'] in legal_moves:
        has_castling.append(['castle queenside'])
        legal_moves.remove(['castle queenside'])
    for move in legal_moves:
        given_piece.x += move[0]
        given_piece.y += move[1]
        evaluate_board()
        attacking_pieces = find_checks(given_piece.side)
        if len(attacking_pieces) > 0:
            moves_to_remove.append(move)
            for attacking_piece in attacking_pieces:
                if given_piece.x == attacking_piece.x and given_piece.y == attacking_piece.y and \
                        len(attacking_pieces) - 1 <= 0:
                    moves_to_remove.remove(move)
        given_piece.x -= move[0]
        given_piece.y -= move[1]
        evaluate_board()

    for removed_move in moves_to_remove:
        legal_moves.remove(removed_move)

    legal_moves.extend(has_castling)
    return legal_moves


evaluate_board()
update_board()


def display_legal_moves(piece_to_move):
    global piece_selected
    global indications
    global possible_moves
    castling = []
    possible_moves = find_legal_moves(piece_to_move)
    piece_selected = piece_to_move
    while len(indications) > 0:
        indications[-1].destroy()
        indications.pop()
    if len(possible_moves) < 1:
        piece_selected = None

    for legal_move in range(len(possible_moves)):
        if len(possible_moves[legal_move]) == 2:
            indications.append(Label(master=root, bg="#43a159", width=2, height=1))
            indications[legal_move].grid(row=7 - piece_selected.y - possible_moves[legal_move][1],
                                         column=piece_selected.x + possible_moves[legal_move][0])
        elif len(possible_moves[legal_move]) == 1:
            if possible_moves[legal_move][0] == "castle kingside":
                indications.append(Label(master=root, bg="#43a159", width=2, height=1))
                indications[legal_move].grid(row=7 - piece_selected.y, column=piece_selected.x + 2)
            elif possible_moves[legal_move][0] == "castle queenside":
                indications.append(Label(master=root, bg="#43a159", width=2, height=1))
                indications[legal_move].grid(row=7 - piece_selected.y, column=piece_selected.x - 2)


def make_move(piece_to_move, move_x, move_y):
    global white_to_move
    global piece_selected
    global possible_moves
    global indications
    enemy_pieces = []
    if piece_to_move.side:
        enemy_pieces = chess_board.black_pieces
    else:
        enemy_pieces = chess_board.white_pieces

    if piece_to_move.identity == "King" and move_x == 69 and move_y == 69:
        piece_to_move.x += 2
        if piece_to_move.side:
            chess_board.rook2_white.x -= 2
        else:
            chess_board.rook1_black.x -= 2
    elif piece_to_move.identity == "King" and move_x == 420 and move_y == 420:
        piece_to_move.x -= 2
        if piece_to_move.side:
            chess_board.rook1_white.x += 3
        else:
            chess_board.rook2_black.x += 3
    else:
        for captured_piece in enemy_pieces:
            if piece_to_move.x + move_x == captured_piece.x and piece_to_move.y + move_y == captured_piece.y and \
                    not captured_piece.captured:
                captured_piece.captured = True
                captured_piece.x = 8
                captured_piece.y = 8
                break
        piece_to_move.x += move_x
        piece_to_move.y += move_y

    if piece_to_move.identity == "Pawn":
        if (piece_to_move.side and piece_to_move.y == 7) or (not piece_to_move.side and piece_to_move.y == 0):
            piece_to_move.identity = "Queen"

    piece_to_move.has_moved = True

    evaluate_board()
    update_board()
    white_to_move = not white_to_move
    while len(indications) > 0:
        indications[-1].destroy()
        indications.pop()
    possible_moves = []
    update_status(white_to_move)


def test_click(event):
    global white_to_move
    global piece_selected
    global possible_moves
    reset = True
    mouse_x = event.x_root - root.winfo_x()
    mouse_y = event.y_root - root.winfo_y()
    # print("mouse click location: " + str(mouse_x) + ", " + str(mouse_y))

    if game_state == "PLAYING":
        if white_to_move:
            pieces_to_move = chess_board.white_pieces
        else:
            pieces_to_move = chess_board.black_pieces

        if piece_selected is not None:
            p_x = square_size * piece_selected.x
            p_y = square_size * (7 - piece_selected.y)
            # this checks if the selected piece was clicked again, in which it should de-select itself
            if p_x + square_size > mouse_x > p_x and p_y + square_size + 24 > mouse_y > 24 + p_y:
                while len(indications) > 0:
                    indications[-1].destroy()
                    indications.pop()
                piece_selected = None
                reset = False

            # this checks if one of the legal moves was selected, in which the piece should move
            castling = []
            if ["castle kingside"] in possible_moves:
                castling.append(["castle kingside"])
                possible_moves.remove(["castle kingside"])

            if ["castle queenside"] in possible_moves:
                castling.append(["castle queenside"])
                possible_moves.remove(["castle queenside"])
            for move in possible_moves:
                if piece_selected is not None and \
                        square_size * (piece_selected.x + move[0]) + square_size > mouse_x > square_size \
                        * (piece_selected.x + move[0]) and square_size * (7 - (piece_selected.y + move[1])) \
                        + square_size + 24 > mouse_y > 24 + square_size * (7 - (piece_selected.y + move[1])):
                    make_move(piece_selected, move[0], move[1])
                    piece_selected = None
                    reset = False
                    break
            if ["castle kingside"] in castling and piece_selected is not None and \
                    square_size * (piece_selected.x + 2) + square_size > mouse_x > square_size \
                    * (piece_selected.x + 2) and square_size * (7 - piece_selected.y) \
                    + square_size + 24 > mouse_y > 24 + square_size * (7 - piece_selected.y):
                make_move(piece_selected, 69, 69)
                piece_selected = None
                reset = False
            if ["castle queenside"] in castling and piece_selected is not None and \
                    square_size * (piece_selected.x - 2) + square_size > mouse_x > square_size \
                    * (piece_selected.x - 2) and square_size * (7 - piece_selected.y) \
                    + square_size + 24 > mouse_y > 24 + square_size * (7 - piece_selected.y):
                make_move(piece_selected, 420, 420)
                piece_selected = None
                reset = False
        if reset:
            for clicked_piece in pieces_to_move:
                if square_size * clicked_piece.x + square_size > mouse_x > square_size * clicked_piece.x and \
                        square_size * (7 - clicked_piece.y) + square_size + 24 > mouse_y > 24 + \
                        square_size * (7 - clicked_piece.y):
                    if clicked_piece != piece_selected:
                        display_legal_moves(clicked_piece)

                    legal_moves2 = find_legal_moves(clicked_piece)
                    # print(str(legal_moves2))
                    reset = False
                    break
        if reset:
            while len(indications) > 0:
                indications[-1].destroy()
                indications.pop()
            piece_selected = None


def update_status(whose_move):
    global game_state
    global white_to_move
    global announcement
    if whose_move:
        announcement = "White to move"
        announcer_banner.config(fg="black", bg="white")
    else:
        announcement = "Black to move"
        announcer_banner.config(fg="white", bg="black")
    moves = 0
    if white_to_move:
        for white_piece in chess_board.white_pieces:
            if len(find_legal_moves(white_piece)) > 0:
                moves += 1
                break
        if moves < 1:
            conclude_game()
            if len(find_checks(True)) > 0:
                announcement = "Black wins by checkmate!"
            else:
                announcement = "Draw by stalemate"
    else:
        for black_piece in chess_board.black_pieces:
            if len(find_legal_moves(black_piece)) > 0:
                moves += 1
                break
        if moves < 1:
            conclude_game()
            if len(find_checks(False)) > 0:
                announcement = "White wins by checkmate!"
            else:
                announcement = "Draw by stalemate"
    announcer_banner.config(text=announcement)


def control_game():
    global game_state
    global move_number
    global possible_moves
    global indications
    global piece_selected
    global white_to_move
    global announcement
    if game_state == "PREP":
        game_state = "PLAYING"
        announcement = "White to move"
        announcer_banner.config(fg="black", bg="white")
        new_game_button.config(text="Reset")
        announcer_banner.config(text=announcement)
        return
    if game_state == "PLAYING" or game_state == "CONCLUDED":
        game_state = "PREP"
        move_number = 1
        possible_moves = []
        indications = []
        piece_selected = None
        white_to_move = True
        chess_board.set_up_pieces()
        evaluate_board()
        update_board()
        new_game_button.config(text="Start New Game")
        new_game_button.config(bg="#32ad10")
        announcement = "Press the Start button\n to begin the game"
        announcer_banner.config(text=announcement, bg="#34b356", fg="black")
        return


def conclude_game():
    global game_state
    game_state = "CONCLUDED"
    new_game_button.config(text="Play Again")


new_game_button.config(command=lambda: control_game())

root.bind("<Button-1>", test_click)

root.mainloop()
