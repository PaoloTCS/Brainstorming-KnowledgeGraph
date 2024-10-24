import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from knowledge_node import KnowledgeNode
from datetime import datetime

def test_similarity_score():
    node1 = KnowledgeNode(id="A", content="Node A", metadata={}, compression_level=0.8, creator="User1", timestamp=datetime.now(), level=1)
    node2 = KnowledgeNode(id="B", content="Node B", metadata={}, compression_level=0.8, creator="User2", timestamp=datetime.now(), level=1)
    score = node1.similarity_score(node2)
    assert 0.0 <= score <= 1.0  # Placeholder check for similarity range

