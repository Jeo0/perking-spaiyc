
# came from https://github.com/ahmedllshafiey/Raylib-Stopwatch/tree/main

import pyray as rl
import datetime
import time

def main():
    # Initialization
    screen_width, screen_height = 350, 350
    rl.set_target_fps(5);
    rl.init_window(screen_width, screen_height, "Raylib Stopwatch")

    # Set window icon
    #rl.set_window_icon(rl.load_image("static/icon.png"))

    font_size = 100
    start_time = time.time()
    elapsed_time  = 0
    continue_timer = False

    Date = datetime.datetime.now().strftime("%X")
    formatted_date = Date.replace(" ", ".").replace(":", ".")
    file_path = f"./data/Lap Record {formatted_date}.txt"

    try:
        # Try to open the file for writing
        with open(file_path, 'w') as file:
            # Perform operations on the file if needed
            file.write("")
            print(f"File '{file_path}' created successfully.")

    except FileExistsError:
        # Handle the case where the file already exists
        print(f"File '{file_path}' already exists.")

    stop_button = rl.Rectangle(screen_width // 2 + 25, screen_height // 2 + 50, 100, 40)
    start_button = rl.Rectangle(stop_button.x - 150, screen_height // 2 + 50, 100, 40)
    lap_button =  rl.Rectangle(screen_width // 2 + 25, screen_height // 2 + 100, 100, 40)
    reset_button = rl.Rectangle(stop_button.x - 150, screen_height // 2 + 100, 100, 40)

    while not rl.window_should_close() :
        # Calculate text size and position
        text = f"{elapsed_time:.1f}"
        text_size = rl.measure_text(text, font_size)
        text_x = (screen_width - text_size) // 2
        text_y = (screen_height - font_size) // 2 - 50

        # Check if the mouse is over the stop button, start button, and lap button
        mouse_point = rl.get_mouse_position()
        is_over_button = rl.check_collision_point_rec(mouse_point, stop_button)
        is_start_button = rl.check_collision_point_rec(mouse_point, start_button)
        is_lap_button = rl.check_collision_point_rec(mouse_point, lap_button)
        is_reset_button = rl.check_collision_point_rec(mouse_point, reset_button)

        # Check for user input to stop the timer
        if is_over_button and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            continue_timer = False
            start_time = 0

        # Check for user input to start the timer
        if is_start_button and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            continue_timer = True
            start_time = time.time() - elapsed_time

        # Check for user input to record lap time
        if is_lap_button and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            with open(file_path, 'a') as file:
                file.write(f"Lap Time: {elapsed_time:.1f} seconds\n")

        if is_reset_button and rl.is_mouse_button_released(rl.MOUSE_LEFT_BUTTON):
            elapsed_time = 0
            start_time = 0
            continue_timer = False

        # Draw
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        rl.draw_text(text, text_x, text_y, font_size, rl.MAROON)

        # Draw stop button
        rl.draw_rectangle_rec(stop_button, rl.GRAY)
        rl.draw_text("Stop", int(stop_button.x) + 25, int(stop_button.y) + 10, int(20), rl.BLACK)

        # Draw start button
        rl.draw_rectangle_rec(start_button, rl.GRAY)
        rl.draw_text("Start", int(start_button.x) + 25, int(start_button.y) + 10, int(20), rl.BLACK)

        # Draw lap button
        rl.draw_rectangle_rec(lap_button, rl.GRAY)
        rl.draw_text("Lap", int(lap_button.x) + 25, int(lap_button.y) + 10, int(20), rl.BLACK)

        # Draw record num button
        rl.draw_rectangle_rec(reset_button, rl.GRAY)
        rl.draw_text("Reset", int(reset_button.x) + 25, int(reset_button.y) + 10, int(20), rl.RED)

        if continue_timer:  
            # Update timer
            elapsed_time = time.time() - start_time

        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
