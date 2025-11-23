from singly_linked_list import SinglyLinkedList, Node

class SplitEvensOdds(SinglyLinkedList):

    def split(self):
        evens = SplitEvensOdds()
        odds = SplitEvensOdds()

        current = self._SinglyLinkedList__head

        # Clear original list
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        while current:
            next_node = current.next
            current.next = None  # detach node

            if current.data % 2 == 0:
                # Append to evens list
                if evens._SinglyLinkedList__head is None:
                    evens._SinglyLinkedList__head = evens._SinglyLinkedList__tail = current
                else:
                    evens._SinglyLinkedList__tail.next = current
                    evens._SinglyLinkedList__tail = current
                evens._SinglyLinkedList__count += 1
            else:
                # Append to odds list
                if odds._SinglyLinkedList__head is None:
                    odds._SinglyLinkedList__head = odds._SinglyLinkedList__tail = current
                else:
                    odds._SinglyLinkedList__tail.next = current
                    odds._SinglyLinkedList__tail = current
                odds._SinglyLinkedList__count += 1

            current = next_node

        return evens, odds
