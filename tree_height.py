# python3

import sys
import threading
import numpy

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
class TreeBuilder:

     def __init__(self):
         self.n = 0
         self.parent = []
         self.cache = []

     def read(self):
         print("Please insert number of nodes (n): ")
         self.n = int(sys.stdin.readline())
         print("Please insert nodes: ")
         self.parent = list(map(int, sys.stdin.readline().split()))
         self.cache = [0] * self.n

     def path_len(self, node_id):
         parent = self.parent[node_id]
         if parent == -1:
             return 1

         if self.cache[node_id]:
             return self.cache[node_id]

         self.cache[node_id] = 1 + self.path_len(self.parent[node_id])
         return self.cache[node_id]

     def compute_height(self):
         return max([self.path_len(i) for i in range(self.n)])

def main():
     readData()

def readData():
     tree = TreeBuilder()
     tree.read()
     print('Height of the tree is:', tree.compute_height())
     readData()

threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))