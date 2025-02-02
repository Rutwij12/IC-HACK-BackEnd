from manim import *

class VectorAndMatrix(Scene):
    def construct(self):
        # Create grid
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        # Create vector
        vector = Arrow(
            start=ORIGIN,
            end=[2, 1, 0],
            color=YELLOW,
            buff=0
        )
        vector_label = MathTex("\\vec{v}", color=WHITE).next_to(
            vector.get_end(), UP + RIGHT, buff=0.2
        )
        
        # Create matrix
        matrix = MathTex(
            "\\begin{bmatrix} 2 & -1 \\\\ 1 & 1 \\end{bmatrix}",
            color=WHITE
        ).scale(1.2)
        matrix_label = MathTex("A = ", color=WHITE).scale(1.2)
        
        # Position matrix on right side
        matrix_group = VGroup(matrix_label, matrix).arrange(RIGHT)
        matrix_group.move_to(RIGHT * 3)
        
        # Create "Transformation Matrix" text
        transform_text = Text(
            "Transformation Matrix",
            color=WHITE,
            font_size=24
        ).next_to(matrix_group, DOWN, buff=0.5)
        
        # Part 1: Vector Introduction (0-4 seconds)
        self.play(
            Create(grid),
            run_time=1
        )
        self.play(
            Create(vector),
            Write(vector_label),
            run_time=1
        )
        self.wait(1)
        
        # Part 2: Matrix Introduction (4-8 seconds)
        self.play(
            Write(matrix_label),
            Write(matrix),
            run_time=2
        )
        self.play(
            Write(transform_text),
            run_time=1
        )
        self.wait(1)
        
        # Part 3: Final Touch (8-12 seconds)
        # Create glow effect by scaling up and down quickly
        self.play(
            vector.animate.scale(1.2),
            matrix_group.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            vector.animate.scale(1/1.2),
            matrix_group.animate.scale(1/1.2),
            run_time=0.5
        )
        
        self.wait(1)