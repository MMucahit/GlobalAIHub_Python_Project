## Ana Pizza Class
class Pizza():
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

## Pizza Class' ından miras alan Pizza Çeşitleri
class Pepperoni(Pizza):
    def __init__(self):
        super().__init__(description='Pepperoni Pizza', cost=800)

class Dominos(Pizza):
    def __init__(self):
        super().__init__(description='Dominos Pizza', cost=900)

class Plain(Pizza):
    def __init__(self):
        super().__init__(description='Plain Pizza', cost=900)

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__(description='Turkish Pizza', cost=1000)

class Classic(Pizza):
    def __init__(self):
        super().__init__(description='Classic Pizza', cost=500)

class Margaritha(Pizza):
    def __init__(self):
        super().__init__(description='Margaritha Pizza', cost=600)

## Ana Sos Class
class Sauce(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)

## Sos Class' ından miras alan Sos çeşitleri
class Mushrooms(Sauce):
    def __init__(self):
        super().__init__(description='Mushrooms', cost=150)

class Meat(Sauce):
    def __init__(self):
        super().__init__(description='Meat', cost=200)

class Corn(Sauce):
    def __init__(self):
        super().__init__(description='Corn', cost=50)

class Onion(Sauce):
    def __init__(self):
        super().__init__(description='Onion', cost=100)

class Olive(Sauce):
    def __init__(self):
        super().__init__(description='Olive', cost=125)

class Cheese(Sauce):
    def __init__(self):
        super().__init__(description='Cheese', cost=125)

import sys

## Sipariş Class' ı
class Order():
    def __init__(self, pizza: Pizza, component:list = []):
        self.instance_list = []
        self._list = []
        self.total = 0

        self.pizza = pizza
        self.component = component

    ## Pizza instance' ı döndürür.
    def get_pizza_instance(self):
        pizza_instance = getattr(sys.modules[__name__], self.pizza)()
       
        return pizza_instance

    ## Sos instance' ı döndürür.
    def get_sauce_instance(self, instance):
        component_instance = getattr(sys.modules[__name__], instance)()

        return component_instance

    ## Sosların instanclarını içeren liste döndürür.
    def get_instance_list(self):
        for instance in self.component:
            self.instance_list.append(self.get_sauce_instance(instance))   

        return self.instance_list

    ## Sosları ve fiyatlarını (Sözlük veri) içeren bir liste döndürür.
    def get_list(self):
        for instance in self.component:
            sauce_cost = self.get_sauce_instance(instance).get_cost()
            self._list.append({instance: sauce_cost})

        return self._list

    ## Seçilen pizzanın ve sosların toplam fiyatını döndürür.
    def get_total_cost(self):
        for instance in self.get_instance_list():
            self.total += instance.get_cost()

        return self.total + self.get_pizza_instance().get_cost()
    
    ## Arayüzde gösterebilmek için bütün bilgileri döndürür.
    def receipt(self):

        pizza_cost = self.get_pizza_instance().get_cost()

        return {'Pizza': {self.pizza: pizza_cost}, 'Sauce': self.get_list()}, self.get_total_cost()