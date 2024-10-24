from athena.board import Board


class Position:
  def __init__(self, 
               board: Board,
               color: str, 
               castle_rights: str,
               en_passant: str,
               move_count: int,
               half_move_count: int) -> None:
    self.board = board
    self.color = color
    self.castle_rights = castle_rights
    self.en_passant = en_passant
    self.move_count = move_count
    self.half_move_count = half_move_count