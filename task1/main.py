from order_n_book import *

def main():
    order_book=OrderBook()
    while True:
        order_book.add_order(Order.from_input())
        next = input("Input N for next or S to stop")
        if next == "s" or next == "S":
            break

    order_book.match_orders()

    print("Start balnce:")
    for i in order_book.start_balnce:
        print("\n {0} balanc".format(i))
        for j in order_book.start_balnce[i]:
            print(order_book.start_balnce[i][j].show_str)

    print("\nAfter match balnce:")
    for i in order_book.balance_changes:
        print("\n {0} balanc".format(i))
        for j in order_book.balance_changes[i]:
            print(order_book.balance_changes[i][j].show_str)

    input("Exit")

if __name__ == "__main__":
    main()
