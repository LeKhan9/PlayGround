from collections import deque

'''
    Given an array where each index represents a room and all values at that index represent keys to other rooms, 
    these algos determine if all rooms are visitable when the start of the journey is the first room. 
    Both DFS and BFS methods are presented here.
'''

START_ROOM_INDEX = 0

def can_visit_all_rooms_dfs(room_arr):
    number_of_rooms = len(room_arr)

    starting_room = START_ROOM_INDEX
    visited = set()

    return dfs(room_arr, starting_room, visited, number_of_rooms)

def dfs(room_arr, curr_room, visited, number_of_rooms):
    visited.add(curr_room)

    if len(visited) == number_of_rooms:
        return True

    for next_room in room_arr[curr_room]:
        if next_room not in visited:
            if dfs(room_arr, next_room, visited, number_of_rooms):
                return True

    return False


def can_visit_all_rooms_bfs(room_arr):
    number_of_rooms = len(room_arr)

    q = deque()
    seen = set()

    q.append(START_ROOM_INDEX)
    seen.add(START_ROOM_INDEX)

    while q:
        curr_room = q.popleft()

        for key in room_arr[curr_room]:
            if key not in seen:
                seen.add(key)
                q.append(key)

                if len(seen) == number_of_rooms:
                    return True

    return len(seen) == number_of_rooms



def run_example():
    test_cases = [
        [[1, 3], [3, 0, 1], [2], [0]], # false
        [[1], [2], [3], []] # true
    ]

    for test_case in test_cases:
        print(f'DFS solution for {test_case} => {can_visit_all_rooms_dfs(test_case)}')
        print(f'BFS solution for {test_case} => {can_visit_all_rooms_bfs(test_case)}\n')


if __name__ == '__main__':
    run_example()
