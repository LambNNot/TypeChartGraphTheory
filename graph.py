from pyvis.network import Network
from typechart_data import PKMN_WEAKNESSES, PKMN_RESISTANCES, PKMN_IMMUNITIES
import networkx as nx

NODE_ID = -1

def get_new_node_id() -> int:
    global NODE_ID
    NODE_ID += 1
    return NODE_ID

def nx_convert(graph: nx.DiGraph) -> Network:
    pos = nx.circular_layout(graph, scale = 500)

    network = Network(directed=True, height="750px", width="100%", bgcolor="#222222", font_color="white")
    for node in graph.nodes:
        network.add_node(node, x = pos[node][0], y = pos[node][1], physics=False, color="white")
    
    return network

def add_weakness_edge(graph: Network, source: str, target: str):    
   graph.add_edge(
        source,
        target,
        color='orange',
        width=3,
        smooth={'type': 'curvedCW', 'roundness': 0.1},
        label='2x'
    )

def add_resistance_edge(graph: Network, source: str, target: str):    
   graph.add_edge(
       source,
       target,
       color='lightblue',
       width=3,
       smooth={'type': 'curvedCW', 'roundness': 0.1},
       label='1/2x'
    )
   
def display_nx(nx_graph: nx.DiGraph) -> None:

    # Convert to pyvis
    graph = nx_convert(nx_graph)
    graph.from_nx(nx_graph)

    # Style
    graph.edges = [] # Clears unstyled edges

    for edge in nx_graph.edges(data=True):
        source, target, attributes = edge
        group = attributes.get('group')

        if group == 'weakness':
            add_weakness_edge(graph, source, target)
        elif group == 'resistance':
            add_resistance_edge(graph, source, target)

    # Display
    graph.toggle_physics(False)
    graph.show('typechart.html', notebook=False)


if __name__ == "__main__":
    # Init graph
    nx_graph = nx.DiGraph()

    # Init nodes
    types = sorted(
        list(PKMN_WEAKNESSES.keys())
    )

    # Init edges
    for type in types:
        nx_graph.add_edges_from(
            [(weakness, type) for weakness in PKMN_WEAKNESSES[type]],
            group='weakness'
        )
        nx_graph.add_edges_from(
            [(type, resistance) for resistance in PKMN_RESISTANCES[type]],
            group="resistance"
        )

    # Display
    display_nx(nx_graph)