# -*- coding: utf-8 -*-
"""bias_celebrity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/176j8UNhnlJnBs9V5RGOQipmTK7Wm8wR6
"""

# Commented out IPython magic to ensure Python compatibility.
# Load the Drive helper and mount
from google.colab import drive

# This will prompt for authorization.
drive.mount('/content/Drive')

# %cd "Drive/My Drive/MLN project/"
!ls

!pip install python-igraph

import igraph
import networkx as nx

graph = g = nx.read_edgelist("input.txt", nodetype = int)
g = igraph.Graph(directed = False)
g.add_vertices(len(graph.nodes()))
g.add_edges(graph.edges)

communities = g.community_multilevel() # louvain
print ("Louvain")
print (communities)
communities = g.community_walktrap().as_clustering() # walktrap
print ("Walktrap")
print (communities)
communities = g.community_infomap() # infomap
print ("Infomap")
print (communities)
communities = g.community_label_propagation() # label propagation
print ("Labprop")
print (communities)

nx.draw(graph, with_labels = True)