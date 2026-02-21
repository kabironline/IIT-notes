def nearest_neighbour_heuristic(graph, start_node, n):
    unvisited = set(range(n))
    unvisited.remove(start_node)
    tour = [start_node]
    current = start_node
    while unvisited:
        nxt = min(unvisited, key=lambda j: graph[current][j])
        unvisited.remove(nxt)
        tour.append(nxt)
        current = nxt
    return tour  # path representation (zero-based, length N)

def get_inputs():
    v = input()
    no_of_inputs = int(input())
    locations = []
    distance_matrix = []
    def fix_dataType(n):
        return float(n)
    for _ in range(no_of_inputs):
        locations.append(list(map(fix_dataType, input().split(' '))))
    for _ in range(no_of_inputs):
        distance_matrix.append(list(map(fix_dataType, input().split(' '))))
    return {
        'no_of_cities': no_of_inputs,
        'distance_type': v,
        'locations': locations,
        'distance_matrix': distance_matrix
    }

def main():
    inputs = get_inputs()
    n = inputs['no_of_cities']
    dist = inputs['distance_matrix']
    tour = nearest_neighbour_heuristic(dist, start_node=0, n=n)
    print(*tour)  # exactly one line, one tour

if __name__ == "__main__":
    main()