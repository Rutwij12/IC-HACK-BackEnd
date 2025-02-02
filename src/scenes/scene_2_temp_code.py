from manim import *

class ScalarRowMultiplication(Scene):
    def construct(self):
        # Initial matrix
        matrix = Matrix([
            [2, 4, 1],
            [3, 1, 5],
            [0, 2, 3]
        ])
        matrix.scale(0.8)
        
        # Position matrix in center
        self.play(Write(matrix))
        
        # Title text
        title = Text("Scalar Multiplication: R₁ → 2R₁", font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Highlight first row - get the row elements
        row_elements = VGroup(*[matrix.get_entries()[i] for i in range(3)])
        row_highlight = SurroundingRectangle(row_elements, color=YELLOW)
        self.play(Create(row_highlight))
        
        # Show multiplication operation
        mult_text = MathTex("\\times 2").next_to(row_highlight, RIGHT)
        self.play(Write(mult_text))
        
        # Show computations above first row
        computations = VGroup(
            MathTex("2\\times2=4"),
            MathTex("2\\times4=8"),
            MathTex("2\\times1=2")
        ).arrange(RIGHT, buff=0.5)
        computations.scale(0.7).next_to(matrix, UP, buff=0.5)
        
        # Small arrows pointing down
        arrows = VGroup(*[
            Arrow(
                start=comp.get_bottom(),
                end=matrix.get_entries()[i].get_top(),
                buff=0.1,
                color=BLUE_C,
                max_tip_length_to_length_ratio=0.15
            )
            for i, comp in enumerate(computations)
        ])
        
        # Show computations and arrows
        self.play(Write(computations), Create(arrows))
        self.wait()
        
        # New matrix
        new_matrix = Matrix([
            [4, 8, 2],
            [3, 1, 5],
            [0, 2, 3]
        ])
        new_matrix.scale(0.8).move_to(matrix)
        
        # Transform to new matrix
        self.play(
            ReplacementTransform(matrix, new_matrix),
            FadeOut(row_highlight),
            FadeOut(computations),
            FadeOut(arrows),
            FadeOut(mult_text)
        )
        
        # Highlight new row in green
        new_row_elements = VGroup(*[new_matrix.get_entries()[i] for i in range(3)])
        new_row_highlight = SurroundingRectangle(new_row_elements, color=GREEN)
        self.play(Create(new_row_highlight))
        self.wait(0.5)
        
        # Final explanation text
        explanation = Text("Each element in R₁ is multiplied by 2", font_size=32)
        explanation.next_to(new_matrix, DOWN, buff=0.5)
        self.play(Write(explanation))
        
        self.wait()
        
        # Fade everything out
        self.play(
            FadeOut(new_matrix),
            FadeOut(new_row_highlight),
            FadeOut(title),
            FadeOut(explanation)
        )