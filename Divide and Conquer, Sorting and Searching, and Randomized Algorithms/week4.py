

# def partition(array, begin, end):
#     pivot = begin
#     for i in range(begin+1, end+1):
#         if array[i] <= array[begin]:
#             pivot += 1
#             array[i], array[pivot] = array[pivot], array[i]
#     array[pivot], array[begin] = array[begin], array[pivot]
#     return pivot


# def RSelect(my_array, order_statistic, begin, array_end):
#     if len(my_array) == 1:
#         return my_array[order_statistic]  
#     pivot = partition(my_array, begin, array_end)
#     if pivot == order_statistic:
#         return my_array[order_statistic]
#     elif pivot > order_statistic:
#         array_end = len(my_array[:pivot-1])       
#         my_array = my_array[:pivot]
#         index_val = RSelect(my_array,order_statistic,begin,array_end)
#     else:
#         array_end = len(my_array[pivot+2:])
#         my_array = my_array[pivot+1:]
#         order_statistic = order_statistic-pivot-1
#         index_val = RSelect(my_array,order_statistic,begin, array_end)
#     return index_val

# array = [3,8,2,5,1,4,7,6,11,16,88]
# print(RSelect(array, 9, 0, (len(array)-1)))
import random

graph = {}
myfile = open('graph.txt')
data = myfile.readlines()
for line in data:
    elements = list(map(str,line.split()))
    graph[elements[0]] = elements[1:]



g = graph

def get_rand_int(g):
    keylist = list(graph.keys())
    v1 = keylist[random.randint(0,len(keylist)-1)]
    v2 = g[v1][random.randint(0,len(g[v1])-1)]

    return(v1, v2)

def mergevertices(g):
    v1, v2 = get_rand_int(g)
    # print(v1,v2)
    g[v1].extend(g[v2])

    for connections in g[v2]:
        l = g[connections]
        for i in range(0,len(l)):
        # for elements in g[connections]:
            if l[i] == v2:

                l[i] = v1

    while v1 in g[v1]:
        g[v1].remove(v1)


    del g[v2]

def mincut(g):
    while len(g) > 2:
        mergevertices(g)

    return len(g[list(g.keys())[0]])   

print(mincut(g))

# print(get_rand_int())