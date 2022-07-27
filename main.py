import sys
from GraphGenerator import construct_graph
from Visualization import *

status_map = {0: "OK", 1: "ERROR"}

def main(fileName):
  # fileName = 'a004_20220201_000002'
  status, V, E = construct_graph('./files/pcaps/'+fileName+'.pcap')
  # print(status_map[status])
  # print(V)
  # print(E)
  status, pngPath = visualize(V, E, fileName)
  print('Generate connected graph image to ',pngPath,': [',status_map[status],']')

if __name__ == '__main__':
  fileName = str(sys.argv[1])
  main(fileName)