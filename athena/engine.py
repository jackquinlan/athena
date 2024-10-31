from dataclasses import dataclass

from athena import Board 
from athena import COLORS, PIECES

@dataclass
class Move:
  start: str
  end: str
  en_passant: str
  castle: bool
  capture: bool

  @property
  def to_algebraic(self) -> str: return 

@dataclass
class Position:
  board: Board
  color: str = 'w'
  castle_rights: str = 'KQkq'
  en_passant: str = '-'
  halfmove_clock: int = 0
  fullmove_count: int = 1

  @property
  def to_fen(self) -> str: return f"{self.board.to_fen} {self.color} {self.castle_rights} {self.en_passant} {self.halfmove_clock} {self.fullmove_count}"

class Engine:
  def __init__(self) -> None:
    return

  def gen_pseudo_legal_moves(self, pos: Position) -> list[Move]:
    print(pos.to_fen)
    return []