from Graph import *
import os

prefixDots = './files/dots/'
prefixImages = './files/images/'

# Visualize ARP frames
def visualize(node_dict, req_edge_dict, fileName):
    stat, dotfile = write_dotfile(node_dict, req_edge_dict, fileName)
    if stat == ERROR:
        return ERROR, None
    stat, pngfile = generate_png_file(dotfile, fileName)
    if stat == ERROR:
        return ERROR, None
    return OK, pngfile


# Write graph visualization info to dot file
def write_dotfile(node_dict,req_edge_dict, fileName):
    dotfile = prefixDots + fileName + '.dot'
    try:
        dotf = open(dotfile, 'w')
    except Exception as e:
        return ERROR,None
    write_basic_attributes(dotf)
    node_num = len(node_dict)
    for key in node_dict:
        node = node_dict[key]
        vnode = VisualNode(node, node_num)
        write_node(dotf, vnode)
    for key in req_edge_dict:
        edge = req_edge_dict[key]
        vedge = VisualEdge(edge)
        write_edge(dotf, vedge)
    dotf.write('}')
    return OK,dotfile


# Write basic visualization attributes to dot file
def write_basic_attributes(dotf):
    dotf.write('digraph g{\n')
    dotf.write('graph [bgcolor=white, overlap=scale]\n')
    dotf.write(
        'node [fixedsize=true, shape=circle, fillcolor=gray, width=0.5, height=0.5, fontsize=10, style=filled, labelfloat=true]\n')
    dotf.write('edge [len=10,splines=line,color=white,arrowhead=vee]\n')


# Write node info to dot file
def write_node(dotf,vnode):
    dotf.write('\t"{0}" [width={1},height={2},fillcolor={3},fontcolor={4},fontsize={5}]\n'
                  .format(vnode.node.get_ipstr(), vnode.width, vnode.width, vnode.color, GRAPH_FONT_COLOR, vnode.fontsize))


# Write edge info to dot file
def write_edge(dotf,vedge):
    dotf.write(
        '\t"{0}"->"{1}"[color={2}, style={3}];\n'.format(vedge.edge.get_src_ipstr(), vedge.edge.get_dst_ipstr(), vedge.color, GRAPH_LINE_TYPE))

# Generate visulization png file
def generate_png_file(dotfile, fileName):
    pngfile = prefixImages + fileName + '.png'
    command = "dot -Ksfdp " + dotfile + " -T png -o " + pngfile
    # print(command)
    try:
        os.system(command)
    except Exception as e:
        return ERROR,None
    return OK, pngfile
