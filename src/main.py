import pyray as rl
#import ctypes   # used only for time_multiplier
from dsa import bldgPark as bp
from dsa import lanePark as lp
from dsa import spacePark as sp
from dsa import qyu 
from unitTests import unitTests as tests
import time


if __name__ == "__main__":

    # window context
    default_screenwidth = int(800*1.9);
    default_screenheight = int(450*1.9);
    rl.init_window(default_screenwidth, default_screenheight, "Hello")
    rl.set_target_fps(24);
    SCREENWIDTH = rl.get_screen_width();
    SCREENHEIGHT = rl.get_screen_height();

    font_size = 25;
    start_time = time.time();
    elapsed_time = 0;
    
    # calculating rectangles
    num_parkspaces = 5;
    num_parklanes = 2;

    # objects 
    pogi = bp.ParkBldg(num_parklanes, num_parkspaces, SCREENWIDTH, SCREENHEIGHT);
    waiting = qyu.Queue();
    time_multiplier = rl.ffi.new('float *', 1.0);
    get_time_multiplier = 0.0; # use this one when doing operations
    random_button_setter_forthe_secondsecond = rl.Rectangle(SCREENWIDTH // 2 + 200, SCREENHEIGHT // 2 + 100);




    while not rl.window_should_close():


        #########################################
        rl.begin_drawing()

        rl.clear_background(rl.WHITE)

        # draw the parking spaces
        # do draw the status also by adjusting the opacity and color
        for lane in range(len(pogi)):
            for space in range(len(pogi[lane])):
                x_pos = 10 + ((pogi.gap_width + pogi.indiv_space_width) * space)
                y_pos = 10 + ((pogi.gap_height + pogi.indiv_space_height) * lane)

                if pogi[lane][space].is_empty():
                    rl.draw_rectangle(x_pos, y_pos, 
                                      pogi.indiv_space_width, pogi.indiv_space_height, 
                                      rl.fade(rl.GREEN, .8))
                else:
                    rl.draw_rectangle(x_pos, y_pos, 
                                      pogi.indiv_space_width, pogi.indiv_space_height, 
                                      rl.fade(rl.MAROON, .8))


        #####################################################
        """ INTERFACE """
        shift_y = 50;
        # interface bg
        rl.draw_rectangle(int(SCREENWIDTH * 0.7), 
                          int(0), 
                          int(SCREENWIDTH*1 - SCREENWIDTH*.7),
                          int(SCREENHEIGHT), 
                          rl.fade(rl.LIGHTGRAY, 0.7))

        # queue
        text_Que = f"Queue: {waiting.size}"
        text_Que_size = rl.measure_text(text_Que, font_size)
        text_Que_x = int((SCREENWIDTH ) * 0.802);
        text_Que_y = int((SCREENHEIGHT - font_size) * 0.186) + shift_y;

        rl.draw_text(text_Que, text_Que_x, text_Que_y, font_size, rl.DARKGRAY)

        # available space
        # calculate how many space are available
        avail_space = 0;
        for lane in pogi:
            for space in lane:
                if not space.is_empty() : avail_space+=1;
        text_AvailSpace = f"Available Space: {avail_space}"
        text_AvailSpace_size = rl.measure_text(text_AvailSpace, font_size)
        text_AvailSpace_x = int((SCREENWIDTH ) * 0.744) + 35;
        text_AvailSpace_y = int((SCREENHEIGHT - font_size) * 0.257)   + shift_y;

        rl.draw_text(text_AvailSpace, text_AvailSpace_x, text_AvailSpace_y, font_size, rl.DARKGRAY)


        # time multiplier slider
        rec_time = rl.Rectangle(int(SCREENWIDTH * .763), 
                                   int(SCREENHEIGHT* .393)+shift_y,
                                   int(SCREENWIDTH * 0.94 - SCREENWIDTH * 0.763),
                                   int(SCREENHEIGHT* .481 - SCREENHEIGHT* .373))

        get_time_multiplier = time_multiplier[0]; # access it
        text_TimeMultiplier = f"Time Multiplier: {get_time_multiplier:0.1f}";
        text_TimeMultiplier_x = int((SCREENWIDTH ) * .776) ;
        text_TimeMultiplier_y = int((SCREENHEIGHT - font_size-10) * 0.373) + shift_y;
        rl.draw_text(text_TimeMultiplier, 
                     text_TimeMultiplier_x,
                     text_TimeMultiplier_y,
                     font_size,
                     rl.DARKGRAY)
        rl.gui_slider_bar(rec_time,
                          "", "",
                          time_multiplier,
                          .0,
                          10.)

        # add vehicle button
        text_addvehicle = "Add a vehicle to Queue"
        rec_addvehicle= rl.Rectangle(int(SCREENWIDTH * .763), 
                                   int(SCREENHEIGHT* .514)+shift_y,
                                   int(SCREENWIDTH * 0.94 - SCREENWIDTH * 0.763),
                                   int(SCREENHEIGHT* .615 - SCREENHEIGHT* .514))

        """ i dont know how to separate the draw from the game logic here """
        if rl.gui_button(rec_addvehicle, text_addvehicle): 
            #car = gen.generate_vehicle();


            # searching through the parkbldg
            # if it is empty, then park there then start the individual timer
            breakflag = False;
            for lane in pogi:
                for space in lane:
                    if space.is_empty():
                        space.add_vehicle("ASd")
                        breakflag = True;
                        break;

                if breakflag:
                    breakflag = False # reset
                    break;


        # DEBUG PRINTING CONTENST OF PARKbldg
        print(pogi)





        # reset
        rl.end_drawing()

    rl.close_window()
