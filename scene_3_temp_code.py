from manim import *

class RowAddition(Scene):
    def construct(self):
        # Initial Setup
        title = Text("Row Addition", font_size=48).to_edge(UP, buff=0.5)
        subtitle = Text("Adding a multiple of one row to another row", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title))
        self.play(Write(subtitle))
        
        # Matrix Example
        original_matrix = Matrix([
            [2, 1],
            [3, 4]
        ], v_buff=1.0, h_buff=0.8)
        original_matrix.move_to(ORIGIN)
        
        matrix_label = Text("Original Matrix", font_size=36)
        matrix_label.next_to(original_matrix, LEFT, buff=1)

        self.play(
            Write(original_matrix),
            Write(matrix_label)
        )
        self.wait()

        # Operation Demonstration
        operation = MathTex(r"R_2 + R_1 \rightarrow R_2", font_size=36)
        operation.next_to(original_matrix, UP, buff=1)

        # Highlight rows
        row1_box = SurroundingRectangle(original_matrix.get_rows()[0], color=BLUE)
        row2_box = SurroundingRectangle(original_matrix.get_rows()[1], color=YELLOW)

        self.play(Write(operation))
        self.play(Create(row1_box), Create(row2_box))
        self.wait()

        # Transform to final matrix
        final_matrix = Matrix([
            [2, 1],
            [5, 5]
        ], v_buff=1.0, h_buff=0.8)
        final_matrix.move_to(original_matrix)

        self.play(
            Transform(original_matrix, final_matrix),
            FadeOut(row1_box),
            FadeOut(row2_box)
        )

        # Final Result
        calculation = Text("New Row 2 = (3,4) + (2,1) = (5,5)", font_size=36)
        calculation.next_to(final_matrix, DOWN, buff=1)

        # Highlight new row
        new_row_box = SurroundingRectangle(final_matrix.get_rows()[1], color=GREEN)

        self.play(Write(calculation))
        self.play(Create(new_row_box))
        self.wait()

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )