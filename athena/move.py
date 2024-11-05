from dataclasses import dataclass

@dataclass
class Move:
  start: int
  end: int

  @property
  def algebraic(self) -> str:
    return f'{chr(97 + self.start % 8)}{8 - self.start // 8}{chr(97 + self.end % 8)}{8 - self.end // 8}'