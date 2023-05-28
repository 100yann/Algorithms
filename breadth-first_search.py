from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque() # create a new queue
    search_queue += graph['you'] # add all values in key 'you' to the search queue
    searched = [] # keep a list of people searched to avoid searching them twice
    while search_queue: # while the queue isn't empty
        person = search_queue.popleft() # grabs the first item off the queue
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a seller!')
                return True    
            else:
                search_queue += graph[person] # add the second-degree connections to the queue of this first-degree connection
                searched.append(person) # add the person to the search list
    return False # if you reach here - no one is a seller

print(search(graph['you']))

'''Running time - O(V+E) where V is number of vertices, E is number of edges'''