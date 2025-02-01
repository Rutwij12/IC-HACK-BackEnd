from manim import *

class FunctionIntroduction(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#FFFFFF"

        # 1. Initial Setup - Title
        title = Text("Functions: The Building Blocks", font_size=40)
        title.set_color("#3B82F6")
        title.to_edge(UP, buff=0.5)

        # 2. Function Introduction
        function_eq = MathTex("y = 2x")
        function_eq.next_to(title, DOWN, buff=0.5)

        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={
                "color": BLACK,
                "stroke_width": 2,
                "include_tip": True,
            },
            x_length=6,
            y_length=6
        )
        axes.shift(DOWN * 0.5)

        # Add labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        # Create function line
        line = axes.plot(lambda x: 2*x, color="#EF4444")
        
        # Create dot and its labels
        dot = Dot(color="#10B981")
        dot.move_to(axes.c2p(1, 2))
        
        input_label = MathTex("\\text{Input: }1").scale(0.8)
        output_label = MathTex("\\text{Output: }2").scale(0.8)
        
        # Position labels near the dot
        input_label.next_to(axes.c2p(1, 0), DOWN)
        output_label.next_to(axes.c2p(0, 2), LEFT)
        
        # Create dashed lines
        v_line = DashedLine(
            axes.c2p(1, 0),
            axes.c2p(1, 2),
            color=GRAY
        )
        h_line = DashedLine(
            axes.c2p(0, 2),
            axes.c2p(1, 2),
            color=GRAY
        )

        # Animation sequence
        self.play(FadeIn(title), run_time=1)
        self.play(Write(function_eq), run_time=1)
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        self.play(Create(line), run_time=2)
        
        # Animate dot movement
        self.play(
            FadeIn(dot),
            Create(v_line),
            Create(h_line),
            Write(input_label),
            Write(output_label),
            run_time=2
        )
        
        # Hold final state
        self.wait(2)
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )