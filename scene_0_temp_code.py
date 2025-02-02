from manim import *

class RightTriangleSine(Scene):
    def construct(self):
        # Title
        title = Text("Sine in Right Triangles").scale(1.2)
        title.to_edge(UP)
        
        # Create and position the right triangle
        # Starting point for the triangle
        start_point = LEFT * 2 + DOWN * 0.5
        
        # Calculate other points
        bottom_right = start_point + RIGHT * 4  # 4 units right
        top_point = start_point + UP * 3        # 3 units up
        
        # Create the triangle sides
        base = Line(start_point, bottom_right, color=BLUE)
        height = Line(bottom_right, top_point, color=RED)
        hypotenuse = Line(start_point, top_point, color=GREEN)
        
        # Create right angle marker
        right_angle = RightAngle(base, height, length=0.4, color=WHITE)
        
        # Create angle theta
        theta = Angle(base, hypotenuse, radius=0.6, color=PURPLE)
        theta_label = MathTex("\\theta", color=PURPLE).scale(0.8)
        theta_label.next_to(theta, LEFT, buff=0.1)
        
        # Create side labels
        height_label = MathTex("3", color=RED)
        base_label = MathTex("4", color=BLUE)
        hyp_label = MathTex("5", color=GREEN)
        
        # Position labels
        height_label.next_to(height, RIGHT, buff=0.2)
        base_label.next_to(base, DOWN, buff=0.2)
        hyp_label.next_to(hypotenuse, UP + RIGHT, buff=0.2)
        
        # Create sine formula
        sine_formula = MathTex(
            "\\sin \\theta = \\frac{\\text{opposite}}{\\text{hypotenuse}} = \\frac{3}{5}"
        ).scale(0.9)
        sine_formula.next_to(base, DOWN, buff=1.5)
        
        # Animation sequence
        # 1. Show title
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        # 2. Draw triangle
        self.play(Create(base))
        self.play(Create(height))
        self.play(Create(hypotenuse))
        self.play(Create(right_angle))
        
        # 3. Add labels
        self.play(
            Write(height_label),
            Write(base_label),
            Write(hyp_label)
        )
        
        # 4. Add angle θ
        self.play(
            Create(theta),
            Write(theta_label)
        )
        
        # 5. Show sine formula with highlighting
        self.play(Write(sine_formula))
        self.play(
            Indicate(height, color=RED),
            Indicate(hypotenuse, color=GREEN)
        )
        
        # Final pause
        self.wait(2)