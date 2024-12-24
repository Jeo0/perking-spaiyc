from context import dsa

def queue_unittest():
    pogi = dsa.qyu.Queue()
    try:
        print("1")
        print(f"pgoi front: {pogi.front()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n2")
        print(f"pgoi rear: {pogi.rear()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n3")
        print(str(pogi))
        print(pogi.get_contents())
    except IndexError as ie:
        print(ie)

    try:
        print("\n4")
        pogi.enqueue("ASD")
    except IndexError as ie:
        print(ie)

    try:
        print("\n5")
        pogi.enqueue("pOIY")
    except IndexError as ie:
        print(ie)

    try:
        print("6")
        print(f"pgoi front: {pogi.front()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n7")
        print(f"pgoi rear: {pogi.rear()}")
    except IndexError as ie:
        print(ie)


    try:
        print("\n8")
        print(str(pogi))
        print(pogi.get_contents())
    except IndexError as ie:
        print(ie)


    try:
        print("\ndeque")
        pogi.dequeue()
    except IndexError as ie:
        print(ie)

    try:
        print("\nfront")
        print(f"pgoi front: {pogi.front()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\nrear")
        print(f"pgoi rear: {pogi.rear()}")
    except IndexError as ie:
        print(ie)


    try:
        print("\nnoice")
        print(str(pogi))
        print(pogi.get_contents())
    except IndexError as ie:
        print(ie)



def stack_unittest():
    pogi = dsa.stak.Stack()
    try:
        print("1")
        print(f"pgoi peek: {pogi.peek()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n2")
        pogi.push("ALSKDJL")
        print(str(pogi))
    except OverflowError as ie:
        print(ie)

    try:
        print("\n3")
        print(f"pgoi peek: {pogi.peek()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n4")
        pogi.push(23)
        print(str(pogi))
    except OverflowError as ie:
        print(ie)

    try:
        print("\n5")
        print(f"pgoi peek: {pogi.peek()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n6")
        print(str(pogi))
        print(pogi.get_contents())
        print(f"pop: {pogi.pop()}")
        print(str(pogi))
        print(pogi.get_contents())
    except IndexError as ie:
        print(ie)

    try:
        print("\n7")
        print(str(pogi))
        print(pogi.get_contents())
        print(f"pgoi peek: {pogi.peek()}")
    except IndexError as ie:
        print(ie)



if __name__ == "__main__":
    stack_unittest()

    print("\n\n\nQUEUEUEUEUE\n")
    queue_unittest()
