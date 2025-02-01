from manim import *

class MatrixMultiplication(Scene):
    def construct(self):
        # Define matrices
        matrix_a = Matrix([["2", "1"], ["3", "4"]])
        matrix_b = Matrix([["5", "6"], ["7", "8"]])
        result_matrix = Matrix([["", ""], ["", ""]])
        final_result = Matrix([["17", "20"], ["43", "50"]])

        # Position matrices
        matrix_a.scale(0.8).move_to([-4, 2, 0])
        matrix_b.scale(0.8).move_to([0, 2, 0])
        result_matrix.scale(0.8).move_to([4, 2, 0])

        # Create labels
        label_a = Text("A", font_size=36).next_to(matrix_a, DOWN, buff=0.3)
        label_b = Text("B", font_size=36).next_to(matrix_b, DOWN, buff=0.3)
        label_result = Text("Result", font_size=36).next_to(result_matrix, DOWN, buff=0.3)
        mult_symbol = Text("×", font_size=48).move_to([-2, 2, 0])

        # Initial display
        self.play(
            FadeIn(matrix_a), FadeIn(label_a),
            FadeIn(matrix_b), FadeIn(label_b),
            FadeIn(result_matrix), FadeIn(label_result),
            FadeIn(mult_symbol),
            run_time=2
        )

        # Helper function for creating calculation text
        def create_calc_text(text):
            return MathTex(text, font_size=40).move_to([0, -2, 0])

        # Function to highlight row and column
        def highlight_elements(row_idx, col_idx):
            row_elements = VGroup(*[matrix_a.get_entries()[i] for i in range(2*row_idx, 2*row_idx+2)])
            col_elements = VGroup(*[matrix_b.get_entries()[i] for i in range(col_idx, 4, 2)])
            
            row_highlight = SurroundingRectangle(row_elements, color=RED, fill_opacity=0.4)
            col_highlight = SurroundingRectangle(col_elements, color=BLUE, fill_opacity=0.4)
            
            return row_highlight, col_highlight

        # Calculations for each position
        calculations = [
            ("(2×5) + (1×7)", "10 + 7", "17", 0, 0),
            ("(2×6) + (1×8)", "12 + 8", "20", 0, 1),
            ("(3×5) + (4×7)", "15 + 28", "43", 1, 0),
            ("(3×6) + (4×8)", "18 + 32", "50", 1, 1)
        ]

        # Process each calculation
        for calc, mid, result, row, col in calculations:
            # Create highlights
            row_rect, col_rect = highlight_elements(row, col)
            
            # Create calculation steps
            calc_text = create_calc_text(calc)
            mid_text = create_calc_text(mid)
            result_text = create_calc_text(result)

            # Show highlights and calculation
            self.play(
                FadeIn(row_rect),
                FadeIn(col_rect),
                Write(calc_text),
                run_time=0.5
            )

            # Transform calculations
            self.play(
                Transform(calc_text, mid_text),
                run_time=0.5
            )
            self.play(
                Transform(calc_text, result_text),
                run_time=0.5
            )

            # Fill result in matrix
            result_entry = MathTex(result, font_size=40)
            result_entry.move_to(result_matrix.get_entries()[2*row + col].get_center())
            
            self.play(
                Write(result_entry),
                run_time=0.5
            )

            # Clean up
            self.play(
                FadeOut(row_rect),
                FadeOut(col_rect),
                FadeOut(calc_text),
                run_time=0.3
            )

        # Final display
        self.play(
            Transform(result_matrix, final_result.scale(0.8).move_to([4, 2, 0])),
            run_time=0.5
        )
        
        # Scale up result briefly
        self.play(
            result_matrix.animate.scale(1.1),
            run_time=0.2
        )
        self.play(
            result_matrix.animate.scale(1/1.1),
            run_time=0.2
        )