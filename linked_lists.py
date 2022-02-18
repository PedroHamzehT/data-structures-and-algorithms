class Element():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next

            current.next = element
        else:
            self.head = element

    def get_position(self, position):
        if position < 1:
            return None

        counter = 1
        current = self.head
        while current and counter <= position:
            if counter == position:
                return current

            current = current.next
            counter += 1

        return None

    def insert(self, element, position):
        if position < 1:
            return None

        if position == 1:
            element.next = self.head
            self.head = element
            return

        counter = 1
        current = self.head
        previous = None
        while current and counter < position:
            counter += 1
            previous = current
            current = current.next

        if previous:
            element.next = current
            previous.next = element
        else:
            self.head = element

    def delete(self, value):
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next

        if current and current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def size(self):
        counter = 1
        current = self.head
        while current:
            current = current.next
            counter += 1

        return counter - 1

    def to_array(self):
        array = []
        current = self.head
        while current:
            array.append(current.value)
            current = current.next

        return array

el1 = Element(1)
el2 = Element(5)

linked_list = LinkedList()
linked_list.append(el1)
linked_list.append(el2)
print(linked_list.get_position(0))
print(linked_list.get_position(1).value)
print(linked_list.get_position(2).value)
print(linked_list.get_position(3))

el3 = Element(10)
el4 = Element(15)
linked_list.append(el3)
linked_list.insert(el4, 2)
print(linked_list.get_position(2).value)
print(linked_list.get_position(3).value)
print(linked_list.get_position(4).value)
print(linked_list.size())
print(linked_list.to_array())

linked_list.delete(5)
print(linked_list.to_array())
linked_list.delete(32)
print(linked_list.to_array())

el5 = Element(3)
el6 = Element(9)
linked_list.insert(el5, 7)
print(linked_list.to_array())
linked_list.insert(el6, 2)
print(linked_list.to_array())
