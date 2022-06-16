# -*- coding: utf-8 -*-
"""ialdaba_colab7.3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DhQvMPqQlrAvTthc4e6Q2k7UBlnR0sSJ

# Lesson 7.3 - Colaboratory Assignment

**Instructions**. Below you will find several text cells with programming (short) problems. You will create how many code cells you need to answer them. Make sure that you and your programming partner contribute to the code.

**BEFORE YOU START**

Complete the cell below with your names.

## 1. Local clustering

Using the IMDB dataset, find the node with the largest degree and obtain its clustering coefficient.
"""

import networkx as nx
from readlist import readlist # readlist being file provided by instructor to read in data

imdb = readlist("imdb.pkl", 0) # .pkl file provided by instructor

# find the node with the largest degree
imdb_degrees = dict(nx.degree(imdb))

max_k = 0
for node in imdb_degrees.keys():
    if imdb_degrees[node] > max_k:
        max_k = imdb_degrees[node]
        max_node = node

print('the node with the highest degree is ', max_node)

# obtain clustering coefficient
def ci(G, i):
    t = 0
    k = G.degree(i)
    v = (k * (k - 1)) / 2
    Gammai = list(G.neighbors(i))
    for c1 in range(k - 1):
        for c2 in range(c1 + 1, k):
            if (c1 < len(Gammai)) and (c2 < len(Gammai)):
                h = Gammai[c1]
                q = Gammai[c2]
                if G.has_edge(h, q):
                    t += 1

    if v != 0:
        return t / v
    else:
        return 0


print("the clustering coefficient is", ci(imdb, max_node))

"""## 2. Plot clustering coefficient in context

Using the same data set (IMDB), plot all clustering coefficients. Put the nodes in the horizontal axis and the clustering coefficient in the vertical axis. For the horizontal axis, you don't have to plot the label for the node, since this can take a bit of tweaking in terms of the spacing in the axis. You can just plot the nodes in terms of their positions in the node set. In practice, this means that your horizontal axis should have values $\{0,1,2,\ldots,n - 1\}$

As a reference, also plot a horizontal line with $\langle c \rangle$. You have done this before, but just as a reminder, you can plot a horizontal line with height `y` using

```python
plt.axhline(y)
```

Consider that there are a lot of nodes in the IMDB network. Therefore, to loop through all clustering coefficients takes about 2 minutes.
"""

import matplotlib.pyplot as plt

c_dict = nx.clustering(imdb)

c_list = [] # list of coefficients (y)
for key in c_dict:
  c = c_dict.get(key)
  c_list.append(c)

# list of positions of keys (x)
pos_list = list(range(0, imdb.order()))

# find ⟨𝑐⟩ to create h line
csum = 0 # Variable for <c>
for c in c_list:
  csum = csum + c # to add c_i , per Def . 3

cavg = csum /imdb.order()

f = plt.figure()
f.set_figwidth(12)
f.set_figheight(12)
plt.plot(pos_list, c_list, ".")
plt.axhline(cavg, color = "red")
plt.xlabel('Node Index') 
plt.ylabel('Clustering Coefficient') 
plt.title("Clustering Coefficients of IMDB")
plt.show()

# not sure why there are two blue horizontal lines showing along the borders of my plot

"""## 3. Create an artificial network

For this problem, we will create an artificial network based on the Karate Club data. To do this, we use the function [`gnm_random_graph()`](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnm_random_graph.html#networkx.generators.random_graphs.gnm_random_graph), which takes two arguments: $n$ and $m$. Save your network as `G`

Use the same $n$ and $m$ as the Karate Club network. This way, you will have a network with the same number of nodes and links, but all links random. Once you've created the network, obtain the clustering coefficient for all nodes and plot them just like you did for the previous problem.
"""

import networkx as nx
Z = nx.karate_club_graph()

# find n of karate network
n = Z.number_of_nodes()

# find m of karate network
m = Z.number_of_edges()

# CREATE ARTIFICAL NETWORK
G = nx.gnm_random_graph(n,m)

c_dict = nx.clustering(G)

c_list = [] # list of coefficients (y)
for key in c_dict:
  c = c_dict.get(key)
  c_list.append(c)

# list of positions of keys (x)
pos_list = list(range(0, G.order()))

# find ⟨𝑐⟩ to create h line
csum = 0 # Variable for <c>
for c in c_list:
  csum = csum + c # to add c_i , per Def . 3

cavg = csum /G.order()

plt.plot(pos_list, c_list, ".")
plt.axhline(cavg, color = "red")
plt.xlabel('Node Index') 
plt.ylabel('Clustering Coefficient') 
plt.title("Clustering Coefficients of G")
plt.show()

"""## 4. Compare Karate Club and `G`

To better visualize the differences between `G` and the Karate Club network, we can plot the clustering coefficient for each node in the same figure. Make sure to use different symbols as well. As an example, if you want to show every point in `G` using circles, you use the argument `"o"`. To use diamonds, you can use `"D"`; for a thick cross, you can use  `"X"`, and so on. For complete list of the available symbols, check the [documentation](https://matplotlib.org/stable/api/markers_api.html)

Also, for each network, create a horizontal line as a reference, This time, that horizontal line will have height equal to the global clustering coefficient.
"""

# function for global coefficient
def C(G):
    T = 0
    V = 0
    for node in G.nodes():
        ti = 0
        k = G.degree(node)
        V += (k * (k - 1)) / 2
        Gammai = list(G.neighbors(node))
        for c1 in range(k - 1):
            for c2 in range(c1 + 1, k):
                h = Gammai[c1]
                q = Gammai[c2]
                if G.has_edge(h, q):
                    ti += 1
        T += ti
    return T / V

c_dict_Z = nx.clustering(Z)

c_list_Z = [] # list of coefficients (y)
for key in c_dict:
  c = c_dict_Z.get(key)
  c_list_Z.append(c)

# list of positions of keys (x)
pos_list_Z = list(range(0, Z.order()))

# global coefficient for Z (karate club)
gcZ = C(Z)
# global coefficient for G
gcG = C(G)

# plot for G
p1 = plt.plot(pos_list, c_list, "d")
plt.axhline(gcG)
# plot for Z (original karate network)
p2 = plt.scatter(pos_list_Z, c_list_Z, c = '#ff7f0e')
plt.axhline(gcZ, color = "#ff7f0e")
plt.xlabel('Node Index') 
plt.ylabel('Clustering Coefficient') 
plt.title("Clustering Coefficients of G and Karate Club")
plt.show()