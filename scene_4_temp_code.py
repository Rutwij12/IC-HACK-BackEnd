from manim import *

class RowOperationsExample(Scene):
    def construct(self):
        # Initial Setup
        title = Text("Row Operations Example").set_color(BLACK).to_edge(UP, buff=0.5)
        
        # Create initial matrix
        initial_matrix = Matrix(
            [[4, 6],
             [2, 5]],
            element_to_mobject_config={"color": BLACK}
        ).scale(0.8)
        initial_matrix.move_to(UP)
        
        # Animation Phase 1: Show initial setup
        self.play(Write(title))
        self.play(Write(initial_matrix))
        self.wait(1)
        
        # Highlight pivot element
        pivot = initial_matrix.get_entries()[0]  # First element (4)
        self.play(pivot.animate.set_color(RED))
        
        # Show operation text
        operation = MathTex(r"R_2 \rightarrow R_2 - (\frac{1}{2})R_1", color=BLACK)
        operation.next_to(initial_matrix, UP, buff=0.5)
        self.play(Write(operation))
        
        # Create intermediate steps
        mult_row = MathTex(r"\frac{1}{2}", r"[4 \quad 6]", r"= [2 \quad 3]", color=BLUE)
        mult_row.next_to(initial_matrix, DOWN, buff=0.5)
        
        # Show multiplication step
        self.play(Write(mult_row))
        self.wait(1)
        
        # Create final matrix
        final_matrix = Matrix(
            [[4, 6],
             [0, 2]],
            element_to_mobject_config={"color": BLACK}
        ).scale(0.8)
        final_matrix.move_to(initial_matrix.get_center())
        
        # Transform to final matrix
        self.play(
            ReplacementTransform(initial_matrix, final_matrix),
            FadeOut(mult_row)
        )
        
        # Highlight the zero
        zero_element = final_matrix.get_entries()[2]  # Element at position (2,1)
        self.play(zero_element.animate.set_color(RED))
        
        # Add "Row Echelon Form" text
        row_echelon_text = Text("Row Echelon Form:", color=BLACK).scale(0.8)
        row_echelon_text.next_to(final_matrix, LEFT, buff=0.5)
        
        # Create box around final matrix
        box = SurroundingRectangle(final_matrix, color=BLUE)
        
        # Show final elements
        self.play(
            Write(row_echelon_text),
            Create(box)
        )
        
        # Highlight stair-step pattern
        stair_elements = [final_matrix.get_entries()[0], final_matrix.get_entries()[3]]  # [4, 2]
        self.play(*[elem.animate.set_color(GREEN) for elem in stair_elements])
        
        # Final pause
        self.wait(1)
        
        # Fade out operation text but keep the main result
        self.play(
            FadeOut(operation),
            FadeOut(title)
        )
        self.wait(1)