import helper
from strategy import UCS, IDS

N, adj, goal = helper.input('input1.txt')

list_expanded, path, res = UCS(N, adj, goal)
print(list_expanded, path, res)
