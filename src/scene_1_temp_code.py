from manim import *

class WhatIsASet(Scene):
    def construct(self):
        # 1. Initial State
        title = Tex("What is a Set?").scale(1.5).to_edge(UP, buff=0.5)
        empty_braces = Tex("\\{ \\}").scale(2)
        
        # Create numbers that will go inside braces
        numbers = [Tex(str(n)).scale(1.5).set_color(YELLOW) for n in [2, 5, 1, 4]]
        # Position numbers horizontally with spacing
        number_group = VGroup(*numbers).arrange(RIGHT, buff=0.7)
        
        # Create the braces that will surround the numbers
        left_brace = Tex("\\{").scale(2)
        right_brace = Tex("\\}").scale(2)
        
        # Position braces around where numbers will be
        brace_group = VGroup(left_brace, right_brace)
        left_brace.next_to(number_group, LEFT, buff=0.2)
        right_brace.next_to(number_group, RIGHT, buff=0.2)
        
        # Animate initial state
        self.play(Write(title))
        self.play(Write(brace_group))
        
        # 2. Adding Elements
        for number in numbers:
            self.play(
                FadeIn(number, scale=1.2),
                rate_func=smooth,
                run_time=0.5
            )
        
        # Create full set group for transformations
        set_group = VGroup(left_brace, *numbers, right_brace)
        
        # 3. Demonstrating Unordered Property
        # First rearrangement (sorted order)
        sorted_numbers = [Tex(str(n)).scale(1.5).set_color(YELLOW) for n in [1, 2, 4, 5]]
        sorted_group = VGroup(*sorted_numbers).arrange(RIGHT, buff=0.7)
        sorted_group.move_to(number_group)
        
        # Random order numbers
        random_numbers = [Tex(str(n)).scale(1.5).set_color(YELLOW) for n in [4, 1, 5, 2]]
        random_group = VGroup(*random_numbers).arrange(RIGHT, buff=0.7)
        random_group.move_to(number_group)
        
        # Add explanatory text
        unordered_text = Tex("Sets are unordered collections", color=LIGHT_BLUE)
        unordered_text.to_edge(DOWN, buff=1.5)
        
        # Animate rearrangements
        self.play(
            Transform(VGroup(*numbers), sorted_group),
            run_time=2
        )
        self.play(
            Transform(VGroup(*numbers), random_group),
            run_time=2
        )
        self.play(Write(unordered_text))
        
        # 4. Final State
        unique_text = Tex("Elements can only appear once", color=LIGHT_BLUE)
        unique_text.next_to(unordered_text, DOWN, buff=0.5)
        
        self.play(Write(unique_text))
        self.wait()