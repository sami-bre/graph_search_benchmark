from graph import Graph
from math import radians,sqrt,sin,cos,atan2

graph = Graph()


print("\nAdding nodes a, b, c, d, e, f")
for item in ['a', 'b', 'c', 'd', 'e', 'f']:
    graph.addNode(item)

graph.show()

graph.addEdge('', 'b')
graph.addEdge('b', 'a')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('a', 'd')
graph.addEdge('d', 'e')
graph.addEdge('b', 'e')
graph.addEdge('c', 'e')

graph.aStarSearch("a","e")

print(f"\ndoes node a exist? : {graph.nodeExists('a')}")
print(f"does node z exist? : {graph.nodeExists('z')}")

print("""\n
after:
graph.addEdge('a', 'b')
graph.addEdge('b', 'a')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('a', 'd')
graph.addEdge('d', 'e')
graph.addEdge('b', 'e')
graph.addEdge('c', 'e')
\n""")
      
graph.show()

graph.addUndirectedEdge('e', 'f')

print("""\n
after:
graph.addUndirectedEdge('e', 'f')
\n""")
      
graph.show()

try:
    print("\nTrying to add an existing edge ... ")
    graph.addEdge('a', 'b') # this should throw an exception
except Exception as e:
    print(e)

graph.deleteNode('f')

print("""\n
after:
graph.deleteNode('f')
\n""")

graph.show()

graph.deleteEdge('d', 'e')

print("""\n
after:
graph.deleteEdge('d', 'e')
\n""")

graph.show()

try:
    print("\nTrying to delete an edge from d to e (again, now it doesn't exist) ... ")
    graph.deleteEdge('d', 'e')
except Exception as e:
    print(e)

try:
    print("\nTrying to delete an edge from z to e ... ")
    graph.deleteEdge('z', 'e')
except Exception as e:
    print(e)

try:
    print("\nTrying to delete an edge from a to z ... ")
    graph.deleteEdge('a', 'z')
except Exception as e:
    print(e)

graph.deleteUndirectedEdge('a', 'b')

print("""\n
after:
graph.deleteUndirectedEdge('a', 'b')
\n""")

graph.show()

                
def haversine_distance(node, goal):
        romania_coordinates : dict[str, tuple[float, float]] = {
                            "Arad": (46.18656, 21.31227),
                            "Bucharest": (44.42676, 26.10254),
                            "Craiova": (44.31813, 23.80450),
                            "Drobeta": (44.62524, 22.65608),
                            "Eforie": (44.06562, 28.63361),
                            "Fagaras": (45.84164, 24.97264),
                            "Giurgiu": (43.90371, 25.96993),
                            "Hirsova": (44.68935, 27.94566),
                            "Iasi": (47.15845, 27.60144),
                            "Lugoj": (45.69099, 21.90346),
                            "Mehadia": (44.90411, 22.36452),
                            "Neamt": (46.97587, 26.38188),
                            "Oradea": (47.05788, 21.94140),
                            "Pitesti": (44.85648, 24.86918),
                            "Rimnicu Vilcea": (45.10000, 24.36667),
                            "Sibiu": (45.79833, 24.12558),
                            "Timisoara": (45.75972, 21.22361),
                            "Urziceni": (44.71667, 26.63333),
                            "Vaslui": (46.64069, 27.72765),
                            "Zerind": (46.62251, 21.51742)
                        }
        latitude_1, longitude_1 = romania_coordinates[node]
        latitude_2, longitude_2 = romania_coordinates[goal]
        
        # Convert latitudes and longitudes from degrees to radians
        latitude_1_rad, longitude_1_rad = radians(latitude_1), radians(longitude_1)
        latitude_2_rad, longitude_2_rad = radians(latitude_2), radians(longitude_2)

        # Haversine formula 
        distance_latitude = latitude_2_rad - latitude_1_rad 
        distance_longitude = longitude_2_rad - longitude_1_rad 
        a = sin(distance_latitude / 2)**2 + cos(latitude_1_rad) * cos(latitude_2_rad) * sin(distance_longitude / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a)) 

         # Earth's radius in kilometers
        R = 6371

        # Distance in kilometers
        distance = R * c

        return distance