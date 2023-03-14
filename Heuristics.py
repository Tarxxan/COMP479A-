class Heuristics:

    @staticmethod
    def hamming_distance(puzzle, successor):

        distance = 0
        for i in range(3):
            for j in range(3):
                if successor[i][j] != puzzle.goal_state[i][j]:
                    distance += 1
        return tuple([distance, successor])

    @staticmethod
    def manhattan_distance(puzzle, successor):
        distance = 0
        for i in range(3):
            for j in range(3):
                if successor[i][j] != 'B':
                    goal_row = (successor[i][j] - 1) // 3
                    goal_col = (successor[i][j] - 1) % 3
                else:
                    goal_row = 2
                    goal_col = 2
                distance += (abs(i - goal_row) + abs(j - goal_col))
        return tuple([distance, successor])

    @staticmethod
    def permutation_distance(puzzle, successor):

        distance = 0
        flattened = [element for sublist in successor for element in sublist]
        for i in range(9):
            for j in range(i + 1, 9):
                if flattened[i] == 'B':
                    distance += 1
                elif flattened[j] != 'B' and flattened[i] > flattened[j]:
                    distance += 1
        return tuple([distance, successor])
    @staticmethod
    def getInvCount(current_state):
        inversions = 0
        flattened = [element for sublist in current_state for element in sublist]
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if flattened[i] != 'B' and flattened[j] != 'B' and flattened[i] > flattened[j]:
                    inversions += 1
        return inversions

    @staticmethod
    def inversion_manhattan(puzzle, successor):
        distance = 0
        for i in range(3):
            for j in range(3):
                if successor[i][j] != 'B':
                    goal_row = (successor[i][j] - 1) // 3
                    goal_col = (successor[i][j] - 1) % 3
                else:
                    goal_row = 2
                    goal_col = 2
                distance += (abs(i - goal_row) + abs(j - goal_col))
            distance += Heuristics.getInvCount(successor)
        return tuple([distance, successor])


