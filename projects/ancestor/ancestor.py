
from queue import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Initialize a graph
    graph = Graph()
    # build a graph of the parents and children
    # Iterate over ancestors' tuple (parent, child)
    for parent, child in ancestors:

        # check if the parent is not in the vertices
        if parent not in graph.vertices:

            # Add parent to the graph vertices
            graph.add_vertex(parent)
        # check if the child is not in the vertices
        if child not in graph.vertices:
            # Add parent to the graph vertices
            graph.add_vertex(child)
        
        # Create an edge of child and parent
        graph.add_edge(child,parent)

    # Apply BFS

    # Initialize a queue
    q = Queue()
    # enqueue the starting_node
    q.enqueue(starting_node)
    # Initialize a visited set
    visited = set()
    # Set the earliest_ancestor to None
    earliest_ancestor = None
    # While the queue is not empty
    while q.size() > 0:
        # Assign the head to the earliest_ancestor
        earliest_ancestor = q.dequeue()
        # Check if the earliest_ancestor has not been visited
        if earliest_ancestor not in visited:

            # If not visited,get the neighbors
            neighbors = graph.get_neighbors(earliest_ancestor)

            # Iterate the neighbors and enqueue
            for neighbor in neighbors:
                q.enqueue(neighbor)
            
            # Add the earliest_ancestor to the visited
            visited.add(earliest_ancestor)

    # If the earliest_ancestor at this point is still the starting_node, yeye dey smell
    if earliest_ancestor == starting_node:
        # Return -1
        return -1
    else:
        # Return the earliest_ancestor
        return earliest_ancestor   