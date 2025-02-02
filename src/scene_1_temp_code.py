from manim import *
import numpy as np

class CircleToSquareTransformation(Scene):
    def construct(self):
        # Create the initial circle with radius 2
        circle = Circle(radius=2, stroke_width=2, stroke_color=WHITE)
        
        # Calculate square side length to maintain same perimeter
        # Circle perimeter = 4π, so square side length = 4π/4 = π
        side_length = PI
        
        # Create the target square centered at origin
        square = Square(side_length=side_length, stroke_width=2, stroke_color=WHITE)
        
        # Create smooth transition by increasing the number of anchor points
        circle.set_n_points(100)
        square.set_n_points(100)
        
        # Initial circle creation animation
        self.play(
            Create(circle),
            run_time=2
        )
        
        # Brief pause after circle creation
        self.wait()
        
        # Transform circle to square
        self.play(
            Transform(
                circle,
                square,
                rate_func=smooth,
                run_time=8
            )
        )
        
        # Brief pause on final square
        self.wait()
        
        # Fade out the final shape
        self.play(
            FadeOut(circle),
            run_time=1
        )
        
        # Final brief pause
        self.wait(0.5)