from dataclasses import dataclass

from athena.board import Board
from athena.constants import DEFAULT_POSITION

@dataclass
class Position:
  board: Board = Board(DEFAULT_POSITION)
  color: str = 'w'
  castle_rights: str = 'KQkq'
  en_passant: str = '-'
  halfmove_clock: int = 0
  fullmove_count: int = 1

  @property
  def to_fen(self) -> str: 
    return (
      f'{self.board.to_fen} {self.color} {self.castle_rights} {self.en_passant} {self.halfmove_clock} {self.fullmove_count}')

  @classmethod
  def from_fen(cls, fen: str):
    return cls(
      board=Board.from_fen(fen.split()[0]), 
      color=fen.split()[1], 
      castle_rights=fen.split()[2], 
      en_passant=fen.split()[3],
      halfmove_clock=int(fen.split()[4]),
      fullmove_count=int(fen.split()[5]))