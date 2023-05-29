# written with the least amount of looking at the example code, pretty successfull overall

graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3

graph['d'] = {}
graph['d']['fin'] = 1

graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def smallest_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for x in costs:
        new_cost = costs[x]
        if new_cost < lowest_cost and x not in processed:
            lowest_cost = new_cost
            lowest_cost_node = x
    return lowest_cost_node


node = smallest_node(costs) # get the first smallest node, that's a neighbour to Start
while node is not None:
    current_node_cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        neighbour_cost = current_node_cost + neighbours[n]
        if neighbour_cost < costs[n]:
            costs[n] = neighbour_cost
            parents[n] = node
    processed.append(node)
    node = smallest_node(costs)

print(parents)
print(costs)

