from manim import *

class TitleScene(Scene):
    def construct(self):
        # Create the main title text
        title = Text(
            "Circle to Square Transformation",
            font="Helvetica",
            font_size=60  # Adjusted for good visibility (approximately 1/6th of screen height)
        )
        
        # Center the title
        title.move_to(ORIGIN)
        
        # Initial state: text with opacity 0
        title.set_opacity(0)
        
        # 1. Fade in (0-2 seconds)
        self.play(
            FadeIn(title, rate_func=smooth),
            run_time=2
        )
        
        # 2. Static display (2-4 seconds)
        self.wait(2)
        
        # 3. Fade out (4-5 seconds)
        self.play(
            FadeOut(title, rate_func=smooth),
            run_time=1
        )