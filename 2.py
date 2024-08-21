# lab 2: Depth first search

#Consder the following graph which is implemented in the code below.
#         5
#       /   \
#     3       7
#   /  \        \
# 2     4 ------ 8   this is a directed graph, arrows are not included but the flow is only on bottom and right.

#Program starts here

graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': [],
}

visited = set()

def dfs(visited, graph, node):
  if node not in visited:
    print(node, end = " ")
    visited.add(node)
    for neighbours in graph[node]:
      dfs(visited, graph, neighbours)

print("Following is the Depth-First Search: ")
dfs(visited, graph, '5')