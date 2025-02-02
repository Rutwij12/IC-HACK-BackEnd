from manim import *

class DerivativeAsTangentSlope(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 4, 1],
            axis_config={"color": GREY},
            tips=True
        ).scale(0.8).shift(DOWN * 0.5)  # Slightly down to make room for text

        # Create the function graph f(x) = x²
        function = axes.plot(lambda x: x**2, color=BLUE)
        
        # Create function label
        function_label = MathTex("f(x) = x^2", color=BLUE)\
            .scale(0.8)\
            .to_corner(UR)\
            .shift(LEFT * 0.5)

        # Initial animations
        self.play(
            Create(axes),
            run_time=1
        )
        self.play(
            Create(function),
            Write(function_label),
            run_time=2
        )

        # Create point and tangent line
        dot = Dot(color=RED).scale(0.8)
        tangent_line = Line(color=YELLOW)
        
        # Function to update point and tangent line
        def update_point_and_line(t):
            # Calculate x position (moving from -1 to 1)
            x = -1 + 2 * t
            # Get point on curve
            point = axes.c2p(x, x**2)
            dot.move_to(point)
            
            # Calculate slope at point (derivative = 2x)
            slope = 2 * x
            
            # Create tangent line points
            dx = 1  # Half-length of tangent line
            x1 = x - dx
            x2 = x + dx
            y1 = x**2 + slope * (-dx)
            y2 = x**2 + slope * dx
            
            start_point = axes.c2p(x1, y1)
            end_point = axes.c2p(x2, y2)
            
            tangent_line.put_start_and_end_on(start_point, end_point)

        # Animate point and tangent line
        self.play(
            Create(dot),
            Create(tangent_line)
        )

        # Animate movement
        self.play(
            UpdateFromAlphaFunc(
                dot,
                lambda mob, alpha: update_point_and_line(alpha)
            ),
            UpdateFromAlphaFunc(
                tangent_line,
                lambda mob, alpha: update_point_and_line(alpha)
            ),
            rate_func=linear,
            run_time=8
        )

        # Add final text
        final_text = Text("Derivative = Slope of Tangent Line", 
                         font="Times New Roman")\
            .scale(0.8)\
            .to_edge(DOWN)\
            .shift(UP * 0.3)

        self.play(
            Write(final_text),
            run_time=2
        )

        # Hold for a moment
        self.wait(2)