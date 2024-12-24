


# two choices
from . import context  # choose this if u are compiling main.py only
#import context  # chose this if u r compiling unitTests.py only


from dsa import qyu
from dsa import lanePark as lp
from dsa import spacePark as sp



def queue_unittest():
    pogi = qyu.Queue()
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
    pogi = sp.ParkSpace()
    try:
        print("1")
        print(f"pgoi peek: {pogi.get_vehicle()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n2")
        pogi.add_vehicle("ALSKDJL")
        print(str(pogi))
    except OverflowError as ie:
        print(ie)

    try:
        print("\n3")
        print(f"pgoi peek: {pogi.get_vehicle()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n4")
        pogi.add_vehicle(23)
        print(str(pogi))
    except OverflowError as ie:
        print(ie)

    try:
        print("\n5")
        print(f"pgoi peek: {pogi.get_vehicle()}")
    except IndexError as ie:
        print(ie)

    try:
        print("\n6")
        print(str(pogi))
        print(f"pop: {pogi.pop_vehicle()}")
        print(str(pogi))
    except IndexError as ie:
        print(ie)

    try:
        print("\n7")
        print(str(pogi))
        print(f"pgoi peek: {pogi.get_vehicle()}")
    except IndexError as ie:
        print(ie)



def lane_test():
    """
    should present:

    [None, None, None, None, None]
    C
    [B, None, D, E, F]
    """

    pogi = lp.ParkLane(5)
    print(pogi)

    sdf = 66;
    for ii in pogi:
        ii.add_vehicle(chr(sdf))
        sdf +=1

    print(pogi[1].pop_vehicle())
    print(pogi)



if __name__ == "__main__":
    print("\n===========\nSKTKACK\n")
    stack_unittest()

    print("\n\n\n===========\nQUEUEUEUEUE\n")
    queue_unittest()
