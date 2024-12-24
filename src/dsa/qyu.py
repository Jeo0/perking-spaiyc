
class Node_Queue:
    def __init__(self, item):
        self.value = item
        self.next = None

class Queue:
    def __init__(self):
        self.__lastOut = None     # the element to be last 
        self.size = 0

    def enqueue(self, item) -> None:
        newNode = Node_Queue(item)

        if self.__lastOut == None:
            self.__lastOut = newNode
            self.__lastOut.next = self.__lastOut    # point to self 

        else:
            firstOut = self.__lastOut.next # get the first one to be ousted
            newNode.next = firstOut

            # before changing our pointer to this data struct
            # set the next pointer to the location of newNode
            self.__lastOut.next = newNode

            # have the newNode be the main location that will always 
            # be referred to when queried 
            self.__lastOut = newNode

        self.size +=1 


    def dequeue(self):
        if self.size == 0:
            raise IndexError(f"ERROR in {self.__class__.__name__}.{self.dequeue.__name__}: "
                             + "No items in queue")

        removedNode = self.__lastOut.next     # have a temp to store the location of the node 2 be removed
        # also explicitly handle when there's only 1 left
        # then just do so as is
        if self.size == 1:
            self.__lastOut = None
        else:
            self.__lastOut.next = removedNode.next 

        self.size -=1
        return removedNode.value


    def front(self):
        if self.size == 0:
            raise IndexError(f"ERROR in {self.__class__.__name__}.{self.front.__name__}: "
                            + "No items in queue")
        return self.__lastOut.next.value


    def rear(self):
        if self.size == 0:
            raise IndexError(f"ERROR in {self.__class__.__name__}.{self.rear.__name__}: "
                            + "No items in queue")
        return self.__lastOut.value


    def get_contents(self) -> list:
        if self.size == 0:
            raise IndexError(f"ERROR in {self.__class__.__name__}.{self.get_contents.__name__}: "
                             + "No items in queue")
        currentNode = self.__lastOut
        contents = []

        while currentNode.next != self.__lastOut:
            contents.append(currentNode.next.value)     # hehe just shift it 
            currentNode = currentNode.next

        contents.append(currentNode.next.value)
        return contents
    

    def __str__(self):
        return " -> ".join(map(str, self.get_contents()))

