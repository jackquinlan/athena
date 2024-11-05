from athena.engine import Engine, Position

class Game:
  def __init__(self, start_position: Position = Position()) -> None:
    self.start_position = start_position
    self.engine = Engine()

  def start(self):
    self.engine.pseudo_legal_moves(self.start_position)
