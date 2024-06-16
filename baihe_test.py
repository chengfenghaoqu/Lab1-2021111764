import networkx as nx
import pytest

# 导入函数
from pyword import shortest_path_length


def test_path_exists():
    graph = nx.DiGraph()
    graph.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
    graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])
    assert shortest_path_length(graph, 'A', 'E') == 4


def test_no_path_exists():
    graph = nx.DiGraph()
    graph.add_node('A')
    graph.add_node('B')
    assert shortest_path_length(graph, 'A', 'B') is None


def test_word_not_in_graph():
    graph = nx.DiGraph()
    graph.add_node('A')
    graph.add_node('B')
    assert shortest_path_length(graph, 'A', 'C') is None
