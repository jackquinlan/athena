from athena.board import Board

DEFAULT_POSITION = {
  'A1': 'R', 'B1': 'N', 'C1': 'B', 'D1': 'Q', 'E1': 'K', 'F1': 'B', 'G1': 'N', 'H1': 'R',
  'A2': 'P', 'B2': 'P', 'C2': 'P', 'D2': 'P', 'E2': 'P', 'F2': 'P', 'G2': 'P', 'H2': 'P',
  'A7': 'p', 'B7': 'p', 'C7': 'p', 'D7': 'p', 'E7': 'p', 'F7': 'p', 'G7': 'p', 'H7': 'p',
  'A8': 'r', 'B8': 'n', 'C8': 'b', 'D8': 'q', 'E8': 'k', 'F8': 'b', 'G8': 'n', 'H8': 'r',
}

def main():
  b = Board(positions=DEFAULT_POSITION)

if __name__ == '__main__':
  main()