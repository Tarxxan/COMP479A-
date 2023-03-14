class EightPuzz:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.closed_list = []

    def get_moves(self, state):
        possible_moves = []
        pos_x, pos_y = self.find_blank_coords(state)

        if pos_x > 0:
            possible_moves.append("up")
        if pos_x < 2:
            possible_moves.append("down")
        if pos_y > 0:
            possible_moves.append("left")
        if pos_y < 2:
            possible_moves.append("right")
        return possible_moves

    def execute_move(self, state, move):
        pos_x, pos_y = self.find_blank_coords(state)
        new_state = self.copy(state)

        if move == "up":
            new_state[pos_x][pos_y] = new_state[pos_x - 1][pos_y]
            new_state[pos_x - 1][pos_y] = state[pos_x][pos_y]
        elif move == "down":
            new_state[pos_x][pos_y] = new_state[pos_x + 1][pos_y]
            new_state[pos_x + 1][pos_y] = state[pos_x][pos_y]
        elif move == "left":
            new_state[pos_x][pos_y] = new_state[pos_x][pos_y - 1]
            new_state[pos_x][pos_y - 1] = state[pos_x][pos_y]
        elif move == "right":
            new_state[pos_x][pos_y] = new_state[pos_x][pos_y + 1]
            new_state[pos_x][pos_y + 1] = state[pos_x][pos_y]

        return new_state

    def successor_state_gen(self, state):
        successors = []
        possible_moves = self.get_moves(state)
        for moves in possible_moves:
            successors.append(self.execute_move(state, moves))
        print(successors)

    def find_blank_coords(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 'B':
                    return i, j

    def copy(self, state):
        return [row[:] for row in state]

    def generate_path(self, closed_list):
        path = []
        path.append(closed_list[-1][1])
        current_state = closed_list[-1][1]
        for i in range(len(closed_list) - 1, -1, -1):
            if current_state == closed_list[i][1]:
                continue
            else:
                if current_state in self.successor_state_gen(closed_list[i][1]):
                    print(current_state)
                    path.append(closed_list[i][1])
                    current_state = closed_list[i][1]
        return path