 
import pyray as rl
from dsa import bldgPark as bp
from dsa import lanePark as lp
from dsa import spacePark as sp
from dsa import qyu 
from unitTests import unitTests as tests # call it from the main function
import routines
import time



def update_routine(SM_dasma, waiting, delta_time, time_multiplier, button_add_vehicle) -> None:
    """ This function has 5 responsibilities """

    """ Generate random number """
    from random import randrange
    plate_number = randrange(1000, 9999)
    plate_text = [chr(randrange(65, 90+1)) for _ in range(3)] # ascii from A -> Z; 
    final_plate = ''.join(plate_text) + '-' + str(plate_number)
    # also there should be 3 letters


    """ 3 THINGS IN THIS LOOP """
    for lane in SM_dasma:
        for space in lane:
            if not space.is_empty():
                # 1. timeout iterator so vehicle can go byebye later
                space.timeout -= delta_time * time_multiplier[0];

                # 2. vehicle removal
                if space.timeout <= 0:
                    space.pop_vehicle()

            # 3. vehicle insertion from queue
            if space.is_empty():
                # always put something on a park space from the waiting queue
                if waiting.size:
                    space.add_vehicle(waiting.dequeue())


    """ BUTTON ADD VEHICLE LOGIC """
    if button_add_vehicle:
        #car = gen.generate_vehicle();

        # bruteforce searching through the parkbldg
        # if it is empty, then park there then start the individual timer
        flagAddedVehicle = False;
        counterSpaceThatIsFull= 0;
        for lane in SM_dasma:
            for space in lane:

                # add if space is free
                if space.is_empty():
                    space.add_vehicle(final_plate);

                    flagAddedVehicle = True;
                    break;

                # else counter for queue
                else:
                    counterSpaceThatIsFull +=1

            # catch here for the previous flagbreak
            # to early break and also reset
            if flagAddedVehicle:
                break;

        # add it to queue if there were no added vehicle
        if not flagAddedVehicle:
            waiting.enqueue(final_plate);







def draw_routine(SCREENWIDTH, SCREENHEIGHT, font_size, shift_y, SM_dasma, waiting, time_multiplier, text_addvehicle, rec_addvehicle) -> None:
    """ WARNING, many of these values are hardcoded and calculated iteratively
        
        This function has no logic except the time_multiplier being modified in here using the slider

        This function has 6 responsibilities
    """


    rl.begin_drawing()
    rl.clear_background(rl.WHITE)

    #####################################################
    """ PARKING BUILDING
        MISMONG PARKING LOT """
    # 1. draw the parking spaces
    for lane in range(len(SM_dasma)):
        for space in range(len(SM_dasma[lane])):
            x_pos = 10 + ((SM_dasma.gap_width + SM_dasma.indiv_space_width) * space)
            y_pos = 10 + ((SM_dasma.gap_height + SM_dasma.indiv_space_height) * lane)

            # draw the status if current space is empty or not
            if SM_dasma[lane][space].is_empty():
                rl.draw_rectangle(x_pos, y_pos, 
                                  SM_dasma.indiv_space_width, SM_dasma.indiv_space_height, 
                                  rl.fade(rl.GREEN, .8))
            else:
                rl.draw_rectangle(x_pos, y_pos, 
                                  SM_dasma.indiv_space_width, SM_dasma.indiv_space_height, 
                                  rl.fade(rl.MAROON, .8))
            # print timeout
            if SM_dasma[lane][space].timeout < 0:
                text_timeout = str(0)
            else:
                text_timeout = f"{SM_dasma[lane][space].timeout:.1f}"
            rl.draw_text(text_timeout, x_pos, y_pos, font_size, rl.BLACK);

            # print the platenumber also
            rl.draw_text(str(SM_dasma[lane][space]), x_pos, y_pos + 50, font_size, rl.BLACK);




    #####################################################
    """ INTERFACE """
    # 2. interface background
    rl.draw_rectangle(int(SCREENWIDTH * 0.7), 
                      int(0), 
                      int(SCREENWIDTH*1 - SCREENWIDTH*.7),
                      int(SCREENHEIGHT), 
                      rl.fade(rl.LIGHTGRAY, 0.7))


    # 3. queue
    text_Que = f"Queue: {waiting.size}"
    text_Que_size = rl.measure_text(text_Que, font_size)
    text_Que_x = int((SCREENWIDTH ) * 0.802);
    text_Que_y = int((SCREENHEIGHT - font_size) * 0.186) + shift_y;

    rl.draw_text(text_Que, text_Que_x, text_Que_y, font_size, rl.DARKGRAY)


    # 4. available space
    # calculate how many space are available
    avail_space = 0;
    for lane in SM_dasma:
        for space in lane:
            if space.is_empty() : avail_space+=1;

    text_AvailSpace = f"Available Space: {avail_space}"
    text_AvailSpace_size = rl.measure_text(text_AvailSpace, font_size)
    text_AvailSpace_x = int((SCREENWIDTH ) * 0.744) + 35;
    text_AvailSpace_y = int((SCREENHEIGHT - font_size) * 0.257)   + shift_y;
    rl.draw_text(text_AvailSpace, text_AvailSpace_x, text_AvailSpace_y, font_size, rl.DARKGRAY)


    # 5. time multiplier slider
    rec_time = rl.Rectangle(int(SCREENWIDTH * .763), 
                               int(SCREENHEIGHT* .393)+shift_y,
                               int(SCREENWIDTH * 0.94 - SCREENWIDTH * 0.763),
                               int(SCREENHEIGHT* .481 - SCREENHEIGHT* .373))

    text_TimeMultiplier = f"Time Multiplier: {time_multiplier[0]:0.1f}";
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

   

    # 6. add vehicle button
    rl.gui_button(rec_addvehicle, text_addvehicle)

    # DEBUG PRINTING CONTENST OF PARKbldg
    print(SM_dasma)
