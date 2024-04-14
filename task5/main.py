import csv
import time
import psutil

def read_transactions(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tx_id, tx_size, tx_fee = row
            transactions.append((tx_id, int(tx_size), int(tx_fee)))
    return transactions

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_block(transactions):
    def insert(root, tx):
        if root is None:
            return TreeNode(tx)
        if tx[2]/tx[1]  < root.data[2]/tx[1] :
            root.left = insert(root.left, tx)
        else:
            root.right = insert(root.right, tx)
        return root

    root = None
    for tx in transactions:
        root = insert(root, tx)

    def dfs_t(node, block_size_limit):
        stack = []
        current = root
        block = []
        total_fee = 0
        block_size = 0

        while current is not None:
            stack.append(current)
            current = current.right

        while len(stack) > 0:
            current = stack.pop()
            if node.data[1] + block_size <= block_size_limit:
                block_size+=node.data[1]
                total_fee+=node.data[2]
                block.append(node.data)

            if current.left is not None:
                current = current.left
                while current is not None:
                    stack.append(current)
                    current = current.right

        return block, len(block), block_size, total_fee

    block, num_transactions, block_size, total_fee = dfs_t(root, 1000000)
    return block, num_transactions, block_size, total_fee


def main():
    transactions = read_transactions('transactions.csv')

    start_time = time.time()
    block, num_transactions, block_size, total_fee = build_block(transactions)
    end_time = time.time()

    construction_time = end_time - start_time

    max_memory = psutil.Process().memory_info().rss

    print("Constructed block:", block)
    print("Num of transaction in block:", num_transactions)
    print("Block size:", block_size, "bytes")
    print("Extracted fee:", total_fee, "satoshies")
    print("Construction time:", construction_time, "s")
    print("Max used memory:", max_memory, "bytes")
    input("Exit")

if __name__ == "__main__":
    main()
