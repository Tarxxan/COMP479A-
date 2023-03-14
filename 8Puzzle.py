from time import sleep

from EightPuzz import EightPuzz
from Heuristics import Heuristics


def depth_first(puzzle):
    i = 0
    open_list = []
    closed_list = []
    start_state = puzzle.initial_state

    open_list = [start_state]

    while open_list:
        #         Replicates stack by popping last element put into list
        current_state = open_list.pop()

        if current_state == puzzle.goal_state:
            return i, current_state, "closed_list " + str(len(closed_list))

        else:
            for moves in puzzle.get_moves(current_state):
                successor_state = puzzle.execute_move(current_state, moves)
                closed_list.append(current_state)

                if successor_state not in closed_list and successor_state not in open_list:
                    open_list.append(successor_state)
        i = i + 1
    return None


def breadth_first(puzzle):
    i = 0
    open_list = []
    closed_list = []
    start_state = puzzle.initial_state

    open_list = [start_state]

    while open_list:
        #         Takes first element in the list.
        current_state = open_list.pop(0)

        if current_state == puzzle.goal_state:
            return i, current_state, "closed_list" + str(len(closed_list))

        else:
            for moves in puzzle.get_moves(current_state):
                successor_state = puzzle.execute_move(current_state, moves)
                closed_list.append(current_state)

                if successor_state not in closed_list and successor_state not in open_list:
                    open_list.append(successor_state)
        i = i + 1
    return None


# Uses heuristics so i will default it to hamming distance
def best_first(puzzle, heuristics):
    i = 0
    open_list = []
    closed_list = []
    start_state = puzzle.initial_state
    open_list = [tuple([1, start_state])]

    while open_list:
        open_list = sorted(open_list, key=lambda tup: tup[0])
        print(open_list)
        current_state_t = open_list.pop(0)

        current_state = current_state_t[1]

        if current_state == puzzle.goal_state:
            puzzle.closed_list = closed_list
            return current_state_t, "closed_list " + str(len(closed_list))
        else:

            for moves in puzzle.get_moves(current_state):
                successor = puzzle.execute_move(current_state, moves)

                match heuristics:
                    case "hamming_distance":
                        successor_states = Heuristics.hamming_distance(puzzle, successor)
                    case "manhattan_distance":
                        successor_states = Heuristics.manhattan_distance(puzzle, successor)
                    case "permutation_distance":
                        successor_states = Heuristics.permutation_distance(puzzle, successor)
                    case "inversion_manhattan":
                        successor_states = Heuristics.inversion_manhattan(puzzle, successor)
                    case _:
                        successor_states = Heuristics.hamming_distance(puzzle, successor)

                if successor_states not in closed_list and successor_states not in open_list:
                    open_list.append(successor_states)
            closed_list.append(current_state_t)
    return None


def a_star(puzzle, heuristics):
    closed_list = []
    start_state = puzzle.initial_state
    open_list = [tuple([1, start_state, 0])]

    while open_list:
        open_list = sorted(open_list, key=lambda tup: tup[0])
        current_state_t = open_list.pop(0)

        current_state = current_state_t[1]
        depth = current_state_t[2]

        if current_state == puzzle.goal_state:
            puzzle.closed_list = closed_list
            return current_state_t


        else:
            execute = True
            for moves in puzzle.get_moves(current_state):
                state = puzzle.execute_move(current_state, moves)
                match heuristics:
                    case "hamming_distance":
                        successor_state = Heuristics.hamming_distance(puzzle, state)
                    case "manhattan_distance":
                        successor_state = Heuristics.manhattan_distance(puzzle, state)
                    case "permutation_distance":
                        successor_state = Heuristics.permutation_distance(puzzle, state)
                    case "inversion_manhattan":
                        successor_state = Heuristics.inversion_manhattan(puzzle, state)
                    case _:
                        successor_state = Heuristics.hamming_distance(puzzle, current_state)

                successor_state = tuple([(successor_state[0] + depth + 1), successor_state[1], depth + 1])

                if not closed_list:
                    open_list.append(successor_state)

                #     remove closed states that have a higher cost
                to_remove = []
                for closed in closed_list:
                    if closed[1] == successor_state[1] and closed[0] > successor_state[0]:
                        open_list.append(successor_state)
                        to_remove.append(closed)

                temp_open_list = open_list[:]
                for expanded in temp_open_list:
                    if expanded[1] == successor_state[1] and expanded[0] > successor_state[0]:
                        open_list.remove(expanded)
                        # print(expanded in open_list)
                        open_list.append(successor_state)
                        execute = False
                        break
                if execute:
                    open_list.append(successor_state)
        closed_list.append(current_state_t)
    return None


initial_state = [['B', 4, 5], [3, 1, 2], [7, 8, 6]]
# initial_state = [[1,2,3],[4,5,6],[7,8,'B']]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

puzzle = EightPuzz(initial_state, goal_state)
print(best_first(puzzle, "inversion_manhattan"))
# print(a_star(puzzle, "inversion_manhattan"))
print(len(puzzle.closed_list))
