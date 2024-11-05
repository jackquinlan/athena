from athena.game import Game
from athena.engine import Position

def main():
  Game(start_position=Position.from_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')).start()

if __name__ == '__main__':
  main()