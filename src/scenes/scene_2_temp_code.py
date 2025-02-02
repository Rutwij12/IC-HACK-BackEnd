from manim import *

class FinalSquare(Scene):
    def construct(self):
        # Create the square with specified dimensions and colors
        square = Square(
            side_length=2,
            fill_color=rgb_to_color([135/255, 206/255, 235/255]),
            fill_opacity=0.5,
            stroke_color=rgb_to_color([0/255, 119/255, 190/255]),
            stroke_width=2
        )
        
        # Center the square at origin (0,0)
        square.move_to(ORIGIN)
        
        # Animation sequence
        # 1. Fade in the square (2 seconds)
        self.play(
            FadeIn(square, rate_func=rate_functions.ease_in_cubic),
            run_time=2
        )
        
        # 2. Hold the square static (3 seconds)
        self.wait(3)
        
        # 3. Fade out the square
        self.play(
            FadeOut(square, rate_func=rate_functions.ease_out_cubic),
            run_time=1
        )