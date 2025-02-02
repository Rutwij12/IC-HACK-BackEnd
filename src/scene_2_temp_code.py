from manim import *

class FinalFadeOutScene(Scene):
    def construct(self):
        # Create the square with specified dimensions
        square = Square(
            side_length=4,
            stroke_color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.1
        ).move_to(ORIGIN)

        # Add the square to the scene (assuming it's continuing from previous scene)
        # In a real continuation, you might not need this line
        self.add(square)

        # 1. Hold Time (1 second)
        self.wait(1)

        # 2. Fade Out Animation with scale
        # Create animation that combines scaling and fading
        fade_out_anim = AnimationGroup(
            square.animate.scale(1.1),
            square.animate.set_opacity(0),
            rate_func=smooth,
            run_time=2.5
        )
        
        # Play the combined animation
        self.play(fade_out_anim)

        # Small wait at the end to ensure clean finish
        self.wait(0.5)