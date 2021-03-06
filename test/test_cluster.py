from hw2skeleton import cluster
from hw2skeleton import io
import os

def test_similarity():
    filename_a = os.path.join("data", "276.pdb")
    filename_b = os.path.join("data", "276.pdb")

    activesite_a = io.read_active_site(filename_a)
    activesite_b = io.read_active_site(filename_b)

    assert cluster.findDistance([activesite_a], [activesite_b]) == 0.0

def test_partition_clustering():
    # tractable subset
    pdb_ids = [276, 276, 10701, 10701]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    assert cluster.cluster_by_partitioning(active_sites,2) == [[10701, 10701], [276, 276]] or [[276, 276], [10701, 10701]]

def test_hierarchical_clustering():
    # tractable subset
    pdb_ids = [276, 276, 10701, 10701]

    active_sites = []
    for id in pdb_ids:
        filepath = os.path.join("data", "%i.pdb"%id)
        active_sites.append(io.read_active_site(filepath))
    assert cluster.cluster_hierarchically(active_sites,2) == [[10701, 10701], [276, 276]] or [[276, 276], [10701, 10701]]