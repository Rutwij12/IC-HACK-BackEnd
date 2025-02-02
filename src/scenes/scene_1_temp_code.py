from manim import *

class CircleToSquare(Scene):
    def construct(self):
        # Create the initial circle
        circle = Circle(
            radius=2,
            stroke_width=2,
            color=WHITE,
            fill_opacity=0
        )

        # Create the target square
        square = Square(
            side_length=4,
            stroke_width=2,
            color=WHITE,
            fill_opacity=0
        )

        # Add circle to scene
        self.add(circle)

        # Pulse animation for the circle
        self.play(
            circle.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(1)

        # Transform circle to square
        self.play(
            Transform(
                circle,
                square,
                rate_func=smooth,
                run_time=6
            )
        )

        # Brief pause at the end
        self.wait(1)