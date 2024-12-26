import pyray as rl
import ctypes

def main():
    # Initialize window
    rl.init_window(800, 450, "Slider Bar Example")
    rl.set_target_fps(60)

    # Variable to hold the slider value
    slider_value = rl.ffi.new('float *', 50.0);

    # Main loop
    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        # Draw the slider bar
        rl.gui_slider_bar(rl.Rectangle(200, 200, 400, 40), "Value", "", slider_value, 0.0, 100.0)

        # Display the current value
        rl.draw_text(f"Current Value: {slider_value.value:.2f}", 250, 250, 20, rl.DARKGRAY)

        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
