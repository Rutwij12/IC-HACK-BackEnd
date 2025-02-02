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
        with self.voiceover(text="""Let's see how this vector stretches when we apply our transformation matrix. Watch as the original blue vector doubles in length while keeping its direction, producing a new red vector - a classic example of an eigenvector.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create coordinate system
            axes = Axes(
                x_range=[-3, 3],
                y_range=[-3, 3],
                axis_config={
                    "stroke_width": 2,
                    "color": BLACK,
                    "include_tip": True,
                },
            )
            # Create grid
            grid = NumberPlane(
                x_range=[-3, 3],
                y_range=[-3, 3],
                background_line_style={
                    "stroke_color": GRAY,
                    "stroke_width": 1,
                    "stroke_opacity": 0.5
                }
            )
            # Initialize vectors
            vector_v = Arrow(
                start=axes.c2p(0, 0),
                end=axes.c2p(2, 2),
                buff=0,
                color=BLUE
            )
            vector_av = Arrow(
                start=axes.c2p(0, 0),
                end=axes.c2p(4, 4),
                buff=0,
                color=RED
            )
            # Create labels
            v_label = MathTex(r"\vec{v} = [2,2]").next_to(
                axes.c2p(2, 2),
                direction=UR,
                buff=0.2
            )
            av_label = MathTex(r"A\vec{v} = [4,4]").next_to(
                axes.c2p(4, 4),
                direction=UR,
                buff=0.2
            )
            # Create matrix and eigenvalue text
            matrix = MathTex(
                r"A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}"
            ).to_corner(UL, buff=1)
            eigenvalue = MathTex(r"\lambda = 2").next_to(
                matrix,
                DOWN,
                buff=0.3
            )
            # Animation sequence
            # 1. Fade in grid and axes
            self.play(
                FadeIn(grid),
                FadeIn(axes),
                run_time=2
            )
            # 2. Draw original vector and its label
            self.play(
                GrowArrow(vector_v),
                Write(v_label),
                run_time=2
            )
            # 3. Show matrix and eigenvalue
            self.play(
                Write(matrix),
                Write(eigenvalue),
                run_time=2
            )
            # 4. Transform vector
            faded_v = vector_v.copy().set_opacity(0.3)
            self.play(
                ReplacementTransform(vector_v, faded_v),
                GrowArrow(vector_av),
                Write(av_label),
                run_time=3
            )
            # Final pause
            self.wait(1)

        # Scene 2
        with self.voiceover(text="""In this visualization, a vector v transforms under matrix multiplication, stretching by a factor of 2. Watch as the blue vector scales to create the red vector - this multiplicative relationship is what defines an eigenvalue and its eigenvector.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create coordinate system
            axes = Axes(
                x_range=[-5, 5],
                y_range=[-5, 5],
                axis_config={"color": GRAY},
                tips=False
            ).set_opacity(0.3)
            # Add light gray grid
            grid = NumberPlane(
                x_range=[-5, 5],
                y_range=[-5, 5],
                background_line_style={
                    "stroke_color": GRAY,
                    "stroke_opacity": 0.3
                }
            )
            # Add coordinate system and grid
            self.play(
                Create(grid),
                Create(axes),
                run_time=1
            )
            # Create original vector
            vector_v = Vector([2, 1], color=BLUE)
            vector_v_label = MathTex("v").set_color(BLUE)
            vector_v_label.next_to(vector_v.get_end(), UP + RIGHT, buff=0.1)
            # Show original vector
            self.play(
                GrowArrow(vector_v),
                Write(vector_v_label),
                run_time=1.5
            )
            self.wait(0.5)
            # Create transformed vector
            vector_av = Vector([4, 2], color=RED)
            vector_av_label = MathTex("Av").set_color(RED)
            vector_av_label.next_to(vector_av.get_end(), UP + RIGHT, buff=0.1)
            # Animate transformation
            self.play(
                Transform(vector_v.copy(), vector_av),
                run_time=2
            )
            self.play(Write(vector_av_label))
            # Create dashed line connecting vector tips
            dashed_line = DashedLine(
                vector_v.get_end(),
                vector_av.get_end(),
                dash_length=0.15,
                color=GRAY
            )
            # Show dashed line
            self.play(Create(dashed_line))
            # Create and show eigenvalue equation
            lambda_text = MathTex("\\lambda = 2").scale(1.2)
            lambda_text.move_to([-3, 2, 0])
            eigen_equation = MathTex("A", "v", "=", "\\lambda", "v")
            eigen_equation.set_color_by_tex_to_color_map({
                "A": WHITE,
                "v": BLUE,
                "\\lambda": WHITE
            })
            eigen_equation.move_to([-3, 1.5, 0])
            self.play(
                Write(lambda_text),
                Write(eigen_equation),
                run_time=1.5
            )
            # Pulse animation for both vectors
            self.play(
                vector_v.animate.scale(1.2),
                vector_av.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=1
            )
            # Final pause
            self.wait(2)
            # Fade out everything
            self.play(
                *[FadeOut(mob) for mob in self.mobjects],
                run_time=1
            )

        # Scene 3
        with self.voiceover(text="""When we multiply an eigenvector by its eigenvalue, the resulting vector points in exactly the same direction - it's just stretched by a factor of 2. This special property makes eigenvectors incredibly useful in linear algebra.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
