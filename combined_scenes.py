from manim import *
import random
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class CombinedScene(VoiceoverScene):
    def construct(self):
        # Set up Azure TTS service
        self.set_speech_service(AzureService(
            voice='en-US-JennyNeural',
            style='friendly'
        ))


        # Scene 1
        with self.voiceover(text="""In linear algebra, we can perform row operations on matrices. When we subtract half of row 1 from row 2, we create an equivalent system that preserves all solutions.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 2
        with self.voiceover(text="""In elementary row operations, we can swap any two rows. Watch as we swap rows 1 and 2 of this matrix, moving the rows into their new positions while maintaining the rest of the matrix unchanged.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 3
        with self.voiceover(text="""We multiply each element in the first row by 2, transforming the values. Watch as 2 becomes 4, 4 becomes 8, and 1 becomes 2, while the other rows stay unchanged.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 4
        with self.voiceover(text="""When we add one row to another in a matrix, we add the numbers in each position. Watch as we add Row 1 to Row 2, combining 3 plus 2 and 4 plus 1 to get our new row of 5 and 5.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 5
        with self.voiceover(text="""Lets simplify this matrix by performing row operations. We multiply the first row by one half and subtract it from the second row to obtain zeros below our pivot, giving us our row echelon form.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
