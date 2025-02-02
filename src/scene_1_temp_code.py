from manim import *

class EigenvalueVisualization(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": GRAY},
            tips=False
        ).set_opacity(0.3)
        
        # Add light gray grid
        grid = NumberPlane(
            x_range=[-5, 5],
            y_range=[-5, 5],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.3
            }
        )

        # Add coordinate system and grid
        self.play(
            Create(grid),
            Create(axes),
            run_time=1
        )

        # Create original vector
        vector_v = Vector([2, 1], color=BLUE)
        vector_v_label = MathTex("v").set_color(BLUE)
        vector_v_label.next_to(vector_v.get_end(), UP + RIGHT, buff=0.1)

        # Show original vector
        self.play(
            GrowArrow(vector_v),
            Write(vector_v_label),
            run_time=1.5
        )
        self.wait(0.5)

        # Create transformed vector
        vector_av = Vector([4, 2], color=RED)
        vector_av_label = MathTex("Av").set_color(RED)
        vector_av_label.next_to(vector_av.get_end(), UP + RIGHT, buff=0.1)

        # Animate transformation
        self.play(
            Transform(vector_v.copy(), vector_av),
            run_time=2
        )
        self.play(Write(vector_av_label))
        
        # Create dashed line connecting vector tips
        dashed_line = DashedLine(
            vector_v.get_end(),
            vector_av.get_end(),
            dash_length=0.15,
            color=GRAY
        )
        
        # Show dashed line
        self.play(Create(dashed_line))

        # Create and show eigenvalue equation
        lambda_text = MathTex("\\lambda = 2").scale(1.2)
        lambda_text.move_to([-3, 2, 0])
        
        eigen_equation = MathTex("A", "v", "=", "\\lambda", "v")
        eigen_equation.set_color_by_tex_to_color_map({
            "A": WHITE,
            "v": BLUE,
            "\\lambda": WHITE
        })
        eigen_equation.move_to([-3, 1.5, 0])

        self.play(
            Write(lambda_text),
            Write(eigen_equation),
            run_time=1.5
        )

        # Pulse animation for both vectors
        self.play(
            vector_v.animate.scale(1.2),
            vector_av.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1
        )

        # Final pause
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )