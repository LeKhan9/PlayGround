from data_structures.graph import Graph


def generate_sample_graph(is_directed=False):
    '''
    Will return a graph obj as such, either undirected or directed based on the optional arg:

    undirected

    [A] -> {'B', 'C'}
    [B] -> {'A', 'D', 'E'}
    [C] -> {'A', 'F'}
    [D] -> {'B'}
    [E] -> {'B', 'F'}
    [F] -> {'E', 'C'}

    directed

    [A] -> {'C', 'B'}
    [B] -> {'E', 'D'}
    [C] -> {'F'}
    [E] -> {'F'}
    '''

    graph = Graph(is_directed)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'F')

    return graph
