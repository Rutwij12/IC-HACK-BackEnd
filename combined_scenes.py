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
        with self.voiceover(text="""Let's explore a two-by-two matrix where each row represents a point in space. As we highlight these rows, watch how they map directly to coordinates on our grid, creating a visual connection between matrix values and geometric points.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # 1. Initial Setup
            title = Text("2×2 Matrix", font_size=40).to_edge(UP)
            matrix = Matrix([
                [2, 1],
                [-1, 3]
            ], h_buff=1.5).scale(1.0)
            # First animation sequence (0-3 seconds)
            self.play(FadeIn(title))
            self.play(Write(matrix))
            self.wait(0.5)
            # 2. Row highlighting sequence (3-7 seconds)
            first_row_text = Text("First Row", font_size=30, color=LIGHT_GRAY).shift(LEFT*3 + UP*1.5)
            second_row_text = Text("Second Row", font_size=30, color=LIGHT_GRAY).shift(LEFT*3 + UP*0.5)
            first_row = matrix.get_rows()[0]
            second_row = matrix.get_rows()[1]
            self.play(
                Write(first_row_text),
                first_row.animate.set_color(BLUE)
            )
            self.wait(0.5)
            self.play(
                Write(second_row_text),
                second_row.animate.set_color(GREEN)
            )
            # 3. Coordinate plane and points sequence (7-11 seconds)
            # Move matrix up and scale down
            self.play(
                matrix.animate.shift(UP).scale(0.8),
                FadeOut(first_row_text),
                FadeOut(second_row_text)
            )
            # Create coordinate plane
            plane = NumberPlane(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                background_line_style={
                    "stroke_opacity": 0.3
                },
                axis_config={
                    "numbers_to_include": np.arange(-3, 4, 1),
                    "font_size": 24
                }
            ).shift(DOWN)
            self.play(Create(plane))
            # Create points and dashed lines
            point1 = Dot(plane.coords_to_point(2, 1), color=BLUE, radius=0.1)
            point2 = Dot(plane.coords_to_point(-1, 3), color=GREEN, radius=0.1)
            # Create dashed lines with correct opacity setting
            dashed_line1 = DashedLine(
                plane.get_origin(), point1.get_center(),
                dash_length=0.1
            ).set_opacity(0.6)
            dashed_line2 = DashedLine(
                plane.get_origin(), point2.get_center(),
                dash_length=0.1
            ).set_opacity(0.6)
            # Create coordinate notations
            coord_text1 = Text("[2, 1] → (2,1)", font_size=30, color=BLUE).shift(LEFT*2)
            coord_text2 = Text("[-1, 3] → (-1,3)", font_size=30, color=GREEN).shift(LEFT*2 + DOWN*0.5)
            self.play(
                Create(dashed_line1),
                Create(dashed_line2),
                FadeIn(point1),
                FadeIn(point2),
                Write(coord_text1),
                Write(coord_text2)
            )
            # 4. Final text and fadeout (11-15 seconds)
            final_text = Text(
                "Matrix rows represent points in space",
                font_size=36,
                color=LIGHT_GRAY
            ).to_edge(DOWN)
            self.play(Write(final_text))
            self.wait(1)
            # Fade everything out
            self.play(
                *[FadeOut(mob) for mob in self.mobjects]
            )
            self.wait(0.5)

        # Scene 2
        with self.voiceover(text="""When multiplying matrices, we start with a 2 by 3 matrix A and a 3 by 2 matrix B. Notice how their inner dimensions both equal 3 - this matching is essential for matrix multiplication to work. The result will be a 2 by 2 matrix.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Title
            title = Text("Matrix Multiplication: Dimensions Matter", color=WHITE)
            title.to_edge(UP)
            # Create matrices
            matrix_a = Matrix(
                [[1, 2, 3],
                 [4, 5, 6]],
                left_bracket="[",
                right_bracket="]"
            ).set_color(BLUE)
            matrix_a.shift(LEFT * 3)
            matrix_b = Matrix(
                [[7, 8],
                 [9, 0],
                 [1, 2]],
                left_bracket="[",
                right_bracket="]"
            ).set_color(RED)
            matrix_b.shift(RIGHT * 3)
            # Create dimension labels
            label_a = Text("A (2×3)", color=BLUE).scale(0.8)
            label_a.next_to(matrix_a, DOWN)
            label_b = Text("B (3×2)", color=RED).scale(0.8)
            label_b.next_to(matrix_b, DOWN)
            # Create highlighted parts
            highlight_a = Text("3", color=BLUE).scale(0.8)
            highlight_a.next_to(label_a, DOWN)
            highlight_a.align_to(label_a.get_center() + RIGHT * 0.3, RIGHT)
            highlight_b = Text("3", color=RED).scale(0.8)
            highlight_b.next_to(label_b, DOWN)
            highlight_b.align_to(label_b.get_center() - RIGHT * 0.3, LEFT)
            # Create arrow and bottom text
            arrow = CurvedArrow(
                highlight_a.get_right(),
                highlight_b.get_left(),
                angle=-TAU/4
            ).set_color(YELLOW)
            match_text = Text("Inner dimensions must match!", color=GREEN).scale(0.8)
            match_text.to_edge(DOWN, buff=1)
            result_text = Text("(2×3) × (3×2) = (2×2)", color=WHITE).scale(0.7)
            result_text.next_to(match_text, DOWN)
            # Animation sequence
            self.play(FadeIn(title))
            self.wait()
            self.play(
                Write(matrix_a),
                FadeIn(label_a)
            )
            self.wait()
            self.play(
                Write(matrix_b),
                FadeIn(label_b)
            )
            self.wait()
            self.play(
                FadeIn(highlight_a),
                FadeIn(highlight_b)
            )
            self.wait()
            self.play(Create(arrow))
            self.play(Write(match_text))
            self.wait()
            self.play(FadeIn(result_text))
            self.wait()

        # Scene 3
        with self.voiceover(text="""Let's see how a single element in matrix multiplication is computed through the dot product. When we multiply these matrices, we take the row values 2 and 3, and multiply them with the column values 4 and 5. Adding the products together gives us our final value of 23.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 4
        with self.voiceover(text="""Let's multiply these two matrices by calculating each element one at a time. Watch how we multiply the rows of matrix A by the columns of matrix B to form our result. Each new number we calculate fills one position in our final matrix.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 5
        with self.voiceover(text="""Let's start by looking at point P at coordinates (2,1). When we apply a 45-degree rotation matrix, we can follow the point as it rotates around the origin, ending at its new position P-prime at approximately (0.7, 2.1). This transformation preserves the point's distance from the origin while changing its orientation.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # 1. Initial Setup
            title = Text("Matrix Rotation Example").scale(0.8).move_to(UP * 3.5)
            # Create coordinate plane
            plane = NumberPlane(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                x_length=6,
                y_length=6,
                background_line_style={
                    "stroke_color": "#CCCCCC",
                    "stroke_opacity": 0.5
                },
                axis_config={"stroke_color": "#999999"}
            ).scale(0.8)
            # Original point and label
            original_point = Dot(plane.coords_to_point(2, 1), color=BLUE)
            original_label = Text("P(2,1)").scale(0.6).set_color(BLUE).next_to(original_point, UR * 0.3)
            # 2. Matrix elements
            rotation_matrix = MathTex(
                "R = \\begin{bmatrix} 0.707 & -0.707 \\\\ 0.707 & 0.707 \\end{bmatrix}"
            ).scale(0.8).move_to(LEFT * 5 + UP * 2)
            matrix_label = Text("45° Rotation Matrix").scale(0.6).next_to(rotation_matrix, UP * 0.5)
            # 3. Matrix multiplication
            multiplication = MathTex(
                "\\begin{bmatrix} 0.707 & -0.707 \\\\ 0.707 & 0.707 \\end{bmatrix}",
                "\\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix}",
                "=",
                "\\begin{bmatrix} 0.707 \\\\ 2.121 \\end{bmatrix}"
            ).scale(0.7).move_to(LEFT * 5)
            # Final point and arc
            end_point = Dot(plane.coords_to_point(0.707, 2.121), color=RED)
            end_label = Text("P'(0.707, 2.121)").scale(0.6).set_color(RED).next_to(end_point, UR * 0.3)
            # Create rotation arc
            start_angle = np.arctan2(1, 2)
            radius = np.sqrt(5) * plane.get_x_unit_size()  # Fixed: using get_x_unit_size()
            arc = Arc(
                radius=radius,
                arc_center=plane.get_origin(),
                start_angle=start_angle,
                angle=PI/4,
                color=RED
            )
            # Animations
            self.play(Write(title))
            self.play(Create(plane))
            self.play(Create(original_point), Write(original_label))
            self.wait()
            # Fade out title and show matrix
            self.play(FadeOut(title))
            self.play(
                Write(rotation_matrix),
                Write(matrix_label)
            )
            self.wait()
            # Show transformation
            self.play(Write(multiplication))
            self.play(
                original_point.animate.set_opacity(0.5),
                original_label.animate.set_opacity(0.5)
            )
            self.play(
                Create(arc),
                Create(end_point)
            )
            self.play(Write(end_label))
            self.wait()

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
