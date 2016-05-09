from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def posibles4EnRaya(state):
    libres = state.moves
    board = state.board
    lista = []
    for hueco in board:
        if board.get(hueco) == "X":
            lista.append(compute_utility(board, hueco, "X"))
    h = sum(lista);
    listaHumano = []
    for hueco in board:
        if board.get(hueco) == "0":
            listaHumano.append(compute_utility(board, hueco, "0"))
    h = h - sum(listaHumano)
    h = h + centro(state);
    return h;


def centro(state):
  h=0;
  for clave, valor in state.board.items():

      if valor == 'X':
          x,y = clave;

          if x == 4:
              h = h + 50;
          if x == 3 or x == 5:
              h = h + 30;
          if x == 2 or x == 6:
              h = h + 15;
          if x == 1 or x == 7:
              h = h + 5;
  return h;



def compute_utility(board, move, player):
    "If X wins with this move, return 1; if O return -1; else return 0."
    lista = [0, 0, 0, 0]
    lista[0] = k_in_row(board, move, player, (0, 1))  # comprobar columna
    lista[1] = k_in_row(board, move, player, (1, 0))  # comprobar fila
    lista[2] = k_in_row(board, move, player, (1, -1))  # comprobar diagonal izquieda
    lista[3] = k_in_row(board, move, player, (1, 1))  # comprobar diagonal derecha

    return sum(lista)


def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    h=0;
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y), '.') == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    a, b = move
    while board.get((a, b), '.') == player:
        n += 1
        a, b = a - delta_x, b - delta_y

    c, d = move

    n -= 1  # Because we counted move itself twice
    if n == 4:
        h = 100000
    if n == 3:
        h = 50
    if (n == 3) and (board.get((x + delta_x, y + delta_y)) == '.') and (board.get((c - delta_x, d -  delta_y))) == '.':
        h = h + 100;
    if (n == 3) and (board.get((a - delta_x, b - delta_y)) == '.') and (board.get((c + delta_x, d +  delta_y))) == '.':
        h = h + 100;
    if n == 2:
        h = 20
    if n == 1:
        h = 1
    return h


def avg(lista):
    return sum(lista) / float(len(lista))
