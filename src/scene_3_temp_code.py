from manim import *

class FundamentalTheoremCalculus(Scene):
    def construct(self):
        # Initial setup
        title = Text("Fundamental Theorem of Calculus").scale(0.8).to_edge(UP, buff=0.5)
        initial_eq = MathTex("f(x) = x^2").next_to(title, DOWN, buff=0.5)

        # Create coordinate system
        axes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 16, 4],
            axis_config={"include_numbers": True},
            tips=False
        ).scale(0.6).shift(DOWN)

        # Create function curve
        curve = axes.plot(lambda x: x**2, x_range=[0, 4], color=BLUE)
        
        # Animate initial setup
        self.play(Write(title), run_time=1)
        self.play(Write(initial_eq), run_time=1)
        self.play(Create(axes), Create(curve), run_time=2)

        # Part 2: Area Function
        area_eq = MathTex(r"{\text{Area Function: }}F(x) = \int_0^x t^2 dt").scale(0.8)
        area_eq.next_to(title, DOWN, buff=0.5)

        # Create moving area
        x_tracker = ValueTracker(0)
        area = always_redraw(
            lambda: axes.get_area(
                curve,
                x_range=[0, x_tracker.get_value()],
                color=[BLUE_D],
                opacity=0.3
            )
        )

        # Area value display
        area_value = DecimalNumber(
            0,
            num_decimal_places=2,
            include_sign=False,
        ).scale(0.6)
        area_value.next_to(axes, RIGHT, buff=0.5)
        area_value.add_updater(
            lambda m: m.set_value((x_tracker.get_value()**3)/3)
        )

        # Part 2 animations
        self.play(
            ReplacementTransform(initial_eq, area_eq),
            Create(area),
        )
        self.add(area_value)
        self.play(x_tracker.animate.set_value(2), run_time=3)

        # Part 3: Derivative Connection
        derivative_eq = MathTex("F'(x) = f(x)").scale(0.8)
        derivative_eq.next_to(area_eq, DOWN, buff=0.3)

        point = Dot(axes.c2p(2, 4), color=YELLOW)
        point_value = MathTex(
            r"\text{At }x=2:",
            r"F(2) = \frac{8}{3}",
            r"F'(2) = f(2) = 4"
        ).scale(0.7)
        point_value.arrange(DOWN, aligned_edge=LEFT).next_to(derivative_eq, DOWN, buff=0.3)

        # Final animations
        self.play(Write(derivative_eq))
        self.play(Create(point))
        self.play(Write(point_value))

        # Pulsing animation for the point
        self.play(
            point.animate.scale(2),
            rate_func=there_and_back,
            run_time=1
        )
        self.play(
            point.animate.scale(2),
            rate_func=there_and_back,
            run_time=1
        )

        # Hold final state
        self.wait()