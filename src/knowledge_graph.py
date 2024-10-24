import networkx as nx
from typing import Dict

class KnowledgeGraph:
    def __init__(self, contributor_id: str):
        self.graph = nx.DiGraph()
        self.contributor_id = contributor_id

    def add_node(self, node):
        self.graph.add_node(node.id, data=node)

    def add_edge(self, source_id, target_id, relation_type):
        self.graph.add_edge(source_id, target_id, relation=relation_type)

    def get_path_signatures(self, source_id, target_id):
        """Retrieve path signatures between two nodes"""
        try:
            return list(nx.all_simple_paths(self.graph, source=source_id, target=target_id))
        except nx.NetworkXNoPath:
            return []
