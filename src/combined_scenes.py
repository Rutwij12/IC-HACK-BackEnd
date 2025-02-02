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
        with self.voiceover(text="""Here's our 2D vector and its transformation matrix. We can see a vector v in the coordinate plane, and on the right, matrix A that will transform this vector. Together, they define a linear transformation in 2D space.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 2
        with self.voiceover(text="""Let's witness how this matrix transforms our vectors. Starting with two unit vectors, watch as they stretch and rotate under the transformation matrix, creating a new geometric pattern on our coordinate grid.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Set up the coordinate grid
            grid = NumberPlane(
                x_range=[-4, 4, 1],
                y_range=[-4, 4, 1],
                background_line_style={
                    "stroke_color": "#888888",
                    "stroke_width": 0.5,
                    "stroke_opacity": 0.5,
                }
            )
            # Define vectors
            v1 = Arrow(start=ORIGIN, end=RIGHT, color=RED, tip_length=0.2)
            v2 = Arrow(start=ORIGIN, end=UP, color=BLUE, tip_length=0.2)
            # Create vector labels
            v1_label = MathTex("v_1", color=RED).next_to(v1.get_end(), RIGHT*0.3 + UP*0.3)
            v2_label = MathTex("v_2", color=BLUE).next_to(v2.get_end(), LEFT*0.3 + UP*0.3)
            # Define transformation matrix
            matrix = [[2, 1], [-1, 1]]
            matrix_tex = MathTex(
                "M = \\begin{bmatrix} 2 & 1 \\\\ -1 & 1 \\end{bmatrix}"
            ).scale(0.8).to_corner(UR, buff=0.5)
            # Step 1: Fade in grid and vectors
            self.play(
                Create(grid),
                GrowArrow(v1),
                GrowArrow(v2),
                Write(v1_label),
                Write(v2_label),
                run_time=3
            )
            # Step 2: Show matrix
            self.play(Write(matrix_tex), run_time=1.5)
            # Create transformed vectors
            v1_transformed = Arrow(
                start=ORIGIN,
                end=np.array([2, -1, 0]),
                color=RED,
                tip_length=0.2
            )
            v2_transformed = Arrow(
                start=ORIGIN,
                end=np.array([1, 1, 0]),
                color=BLUE,
                tip_length=0.2
            )
            # Create transformed vector labels
            mv1_label = MathTex("Mv_1", color=RED).next_to(v1_transformed.get_end(), RIGHT*0.3 + UP*0.3)
            mv2_label = MathTex("Mv_2", color=BLUE).next_to(v2_transformed.get_end(), RIGHT*0.3 + UP*0.3)
            # Step 3: Apply transformation
            self.play(
                grid.animate.apply_matrix(matrix),
                Transform(v1, v1_transformed),
                Transform(v2, v2_transformed),
                v1_label.animate.set_opacity(0.3),
                v2_label.animate.set_opacity(0.3),
                run_time=6
            )
            # Step 4: Add transformed labels
            self.play(
                Write(mv1_label),
                Write(mv2_label),
                run_time=1.5
            )
            # Final pause
            self.wait(1.5)

        # Scene 3
        with self.voiceover(text="""Let's watch an eigenvector in action. When this vector is transformed by our matrix, it simply stretches by a factor of 3, keeping the same direction. This special behavior defines it as an eigenvector.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create coordinate system
            plane = NumberPlane(
                x_range=[-5, 5, 1],
                y_range=[-5, 5, 1],
                background_line_style={
                    "stroke_color": GRAY_D,
                    "stroke_width": 1,
                    "stroke_opacity": 0.5
                }
            ).set_opacity(0.5)
            # Initial vector
            vector = Vector([1, 1], color=YELLOW)
            vector_label = MathTex("\\vec{v}", color=WHITE).next_to(vector.get_end(), UP+RIGHT, buff=0.1)
            # Matrix and eigenvalue
            matrix = MathTex(
                "A = \\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}",
                color=WHITE
            ).to_corner(UR, buff=0.5)
            eigenvalue = MathTex("\\lambda = 3", color=WHITE).next_to(matrix, DOWN)
            # Transformed vector (scaled by λ=3)
            transformed_vector = Vector([3, 3], color=YELLOW)
            # Dashed line for transformation path
            dashed_line = DashedLine(
                vector.get_end(),
                transformed_vector.get_end(),
                color=GRAY_C
            )
            # Text elements
            transform_text = Text(
                "When transformed by matrix A...",
                color=WHITE,
                font_size=36
            ).to_edge(UP, buff=0.5)
            eigenvector_text = Text(
                "Eigenvector: Only scales, doesn't rotate",
                color=WHITE,
                font_size=36
            ).to_edge(DOWN, buff=0.5)
            # Animation sequence
            self.play(
                Create(plane),
                run_time=1
            )
            self.play(
                GrowArrow(vector),
                Write(vector_label),
                run_time=2
            )
            self.play(
                Write(transform_text),
                Write(matrix),
                Write(eigenvalue),
                run_time=2
            )
            # Transform sequence
            self.play(
                vector.animate.set_opacity(0.3),
                GrowArrow(transformed_vector),
                Create(dashed_line),
                run_time=3
            )
            # Final text and glow effect
            self.play(
                Write(eigenvector_text),
                run_time=1
            )
            # Glow effect
            glow_group = VGroup(vector, transformed_vector)
            self.play(
                glow_group.animate.set_stroke(color=YELLOW, width=5),
                rate_func=there_and_back,
                run_time=2
            )
            # Pause for a moment at the end
            self.wait(1)

        # Scene 4
        with self.voiceover(text="""Here we have a vector v on a coordinate plane. When transformed by matrix A, it's stretched by a factor of 4 while maintaining its direction - making it an eigenvector with eigenvalue 4.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create coordinate plane with specified scale
            plane = NumberPlane(
                x_range=[-12, 12, 1],
                y_range=[-12, 12, 1],
                x_length=12,
                y_length=7,
                background_line_style={
                    "stroke_opacity": 0.4
                }
            ).scale(0.5)
            # Create vectors
            original_vector = Arrow(
                plane.coords_to_point(0, 0),
                plane.coords_to_point(1, 0.5),
                color=BLUE,
                buff=0,
                stroke_width=2,
                tip_length=0.2
            )
            transformed_vector = Arrow(
                plane.coords_to_point(0, 0),
                plane.coords_to_point(4, 2),
                color=RED,
                buff=0,
                stroke_width=2,
                tip_length=0.2
            )
            # Create labels
            v_label = MathTex("v", color=BLUE).scale(0.8)
            v_label.next_to(original_vector.get_center(), UP+RIGHT, buff=0.2)
            four_v_label = MathTex("4v", color=RED).scale(0.8)
            four_v_label.next_to(transformed_vector.get_center(), UP+RIGHT, buff=0.2)
            # Create matrix and equation text
            matrix_A = MathTex(
                r"A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}"
            ).scale(0.8).move_to([-5, 2.5, 0])
            equation = MathTex(r"Av = \lambda v").scale(0.8).next_to(matrix_A, DOWN, buff=0.5)
            lambda_val = MathTex(r"\lambda = 4").scale(0.8).next_to(equation, DOWN, buff=0.5)
            orig_vector_text = Text("Original eigenvector", color=BLUE, font_size=24)
            orig_vector_text.move_to([-5, 3, 0])
            final_text = Text("The eigenvector is scaled by λ = 4", font_size=24)
            final_text.move_to([0, -3, 0])
            # Animation sequence
            # 0-3 seconds
            self.play(
                Create(plane),
                run_time=1
            )
            self.play(
                Create(original_vector),
                Write(v_label),
                FadeIn(orig_vector_text),
                run_time=1
            )
            # 3-6 seconds
            self.play(
                Write(matrix_A),
                Write(equation),
                Write(lambda_val),
                run_time=1.5
            )
            # 6-9 seconds
            original_vector_faded = original_vector.copy().set_opacity(0.5)
            self.play(
                Transform(original_vector, original_vector_faded),
                Create(transformed_vector),
                Write(four_v_label),
                run_time=1.5
            )
            # 9-12 seconds
            dashed_line = DashedLine(
                start=original_vector.get_end(),
                end=transformed_vector.get_end(),
                color=GRAY,
                stroke_opacity=0.7
            )
            self.play(
                Create(dashed_line),
                Write(final_text),
                run_time=1
            )
            # Final highlight pulse
            self.play(
                original_vector.animate.set_color(YELLOW),
                transformed_vector.animate.set_color(YELLOW),
                run_time=0.25
            )
            self.play(
                original_vector.animate.set_color(BLUE),
                transformed_vector.animate.set_color(RED),
                run_time=0.25
            )
            self.wait(1)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
