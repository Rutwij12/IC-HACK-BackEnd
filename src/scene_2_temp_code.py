from manim import *
import numpy as np

class RiemannSumApproximation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 4.2, 1],
            axis_config={"include_tip": False},
            x_length=6,
            y_length=5
        ).shift(LEFT)

        # Add labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Create the function curve
        def func(x):
            return x**2

        curve = axes.plot(func, color=BLUE)
        
        # Function to create rectangles for Riemann sum
        def create_riemann_rectangles(n_rectangles):
            dx = 2/n_rectangles
            rectangles = VGroup()
            for i in range(n_rectangles):
                x = i * dx
                height = func(x)
                rect = Rectangle(
                    width=dx,
                    height=height,
                    fill_opacity=0.6,
                    fill_color=PURPLE,
                    stroke_width=1
                )
                rect.next_to(axes.c2p(x, 0), UP, buff=0)
                rect.stretch_to_fit_height(height * axes.y_axis.scaling.scale)
                rectangles.add(rect)
            return rectangles

        # Initial setup
        self.play(
            Create(axes),
            Create(x_label),
            Create(y_label),
            Create(curve),
            run_time=2
        )

        # Part 1: 4 rectangles
        rectangles_4 = create_riemann_rectangles(4)
        area_text_4 = MathTex("\\text{Area } \\approx 2.67").scale(0.8)
        area_text_4.to_corner(DR)

        self.play(
            Create(rectangles_4),
            Write(area_text_4),
            run_time=2
        )

        # Part 2: 8 rectangles
        rectangles_8 = create_riemann_rectangles(8)
        area_text_8 = MathTex("\\text{Area } \\approx 2.75").scale(0.8)
        area_text_8.to_corner(DR)

        self.play(
            Transform(rectangles_4, rectangles_8),
            Transform(area_text_4, area_text_8),
            run_time=2
        )

        # Part 3: 16 rectangles
        rectangles_16 = create_riemann_rectangles(16)
        area_text_16 = MathTex("\\text{Area } \\approx 2.83").scale(0.8)
        area_text_16.to_corner(DR)

        self.play(
            Transform(rectangles_4, rectangles_16),
            Transform(area_text_4, area_text_16),
            run_time=2
        )

        # Show true area
        true_area = MathTex("\\text{True Area } = 2.67").scale(0.8)
        true_area.next_to(area_text_16, DOWN)

        self.play(
            Write(true_area),
            run_time=1
        )

        # Final pause
        self.wait(2)