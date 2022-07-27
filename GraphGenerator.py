from Graph import *
import dpkt
import socket

# Generate graph: Vertices and Edges
def construct_graph(pcappath):
    # Declare variables
    req_edge_dict = dict()
    rep_edge_dict = dict()
    node_dict = dict()
    with open(pcappath, 'rb') as f:
        # Load pcap records
        try:
            pcap = dpkt.pcap.Reader(f)
        except Exception as e:
            print("Error in GraphGenerator/construct_graph " + pcappath + ": 0" + str(e))
            return ERROR,None,None
        # Deal with ARP packets
        try:
            for ts, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)
                if eth.type != 2054:
                    continue
                try:
                    arp = eth.arp
                except Exception as e:
                    print("Error in GraphGenerator/construct_graph " + pcappath + ": 1" + str(e))
                    continue
                src_ipstr = socket.inet_ntoa(arp.spa)
                dst_ipstr = socket.inet_ntoa(arp.tpa)
                type = arp.op

                # Construct edges
                if type == 1:
                    req_edge_dict[(src_ipstr, dst_ipstr)] = \
                        req_edge_dict.setdefault((src_ipstr, dst_ipstr), RequestEdge(src_ipstr, dst_ipstr))
                    req_edge_dict[(src_ipstr, dst_ipstr)].num += 1
                if type == 2:#
                    rep_edge_dict[(src_ipstr, dst_ipstr)] = \
                        rep_edge_dict.setdefault((src_ipstr, dst_ipstr), ReplyEdge(src_ipstr, dst_ipstr))
                    rep_edge_dict[(src_ipstr, dst_ipstr)].num += 1
        except Exception as e:
            print("Error in GraphGenerator/construct_graph " + pcappath + ": 2" + str(e))
            #return ERROR,None,None
        # Construct nodes based on edges
        for key in req_edge_dict:
            req_edge = req_edge_dict[key]
            src_ipstr = req_edge.get_src_ipstr()
            dst_ipstr = req_edge.get_dst_ipstr()
            node_dict[src_ipstr] = node_dict.setdefault(src_ipstr,Node(src_ipstr))
            node_dict[src_ipstr].degree += 1
            if dst_ipstr not in node_dict:
                new_node = Node(dst_ipstr)
                node_dict[dst_ipstr] = new_node
    return OK,node_dict,req_edge_dict
