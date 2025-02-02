from manim import *

class RowSwapOperation(Scene):
    def construct(self):
        # Create the initial matrix with row labels
        matrix = Matrix(
            [[2, 1, 4],
             [5, 3, 7],
             [1, 0, 2]],
            v_buff=0.8  # Increased vertical buffer for clearer visualization
        )
        
        # Create row labels
        row_labels = VGroup()
        for i in range(3):
            label = MathTex(f"R_{{{i+1}}}")
            label.next_to(matrix.get_rows()[i], LEFT, buff=0.5)
            row_labels.add(label)
            
        # Create the swap operation text
        swap_text = MathTex(r"R_1 \leftrightarrow R_2")
        swap_text.next_to(matrix, UP, buff=0.5)
        
        # Initial display of matrix and labels
        self.play(
            Write(matrix),
            Write(row_labels),
            run_time=2
        )
        self.wait(1)
        
        # Highlight rows to be swapped
        row1 = matrix.get_rows()[0].copy()
        row2 = matrix.get_rows()[1].copy()
        row1_label = row_labels[0].copy()
        row2_label = row_labels[1].copy()
        
        self.play(
            row1.animate.set_color(BLUE),
            row2.animate.set_color(YELLOW),
            Write(swap_text),
            run_time=1
        )
        self.wait(1)
        
        # Calculate positions for smooth swap animation
        row1_target = row2.get_center()
        row2_target = row1.get_center()
        label1_target = row2_label.get_center()
        label2_target = row1_label.get_center()
        
        # Perform the swap animation
        self.play(
            row1.animate.move_to(row1_target),
            row2.animate.move_to(row2_target),
            row_labels[0].animate.move_to(label1_target),
            row_labels[1].animate.move_to(label2_target),
            rate_func=rate_functions.ease_in_out_sine,
            run_time=3
        )
        
        # Create the final matrix
        final_matrix = Matrix(
            [[5, 3, 7],
             [2, 1, 4],
             [1, 0, 2]],
            v_buff=0.8
        )
        final_matrix.move_to(matrix)
        
        # Fade out colored rows and show final matrix
        self.play(
            FadeOut(row1),
            FadeOut(row2),
            FadeIn(final_matrix),
            run_time=1
        )
        
        # Hold the final state
        self.wait(2)