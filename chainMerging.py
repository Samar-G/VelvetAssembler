def calculateInDegree(node, graph):
    in_degree = 0
    for x in graph['edges']:
        if node==x[1]:
            in_degree+=1
    return in_degree

def calculateOutDegree(node, graph):
    out_degree = 0
    for x in graph['edges']:
        if node==x[0]:
            out_degree+=1
    return out_degree
    
def mergeChains(graph,k):
    canMerge = True
    
    while canMerge:
        canMerge = False
        for edge in graph['edges']: # Condition 1
            if(calculateOutDegree(edge[0],graph)== 1 and calculateInDegree(edge[1],graph) == 1):
                canMerge = True
                merged=edge[0]+edge[1][k-1]
                x=graph['nodes'].index(edge[0])
                y=graph['nodes'].index(edge[1])
                graph['nodes'][x]=str(merged)
                del graph['nodes'][y]
                del graph['edges'][graph['edges'].index(edge)]
#                graph['nodes']=graph['nodes'][:x] 
                for x in graph['edges']:
                    if x[0]==edge[1]:
                        x[0]= merged
                    if x[1]==edge[0]:
                        x[1] = merged
    return graph


graph = {'nodes':['GAC', 'ACC', 'CCG', 'CGT', 'GTA', 'TAA', 'AAT', 'TAG', 'ACT',
                  'CTG', 'TGT'],
        'edges':[['GAC', 'ACC'], ['GAC', 'ACT'], ['ACC', 'CCG'], ['CCG', 'CGT'],
                 ['CGT', 'GTA'], ['GTA', 'TAA'], ['TAA', 'AAT'],['GTA', 'TAG'],
                 ['ACT', 'CTG'], ['CTG','TGT'], ['TGT', 'GTA']]
         }

newGraph = mergeChains(graph,3)

print(newGraph)
        
