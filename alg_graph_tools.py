class Node:

    def __init__(self, adj_list : list, name : str) -> None:
        self.name = name
        self.color = 0
        self.parent = None
        self.adj = adj_list
    
    def __str__(self) -> str:
        return f"Node({self.name}): {self.parent = }, {self.adj = }"

    def __repr__(self) -> str:
        return self.__str__()

def create_graph(adj_list : list) -> list:
    new_list = []
    for i,n in enumerate(adj_list):
        new_list.append(Node(n, str(i)))
    for node in new_list:
        node.adj = [new_list[n] for n in node.adj]
    return new_list