import pandas as pd
import networkx as nx


global data , G

data = pd.read_csv("cities_in_az.csv")

G = nx.from_pandas_edgelist(data , source = 'Origin' , target = 'Destiny', edge_attr = True )

def default():
    i=0
    for key in G.nodes.keys():
        G.nodes[key]["Estimated Time"] = 10000000000000
   
    for origin in data.Origin:
        G.nodes[origin][data.Destiny[i]] = data.Hours[i]
        i+=1     
        
#nx.draw(G , with_labels = True , node_color = 'skyblue')



#So I should define a function that finds the optimal path for given origin and destination
def OptimalPath(origin,destination):
    if(origin == destination):
        return 0
    default()
    G.nodes[origin]['Estimated Time'] = 0
    my_list = []
    
    while(1):
        my_neighbors = list(G.neighbors(origin))
        for neighbour in my_neighbors:
            
            if(G.nodes[neighbour]['Estimated Time'] > (G.nodes[origin][neighbour] + G.nodes[origin]['Estimated Time'])  ):
                if(G.nodes[neighbour]['Estimated Time'] in my_list):
                    my_list.remove(G.nodes[neighbour]['Estimated Time'])
                G.nodes[neighbour]['Estimated Time'] = G.nodes[origin][neighbour]
                my_list.append(G.nodes[origin][neighbour])

        my_list.sort()
        my_list = sorted(my_list)
        a = my_list.pop()

        for g in G.nodes.keys():
            if(a == G.nodes[g]['Estimated Time']):
                origin = g
        print(origin)        

        if(my_list == []):
            return G.nodes[destination]['Estimated Time']





a = OptimalPath('Baku','Kurdamir')
a
#G.nodes["Baku"]['Estimated Time']

for g in G.nodes.keys():
    print(g)
    print(G.nodes[g])
    print('\n')