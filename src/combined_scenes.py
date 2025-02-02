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
        with self.voiceover(text="""A perfect circle appears, elegantly filling the space before gracefully fading away - a simple demonstration of geometric beauty.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Set the background color
            self.camera.background_color = BLACK
            # Create the circle with specified properties
            circle = Circle(
                radius=2,
                color=BLUE_D,
                stroke_width=2,
                fill_opacity=0.5
            ).move_to(ORIGIN)
            # Animation sequence
            # 1. FadeIn (0.0s to 0.3s)
            self.play(
                FadeIn(circle, scale=1.2),
                run_time=0.3
            )
            # 2. Hold (0.3s to 0.7s)
            self.wait(0.4)
            # 3. FadeOut (0.7s to 1.0s)
            self.play(
                FadeOut(circle),
                run_time=0.3
            )

        # Scene 2
        with self.voiceover(text="""In this shape transformation, a circle with equal area morphs smoothly into a square, demonstrating how different shapes can occupy the same space while maintaining their area of approximately twelve and a half square units.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Define colors
            fill_color = "#89CFF0"  # light blue
            stroke_color = "#0066CC"  # darker blue
            # Create initial circle
            circle = Circle(
                radius=2,
                fill_color=fill_color,
                fill_opacity=1,
                stroke_color=stroke_color,
                stroke_width=2
            )
            # Calculate square side length to maintain approximate area
            # Area of circle = πr² ≈ 12.57
            # Side of square = √(πr²)
            square_side = np.sqrt(PI * 4)  # ≈ 3.54
            # Create target square with same area
            square = Square(
                side_length=square_side,
                fill_color=fill_color,
                fill_opacity=1,
                stroke_color=stroke_color,
                stroke_width=2
            )
            # Add labels to show the transformation
            circle_text = Text("Area ≈ 12.57", font_size=36)
            circle_text.to_edge(UP)
            square_text = Text("Area ≈ 12.57", font_size=36)
            square_text.to_edge(UP)
            # Initial state
            self.add(circle, circle_text)
            # Transform circle to square
            self.play(
                Transform(circle, square),
                Transform(circle_text, square_text),
                rate_func=smooth,
                run_time=1.5
            )
            # Pause briefly at the end
            self.wait(0.5)

        # Scene 3
        with self.voiceover(text="""And here we have our perfect square, completing our circle's transformation journey.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Calculate square side length based on circle with radius 2
            # Area of circle = πr² = 4π
            # side_length = √(4π)
            side_length = np.sqrt(4 * PI)
            # Create the square with specified properties
            square = Square(
                side_length=side_length,
                stroke_width=2,
                stroke_color="#2596BE",
                fill_color="#2596BE",
                fill_opacity=1
            )
            # Position square at center (ORIGIN)
            square.move_to(ORIGIN)
            # Add square to scene (it's already visible at start)
            self.add(square)
            # Wait for 0.5 seconds
            self.wait(0.5)
            # Fade out the square over 0.3 seconds
            self.play(FadeOut(square), run_time=0.3)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
