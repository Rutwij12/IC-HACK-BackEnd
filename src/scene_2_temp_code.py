from manim import *

class SetMembershipDemonstration(Scene):
    def construct(self):
        # Create the circle (set A)
        circle = Circle(radius=2, color="#2C3E50", stroke_width=2)
        circle.set_fill(color="#2C3E50", opacity=0.1)

        # Create the set label
        set_label = MathTex("A = \\{1, 2, 3, 4\\}").scale(1.2)
        set_label.move_to(circle.get_top() + DOWN * 0.5)

        # Create elements inside the circle
        element_2 = MathTex("2").move_to(circle.get_center() + LEFT)
        element_4 = MathTex("4").move_to(circle.get_center() + RIGHT)

        # Create elements outside the circle
        element_5 = MathTex("5").move_to(circle.get_center() + LEFT * 2 + DOWN)
        element_7 = MathTex("7").move_to(circle.get_center() + RIGHT * 2 + DOWN)

        # Create membership statements
        membership_2 = MathTex("2 \\in A").move_to(LEFT * 2.5 + UP * 2)
        membership_4 = MathTex("4 \\in A").move_to(RIGHT * 2.5 + UP * 2)
        membership_5 = MathTex("5 \\notin A").move_to(LEFT * 2.5 + DOWN * 2)
        membership_7 = MathTex("7 \\notin A").move_to(RIGHT * 2.5 + DOWN * 2)

        # Color the membership symbols
        for tex in [membership_2, membership_4]:
            tex[0][1].set_color("#27AE60")  # Color ∈ green
        
        for tex in [membership_5, membership_7]:
            tex[0][1].set_color("#E74C3C")  # Color ∉ red

        # Initial animations
        self.play(
            Create(circle),
            FadeIn(set_label)
        )

        # Animate the inside elements and their membership statements
        self.wait(0.5)
        self.play(FadeIn(element_2))
        self.play(FadeIn(membership_2))
        
        self.wait(0.5)
        self.play(FadeIn(element_4))
        self.play(FadeIn(membership_4))

        # Animate the outside elements and their membership statements
        self.wait(0.5)
        self.play(FadeIn(element_5))
        self.play(FadeIn(membership_5))
        
        self.wait(0.5)
        self.play(FadeIn(element_7))
        self.play(FadeIn(membership_7))

        # Final pause
        self.wait(1)