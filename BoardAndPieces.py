class Piece:
    identity = ""
    # location = Coordinates(0, 0)
    x = 0
    y = 0
    side = True
    move_set = []
    captured = False
    has_moved = False

    def __init__(self, color, piece_type, location_x, location_y):
        self.identity = piece_type
        self.x = location_x
        self.y = location_y
        self.side = color
        self.move_set = []
        self.captured = False


class Board:

    def __init__(self):
        pass

    orientation = True
    white_pieces = []
    black_pieces = []

    a_pawn_white = Piece(True, "Pawn", 0, 1)
    b_pawn_white = Piece(True, "Pawn", 1, 1)
    c_pawn_white = Piece(True, "Pawn", 2, 1)
    d_pawn_white = Piece(True, "Pawn", 3, 1)
    e_pawn_white = Piece(True, "Pawn", 4, 1)
    f_pawn_white = Piece(True, "Pawn", 5, 1)
    g_pawn_white = Piece(True, "Pawn", 6, 1)
    h_pawn_white = Piece(True, "Pawn", 7, 1)
    rook1_white = Piece(True, "Rook", 0, 0)
    knight1_white = Piece(True, "Knight", 1, 0)
    bishop1_white = Piece(True, "Bishop", 2, 0)
    queen_white = Piece(True, "Queen", 3, 0)
    king_white = Piece(True, "King", 4, 0)
    bishop2_white = Piece(True, "Bishop", 5, 0)
    knight2_white = Piece(True, "Knight", 6, 0)
    rook2_white = Piece(True, "Rook", 7, 0)

    white_pieces.extend([a_pawn_white, b_pawn_white, c_pawn_white, d_pawn_white,
                         e_pawn_white, f_pawn_white, g_pawn_white, h_pawn_white,
                         rook1_white, knight1_white, bishop1_white, queen_white,
                         king_white, bishop2_white, knight2_white, rook2_white])

    h_pawn_black = Piece(False, "Pawn", 7, 6)
    g_pawn_black = Piece(False, "Pawn", 6, 6)
    f_pawn_black = Piece(False, "Pawn", 5, 6)
    e_pawn_black = Piece(False, "Pawn", 4, 6)
    d_pawn_black = Piece(False, "Pawn", 3, 6)
    c_pawn_black = Piece(False, "Pawn", 2, 6)
    b_pawn_black = Piece(False, "Pawn", 1, 6)
    a_pawn_black = Piece(False, "Pawn", 0, 6)
    rook1_black = Piece(False, "Rook", 7, 7)
    knight1_black = Piece(False, "Knight", 6, 7)
    bishop1_black = Piece(False, "Bishop", 5, 7)
    king_black = Piece(False, "King", 4, 7)
    queen_black = Piece(False, "Queen", 3, 7)
    bishop2_black = Piece(False, "Bishop", 2, 7)
    knight2_black = Piece(False, "Knight", 1, 7)
    rook2_black = Piece(False, "Rook", 0, 7)

    black_pieces.extend([h_pawn_black, g_pawn_black, f_pawn_black, e_pawn_black,
                         d_pawn_black, c_pawn_black, b_pawn_black, a_pawn_black,
                         rook1_black, knight1_black, bishop1_black, king_black,
                         queen_black, bishop2_black, knight2_black, rook2_black])

    def place_piece(self, piece_to_set, x_dot, y_dot):
        piece_to_set.x = x_dot
        piece_to_set.y = y_dot

    def set_up_pieces(self):
        for index2 in range(0, 8):
            if index2 < 8:
                self.white_pieces[index2].identity = "Pawn"
                self.black_pieces[index2].identity = "Pawn"
            self.place_piece(self.white_pieces[index2], index2, 1)
            self.place_piece(self.white_pieces[index2 + 8], index2, 0)
            self.place_piece(self.black_pieces[index2], 7 - index2, 6)
            self.place_piece(self.black_pieces[index2 + 8], 7 - index2, 7)
            self.white_pieces[index2].captured = False
            self.white_pieces[index2 + 8].captured = False
            self.black_pieces[index2].captured = False
            self.black_pieces[index2 + 8].captured = False

            self.white_pieces[index2].has_moved = False
            self.white_pieces[index2 + 8].has_moved = False
            self.black_pieces[index2].has_moved = False
            self.black_pieces[index2 + 8].has_moved = False
