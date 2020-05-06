from collections import deque
from utils.graph.factory import generate_sample_graph



def dfs(graph, source_node, visited=None):
    if not source_node:
        return

    if not visited:
        visited = set()

    print(source_node, end=' ')
    visited.add(source_node)

    for neighbour in graph.get_neighbours(source_node):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)



def bfs(graph, source_node):
    q = deque()
    visited = {source_node}

    q.append(source_node)

    while q:
        q_size = len(q)

        for _ in range(q_size):
            curr_node = q.popleft()
            print(curr_node, end=' ')

            for neighbour in graph.get_neighbours(curr_node):
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)



def run_example():
    '''
        Runs DFS and BFS with the sample graphs below

    [A] -> {'B', 'C'}
    [B] -> {'A', 'D', 'E'}
    [C] -> {'A', 'F'}
    [D] -> {'B'}
    [E] -> {'B', 'F'}
    [F] -> {'E', 'C'}

    '''

    graph = generate_sample_graph()

    run_dfs(graph)
    run_bfs(graph)



def run_dfs(graph):
    print('\n DFS output:', end=' ')
    dfs(graph, 'A') # A B E F C D




def run_bfs(graph):
    print('\n BFS output:', end=' ')
    bfs(graph, 'A') # A C B F E D




if __name__ == '__main__':
    run_example()
