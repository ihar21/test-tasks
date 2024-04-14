import json

class Transaction:
    def __init__(self, txid, inputs, outputs):
        self.txid = txid
        self.inputs = inputs
        self.outputs = outputs

def read_blockchain_from_file(file_path):
    with open(file_path, 'r') as file:
        blockchain = json.load(file)
    return blockchain

def filter(transactions):
    filtered_transactions = []
    for block in blockchain:
        for tx in block["transactions"]:
            if len(tx["inputs"]) == 1 and len(tx["outputs"]) == 2:
                filtered_transactions.append(
                    Transaction(tx["txid"], tx["inputs"], tx["outputs"])
                )
    return filtered_transactions

def build_graphs(transactions):
    graph = {}
    for tx in transactions:
        graph[tx.txid] = [input_tx["txid"] for input_tx in tx.inputs]
    return graph


def dfs(graph, node, current_chain):
    global longest_chains, max_chain_length
    if node not in graph:
        return
    current_chain.append(node)
    if len(current_chain) > max_chain_length:
        max_chain_length = len(current_chain)
        longest_chains = [list(current_chain)]
    elif len(current_chain) == max_chain_length:
        longest_chains.append(list(current_chain))
    for neighbor in graph[node]:
        dfs(graph, neighbor, current_chain)
    current_chain.pop()

def find_longest_chains(graph):
    global longest_chains, max_chain_length
    for txid in graph:
        dfs(graph, txid, [])
    return longest_chains


file_path = 'blockchain.json'
blockchain = read_blockchain_from_file(file_path)
blockchain = filter(blockchain)
graph = build_graphs(blockchain)

longest_chains = []
max_chain_length = 0
longest_chain=find_longest_chains(graph)
print(longest_chain)
input("Exit")

