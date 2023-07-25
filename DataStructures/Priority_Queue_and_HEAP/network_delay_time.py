"""
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui,vi,wi) 
ui is the source node, 
vi is the target node
wi is the time it takes for a signal to travel from source to target

We will send a signal from a given node k.
Return the minimum time it takes for all the n nodes to receive the signal.
if it is impossible for all the n nodes to receive the signal return -1.


Input : times[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
output : 2
"""