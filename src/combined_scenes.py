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
        with self.voiceover(text="""Let's look at the parabola function x squared. As we plot the curve from zero to one and shade underneath, we can find that the exact area equals one-third using integration.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create the coordinate system
            grid = NumberPlane(
                x_range=[-0.5, 1.5, 0.5],
                y_range=[0, 1.5, 0.5],
                x_length=8,
                y_length=6,
                background_line_style={
                    "stroke_color": "#ecf0f1",
                    "stroke_width": 1,
                    "stroke_opacity": 0.8
                }
            ).shift(LEFT)
            axes = Axes(
                x_range=[-0.5, 1.5, 0.5],
                y_range=[0, 1.5, 0.5],
                x_length=8,
                y_length=6,
                axis_config={
                    "stroke_color": "#2c3e50",
                    "stroke_width": 2,
                }
            ).shift(LEFT)
            # Create axis labels
            x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
            y_label = MathTex("y").next_to(axes.y_axis, UP)
            # Create the curve
            curve = axes.plot(
                lambda x: x**2,
                x_range=[0, 1],
                color="#3498db",
                stroke_width=3
            )
            # Create area
            area = axes.get_area(
                curve,
                x_range=(0, 1),
                color="#3498db",
                opacity=0.4
            )
            # Create vertical lines
            v_line_0 = DashedLine(
                axes.c2p(0, 0),
                axes.c2p(0, 0.5),
                dash_length=0.1,
                color="#95a5a6"
            )
            v_line_1 = DashedLine(
                axes.c2p(1, 0),
                axes.c2p(1, 1),
                dash_length=0.1,
                color="#95a5a6"
            )
            # Create text
            function_label = MathTex("f(x) = x^2").scale(1.2)
            function_label.move_to(axes.c2p(1.5, 1.3))
            area_text = MathTex(r"\text{Area} = \int_0^1 x^2 dx = \frac{1}{3}").scale(1.2)
            area_text.move_to(axes.c2p(1.5, 0.8))
            # Animation sequence
            self.play(
                FadeIn(grid),
                Create(axes),
                FadeIn(x_label),
                FadeIn(y_label),
                run_time=3
            )
            self.play(
                Create(curve),
                run_time=3
            )
            self.play(
                Write(function_label),
                run_time=2
            )
            self.play(
                Create(v_line_0),
                Create(v_line_1),
                run_time=1
            )
            self.play(
                FadeIn(area),
                run_time=2
            )
            self.play(
                Write(area_text),
                run_time=2
            )
            self.wait(2)

        # Scene 2
        with self.voiceover(text="""We start with a parabola and break it into rectangles. As we increase the number of rectangles from 4 to 8 to 16, watch how our approximation of the area under the curve becomes more accurate.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 3
        with self.voiceover(text="""Let's find an antiderivative using the power rule. Starting with x squared, we first add 1 to the exponent, giving us x cubed. Then, we divide by the new exponent - 3 - to get our antiderivative: x cubed over 3.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Title
            title = Text("Power Rule for Antiderivatives").scale(0.8)
            title.to_edge(UP, buff=0.5)
            # Original function setup
            original_label = Text("Original Function:", color=WHITE).scale(0.6)
            original_function = MathTex("f(x) = x^2", color=BLUE)
            original_group = VGroup(original_label, original_function).arrange(DOWN, buff=0.3)
            original_group.move_to(LEFT * 3)
            # Arrows and transformation labels
            arrow1 = Arrow(LEFT * 1.5, RIGHT * 0.5, color=GRAY)
            arrow1.next_to(original_function, RIGHT, buff=0.5)
            step1_label = Text("+1 to exponent", color=WHITE).scale(0.5)
            step1_label.next_to(arrow1, UP, buff=0.2)
            # First transformation
            intermediate = MathTex("x^3", color=BLUE)
            intermediate.next_to(arrow1, RIGHT, buff=0.5)
            # Second arrow and label
            arrow2 = Arrow(LEFT * 0.5, RIGHT * 1.5, color=GRAY)
            arrow2.next_to(intermediate, RIGHT, buff=0.5)
            step2_label = Text("÷ by new exponent (3)", color=WHITE).scale(0.5)
            step2_label.next_to(arrow2, UP, buff=0.2)
            # Final antiderivative
            antider_label = Text("Antiderivative:", color=WHITE).scale(0.6)
            final_function = MathTex("F(x) = \\frac{x^3}{3}", color=GREEN)
            final_group = VGroup(antider_label, final_function).arrange(DOWN, buff=0.3)
            final_group.move_to(RIGHT * 3)
            # Animations
            self.play(FadeIn(title), run_time=0.5)
            self.play(
                FadeIn(original_label),
                FadeIn(original_function),
                run_time=1
            )
            self.play(
                Create(arrow1),
                FadeIn(step1_label),
                run_time=1
            )
            self.play(
                TransformFromCopy(original_function, intermediate),
                run_time=1.5
            )
            self.play(
                Create(arrow2),
                FadeIn(step2_label),
                run_time=1
            )
            self.play(
                TransformFromCopy(intermediate, final_function),
                FadeIn(antider_label),
                run_time=1.5
            )
            # Hold the final scene
            self.wait(2)

        # Scene 4
        with self.voiceover(text="""Let's understand how the Fundamental Theorem of Calculus works with a simple example. Using x-squared as our function, we'll find the area between x equals 1 and 2 by using its antiderivative. Watch as we evaluate step by step to arrive at our final answer of seven-thirds.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Title and General Formula
            title = Text("Fundamental Theorem of Calculus", font_size=40)
            title.to_edge(UP, buff=0.5)
            general_formula = MathTex(
                r"\int_a^b f(x)dx = F(b) - F(a)",
                font_size=36
            )
            general_formula.next_to(title, DOWN, buff=0.3)
            subtitle = Text("where F(x) is the antiderivative of f(x)", font_size=28)
            subtitle.next_to(general_formula, DOWN, buff=0.2)
            # Animate Part 1
            self.play(Write(title), run_time=1)
            self.play(
                Write(general_formula),
                Write(subtitle),
                run_time=1.5
            )
            # Group and move initial elements up
            initial_group = VGroup(title, general_formula, subtitle)
            self.play(
                initial_group.animate.scale(0.8).to_edge(UP, buff=0.2),
                run_time=1
            )
            # Part 2: Specific Example
            integral = MathTex(
                r"\int_1^2 x^2 dx = \left[\frac{1}{3}x^3\right]_1^2",
                font_size=36
            )
            integral.move_to(ORIGIN)
            steps = VGroup(
                MathTex(r"= \frac{1}{3}(2^3) - \frac{1}{3}(1^3)", font_size=36),
                MathTex(r"= \frac{1}{3}(8) - \frac{1}{3}(1)", font_size=36),
                MathTex(r"= \frac{8}{3} - \frac{1}{3}", font_size=36),
                MathTex(r"= \frac{7}{3}", font_size=36)
            )
            # Position steps
            for i, step in enumerate(steps):
                if i == 0:
                    step.next_to(integral, DOWN, buff=0.5)
                else:
                    step.next_to(steps[i-1], DOWN, buff=0.3)
            # Animate Part 2
            self.play(Write(integral), run_time=1)
            for step in steps:
                self.play(Write(step), run_time=0.75)
            # Part 3: Highlight Final Answer
            final_answer = steps[-1]
            highlighted_answer = MathTex(r"= \frac{7}{3}", font_size=48, color=YELLOW)
            highlighted_answer.move_to(final_answer)
            brace = Brace(highlighted_answer, DOWN)
            brace_text = Text(
                "Area under curve from x=1 to x=2",
                font_size=24
            )
            brace_text.next_to(brace, DOWN, buff=0.2)
            # Animate Part 3
            self.play(
                ReplacementTransform(final_answer, highlighted_answer),
                run_time=0.75
            )
            self.play(
                Create(brace),
                Write(brace_text),
                run_time=1
            )
            # Pause at the end
            self.wait(1)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
