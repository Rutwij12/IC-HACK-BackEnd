from manim import *
import random
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class CombinedScene(VoiceoverScene):
    def construct(self):
        # Set up Azure TTS service
        self.set_speech_service(AzureService(
            voice='en-US-JennyNeural',
            style='friendly'
        ))


        # Scene 1
        with self.voiceover(text="""Let's look at how we can approximate the area under this curve. As we add more rectangles beneath it, we get closer to finding the true area, though we can see the rectangles don't fit perfectly under the curve's shape.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create axes
            axes = Axes(
                x_range=[-1, 3, 1],
                y_range=[0, 9, 1],
                axis_config={
                    "include_numbers": True,
                    "include_ticks": True,
                    "stroke_width": 2
                },
                tips=False
            ).scale(0.8)
            # Center axes slightly below center
            axes.shift(DOWN * 0.5)
            # Create grid (subtle)
            grid = NumberPlane(
                x_range=[-1, 3, 1],
                y_range=[0, 9, 1],
                background_line_style={
                    "stroke_color": GREY,
                    "stroke_width": 0.5,
                    "stroke_opacity": 0.2
                },
                axis_config={"stroke_opacity": 0}
            ).scale(0.8)
            grid.shift(DOWN * 0.5)
            # Create function curve
            curve = axes.plot(
                lambda x: x**2,
                x_range=[0, 2],
                color=BLUE,
                stroke_width=2
            )
            # Create area
            area = axes.get_area(
                curve,
                x_range=[0, 2],
                color=BLUE,
                opacity=0.3
            )
            # Create "Area = ?" label
            area_label = Text(
                "Area = ?",
                font_size=30,
                color=WHITE
            ).move_to(axes.coords_to_point(1, 3))
            # Create rectangles
            rectangles = VGroup()
            x_values = [0, 0.5, 1, 1.5, 2]
            for i in range(len(x_values)-1):
                x = x_values[i]
                height = x**2
                dx = x_values[i+1] - x_values[i]
                rect = Rectangle(
                    width=dx * axes.get_x_unit_size(),
                    height=height * axes.get_y_unit_size(),
                    color=ORANGE,
                    fill_opacity=0.5,
                    stroke_width=1
                )
                rect.move_to(
                    axes.coords_to_point(x + dx/2, height/2),
                    aligned_edge=ORIGIN
                )
                rectangles.add(rect)
            # Create titles
            main_title = Text(
                "Approximating with Rectangles",
                font_size=36,
                color=WHITE
            ).to_edge(UP, buff=0.5)
            sub_title = Text(
                "Better approximation needs more rectangles",
                font_size=24,
                color=WHITE
            ).next_to(main_title, DOWN, buff=0.3)
            # Animation sequence
            self.play(
                Create(grid),
                Create(axes),
                run_time=1.5
            )
            self.play(
                Create(curve),
                run_time=1.5
            )
            self.play(
                FadeIn(area),
                Write(area_label),
                run_time=2
            )
            for rect in rectangles:
                self.play(
                    Create(rect),
                    run_time=0.3
                )
            self.wait(1)
            self.play(
                Write(main_title),
                Write(sub_title),
                run_time=2
            )
            self.wait(2)

        # Scene 2
        with self.voiceover(text="""Starting with a parabola, we approximate its area using rectangles. As we increase from 2 to 4 to 8 rectangles, watch how our approximation gets closer and closer to the true area of two-and-two-thirds square units.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create axes
            axes = Axes(
                x_range=[0, 2.5, 0.5],
                y_range=[0, 4.5, 1],
                axis_config={"color": WHITE},
                tips=False
            ).scale(1.2).shift(DOWN * 0.5)
            # Create the function curve
            def func(x):
                return x**2
            graph = axes.plot(func, color=BLUE, x_range=[0, 2])
            # Labels
            func_label = MathTex("f(x) = x^2").scale(0.8).to_corner(UL)
            # 1. Initial setup (0-3 seconds)
            self.play(
                Create(axes),
                run_time=1
            )
            self.play(
                Create(graph),
                Write(func_label),
                run_time=2
            )
            # 2. Two rectangles (3-6 seconds)
            rects_2 = VGroup()
            x_vals_2 = [0, 1, 2]
            for i in range(len(x_vals_2)-1):
                height = func(x_vals_2[i])
                rect = axes.get_riemann_rectangles(
                    graph,
                    x_range=[x_vals_2[i], x_vals_2[i+1]],
                    dx=(x_vals_2[i+1]-x_vals_2[i]),
                    input_sample_type="left",
                    color=YELLOW,
                    fill_opacity=0.5
                )
                rects_2.add(rect[0])
            sum_2 = MathTex("\\text{Sum} = 1.00").scale(0.8).to_corner(DR)
            self.play(
                Create(rects_2),
                Write(sum_2),
                run_time=3
            )
            # 3. Four rectangles (6-9 seconds)
            rects_4 = VGroup()
            x_vals_4 = [0, 0.5, 1, 1.5, 2]
            for i in range(len(x_vals_4)-1):
                height = func(x_vals_4[i])
                rect = axes.get_riemann_rectangles(
                    graph,
                    x_range=[x_vals_4[i], x_vals_4[i+1]],
                    dx=(x_vals_4[i+1]-x_vals_4[i]),
                    input_sample_type="left",
                    color=YELLOW,
                    fill_opacity=0.5
                )
                rects_4.add(rect[0])
            sum_4 = MathTex("\\text{Sum} \\approx 2.33").scale(0.8).to_corner(DR)
            self.play(
                ReplacementTransform(rects_2, rects_4),
                ReplacementTransform(sum_2, sum_4),
                run_time=3
            )
            # 4. Eight rectangles (9-12 seconds)
            rects_8 = VGroup()
            x_vals_8 = [i * 0.25 for i in range(9)]
            for i in range(len(x_vals_8)-1):
                height = func(x_vals_8[i])
                rect = axes.get_riemann_rectangles(
                    graph,
                    x_range=[x_vals_8[i], x_vals_8[i+1]],
                    dx=0.25,
                    input_sample_type="left",
                    color=YELLOW,
                    fill_opacity=0.5
                )
                rects_8.add(rect[0])
            sum_8 = MathTex("\\text{Sum} \\approx 2.65").scale(0.8).to_corner(DR)
            self.play(
                ReplacementTransform(rects_4, rects_8),
                ReplacementTransform(sum_4, sum_8),
                run_time=3
            )
            # 5. Final text (12-15 seconds)
            approx_text = Text("More rectangles → Better approximation", 
                              font_size=36).to_edge(UP)
            true_area = MathTex("\\text{True area} = \\frac{8}{3} \\approx 2.67"
                               ).scale(0.8).next_to(sum_8, UP)
            self.play(
                Write(approx_text),
                Write(true_area),
                run_time=3
            )

        # Scene 3
        with self.voiceover(text="""Here's how f(x) = x² helps us understand derivatives and integrals. The original function curves upward in blue. Its derivative shows us the slope at each point in green, while the red shaded area represents its integral. Together, they demonstrate how derivatives and integrals are inverse operations.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create the axes
            axes = Axes(
                x_range=[-2, 2, 0.5],
                y_range=[-3, 6, 1],
                axis_config={"color": GREY},
                tips=False
            ).add_coordinates()
            # Create the original function f(x) = x²
            function = axes.plot(lambda x: x**2, x_range=[-1.5, 1.5], color=BLUE)
            function_label = MathTex("f(x) = x^2", color=BLUE).move_to([1, 4, 0])
            # Initial display
            self.play(
                Create(axes),
                run_time=1
            )
            self.play(
                Create(function),
                Write(function_label),
                run_time=1
            )
            self.wait(1)
            # Derivative visualization
            x_point = 0.5
            slope = 2 * x_point
            point = axes.c2p(x_point, x_point**2)
            # Create tangent line using Line instead of TangentLine
            dx = 0.01
            point1 = axes.c2p(x_point - dx, (x_point - dx)**2)
            point2 = axes.c2p(x_point + dx, (x_point + dx)**2)
            tangent_vector = (point2 - point1) / (2 * dx)
            tangent_line = Line(
                point - tangent_vector,
                point + tangent_vector,
                color=GREEN
            ).scale(2)  # Scale to make the line longer
            derivative_label = MathTex("f'(x) = 2x", color=GREEN).move_to([1, 2, 0])
            slope_label = MathTex(f"\\text{{slope}} = {slope}", color=GREEN).scale(0.7).next_to(point, UR, buff=0.2)
            self.play(
                Create(tangent_line),
                Write(derivative_label),
                Write(slope_label),
                run_time=1
            )
            self.wait(1)
            # Integral visualization
            x_tracker = ValueTracker(0)
            area = always_redraw(
                lambda: axes.get_area(
                    function,
                    x_range=[0, x_tracker.get_value()],
                    color=RED,
                    opacity=0.3
                )
            )
            integral_label = MathTex("\\int f(x)dx = \\frac{x^3}{3}", color=RED).move_to([-1.5, -2, 0])
            self.play(
                FadeOut(tangent_line),
                FadeOut(slope_label),
                run_time=0.5
            )
            self.play(
                Create(area),
                x_tracker.animate.set_value(1.5),
                Write(integral_label),
                run_time=2
            )
            self.wait(1)
            # Final connection
            final_text = MathTex("F'(x) = f(x)", color=WHITE).move_to([0, -2.5, 0])
            # Highlight pulse of all functions
            self.play(
                function.animate.set_stroke(width=6),
                run_time=0.5
            )
            self.play(
                function.animate.set_stroke(width=2),
                Write(final_text),
                run_time=0.5
            )
            # Final pause
            self.wait(1)

        # Scene 4
        with self.voiceover(text="""The area under this parabola accumulates to create the antiderivative below. As we sweep from left to right, watch how each point on the orange curve represents the total area accumulated up to that position.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create axes for both plots
            top_axes = Axes(
                x_range=[0, 2.5, 0.5],
                y_range=[0, 4, 1],
                x_length=6,
                y_length=3,
                axis_config={"include_tip": False}
            ).shift(UP*1.5)
            bottom_axes = Axes(
                x_range=[0, 2.5, 0.5],
                y_range=[0, 4, 1],
                x_length=6,
                y_length=3,
                axis_config={"include_tip": False}
            ).shift(DOWN*1.5)
            # Create labels for the axes using Text instead of MathTex
            top_label = Text("f(x) = x²", font_size=24).next_to(top_axes, UP)
            bottom_label = Text("F(x) = ∫f(x)dx = (1/3)x³", font_size=24).next_to(bottom_axes, UP)
            # Create the function curves
            def f(x): return x**2
            def F(x): return (x**3)/3
            top_curve = top_axes.plot(f, color=BLUE, x_range=[0, 2])
            bottom_curve = bottom_axes.plot(F, color=ORANGE, x_range=[0, 2])
            # Initial setup animation
            self.play(
                Create(top_axes),
                Create(bottom_axes),
                Write(top_label),
                Write(bottom_label)
            )
            # Draw the original function
            self.play(Create(top_curve))
            # Create moving vertical line and point
            x_tracker = ValueTracker(0)
            vertical_line = always_redraw(
                lambda: top_axes.get_vertical_line(
                    top_axes.input_to_graph_point(x_tracker.get_value(), top_curve)
                ).set_color(YELLOW)
            )
            area = always_redraw(
                lambda: top_axes.get_area(
                    top_curve,
                    [0, x_tracker.get_value()],
                    color=BLUE,
                    opacity=0.3
                )
            )
            bottom_point = always_redraw(
                lambda: Dot(
                    bottom_axes.coords_to_point(
                        x_tracker.get_value(),
                        F(x_tracker.get_value())
                    ),
                    color=ORANGE
                )
            )
            bottom_trace = always_redraw(
                lambda: bottom_axes.plot(
                    F,
                    x_range=[0, x_tracker.get_value()],
                    color=ORANGE
                )
            )
            # Add vertical line and start area accumulation
            self.play(Create(vertical_line), Create(bottom_point))
            self.play(Create(area))
            # Animate the movement
            self.play(
                x_tracker.animate.set_value(2),
                Create(bottom_trace),
                run_time=6,
                rate_func=linear
            )
            # Add final label using Text instead of MathTex
            final_label = Text("F'(x) = f(x)", font_size=36).move_to(ORIGIN)
            # Highlight both curves
            self.play(
                Flash(top_curve, color=BLUE, line_length=0.2),
                Flash(bottom_curve, color=ORANGE, line_length=0.2),
                Write(final_label)
            )
            self.wait()

        # Scene 5
        with self.voiceover(text="""Let's see the power rule for integration in action. When integrating x raised to a power, we increase the power by one, divide by the new power, and add a constant. For example, integrating x squared becomes x cubed over three plus C. Notice how the integral function grows more steeply than the original.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # 1. Initial title and general formula
            title = MathTex(r"\text{Power Rule for Integration}").scale(1.2)
            general_formula = MathTex(r"\int x^n dx = \frac{x^{n+1}}{n+1} + C")
            title.move_to(UP * 3)
            general_formula.move_to(UP * 2)
            self.play(
                FadeIn(title),
                FadeIn(general_formula)
            )
            # 2. Specific example and solution
            self.play(
                title.animate.shift(UP * 0.5),
                general_formula.animate.shift(UP * 0.5)
            )
            example = MathTex(r"\int x^2 dx")
            step1 = MathTex(r"= \frac{x^{2+1}}{2+1} + C")
            step2 = MathTex(r"= \frac{x^3}{3} + C")
            example.move_to(UP * 1)
            step1.move_to(UP * 0.5)
            step2.move_to(ORIGIN)
            self.play(FadeIn(example))
            self.play(FadeIn(step1))
            self.play(FadeIn(step2))
            # Wait a moment to read
            self.wait()
            # 3. Fade out all previous elements
            self.play(
                FadeOut(title),
                FadeOut(general_formula),
                FadeOut(example),
                FadeOut(step1),
                FadeOut(step2)
            )
            # 4. Create coordinate system and plot curves
            axes = Axes(
                x_range=[-2, 2, 1],
                y_range=[-3, 3, 1],
                axis_config={"include_tip": True},
                x_length=6,
                y_length=6
            )
            # Add grid
            grid = axes.add_coordinates()
            # Create graphs
            function = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])
            antiderivative = axes.plot(lambda x: (x**3)/3, color=RED, x_range=[-2, 2])
            # Labels for the functions
            function_label = MathTex("f(x) = x^2").scale(0.8).move_to(RIGHT * 2 + UP * 1.5)
            antider_label = MathTex("F(x) = \\frac{x^3}{3}").scale(0.8).move_to(LEFT * 2 + DOWN * 2)
            # Add origin label
            origin_dot = Dot(axes.c2p(0, 0), radius=0.05)
            origin_label = MathTex("0").scale(0.6).next_to(origin_dot, DL, buff=0.1)
            # Show coordinate system and curves
            self.play(
                Create(axes),
                Create(grid)
            )
            self.play(
                Create(function),
                FadeIn(function_label)
            )
            self.play(
                Create(antiderivative),
                FadeIn(antider_label)
            )
            self.play(
                Create(origin_dot),
                Write(origin_label)
            )
            # Final pause
            self.wait(2)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
