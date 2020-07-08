from data_structures.graph import Graph
from collections import deque

PERSON_INDEX = 0
START_LEVEL = 0
DIST_INDEX = 1

def find_friend_of_k_distance(graph, source, k):
    '''
        Given an undirected network of friends, for a given person, find friends that are k hops away in terms of relation
    '''

    q = deque()
    visited = set()

    start_level = START_LEVEL

    q.append((source, start_level))
    visited.add(source)

    while q:
        q_size = len(q)

        for _ in range(q_size):
            if q[PERSON_INDEX][DIST_INDEX] == k:
                return [name for name, dist in q]

            person, level = q.popleft()

            for friend in graph.get_neighbours(person):
                if friend not in visited:
                    visited.add(friend)
                    q.append((friend, level + 1))

    return []



def generate_sample_friend_network():
    graph = Graph()

    graph.add_edge('Alex', 'Bob')
    graph.add_edge('Bob', 'Dan')
    graph.add_edge('Bob', 'Charlie')
    graph.add_edge('Charlie', 'Elsa')
    graph.add_edge('Elsa', 'Genna')

    return graph



def run_example():
    graph = generate_sample_friend_network()

    test_cases = [('Genna', 3), ('Alex', 2), ('Bob', 1)]

    for person, dist in test_cases:
        print(f'Friends that are {dist} distance from {person} => {find_friend_of_k_distance(graph, person, dist)}')

    '''
        Friends that are 3 distance from Genna => ['Bob']
        Friends that are 2 distance from Alex => ['Dan', 'Charlie']
        Friends that are 1 distance from Bob => ['Dan', 'Charlie', 'Alex']
    '''



if __name__ == '__main__':
    run_example()
