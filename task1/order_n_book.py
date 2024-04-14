import copy

class Order:
    def __init__(self, user_id: int, amount: float, price: float, side: bool):
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side

    @classmethod
    def from_input(cls):
        user_id = int(input("Input user_id: "))
        amount = float(input("Input amount: "))
        price = float(input("Input price: "))
        side = bool(int(input("Inupt 1 for buy or 0 for sell: ")))
        return cls(user_id, amount, price, side)

    @property
    def _show_str(self):
        return "id:{0} amount{1} price{2} side{3}".format(self.user_id,self.amount,self.price,self.side)

class BalanceChange:
    def __init__(self, user_id, value, currency):
        self.user_id = user_id
        self.value = value
        self.currency = currency

    @property
    def show_str(self):
        return "id:{0} value:{1} currency:{2}".format(self.user_id, self.value, self.currency)




class OrderBook:
    def __init__(self, debug=False):
        self.sell_orders = []
        self.buy_orders = []
        self.debug=debug
        self.balance_changes = {"UAH":{},"USD":{}}
        self.start_balnce=[]

    def add_order(self, order: Order):
        if order.side:
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)


    def _show_orders(self):
        for i in self.sell_orders:
            print(i._show_str)

        print("\n")
        for i in self.buy_orders:
            print(i._show_str)

    def match_orders(self):
        self.buy_orders.sort(key=lambda x: x.price, reverse=True)
        self.sell_orders.sort(key=lambda x: x.price)
        for sell_order, buy_order in zip(self.sell_orders, self.buy_orders):
            if sell_order.user_id not in self.balance_changes["UAH"]:
                self.balance_changes["UAH"][sell_order.user_id]=BalanceChange(sell_order.user_id, sell_order.amount, "UAH")
            else:
                self.balance_changes["UAH"][sell_order.user_id].value+=sell_order.amount
            if buy_order.user_id not in self.balance_changes["USD"]:
                self.balance_changes["USD"][buy_order.user_id]=BalanceChange(buy_order.user_id, buy_order.amount*buy_order.price, "USD")
            else:
                self.balance_changes["USD"][buy_order.user_id].value+=buy_order.amount*buy_order.price
        self.start_balnce = copy.deepcopy(self.balance_changes)
        while self.sell_orders and self.buy_orders:

            self.balance_changes["UAH"][self.sell_orders[0].user_id].value-=self.buy_orders[0].amount
            try:
                self.balance_changes["USD"][self.sell_orders[0].user_id].value+=self.buy_orders[0].amount*self.sell_orders[0].price
            except KeyError:
                self.balance_changes["USD"][self.sell_orders[0].user_id] = BalanceChange(self.sell_orders[0].user_id, self.buy_orders[0].amount * self.sell_orders[0].price, "USD")


            try:
                self.balance_changes["UAH"][self.buy_orders[0].user_id].value+=self.sell_orders[0].amount
            except KeyError:
                self.balance_changes["UAH"][self.buy_orders[0].user_id] = BalanceChange(self.buy_orders[0].user_id, self.sell_orders[0].amount, "UAH")


            self.balance_changes["USD"][self.buy_orders[0].user_id].value-=self.sell_orders[0].amount*self.buy_orders[0].price

            if self.debug:print("Transaction:",self.sell_orders[0]._show_str,"->",self.buy_orders[0]._show_str)#debug
            self.sell_order = self.sell_orders.pop(0)
            self.buy_order = self.buy_orders.pop(0)

            if self.debug:self._show_orders()





def test_orders():
    order_book = OrderBook()

    #UAH to USD 29.03.24 0.025


    order_book.add_order(Order(user_id=1, amount=100, price=0.062, side=True))
    order_book.add_order(Order(user_id=5, amount=100, price=0.072, side=True))
    order_book.add_order(Order(user_id=3, amount=75, price=0.081, side=True))
    order_book.add_order(Order(user_id=7, amount=500, price=0.091, side=True))
    order_book.add_order(Order(user_id=7, amount=100, price=0.073, side=True))
    order_book.add_order(Order(user_id=19, amount=100, price=0.092, side=True))
    order_book.add_order(Order(user_id=14, amount=100, price=0.09, side=True))
    order_book.add_order(Order(user_id=5, amount=100, price=0.08, side=True))
    order_book.add_order(Order(user_id=3, amount=75, price=0.09, side=True))
    order_book.add_order(Order(user_id=7, amount=500, price=0.080, side=True))
    order_book.add_order(Order(user_id=7, amount=100, price=0.060, side=True))
    order_book.add_order(Order(user_id=20, amount=100, price=0.070, side=True))


    order_book.add_order(Order(user_id=4, amount=30, price=0.025, side=False))
    order_book.add_order(Order(user_id=2, amount=50, price=0.021, side=False))
    order_book.add_order(Order(user_id=2, amount=50, price=0.023, side=False))
    order_book.add_order(Order(user_id=7, amount=50, price=0.024, side=False))
    order_book.add_order(Order(user_id=4, amount=100, price=0.026, side=False))
    order_book.add_order(Order(user_id=1, amount=50, price=0.020, side=False))
    order_book.add_order(Order(user_id=10, amount=30, price=0.01, side=False))
    order_book.add_order(Order(user_id=2, amount=500, price=0.01, side=False))
    order_book.add_order(Order(user_id=11, amount=50, price=0.023, side=False))
    order_book.add_order(Order(user_id=7, amount=50, price=0.024, side=False))
    order_book.add_order(Order(user_id=30, amount=300, price=0.026, side=False))
    order_book.add_order(Order(user_id=1, amount=50, price=0.020, side=False))

    order_book.match_orders()

    return order_book


