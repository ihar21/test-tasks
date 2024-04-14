import csv
import random

def generate_transactions_csv(filename, num_transactions):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['tx_id', 'tx_size', 'tx_fee'])
        for i in range(1, num_transactions + 1):
            tx_size = random.randint(100, 1000)
            tx_fee = random.randint(1000, 10000)
            writer.writerow([i, tx_size, tx_fee])

if __name__ == "__main__":
    generate_transactions_csv('transactions.csv', 100000)

