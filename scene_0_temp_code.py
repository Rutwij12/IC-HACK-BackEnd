from manim import *

class MatrixRowOperations(Scene):
    def construct(self):
        # Create the original matrix
        matrix = Matrix([
            [2, 1],
            [1, 3]
        ]).scale(1.5)
        
        # Create the transformed matrix
        matrix_after = Matrix([
            [2, 1],
            [0, 2.5]
        ]).scale(1.5)
        
        # Create the arrow
        arrow = Arrow(
            start=RIGHT * 0.5,
            end=RIGHT * 2,
            color=YELLOW
        )
        
        # Group the matrices and arrow
        matrix_group = VGroup(
            matrix,
            arrow,
            matrix_after
        ).arrange(RIGHT, buff=0.5)
        
        # Create all text elements
        title = Text(
            "We can modify matrix rows to solve equations",
            font_size=36
        ).to_edge(UP, buff=1.5)
        
        row_op = MathTex(
            "R_2 \\rightarrow R_2 - \\frac{1}{2}R_1",
            color=LIGHT_GRAY,
            font_size=36
        ).next_to(matrix_group, DOWN, buff=1)
        
        final_message = Text(
            "These changes preserve solutions",
            color=BLUE,
            font_size=36
        ).next_to(row_op, DOWN, buff=0.8)
        
        # Animations
        # First phase: Show original matrix
        self.play(
            FadeIn(matrix),
            run_time=0.5
        )
        
        # Second phase: Show title
        self.play(
            FadeIn(title),
            run_time=0.5
        )
        
        # Third phase: Show arrow and transformed matrix
        self.play(
            FadeIn(arrow),
            FadeIn(matrix_after),
            run_time=1
        )
        
        # Fourth phase: Show row operation text
        self.play(
            FadeIn(row_op),
            run_time=0.5
        )
        
        # Final phase: Show final message
        self.play(
            FadeIn(final_message),
            run_time=0.5
        )
        
        # Pause at the end to show the complete scene
        self.wait(2)