# -*- coding: utf-8 -*-
"""walktrap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jl_DWKiXB0c16fkSAuff-tUEQkSu0xwH
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

graph = g = nx.read_gml("adjnoun.gml", label = 'id')
list_ = graph.nodes()
for node in list_:
  print (node)
  print ([n for n in graph.neighbors(node)])
for node in graph.neighbors(17):
  print ([n for n in graph.neighbors(node)])