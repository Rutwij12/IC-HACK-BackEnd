from manim import *

class DotProductVisualization(Scene):
    def construct(self):
        # Define colors
        blue_color = "#3498db"
        green_color = "#2ecc71"

        # Create matrices
        matrix_a = Matrix([[2, 3]], element_alignment_corner=DR)
        matrix_a.scale(1.0).set_color(blue_color)
        matrix_a.shift(LEFT * 2)

        matrix_b = Matrix([[4], [5]], element_alignment_corner=DR)
        matrix_b.scale(1.0).set_color(green_color)
        matrix_b.shift(RIGHT * 2)

        # Create title
        title = Text("Computing Single Element Using Dot Product", font_size=36)
        title.to_edge(UP)

        # Step 1: Initial fade in
        self.play(
            FadeIn(matrix_a),
            FadeIn(matrix_b),
            Write(title)
        )
        self.wait(2)
        self.play(FadeOut(title))

        # Step 2: Highlight row and column
        row = matrix_a.copy()
        column = matrix_b.copy()
        row.set_color(BLUE_A)
        column.set_color(GREEN_A)

        dot_product_text = Text("Row × Column = Dot Product", font_size=32)
        dot_product_text.to_edge(UP)

        self.play(
            ShowPassingFlash(row),
            ShowPassingFlash(column),
            Write(dot_product_text)
        )
        self.wait()

        # Step 3: Move to calculation format
        calculation = MathTex(
            "(2 \\times 4) + (3 \\times 5)",
            font_size=36
        ).shift(DOWN)

        self.play(
            Write(calculation),
            matrix_a.animate.shift(UP),
            matrix_b.animate.shift(UP)
        )
        self.wait()

        # Step 4: Show result
        result_step1 = MathTex("(8) + (15)", font_size=36).shift(DOWN * 2)
        final_result = MathTex("= 23", font_size=36).shift(DOWN * 3)

        self.play(Write(result_step1))
        self.wait()
        self.play(Write(final_result))
        self.wait()

        # Final fadeout
        all_objects = VGroup(
            matrix_a, matrix_b, dot_product_text,
            calculation, result_step1, final_result
        )
        self.play(FadeOut(all_objects))
        self.wait()