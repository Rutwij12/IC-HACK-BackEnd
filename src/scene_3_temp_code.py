from manim import *

class EigenvectorDemo(Scene):
    def construct(self):
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