import pyray as rl
from dsa import bldgPark as bp
from dsa import lanePark as lp
from dsa import spacePark as sp
from dsa import qyu 
from unitTests import unitTests as tests # call it from the main function
import routines
import time


if __name__ == "__main__":
    tests.randomizedpop_test()

    # window context
    default_screenwidth = int(800*1.9);
    default_screenheight = int(450*1.9);
    rl.init_window(default_screenwidth, default_screenheight, "PARKING LOT IN DASMA")
    rl.set_target_fps(24);
    SCREENWIDTH = rl.get_screen_width();
    SCREENHEIGHT = rl.get_screen_height();

    font_size = 25;
    custom_font = rl.load_font("font-calibri/calibri-regular.ttf")
    

    # calculating rectangles
    num_parkspaces = 5;
    num_parklanes = 2;


    # objects 
    SM_dasma = bp.ParkBldg(num_parklanes, num_parkspaces, SCREENWIDTH, SCREENHEIGHT);
    waiting = qyu.Queue();
    time_multiplier = rl.ffi.new('float *', 1.0);
    lastframe_time = time.time(); # used for calculating delta time
    # flagDrawTimeOut = rl.ffi.new('bool *', False); """ nevermind """



    """ MAIN LOOP """
    while not rl.window_should_close():
        # for interface
        shift_y = 50; 


        # updating the removal
        current_time = time.time();
        delta_time = current_time - lastframe_time; # time passed from last fram
        lastframe_time = current_time


        # for the add vehicle button
        # i dont know how to separate this
        text_addvehicle = "Add a vehicle\nto Queue"
        rec_addvehicle= rl.Rectangle(int(SCREENWIDTH * .763), 
                                   int(SCREENHEIGHT* .514)+shift_y,
                                   int(SCREENWIDTH * 0.94 - SCREENWIDTH * 0.763),
                                   int(SCREENHEIGHT* .615 - SCREENHEIGHT* .514))
        button_add_vehicle = rl.gui_button(rec_addvehicle, text_addvehicle)



        # routines
        routines.update_routine(SM_dasma, waiting, delta_time, time_multiplier, button_add_vehicle)

        routines.draw_routine(custom_font, SCREENWIDTH, SCREENHEIGHT, font_size, shift_y,
                              SM_dasma, waiting, time_multiplier, text_addvehicle, rec_addvehicle)

        """ ENVERMIND
        # 7. draw timeout toggle button
        if rl.gui_check_box(rl.Rectangle(SCREENWIDTH - 280, SCREENHEIGHT - 240 , 30, 30), "Show timeout", flagDrawTimeOut): 
            flagDrawTimeOut[0] = not flagDrawTimeOut[0]
        """

        rl.end_drawing()

    rl.close_window()
