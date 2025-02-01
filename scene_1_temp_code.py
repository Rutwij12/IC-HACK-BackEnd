from manim import *

class UnitVectors(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "include_ticks": True,
                "tick_size": 0.1,
            },
        )
        
        # Add labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        coords = VGroup(axes, x_label, y_label)

        # Fade in coordinate system
        self.play(Create(coords), run_time=2)
        
        # Create i-hat vector
        i_hat = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 0),
            color=RED,
            buff=0
        )
        i_hat_label = MathTex(r"\hat{\imath}").next_to(i_hat.get_tip(), UP, buff=0.2).set_color(RED)
        
        # Draw i-hat vector and label
        self.play(Create(i_hat), Write(i_hat_label))
        self.play(Flash(i_hat.get_tip(), color=RED, flash_radius=0.3))
        
        # Create j-hat vector
        j_hat = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 1),
            color=BLUE,
            buff=0
        )
        j_hat_label = MathTex(r"\hat{\jmath}").next_to(j_hat.get_tip(), RIGHT, buff=0.2).set_color(BLUE)
        
        # Draw j-hat vector and label
        self.play(Create(j_hat), Write(j_hat_label))
        self.play(Flash(j_hat.get_tip(), color=BLUE, flash_radius=0.3))
        
        # Create matrix
        matrix = MathTex(
            r"\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}"
        ).scale(0.8).move_to([4, 2, 0])
        matrix_text = Text("Unit vectors as matrix columns", font_size=24).next_to(matrix, DOWN)
        
        # Create dashed lines connecting matrix to vectors
        dash_to_i = DashedLine(
            matrix.get_left() + LEFT * 0.3,
            i_hat.get_tip(),
            color=RED,
            opacity=0.5
        )
        dash_to_j = DashedLine(
            matrix.get_right() + RIGHT * 0.3,
            j_hat.get_tip(),
            color=BLUE,
            opacity=0.5
        )
        
        # Show matrix, text, and dashed lines
        self.play(
            Write(matrix),
            Write(matrix_text),
            Create(dash_to_i),
            Create(dash_to_j)
        )
        
        # Add bottom text
        bottom_text = Text("Basis of 2D space", font_size=28).move_to([0, -2.5, 0])
        
        # Final highlight and text
        self.play(
            Write(bottom_text),
            Flash(i_hat.get_tip(), color=RED, flash_radius=0.3),
            Flash(j_hat.get_tip(), color=BLUE, flash_radius=0.3)
        )
        
        # Pause at the end
        self.wait()