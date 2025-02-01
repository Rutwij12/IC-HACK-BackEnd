from manim import *

class IntroductionToVectors(Scene):
    def construct(self):
        # 1. Coordinate System Introduction
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_ticks": True,
                "include_tip": True,
            },
        )
        
        # Add labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        # Create grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )

        # Animate coordinate system
        self.play(
            FadeIn(grid),
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )

        # 2. Vector Introduction
        # Create main vector
        vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(3, 2),
            buff=0,
            color="#FF4444",
            stroke_width=3,
        )

        # Animate vector creation
        self.play(
            GrowArrow(vector),
            run_time=2
        )
        self.wait()

        # 3. Component Breakdown
        # Create dashed lines for components
        x_component = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(3, 0),
            color="#3498DB",
            dash_length=0.2
        )
        
        y_component = DashedLine(
            axes.c2p(3, 0),
            axes.c2p(3, 2),
            color="#2ECC71",
            dash_length=0.2
        )

        # Create right angle symbol
        right_angle = RightAngle(
            x_component,
            y_component,
            length=0.2,
            color=WHITE
        )

        # Create component labels
        x_component_label = MathTex("3").scale(0.8)
        x_component_label.next_to(x_component, DOWN, buff=0.2)
        
        y_component_label = MathTex("2").scale(0.8)
        y_component_label.next_to(y_component, RIGHT, buff=0.2)

        # Create vector notation
        vector_notation = MathTex(r"\vec{v} = (3,2)")
        vector_notation.scale(0.8)
        vector_notation.move_to(axes.c2p(3, 3))

        # Animate components and labels
        self.play(
            Create(x_component),
            Create(y_component),
            run_time=2
        )
        
        self.play(
            Create(right_angle),
            Write(x_component_label),
            Write(y_component_label),
            run_time=2
        )

        self.play(
            Write(vector_notation),
            run_time=1
        )

        # Final pause
        self.wait(2)