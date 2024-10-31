import numpy as np

from athena import COLORS, PIECES


class Bitboard:
  def __init__(self, bb: np.int64) -> None:
    self.bb = bb

  def get_bit(self, i: int) -> bool: return (self.bb >> i) & 1
  def set_bit(self, i: int) -> None: self.bb |= 1 << i

  @property
  def empty(self) -> bool: return self.bb == 0

  def __str__(self) -> str:
    board_lines = []
    for r in range(7, -1, -1):   # Iterate from rank 8 to 1 (reverse)
      row = []
      for f in range(8):         # Iterate from file A to H
        if f == 0: row.append(str(r+ 1))
        idx = r * 8 + f
        row.append('1' if self.get_bit(idx) else '0')
      board_lines.append(' '.join(row))
    return '\n'.join([*board_lines, '  A B C D E F G H'])


class Board:
  def __init__(self, positions: dict[str, str]) -> None:
    self.positions = positions
    self.bitboards = self.set_bitboards()

  def set_bitboards(self) -> dict[str, Bitboard]:
    bit: dict[str, Bitboard] = { piece: Bitboard(0) for piece in PIECES }
    for pos, piece in self.positions.items():
      assert piece in PIECES, f'Invalid piece: {piece}'
      bit[piece].set_bit(self.algebraic_to_index(pos))
    return bit
  
  def algebraic_to_index(self, pos: str) -> int:
    file = ord(pos[0].lower()) - ord('a')
    rank = int(pos[1]) - 1
    return rank * 8 + file
  
  def get_piece_bitboard(self, piece: str) -> Bitboard:
    assert piece in PIECES, f'Invalid piece: {piece}'
    return self.bitboards[piece]

  def get_color_bitboard(self, color: str) -> Bitboard:
    # depending on the color, create a single bitboard of occupied squares
    assert color in COLORS, f'Invalid color: {color}'
    return Bitboard(sum([bb.bb for piece, bb in self.bitboards.items() if piece.islower() == (color == 'b')]))

  @property
  def to_fen(self) -> str:
    # Generate a FEN string from the current board state
    fen = ''
    for r in range(7, -1, -1):
      empty = 0
      for f in range(8):
        square = r * 8 + f
        square_occupied = False
        for p, bb in self.bitboards.items():
          if bb.get_bit(square):
            if empty > 0:
              fen += str(empty)
              empty = 0
            fen += p
            square_occupied = True
            break
        if not square_occupied: 
          empty += 1
      if empty > 0: 
        fen += str(empty)
      fen += '/' if r > 0 else '' 
    return fen
        