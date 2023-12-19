#!/usr/bin/python3
"""This module contains a Node class and a SLL class"""


class Node:
    """A class defining the node of a SLL"""
    def __init__(self, data, next_node=None):
        """
        Desc:
            Initialize the node object with these attributes

        Args:
            data (int): The data in the linked list
            next_node (str): the next node in the LL
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves a priv attr of the Node(data)"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set a priv attr of the Node(data)

        Args:
            value (int): The value to be set for the data of the node

        Raises:
            TypeError: If the value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the private attr next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Desc:
            Set a private attr next_node

        Args:
            value (int): The value to be set as the next_node

        Raises:
            TypeError: If the value is not a Node or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """A class to define singly linked list objects"""
    def __init__(self):
        """Initialize an empty SLL"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Desc:
            Insert a new node in sorted order

        Args:
            value (int): The data to be inserted into the LL
        """

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None
                    and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """String representation of Linked list"""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
