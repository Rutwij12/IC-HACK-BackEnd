from manim import *

class EigenvectorVisualization(Scene):
    def construct(self):
        # Create coordinate system
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GRAY_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).set_opacity(0.5)

        # Initial vector
        vector = Vector([1, 1], color=YELLOW)
        vector_label = MathTex("\\vec{v}", color=WHITE).next_to(vector.get_end(), UP+RIGHT, buff=0.1)

        # Matrix and eigenvalue
        matrix = MathTex(
            "A = \\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}",
            color=WHITE
        ).to_corner(UR, buff=0.5)
        
        eigenvalue = MathTex("\\lambda = 3", color=WHITE).next_to(matrix, DOWN)

        # Transformed vector (scaled by λ=3)
        transformed_vector = Vector([3, 3], color=YELLOW)
        
        # Dashed line for transformation path
        dashed_line = DashedLine(
            vector.get_end(),
            transformed_vector.get_end(),
            color=GRAY_C
        )

        # Text elements
        transform_text = Text(
            "When transformed by matrix A...",
            color=WHITE,
            font_size=36
        ).to_edge(UP, buff=0.5)

        eigenvector_text = Text(
            "Eigenvector: Only scales, doesn't rotate",
            color=WHITE,
            font_size=36
        ).to_edge(DOWN, buff=0.5)

        # Animation sequence
        self.play(
            Create(plane),
            run_time=1
        )
        
        self.play(
            GrowArrow(vector),
            Write(vector_label),
            run_time=2
        )

        self.play(
            Write(transform_text),
            Write(matrix),
            Write(eigenvalue),
            run_time=2
        )

        # Transform sequence
        self.play(
            vector.animate.set_opacity(0.3),
            GrowArrow(transformed_vector),
            Create(dashed_line),
            run_time=3
        )

        # Final text and glow effect
        self.play(
            Write(eigenvector_text),
            run_time=1
        )

        # Glow effect
        glow_group = VGroup(vector, transformed_vector)
        self.play(
            glow_group.animate.set_stroke(color=YELLOW, width=5),
            rate_func=there_and_back,
            run_time=2
        )

        # Pause for a moment at the end
        self.wait(1)