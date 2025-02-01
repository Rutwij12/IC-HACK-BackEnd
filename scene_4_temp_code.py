from manim import *
import numpy as np

class MatrixRotationExample(Scene):
    def construct(self):
        # 1. Initial Setup
        title = Text("Matrix Rotation Example").scale(0.8).move_to(UP * 3.5)
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": "#CCCCCC",
                "stroke_opacity": 0.5
            },
            axis_config={"stroke_color": "#999999"}
        ).scale(0.8)

        # Original point and label
        original_point = Dot(plane.coords_to_point(2, 1), color=BLUE)
        original_label = Text("P(2,1)").scale(0.6).set_color(BLUE).next_to(original_point, UR * 0.3)

        # 2. Matrix elements
        rotation_matrix = MathTex(
            "R = \\begin{bmatrix} 0.707 & -0.707 \\\\ 0.707 & 0.707 \\end{bmatrix}"
        ).scale(0.8).move_to(LEFT * 5 + UP * 2)
        
        matrix_label = Text("45° Rotation Matrix").scale(0.6).next_to(rotation_matrix, UP * 0.5)

        # 3. Matrix multiplication
        multiplication = MathTex(
            "\\begin{bmatrix} 0.707 & -0.707 \\\\ 0.707 & 0.707 \\end{bmatrix}",
            "\\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix}",
            "=",
            "\\begin{bmatrix} 0.707 \\\\ 2.121 \\end{bmatrix}"
        ).scale(0.7).move_to(LEFT * 5)

        # Final point and arc
        end_point = Dot(plane.coords_to_point(0.707, 2.121), color=RED)
        end_label = Text("P'(0.707, 2.121)").scale(0.6).set_color(RED).next_to(end_point, UR * 0.3)
        
        # Create rotation arc
        start_angle = np.arctan2(1, 2)
        radius = np.sqrt(5) * plane.get_x_unit_size()  # Fixed: using get_x_unit_size()
        arc = Arc(
            radius=radius,
            arc_center=plane.get_origin(),
            start_angle=start_angle,
            angle=PI/4,
            color=RED
        )

        # Animations
        self.play(Write(title))
        self.play(Create(plane))
        self.play(Create(original_point), Write(original_label))
        self.wait()

        # Fade out title and show matrix
        self.play(FadeOut(title))
        self.play(
            Write(rotation_matrix),
            Write(matrix_label)
        )
        self.wait()

        # Show transformation
        self.play(Write(multiplication))
        self.play(
            original_point.animate.set_opacity(0.5),
            original_label.animate.set_opacity(0.5)
        )
        self.play(
            Create(arc),
            Create(end_point)
        )
        self.play(Write(end_label))
        self.wait()