from manim import *

class SetUniqueness(Scene):
    def construct(self):
        # Title
        title = Text("Sets Have No Duplicates", font_size=48).to_edge(UP, buff=0.5)
        
        # Create the set with braces
        left_brace = Text("{", font_size=60)
        right_brace = Text("}", font_size=60)
        numbers = VGroup(*[Text(str(num), font_size=48) for num in [2, 5, 8, 3]])
        
        # Position the numbers and braces
        numbers.arrange(RIGHT, buff=0.5)
        left_brace.next_to(numbers, LEFT, buff=0.2)
        right_brace.next_to(numbers, RIGHT, buff=0.2)
        
        # Group everything together
        set_group = VGroup(left_brace, numbers, right_brace)
        set_group.move_to(ORIGIN)
        
        # Create the duplicate number and arrow
        duplicate = Text("5", font_size=48, color=RED)
        arrow = Arrow(start=DOWN * 2, end=DOWN * 0.5, color=WHITE)
        attempt_text = Text("Attempt to add 5", font_size=36)
        attempt_text.next_to(arrow, DOWN, buff=0.2)
        
        # Position duplicate number below
        duplicate.next_to(arrow, DOWN, buff=0.5)
        
        # Create rejection X
        rejection_x = Text("×", font_size=60, color=RED)
        
        # Bottom text
        bottom_text = Text("Duplicate elements are not allowed", 
                          font_size=36, 
                          color=LIGHT_GRAY)
        bottom_text.to_edge(DOWN, buff=1)
        
        # Animations
        # Part 1: Title and original set
        self.play(FadeIn(title))
        self.play(Write(left_brace), Write(right_brace))
        
        for number in numbers:
            self.play(FadeIn(number), run_time=0.5)
        self.wait(0.5)
        
        # Part 2: Duplicate attempt
        self.play(
            FadeIn(arrow),
            FadeIn(attempt_text),
            FadeIn(duplicate)
        )
        
        # Animate duplicate moving up
        target_pos = numbers[1].get_center()  # Position of existing 5
        self.play(duplicate.animate.move_to(target_pos))
        
        # Show rejection
        rejection_x.move_to(duplicate)
        self.play(
            FadeIn(rejection_x),
            duplicate.animate.scale(1.2).shift(UP * 0.1),  # Small bounce effect
        )
        self.play(
            duplicate.animate.scale(1/1.2).shift(DOWN * 0.1),  # Return from bounce
            run_time=0.3
        )
        
        # Fade out duplicate
        self.play(FadeOut(duplicate), FadeOut(rejection_x))
        
        # Show bottom text
        self.play(FadeIn(bottom_text))
        
        # Final pause
        self.wait(1)