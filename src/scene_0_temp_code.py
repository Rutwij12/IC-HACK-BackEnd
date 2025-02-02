from manim import *

class SetDefinition(Scene):
    def construct(self):
        # Part 1: Create circles with different colors
        circle1 = Circle(radius=0.5, color=RED).move_to(LEFT*3)
        circle2 = Circle(radius=0.5, color=BLUE).move_to(ORIGIN)
        circle3 = Circle(radius=0.5, color=GREEN).move_to(RIGHT*3)

        # Animate circles appearing
        self.play(FadeIn(circle1))
        self.wait(0.5)
        self.play(FadeIn(circle2))
        self.wait(0.5)
        self.play(FadeIn(circle3))
        self.wait(0.5)

        # Part 2: Create and add numbers
        num1 = Text("1", color=WHITE, font_size=36).move_to(circle1.get_center())
        num2 = Text("2", color=WHITE, font_size=36).move_to(circle2.get_center())
        num3 = Text("3", color=WHITE, font_size=36).move_to(circle3.get_center())

        # Write numbers simultaneously
        self.play(
            Write(num1),
            Write(num2),
            Write(num3)
        )
        self.wait(0.5)

        # Part 3: Move circles with numbers to final positions
        # Group circles with their numbers
        group1 = VGroup(circle1, num1)
        group2 = VGroup(circle2, num2)
        group3 = VGroup(circle3, num3)

        # Animate movement to final positions
        self.play(
            group1.animate.move_to(LEFT),
            group2.animate.move_to(ORIGIN),
            group3.animate.move_to(RIGHT),
            run_time=1
        )

        # Create and add braces and commas
        left_brace = Text("{", color=WHITE, font_size=60).next_to(group1, LEFT, buff=0.2)
        right_brace = Text("}", color=WHITE, font_size=60).next_to(group3, RIGHT, buff=0.2)
        
        comma1 = Text(",", color=WHITE, font_size=36).move_to(
            (group1.get_center() + group2.get_center()) / 2
        )
        comma2 = Text(",", color=WHITE, font_size=36).move_to(
            (group2.get_center() + group3.get_center()) / 2
        )

        # Add braces and commas
        self.play(
            FadeIn(left_brace),
            FadeIn(right_brace),
            Write(comma1),
            Write(comma2)
        )
        self.wait(0.5)

        # Add title text
        title = Text("A Set: A collection of distinct objects", 
                    color=WHITE, 
                    font_size=40
        ).to_edge(UP, buff=1)

        self.play(Write(title))
        self.wait(2)