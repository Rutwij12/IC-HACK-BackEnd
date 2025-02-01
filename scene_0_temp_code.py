from manim import *

class LinearFunctionTransformation(Scene):
    def construct(self):
        # Part 1: Function Introduction
        title = Text("Linear Function", font_size=36).shift(UP * 3)
        function = MathTex("y = 2x + 1", font_size=36).shift(UP * 2)
        
        self.play(
            Write(title),
            Write(function)
        )
        self.wait(0.5)

        # Part 2: Create number lines
        x_line = NumberLine(
            x_range=[-3, 5],
            length=6,
            include_numbers=True,
            include_tip=True
        ).shift(LEFT * 3)
        
        y_line = NumberLine(
            x_range=[-3, 5],
            length=6,
            include_numbers=True,
            include_tip=True
        ).shift(RIGHT * 3)

        x_label = Text("x", font_size=24).next_to(x_line, DOWN)
        y_label = Text("y", font_size=24).next_to(y_line, DOWN)

        self.play(
            Create(x_line),
            Create(y_line),
            Write(x_label),
            Write(y_label)
        )

        # Create function box
        function_box = Rectangle(height=1, width=2, fill_color=LIGHT_GRAY, 
                               fill_opacity=0.3, stroke_color=GRAY)
        box_text = MathTex("f(x) = 2x + 1", font_size=24)
        box_group = VGroup(function_box, box_text)

        self.play(
            Create(function_box),
            Write(box_text)
        )

        # Create dots and arrows
        input_outputs = [(0, 1), (1, 3), (2, 5)]
        colors = [BLUE, GREEN, RED]
        
        for i, (x_val, y_val) in enumerate(input_outputs):
            # Create dots
            x_dot = Dot(x_line.number_to_point(x_val), color=colors[i])
            y_dot = Dot(y_line.number_to_point(y_val), color=colors[i])
            
            # Create labels
            x_text = MathTex(f"x={x_val}", font_size=24, color=colors[i])\
                .next_to(x_dot, UP)
            y_text = MathTex(f"y={y_val}", font_size=24, color=colors[i])\
                .next_to(y_dot, UP)
            
            # Create curved arrow
            arrow = CurvedArrow(
                start_point=x_dot.get_center(),
                end_point=y_dot.get_center(),
                color=colors[i],
                stroke_width=2,
                angle=PI/4
            )

            # Animate elements
            self.play(
                Create(x_dot),
                Write(x_text),
                Create(arrow),
                Create(y_dot),
                Write(y_text),
                run_time=1
            )
            self.wait(0.5)

        # Final pause and fadeout
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )