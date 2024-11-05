from dataclasses import dataclass

from athena.position import Position
from athena.move import Move
from athena.board import Bitboard

def trailing_zeros(n: int) -> int: return (n & -n).bit_length() - 1

class Engine:
  def __init__(self) -> None:
    return

  def pseudo_legal_moves(self, pos: Position) -> list[Move]:
    # Generate a list of pseudo-legal moves for the current position
    moves: list[Move] = []
    for p, bb in pos.board.bitboards.items():
      if pos.color != pos.board.get_piece_color(p) or bb.is_empty: continue # only generate moves for current color and if the piece exists
      # generate pawn moves
      if p.lower() == 'p':
        moves.extend(self.pawn_moves(pos))
    return moves
  
  def pawn_moves(self, pos: Position) -> list[Move]:
    moves = []
    pawns = pos.board.get_piece_bitboard('P' if pos.color == 'w' else 'p')
    empty = pos.board.empty
    
    single_pushes = (pawns.bb << 8) & empty.bb if pos.color == 'w' else (pawns.bb >> 8) & empty.bb
    moves.extend(self.extract_moves(Bitboard(single_pushes), 8))
    return moves
  
  def extract_moves(self, bitboard: Bitboard, offset: int) -> list[Move]:
    moves = []
    while not bitboard.is_empty:
      index = trailing_zeros(bitboard.bb)
      moves.append(Move(index-offset, index))
      bitboard.clear_bit(index)
    return moves