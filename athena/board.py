import numpy as np

PIECES = ['p', 'n', 'b', 'r', 'q', 'k', 'P', 'N', 'B', 'R', 'Q', 'K']


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
  
  def get_bitboard(self, piece: str) -> Bitboard:
    return self.bitboards[piece]
