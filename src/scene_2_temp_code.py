from manim import *

class EigenvectorVisualization(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": GREY_B},
            tips=False
        )

        # Create the original vector (blue)
        original_vector = Arrow(
            start=axes.coords_to_point(0, 0),
            end=axes.coords_to_point(1, 1),
            color=BLUE,
            buff=0
        )

        # Create the transformed vector (red)
        transformed_vector = Arrow(
            start=axes.coords_to_point(0, 0),
            end=axes.coords_to_point(2, 2),
            color=RED,
            buff=0
        )

        # Create labels
        eigenvector_label = Text("Eigenvector", font_size=36)
        eigenvector_label.next_to(original_vector.get_center(), LEFT, buff=0.5)
        
        lambda_label = MathTex(r"\lambda = 2", font_size=36)
        lambda_label.to_corner(UR, buff=0.5)

        # Animation sequence
        # 1. Fade in original vector and its label
        self.play(
            Create(axes, run_time=0.5),
            Create(original_vector),
            Write(eigenvector_label),
            run_time=2
        )
        self.wait(1)

        # 2. Fade in transformed vector
        self.play(
            Create(transformed_vector),
            run_time=2
        )
        self.wait(1)

        # 3. Fade in lambda label
        self.play(
            Write(lambda_label),
            run_time=1
        )
        self.wait(2)

        # 4. Hold and fade everything out
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in [
                axes, original_vector, transformed_vector,
                eigenvector_label, lambda_label
            ]],
            run_time=1
        )