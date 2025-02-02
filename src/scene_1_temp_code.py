from manim import *

class SetMembershipVisualization(Scene):
    def construct(self):
        # Part 1: Initial Setup
        set_text = MathTex("A = \\{2, 4, 6, 8\\}")
        set_text[0][0].set_color(BLUE)  # Color the 'A' blue
        set_text.shift(UP)
        
        title = Text("Set Membership Examples", font_size=36)
        title.next_to(set_text, DOWN, buff=0.5)
        
        # Fade in the initial elements
        self.play(
            FadeIn(set_text),
            FadeIn(title)
        )
        self.wait(1)

        # Part 2: Membership Tests
        # Row 1
        test1 = MathTex("2 \\in A").shift(LEFT * 2 + DOWN)
        checkmark1 = Text("✓", color=GREEN).next_to(test1, RIGHT, buff=0.5)
        
        # Row 2
        test2 = MathTex("5 \\in A").shift(LEFT * 2 + DOWN * 2)
        x_mark = Text("✗", color=RED).next_to(test2, RIGHT, buff=0.5)
        
        # Row 3
        test3 = MathTex("8 \\in A").shift(LEFT * 2 + DOWN * 3)
        checkmark2 = Text("✓", color=GREEN).next_to(test3, RIGHT, buff=0.5)

        # Animate membership tests
        self.play(Write(test1))
        self.play(Create(checkmark1))
        self.wait(0.5)
        
        self.play(Write(test2))
        self.play(Create(x_mark))
        self.wait(0.5)
        
        self.play(Write(test3))
        self.play(Create(checkmark2))
        self.wait(0.5)

        # Part 3: Highlight membership symbols
        for test in [test1, test2, test3]:
            self.play(
                test[0][1].animate.set_color(BLUE),
                run_time=0.3
            )
        
        # Add explanation note
        note = Text("∈ means 'is an element of'", font_size=32)
        note.shift(DOWN * 4)
        self.play(FadeIn(note))
        
        self.wait(1)