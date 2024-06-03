#增加注释
#对Lab1进行修改
import networkx as nx  
import matplotlib.pyplot as plt  
import re  
from collections import defaultdict  
import random  


def read_text_and_create_graph(file_path):
    G = nx.DiGraph()  
    text = open(file_path, 'r', encoding='utf-8').read()  
    words = re.findall(r'\b\w+\b', text)  
      
    # 使用滑动窗口来构建词对关系  
    for i in range(len(words) - 1):  
        G.add_edge(words[i], words[i + 1])
    return G  


def print_graph(G):  
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, font_weight='bold')  
    plt.show()


def find_all_bridge_words(G, word1, word2):
    if not G.has_node(word1) or not G.has_node(word2):
        return None

    bridge_words = []  # 创建一个空列表来存储桥接词
    # 遍历word1的邻居节点
    for neighbor in G.neighbors(word1):
        # 检查该邻居节点是否有指向word2的边
        if G.has_edge(neighbor, word2):
            bridge_words.append(neighbor)  # 将桥接词添加到列表中

    if bridge_words:
        return bridge_words  # 返回桥接词列表
    else:
        return None  # 没有找到满足条件的桥接词


def insert_bridge_words_in_text(G, text):
    words = text.split()  # 将新文本分割成单词列表
    new_text = []  # 用于存储插入桥接词后的单词列表

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]

        # 检查图中是否存在word1和word2之间的桥接词
        bridge_words = find_all_bridge_words(G, word1, word2)

        # 如果有桥接词，则随机选择一个插入
        if bridge_words:
            random_bridge_word = random.choice(bridge_words)
            new_text.append(word1)
            new_text.append(random_bridge_word)
        else:
            new_text.append(word1)

            # 添加最后一个单词，因为它后面没有跟随的单词了
    new_text.append(words[-1])

    return ' '.join(new_text)  # 将单词列表重新组合成字符串并返回

def shortest_path_length(G, word1, word2):
    if not G.has_node(word1) or not G.has_node(word2):
        return None
    try:
        for c in nx.shortest_path(G, source=word1, target=word2):
            print(f"{c}->")
        return len(nx.shortest_path(G, source=word1, target=word2)) - 1  
    except nx.NetworkXNoPath:  
        return None


def random_walk(G):
    path = []
    edges = set()
    node = random.choice(list(G.nodes()))
    path.append(node)

    while G.out_degree(node) > 0:
        neighbors = list(G.neighbors(node))
        next_node = random.choice(neighbors)
        edge = (node, next_node)

        edges.add(edge)
        path.append(next_node)
        node = next_node

        #检查有向边是否已经访问过
        if edge in edges:
            break

        # 将遍历的节点写入文件
    with open('random_walk_path.txt', 'w') as f:
        for node in path:
            f.write(str(node) + '\n')

    return path


# 从文本中读取数据并创建有向图  
G = read_text_and_create_graph('example.txt')
# 打印图结构  
print_graph(G)
# 找到两个词之间的桥接词
word1 = input("word1:")
word2 = input("word2:")
# 检查word1和word2是否在图中
if not G.has_node(word1) or not G.has_node(word2):
    print(f"No '{word1}' or '{word2}' in the graph!")
else:
    bridge_words_list = find_all_bridge_words(G, word1, word2)
    if bridge_words_list:
        print(f"The bridge words between '{word1}' and '{word2}' are: ")
        for bridge_word in bridge_words_list:
            print(f"{bridge_word}")
    else:
        print(f"No bridge words from '{word1}'to '{word2}'!")

# 插入桥接词到新文本中并打印
new_text = input("new_text:")
new_text_with_bridge = insert_bridge_words_in_text(G,new_text)
print(f"New text with bridge word: {new_text_with_bridge}")

# 计算两个单词之间的最短路径长度
word3=input("word3:")
word4=input("word4:")
path_length = shortest_path_length(G, word3, word4)
if path_length is not None:
    print(f"Shortest path length between '{word3}' and '{word4}': {path_length}")
else:
    print(f"No way from '{word3}' to '{word4}'!")

# 进行随机游走并打印路径
random_path = random_walk(G)
print(f"Random walk path: {random_path}")
