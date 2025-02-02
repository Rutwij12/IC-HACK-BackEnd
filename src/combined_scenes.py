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
        with self.voiceover(text="""Welcome to our exploration of geometric transformations. Today, we'll witness the fascinating process of morphing a perfect circle into a square.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create the main title text
            title = Text(
                "Circle to Square Transformation",
                font="Helvetica",
                font_size=60  # Adjusted for good visibility (approximately 1/6th of screen height)
            )
            # Center the title
            title.move_to(ORIGIN)
            # Initial state: text with opacity 0
            title.set_opacity(0)
            # 1. Fade in (0-2 seconds)
            self.play(
                FadeIn(title, rate_func=smooth),
                run_time=2
            )
            # 2. Static display (2-4 seconds)
            self.wait(2)
            # 3. Fade out (4-5 seconds)
            self.play(
                FadeOut(title, rate_func=smooth),
                run_time=1
            )

        # Scene 2
        with self.voiceover(text="""Watch as this circle smoothly transforms into a square, while keeping its perimeter constant throughout the entire transformation. Notice how each point of the circle gradually shifts to form the straight edges and sharp corners of the square.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create the initial circle with radius 2
            circle = Circle(radius=2, stroke_width=2, stroke_color=WHITE)
            # Calculate square side length to maintain same perimeter
            # Circle perimeter = 4π, so square side length = 4π/4 = π
            side_length = PI
            # Create the target square centered at origin
            square = Square(side_length=side_length, stroke_width=2, stroke_color=WHITE)
            # Create smooth transition by increasing the number of anchor points
            circle.set_n_points(100)
            square.set_n_points(100)
            # Initial circle creation animation
            self.play(
                Create(circle),
                run_time=2
            )
            # Brief pause after circle creation
            self.wait()
            # Transform circle to square
            self.play(
                Transform(
                    circle,
                    square,
                    rate_func=smooth,
                    run_time=8
                )
            )
            # Brief pause on final square
            self.wait()
            # Fade out the final shape
            self.play(
                FadeOut(circle),
                run_time=1
            )
            # Final brief pause
            self.wait(0.5)

        # Scene 3
        with self.voiceover(text="""Our square pattern completes its journey, gradually fading away while softly expanding - leaving us with a clean finish to our mathematical exploration.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create the square with specified dimensions
            square = Square(
                side_length=4,
                stroke_color=WHITE,
                fill_color=WHITE,
                fill_opacity=0.1
            ).move_to(ORIGIN)
            # Add the square to the scene (assuming it's continuing from previous scene)
            # In a real continuation, you might not need this line
            self.add(square)
            # 1. Hold Time (1 second)
            self.wait(1)
            # 2. Fade Out Animation with scale
            # Create animation that combines scaling and fading
            fade_out_anim = AnimationGroup(
                square.animate.scale(1.1),
                square.animate.set_opacity(0),
                rate_func=smooth,
                run_time=2.5
            )
            # Play the combined animation
            self.play(fade_out_anim)
            # Small wait at the end to ensure clean finish
            self.wait(0.5)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
