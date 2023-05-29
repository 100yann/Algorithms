# dijkstra's algorithm is used to calculate the shortest path for a weighted graph
# a weighted graph has weights (numbers) assigned to each edge between each node
# it only works when all weights are positive numbers

graph = {}

graph['start'] = {}
graph['start']['a'] = 6 # weight of edge from Start to A is 6
graph['start']['b'] = 2 # weight of edge from Start to B is 2

#print(graph['start'].keys()) # get all neighbours of node start
#print(graph['start']['a'], graph['start']['b']) # get weights of their edges

graph['a'] = {}
graph['a']['fin'] = 1 # weight of edge from A to FIN is 1

graph['b'] = {}
graph['b']['a'] = 3 # weight of edge from B to A is 3
graph['b']['fin'] = 5 # weight of edge from B to FIN is 5

graph['fin'] = {} # the node FIN has no neighbours


# make costs hash table
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity 

# make parents hash table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] # keep track of processed nodes


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for x in neighbors.keys():
        new_cost = cost + neighbors[x]
        if costs[x] > new_cost:
            costs[x] = new_cost
            parents[x] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

