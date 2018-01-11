import sys
import random
import copy

def choose_random_edge(data):
    a = random.randint(0,len(data)-1)
    b = random.randint(1,len(data[a])-1)
    return a,b

def compute_nodes(data):
    data_head = []
    for i in range(len(data)):
        data_head.append(data[i][0])
    return data_head

def find_index(data_head,data,u,v):
    index = data_head.index(data[u][v])
    return index

def replace(data_head,data,index,u):
    for i in data[index][1:]:
        index_index = data_head.index(i)
        for position,value in enumerate(data[index_index]):
            if value == data[index][0]:
                data[index_index][position] = data[u][0]
    return data

def merge(data):
    u,v = choose_random_edge(data)
    #print u,v
    data_head = compute_nodes(data)
    index = find_index(data_head,data,u,v)
    data[u].extend(data[index][1:])
    #print data
    data = replace(data_head,data,index,u)
    #print data
    data[u][1:] = [x for x in data[u][1:] if x!=data[u][0]]
    #print data
    data.remove(data[index])
    #print data
    return data

def KargerMinCut(data):
    data = copy.deepcopy(data)
    while len(data) > 2:
        data = merge(data)
        #print data
    num = len(data[0][1:])
    return num

def calc_number(data, iteration):
    list = []
    for i in range(iteration):
        list.append(KargerMinCut(data))
    return min(list)

def read_data(path):
    with open(path) as f:
        data = []
        for ln in f:
            line = ln.split()
            if line:
                a = [int(x) for x in line]
                data.append(a)
    return data

def main():
    path = sys.argv[1]
    data = read_data(path)
    min_cut = None # 17
    while True:
        result = KargerMinCut(data)
        if min_cut is None or min_cut > result:
            min_cut = result
        print(f'{result} ({min_cut})')

if __name__ == "__main__":
    main()
