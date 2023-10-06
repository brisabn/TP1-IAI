import numpy as np

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other): # Usado na Uniform Cost
        return self.cost < other.cost
    
    def get_solution_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))

    def generate_children(self):
        children = []
        empty_row, empty_col = np.where(self.state == 0)
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if self.is_valid_move(new_row, new_col):
                new_state = self._swap(empty_row, empty_col, new_row, new_col)
                cost = self.cost + 1  # Incrementa o custo ao se mover para o novo estado
                children.append(Node(new_state, self, move, cost))

        return children

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3

    def _swap(self, r1, c1, r2, c2):
        new_state = np.copy(self.state)
        new_state[r1, c1], new_state[r2, c2] = new_state[r2, c2], new_state[r1, c1]
        return new_state
    

class EightPuzzle:
    def __init__(self, initial_state):
        # Define o estado objetivo
        self.goal_state = np.array([[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 0]])
        self.initial_state = initial_state

    def count_steps(self, solution):
        return len(solution) if solution else 0

    def print_state(self, state):
        # Função para imprimir o estado do quebra-cabeça
        for row in state:
            print(' '.join(map(str, row)))

    def print_steps(self, solution):
        if solution:
            current_state = self.initial_state.copy()
            for state in solution:
                self.print_state(current_state)
                current_state = state.copy()
                print()  # Adiciona uma linha em branco após cada estado




