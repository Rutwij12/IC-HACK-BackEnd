from manim import *
import numpy as np

class MatrixTransformation(Scene):
    def construct(self):
        # Set up the coordinate grid
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": "#888888",
                "stroke_width": 0.5,
                "stroke_opacity": 0.5,
            }
        )

        # Define vectors
        v1 = Arrow(start=ORIGIN, end=RIGHT, color=RED, tip_length=0.2)
        v2 = Arrow(start=ORIGIN, end=UP, color=BLUE, tip_length=0.2)
        
        # Create vector labels
        v1_label = MathTex("v_1", color=RED).next_to(v1.get_end(), RIGHT*0.3 + UP*0.3)
        v2_label = MathTex("v_2", color=BLUE).next_to(v2.get_end(), LEFT*0.3 + UP*0.3)

        # Define transformation matrix
        matrix = [[2, 1], [-1, 1]]
        matrix_tex = MathTex(
            "M = \\begin{bmatrix} 2 & 1 \\\\ -1 & 1 \\end{bmatrix}"
        ).scale(0.8).to_corner(UR, buff=0.5)

        # Step 1: Fade in grid and vectors
        self.play(
            Create(grid),
            GrowArrow(v1),
            GrowArrow(v2),
            Write(v1_label),
            Write(v2_label),
            run_time=3
        )

        # Step 2: Show matrix
        self.play(Write(matrix_tex), run_time=1.5)

        # Create transformed vectors
        v1_transformed = Arrow(
            start=ORIGIN,
            end=np.array([2, -1, 0]),
            color=RED,
            tip_length=0.2
        )
        v2_transformed = Arrow(
            start=ORIGIN,
            end=np.array([1, 1, 0]),
            color=BLUE,
            tip_length=0.2
        )

        # Create transformed vector labels
        mv1_label = MathTex("Mv_1", color=RED).next_to(v1_transformed.get_end(), RIGHT*0.3 + UP*0.3)
        mv2_label = MathTex("Mv_2", color=BLUE).next_to(v2_transformed.get_end(), RIGHT*0.3 + UP*0.3)

        # Step 3: Apply transformation
        self.play(
            grid.animate.apply_matrix(matrix),
            Transform(v1, v1_transformed),
            Transform(v2, v2_transformed),
            v1_label.animate.set_opacity(0.3),
            v2_label.animate.set_opacity(0.3),
            run_time=6
        )

        # Step 4: Add transformed labels
        self.play(
            Write(mv1_label),
            Write(mv2_label),
            run_time=1.5
        )

        # Final pause
        self.wait(1.5)