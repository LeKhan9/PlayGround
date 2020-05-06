from collections import defaultdict

class NodeNotFoundException(Exception):
    pass

class Graph:
    def __init__(self, is_directed=False):
        self.graph = defaultdict(set)
        self.is_directed = is_directed

    def add_edge(self, source, sink):
        self.graph[source].add(sink)

        if not self.is_directed:
            self.graph[sink].add(source)

    def get_neighbours(self, node):
        if node not in self.graph:
            raise NodeNotFoundException('Node is not in graph')

        return self.graph.get(node, {})

    def remove_edge(self, source, sink):
        self._remove_edge(source, sink)

        if not self.is_directed:
            self._remove_edge(sink, source)

    def _remove_edge(self, source, sink):
        if source not in self.graph:
            raise NodeNotFoundException('Source node is not in graph')

        if sink not in self.graph[source]:
            raise NodeNotFoundException('Sink node is not in graph')

        self.graph[source].remove(sink)

    def __str__(self):
        visual_str = ''
        for source, neighbours in self.graph.items():
            visual_str += f'[{source}] -> {neighbours}\n'

        return visual_str
