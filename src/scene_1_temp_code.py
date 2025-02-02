from manim import *
import numpy as np

class RiemannSumsScene(Scene):
    def construct(self):
        # Create the coordinate system
        axes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False, "color": GREY},
        ).add_coordinates()
        
        # Create the function curve
        curve = axes.plot(lambda x: x**2, x_range=[0, 2], color=BLUE)
        
        # Create function label
        func_label = MathTex("f(x) = x^2").scale(0.8)
        func_label.to_corner(UR).shift(LEFT * 0.5)
        
        # Initial state (0-3s)
        self.play(
            FadeIn(axes),
            run_time=1
        )
        self.play(
            Create(curve),
            FadeIn(func_label),
            run_time=2
        )
        
        # Function to create rectangles
        def create_riemann_rectangles(n_rectangles):
            dx = 2 / n_rectangles
            rectangles = VGroup()
            for i in range(n_rectangles):
                x = i * dx
                height = x**2
                rect = Rectangle(
                    width=dx,
                    height=height,
                    fill_opacity=0.6,
                    fill_color=ORANGE,
                    stroke_width=0.5
                )
                rect.next_to(axes.c2p(x, 0), UP, buff=0)
                rect.stretch_to_fit_height(height * axes.y_axis.scaling.scale_factor)
                rectangles.add(rect)
            return rectangles
        
        # First approximation (3-6s)
        rects_4 = create_riemann_rectangles(4)
        self.play(
            FadeIn(rects_4),
            run_time=3
        )
        
        # Refinement (6-11s)
        rects_8 = create_riemann_rectangles(8)
        rects_16 = create_riemann_rectangles(16)
        
        self.play(
            ReplacementTransform(rects_4, rects_8),
            run_time=2.5
        )
        
        self.play(
            ReplacementTransform(rects_8, rects_16),
            run_time=2.5
        )
        
        # Final text (11-15s)
        final_text = Text(
            "As rectangles get thinner, approximation improves",
            font_size=24
        ).to_edge(DOWN)
        
        self.play(
            FadeIn(final_text),
            run_time=2
        )
        
        # Hold for remaining time
        self.wait(2)