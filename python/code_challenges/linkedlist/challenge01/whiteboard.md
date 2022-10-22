### Problem Domain :
**delete a given node from linked list withou access the head**
input : node 
output: list of linked list without node

### test case :
[4,5,1,9]
* input :5, output:[4,1,9]
* input:1 output:[4,5,9]


### visualization
<img alt="" src="../../../assets/linked-list/ll-01-node1.jpg" style="width: 300px; height: 215px;">
<img alt="" src="../../../assets/linked-list/ll-01-node2.jpg" style="width: 300px; height: 236px;">



### Algorithms
1. Copy data of the next node to the current node.

2. Change the next pointer of the current node to the next pointer of the next node.

### Big O
time :o(1)

space: o(1)