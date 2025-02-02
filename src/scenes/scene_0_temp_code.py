from manim import *

class ShapeMorphingIntro(Scene):
    def construct(self):
        # Create the circle with specified properties
        circle = Circle(
            radius=1.5,
            color=WHITE,
            fill_color="#2E86C1",
            fill_opacity=1,
            stroke_width=3
        )
        
        # Initial pause (0-1 seconds)
        self.wait(1)
        
        # Combine Create and FadeIn animations with scaling
        circle.scale(0.8)  # Start from smaller size
        self.play(
            Create(circle),
            FadeIn(circle),
            circle.animate.scale(1.25),  # Scale to final size (1/0.8 = 1.25)
            run_time=3,
            rate_func=smooth
        )
        
        # Hold the circle static (4-6 seconds)
        self.wait(2)
        
        # Fade out the circle (6-8 seconds)
        self.play(
            FadeOut(circle),
            run_time=2,
            rate_func=smooth
        )