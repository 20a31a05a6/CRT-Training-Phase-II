#merge Sorting

def merge_sort(arr,left,right):
    pass




def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left_arr=[i for i arr[1:] if i<=pivot]
    right_arr=[i for i arr[1:] if i>pivot]
    return quick_sort(left_arr) +pivot+ quick_sort(right_arr)

arr=[30,10,20,70,40,20,90]

res=quick_sort(arr)
print(res)


#Breadth First Search (BFS) using Level Order algorithm(undirected graph)
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
graph={
    '5':['3','7','9'],
    '3':['2','4'],
    '7':['8'],
    '2':['4'],
    '4':['8'],
    '8':[],
    '9':['2','8'],
    }
visited=[]
queue=[]
bfs(visited,graph,'5')
              
#depth first search alogorithm
# Define a graph as a dictionary of lists
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # Create a set to store visited nodes

def dfs(node):
    """Performs depth-first search (DFS) starting from the given node."""
    if node not in visited:
        print(node, end=' ')  # Print the current node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)  # Recursively call dfs on the neighbor nodes

# Perform DFS starting from node 'A'
dfs('A')

