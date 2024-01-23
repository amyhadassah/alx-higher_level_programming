#!/usr/bin/python3
"""Defines a Node and SinglyLinkedList classes."""


class Node:
    """A class that defines a node of a singly linked list.

    Attributes:
        data (int): The data of the node, must be an integer.
        next_node (Node): The next node in the singly linked list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If value is not a Node object and is not None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the list at the correct sorted position.

        Args:
            value (int): The data value of the new node to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
