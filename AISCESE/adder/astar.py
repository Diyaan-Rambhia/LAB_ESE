import heapq

start = (1,2,3,4,0,6,7,5,8)
goal  = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    h = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            r1, c1 = i//3, i%3
            r2, c2 = goal_pos//3, goal_pos%3

            h += abs(r1-r2) + abs(c1-c2)

    return h

def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        zero = state.index(0)
        r, c = zero//3, zero%3

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr, dc in moves:
            nr, nc = r+dr, c+dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr*3 + nc

                new_state = list(state)
                new_state[zero], new_state[new_pos] = \
                    new_state[new_pos], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    new_g = g+1
                    new_f = new_g + heuristic(new_state)

                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state, path+[state])
                    )

    return None

solution = astar(start)

if solution:
    print("Solution found:")
    for state in solution:
        for i in range(0,9,3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
