class Product(object):
    pass


class Inventory(object):
    def __init__(self):
        self.__items = []
        # private variable 정확하게는 맹글링이 일어나서 접근이 안되는 것

    @property  # decorator라고 함 - property는 함수를 변수 명처럼 쓸 수 있게 함.
    def items(self):
        return self.__items  # 맹글링된 필드에 접근할 수 있도록 함.

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)
