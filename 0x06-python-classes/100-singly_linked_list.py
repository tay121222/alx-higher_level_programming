#!/usr/bin/python3

class Node:
    """
    A node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the a sorted position in the list.
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            temp = self.__head
            new_node = Node(value)

            if temp.data > new_node.data:
                new_node.next_node = temp
                self.__head = new_node
            else:
                while temp.next_node is not None:
                    if new_node.data < temp.next_node.data:
                        new_node.next_node = temp.next_node
                        temp.next_node = new_node
                        return
                    temp = temp.next_node
                temp.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        nodes = ""
        temp = self.__head
        while temp:
            nodes += str(temp.data)

            if temp.next_node is not None:
                nodes += '\n'
            temp = temp.next_node
        return nodes
