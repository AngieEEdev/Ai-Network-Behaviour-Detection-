import networkx as nx

def build_graph(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        if 'srcip' in df.columns and 'dstip' in df.columns:
            G.add_edge(row['srcip'], row['dstip'])
    return G