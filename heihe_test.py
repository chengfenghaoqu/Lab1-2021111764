"""
这是一个模块级别的文档字符串。
它简要描述了模块的目的和功能。
"""
import pytest
from pyword import find_all_bridge_words
from networkx import Graph


# 测试数据准备
@pytest.fixture
def setup_graph():
    """
            这是一个函数级别的文档字符串。
            它描述了函数的功能、参数和返回值。
    """
    graph = Graph()
    graph.add_nodes_from(['word_1', 'word_2', 'bridge_word_1', 'bridge_word_2',
                          'other_word', 'word_3'])
    graph.add_edges_from([('word_1', 'bridge_word_1'), ('word_1', 'bridge_word_2'),
                          ('bridge_word_1', 'word_2'), ('bridge_word_2', 'word_2'),
                          ('bridge_word_1', 'word_3')])
    return graph


def test_find_all_bridge_words(setup_graph):
    """
            这是一个函数级别的文档字符串。
            它描述了函数的功能、参数和返回值。
    """
    # 多个桥接词情况测试
    print()
    result = find_all_bridge_words(setup_graph, 'word_1', 'word_2')
    print(f"Result for 'word_1' -> 'word_2': {result}")
    assert result == ['bridge_word_1', 'bridge_word_2'], "Should return the correct bridge words"

    # 一个桥接词的测试
    result = find_all_bridge_words(setup_graph, 'word_1', 'word_3')
    print(f"Result for 'word_1' -> 'word_2': {result}")
    assert result == ['bridge_word_1'], "Should return the correct bridge words"

    # 没有桥接词的情况测试
    result = find_all_bridge_words(setup_graph, 'word_1', 'other_word')
    print(f"Result for 'word_1' -> 'other_word': {result}")
    assert result is None, "Should return None when there are no bridge words"

    # 一个节点不存在的情况测试
    result = find_all_bridge_words(setup_graph, 'word_1', 'nonexistent_word')
    print(f"Result for 'word_1' -> 'nonexistent_word': {result}")
    assert result is None, "Should return None when one of the nodes does not exist"

    # 两个节点都不存在的情况测试
    result = find_all_bridge_words(setup_graph, 'nonexistent_word_1', 'nonexistent_word_2')
    print(f"Result for 'nonexistent_word_1' -> 'nonexistent_word_2': {result}")
    assert result is None, "Should return None when both nodes do not exist"
