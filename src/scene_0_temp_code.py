from manim import *

class AreaUnderCurve(Scene):
    def construct(self):
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