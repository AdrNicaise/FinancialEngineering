import pandas as pd

class Order():
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.order_id = 0
        def __eq__(self, other): # Is self equal to other ?
            return other and self.quantity == other.quantity and self.price == other.price
        def __lt__(self, other): # Is self less than other ?
            return other and self.price < other.price    
        def __str__(self): # String representation of an instance of the Order class
            return f'{self.quantity}@{self.price}'
        def __repr__(self):
            return f'Order({self.quantity},{self.price})'
        def setOrder(self, value):
            self.order_id = value
        def getOrder(self):
            return self.order_id
        def setQuantity(self, value):
            self.quantity = value
        def getQuantity(self):
            return self.quantity
        def setPrice(self, value):
            self.price = value
        def getPrice(self):
            return self.price

class Book(Order):
    def __init__(self, name):
        self.name = name
        self.buy_orders = []
        self.sell_orders = []
        self.count = 0
                                                                                   
    def tabular_print(self):
        dataframe_buy = pd.Dataframe(self.buy_orders, columns = ["BUY"])
        dataframe_sell = pd.Dataframe(self.sell_orders, columns = ["SELL"])
        final_dataframe = pd.concat([dataframe_buy, dataframe_sell], axis = 1).fillna("        ")
        return(final_dataframe.to_markdown())
    
    def insert_buy(self, quantity, price):
        order1 = Order(quantity, price)
        self.count = self.count+1
        order1.setOrder(self.count)
        print("----------------------")
        print("--- Insert BUY ", order1.__str__() , " id=" , order1.getOrder() , " on ", self.name ,"\n", "Book on ", self.name)
        
        sell_index = -1
        if len(self.sell_orders) != 0:
            for i in range(len(self.sell_orders)):
               if self.sell_orders[i].getPrice() == order1.price:
                   sell_index = i

        if sell_index == -1
            self.buy_orders.append(order1)
        else:
            if self.sell_orders[sell_index].getQuantity() - order1.quantity > 0:
                self.sell_orders[sell_index].setQuantity(self.sell_orders[sell_index].getQuantity - order1.quantity)
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
            elif self.sell_orders[sell_index].getQuantity() - order1.quantity == 0:
                del(self.sell_orders[sell_index])
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
            else:
                order1.setQuantity(self.sell_orders[sell_index].quantity - order1.quantity)
                self.buy_orders.append(order1)
                del(self.sell_orders[sell_index])
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
        self.buy_orders=sorted(self.buy_orders, key = lambda Order : Order.price, reverse=True)
        self.sell_orders=sorted(self.sell_orders, key = lambda Order : Order.price, reverse=True)

        for i in range(len(self.sell_orders)):
            print ("SELL ", self.sell_orders[i].__str__(), " id=", self.sell_orders[i].getOrder())
        for i in range(len(self.buy_orders)):
            print ("BUY ", self.buy_orders[i].__str__(), " id=", self.buy_orders[i].getOrder())

    def insert_sell(self, quantity, price):
        order1 = Order(quantity, price)
        self.count =self.count+1
        order1.setOrder(self.count)
        print("----------------------")
        print("--- Insert SELL ", order1.__str__() , " id=" , order1.getOrder() , " on ", self.name ,"\n", "Book on ", self.name)

        buy_index = -1
        if len(self.buy_orders) != 0:
            for i in range(len(self.buy_orders)):
                if self.sell_orders[i].getPrice() == order1.price:
                    buy_index = i

        if buy_index == -1:
            self.sell_orders.append(order1)
        else:
            if self.buy_orders[buy_index].getQuantity() - order1.quantity > 0:
                self.buy_orders[buy_index].setQuantity(self.buy_orders[buy_index].getQuantity - order1.quantity)
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
            elif self.buy_orders[buy_index].getQuantity() - order1.quantity == 0:
                del(self.buy_orders[buy_index])
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
            else:
                order1.setQuantity(self.buy_orders[buy_index].getQuantity() - order1.quantity)
                self.sell_orders.append(order1)
                del(self.buy_orders[buy_index])
                print("Execute", (order1.quantity, " at ", order1.price, " on " , self.name))
        self.buy_orders=sorted(self.buy_orders, key = lambda Order : Order.price, reverse=True)
        self.sell_orders=sorted(self.sell_orders, key = lambda Order : Order.price, reverse=True)
        
        for i in range(len(self.sell_orders)):
            print ("SELL ", self.sell_orders[i].__str__(), " id=", self.sell_orders[i].getOrder())

        for i in range(len(self.buy_orders)):
            print ("BUY ", self.buy_orders[i].__str__(), " id=", self.buy_orders[i].getOrder())
