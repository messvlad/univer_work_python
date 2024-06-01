class Node:
    def __init__(self, data):
        # Данные о вершинах
        self.data = data
        # Значени левой и правой вершины по умолчанию
        self.left = self.right = None
        return

class Tree:

    def __init__(self):
        self.root = None
        self.myStack = []
        self.delStack = []
        self.novStack = []
        return

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        # сравнение текущего значения с текущем значением в узле, то такое значение мы не добовляем в древо
        if value == node.data:
            return node, parent, True

        # сравнение текущего значения с текущем значением в узле
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        # сравнение текущего значения с текущем значением в узле
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    # Добавления вершин
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        # метод для нахождения родительской вершины
        s, p, fl_find = self.__find(self.root, None, obj.data)
        # распределение на левую и правую ветвь
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):

        if node is None:
            return
        self.show_tree(node.left)
        element = str(node.data)
        self.myStack.append(element)
        myStack1.append(element)
        self.show_tree(node.right)
        element = str(node.data)
        self.novStack.append(element)
        novStack1.append(element)

        if len(self.delStack) < 100:
            self.delStack.append(element)
            delStack1.append(element)

        # print(self.delStack)
        print(self.novStack)
        if len(self.novStack) >= 500:
            for step in self.delStack:
                self.novStack.reverse()
                novStack1.reverse()

                self.novStack.pop()
                novStack1.pop()

                self.novStack.reverse()
                novStack1.reverse()

        return myStack1, novStack1, delStack1


myStack1 = []
novStack1 = []
delStack1 = []
myStack2 = []
novStack2 = []
delStack2 = []


def get():

    v = []

    for element in range(1, 501):
        v.append(element)
    t = Tree()

    for x in v:
        t.append(Node(x))
    t.show_tree(t.root)
    myStack2, novStack2, delStack2 = t.show_tree(t.root)
    print(f'1   \n{myStack1}')
    print(f'{novStack1}')
    print(f'{delStack1}')


get()
