from pyray import *
from dsa import lanePark as lp
from dsa import spacePark as sp

if __name__ == "__main__":
    pogi = lp.ParkLane(5)
    print(pogi)

    what = sp.ParkSpace()
    print(what)

    '''
    init_window(800, 450, "Hello")
    set_target_fps(1);
    while not window_should_close():
        begin_drawing()

        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)

        end_drawing()
    close_window()
    '''
