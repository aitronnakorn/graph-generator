# Status
OK = 0
ERROR = 1

# Configuration Graph for visualization
GRAPH_BASIC_WIDTH = 1
GRAPH_DEGREE_RATIO = 0.5
GRAPH_FONT_RATIO = 8
GRAPH_FONT_COLOR = 'black'
GRAPH_LINE_TYPE = 'bold'

GRAPH_NODE_LEVEL0_LIMIT = 0
GRAPH_NODE_LEVEL1_LIMIT = 3
GRAPH_NODE_LEVEL2_LIMIT = 20

GRAPH_EDGE_LEVEL0_LIMIT = 0
GRAPH_EDGE_LEVEL1_LIMIT = 5
GRAPH_EDGE_LEVEL2_LIMIT = 100
GRAPH_EDGE_LEVEL3_LIMIT = 900

GRAPH_COLOR_LEVEL0 = 'gray'
GRAPH_COLOR_LEVEL1 = 'lightskyblue'
GRAPH_COLOR_LEVEL2 = 'tan1'
GRAPH_COLOR_LEVEL3 = 'crimson'

# Host sending and receiving ARP frame
class Node:
    ip = None
    degree = 0
    def __init__(self,ipstr):
        self.ip = ipstr
    def get_ipstr(self):
        return str(self.ip)

# ARP Request
class RequestEdge:
    src_ip = None
    dst_ip = None
    num = 0
    def __init__(self,src_ipstr,dst_ipstr):
        self.src_ip = src_ipstr
        self.dst_ip = dst_ipstr
    def get_src_ipstr(self):
        return str(self.src_ip)
    def get_dst_ipstr(self):
        return str(self.dst_ip)

# ARP Reply
class ReplyEdge:
    src_ip = None
    dst_ip = None
    num = 0
    def __init__(self,src_ipstr,dst_ipstr):
        self.src_ip = src_ipstr
        self.dst_ip = dst_ipstr
    def get_src_ipstr(self):
        return str(self.src_ip)
    def get_dst_ipstr(self):
        return str(self.dst_ip)

# Host for visulization
# It's a class that contains a node, a width, a color, and a fontsize
class VisualNode:
    node = None
    width = 0
    color = ''
    fontsize = 0
    def __init__(self,node,node_num):
        self.node = node
        self.width = GRAPH_BASIC_WIDTH+(node.degree*GRAPH_DEGREE_RATIO)/node_num
        self.fontsize = self.width*GRAPH_FONT_RATIO
        if node.degree > GRAPH_NODE_LEVEL2_LIMIT:
            self.color = GRAPH_COLOR_LEVEL3
        elif node.degree <= GRAPH_NODE_LEVEL2_LIMIT and node.degree > GRAPH_NODE_LEVEL1_LIMIT:
            self.color = GRAPH_COLOR_LEVEL2
        elif node.degree <= GRAPH_NODE_LEVEL1_LIMIT and node.degree > GRAPH_NODE_LEVEL0_LIMIT:
            self.color = GRAPH_COLOR_LEVEL1
        else:
            self.color = GRAPH_COLOR_LEVEL0

# Edge for visulization
# > This class is used to store the edge and the color of the edge
class VisualEdge:
    edge = None
    color = ''
    def __init__(self,edge):
        self.edge = edge
        if edge.num > GRAPH_EDGE_LEVEL3_LIMIT:
            self.color = GRAPH_COLOR_LEVEL3
        elif edge.num > GRAPH_EDGE_LEVEL2_LIMIT and edge.num <= GRAPH_EDGE_LEVEL3_LIMIT:
            self.color = GRAPH_COLOR_LEVEL2
        elif edge.num > GRAPH_EDGE_LEVEL1_LIMIT and edge.num <= GRAPH_EDGE_LEVEL2_LIMIT:
            self.color = GRAPH_COLOR_LEVEL1
        elif edge.num > GRAPH_EDGE_LEVEL0_LIMIT and edge.num <= GRAPH_EDGE_LEVEL1_LIMIT:
            self.color = GRAPH_COLOR_LEVEL0
