from manim import *

class CollectionsIntroduction(Scene):
    def construct(self):
        # Title
        title = Text("Collections of Objects").move_to(UP * 2)
        
        # Create shapes
        # Circles group
        circles = VGroup(*[Circle(radius=0.25) for _ in range(3)])
        circles.arrange(RIGHT, buff=0.5)
        circles.move_to(LEFT * 4)
        circles.set_color(BLUE)
        circles_outline = SurroundingRectangle(circles, corner_radius=0.2, buff=0.3)
        circles_outline.set_stroke(color=BLUE_A, opacity=0.5)
        
        # Squares group
        squares = VGroup(*[Square(side_length=0.5) for _ in range(3)])
        squares.arrange(RIGHT, buff=0.5)
        squares.move_to(ORIGIN)
        squares.set_color(RED)
        squares_outline = SurroundingRectangle(squares, corner_radius=0.2, buff=0.3)
        squares_outline.set_stroke(color=RED_A, opacity=0.5)
        
        # Triangles group
        triangles = VGroup(*[Triangle().scale(0.5) for _ in range(3)])
        triangles.arrange(RIGHT, buff=0.5)
        triangles.move_to(RIGHT * 4)
        triangles.set_color(GREEN)
        triangles_outline = SurroundingRectangle(triangles, corner_radius=0.2, buff=0.3)
        triangles_outline.set_stroke(color=GREEN_A, opacity=0.5)
        
        # Bottom text
        bottom_text = Text("Related items can be grouped together").move_to(DOWN * 2)
        
        # Animations
        # Title phase (0-3 seconds)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(2.5)
        
        # First group - Circles (3-6 seconds)
        self.play(FadeIn(circles), run_time=0.5)
        self.play(Create(circles_outline), run_time=0.5)
        self.wait(2)
        
        # Second group - Squares (6-9 seconds)
        self.play(FadeIn(squares), run_time=0.5)
        self.play(Create(squares_outline), run_time=0.5)
        self.wait(2)
        
        # Third group - Triangles (9-12 seconds)
        self.play(FadeIn(triangles), run_time=0.5)
        self.play(Create(triangles_outline), run_time=0.5)
        self.wait(2)
        
        # Final text (12-15 seconds)
        self.play(FadeIn(bottom_text), run_time=0.5)
        self.wait(2.5)