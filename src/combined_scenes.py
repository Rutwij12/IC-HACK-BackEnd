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
        with self.voiceover(text="""Let's see how sets are formed - starting with individual elements, like one, two, and three. When we bring these distinct numbers together and enclose them in braces, we create a mathematical set - a collection of unique objects.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 2
        with self.voiceover(text="""Let's look at set membership. In the set A containing two, four, six, and eight, we can check if numbers belong. Two and eight are elements of A, but five is not - notice how we use the special membership symbol to write these statements.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 3
        with self.voiceover(text="""Let's explore sets, starting with the empty set - our foundation. A finite set contains a countable number of elements, like {1, 2, 3}. And remember, in any set, the order of elements doesn't matter - {1, 2} equals {2, 1}.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Empty Set
            empty_set_title = Text("Empty Set", font_size=48).shift(UP*1.5)
            empty_set_symbol = MathTex("\\emptyset", font_size=72).shift(UP*0.3)
            empty_set_braces = MathTex("\\{\\}", font_size=48).shift(DOWN*0.3)
            empty_set_explanation = Text("A set with no elements", font_size=36).shift(DOWN*1.3)
            empty_set_cardinality = MathTex("|\\emptyset| = 0", font_size=40).shift(DOWN*2)
            # Animate Part 1
            self.play(FadeIn(empty_set_title))
            self.play(FadeIn(empty_set_symbol))
            self.play(FadeIn(empty_set_braces))
            self.play(FadeIn(empty_set_explanation))
            self.play(FadeIn(empty_set_cardinality))
            part1_group = VGroup(empty_set_title, empty_set_symbol, empty_set_braces, 
                               empty_set_explanation, empty_set_cardinality)
            self.wait(1)
            self.play(FadeOut(part1_group))
            # Part 2: Finite Sets
            finite_sets_title = Text("Finite Sets", font_size=48).shift(UP*1.5)
            set1 = MathTex("\\{1\\}", font_size=40).shift(LEFT*3)
            set2 = MathTex("\\{1, 2, 3\\}", font_size=40)
            set3 = MathTex("\\{a, b, c\\}", font_size=40).shift(RIGHT*3)
            card1 = MathTex("|A| = 1", font_size=36).next_to(set1, DOWN)
            card2 = MathTex("|A| = 3", font_size=36).next_to(set2, DOWN)
            card3 = MathTex("|A| = 3", font_size=36).next_to(set3, DOWN)
            finite_explanation = MathTex("|A| < \\infty", "\\text{ finite cardinality}", 
                                       font_size=40).shift(DOWN*1.3)
            # Animate Part 2
            self.play(FadeIn(finite_sets_title))
            self.play(FadeIn(set1), FadeIn(set2), FadeIn(set3))
            self.play(FadeIn(card1), FadeIn(card2), FadeIn(card3))
            self.play(FadeIn(finite_explanation))
            part2_group = VGroup(finite_sets_title, set1, set2, set3, 
                               card1, card2, card3, finite_explanation)
            self.wait(1)
            self.play(FadeOut(part2_group))
            # Part 3: Order Property
            order_title = Text("Set Property: Order Doesn't Matter", 
                             font_size=48).shift(UP*1.5)
            set_initial = MathTex("\\{1, 2\\}", font_size=48).shift(UP*0.3)
            set_final = MathTex("\\{2, 1\\}", font_size=48).shift(UP*0.3)
            # Create circular arrow
            arrow = Arc(radius=0.5, angle=-2*PI, 
                       stroke_width=3).next_to(set_initial, RIGHT)
            axiom = Text("Axiom of Extensionality: {1, 2} = {2, 1}", 
                        font_size=36).shift(DOWN*1.3)
            # Animate Part 3
            self.play(FadeIn(order_title))
            self.play(FadeIn(set_initial))
            self.play(Create(arrow))
            self.play(Transform(set_initial, set_final))
            self.play(FadeIn(axiom))
            self.wait(1)

        # Scene 4
        with self.voiceover(text="""When set A contains all the elements of set B, B is a subset of A. Here, the elements 2, 4, and 6 belong to both sets, making B a subset of A.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Colors
            light_blue = "#ADD8E6"
            darker_blue = "#4682B4"
            # 1. Title sequence
            title = Text("Subsets", font_size=48)
            title.move_to(UP * 2)
            self.play(FadeIn(title))
            self.wait(1)
            self.play(FadeOut(title))
            # 2. Create Set A
            circle_a = Circle(radius=2, color=light_blue)
            circle_a.set_fill(light_blue, opacity=0.3)
            label_a = Text("A", font_size=36).next_to(circle_a, UR, buff=0.1)
            # Create numbers for Set A
            numbers_a = VGroup()
            positions = [
                UP * 0.8 + LEFT * 0.8,    # 1
                UP * 0.8 + RIGHT * 0.8,   # 2
                LEFT * 1.2,               # 3
                RIGHT * 1.2,              # 4
                DOWN * 0.8 + LEFT * 0.8,  # 5
                DOWN * 0.8 + RIGHT * 0.8  # 6
            ]
            for i, pos in zip(range(1, 7), positions):
                num = Text(str(i), font_size=36, color=BLACK)
                num.move_to(pos)
                numbers_a.add(num)
            # Animate Set A
            self.play(
                Create(circle_a),
                Write(label_a)
            )
            self.play(Write(numbers_a))
            self.wait(1)
            # 3. Create Set B
            circle_b = Circle(radius=1, color=darker_blue)
            circle_b.set_fill(darker_blue, opacity=0.3)
            circle_b.shift(RIGHT * 0.5 + DOWN * 0.3)  # Position within A
            label_b = Text("B", font_size=36).next_to(circle_b, DR, buff=0.1)
            # Create highlights for subset elements
            subset_indices = [1, 3, 5]  # indices for 2, 4, 6 in numbers_a
            highlights = VGroup()
            for idx in subset_indices:
                highlight = Circle(radius=0.3, color=YELLOW, fill_opacity=0.2)
                highlight.move_to(numbers_a[idx].get_center())
                highlights.add(highlight)
            # Animate Set B and highlights
            self.play(
                Create(circle_b),
                Write(label_b)
            )
            self.play(FadeIn(highlights))
            self.wait(1)
            # 4. Add subset symbol and text
            subset_symbol = MathTex(r"\subseteq", font_size=48)
            subset_symbol.next_to(circle_a, RIGHT, buff=0.5)
            subset_text = MathTex(r"B \subseteq A", font_size=36)
            subset_text.next_to(circle_a, DOWN, buff=0.5)
            self.play(
                Write(subset_symbol),
                Write(subset_text)
            )
            self.wait(2)
            # Fade everything out
            self.play(
                *[FadeOut(mob) for mob in [
                    circle_a, circle_b, label_a, label_b,
                    numbers_a, highlights, subset_symbol, subset_text
                ]]
            )

        # Scene 5
        with self.voiceover(text="""Let's explore set operations using two simple sets - A and B. As we see in our Venn diagram, their union includes all numbers from both sets, while their intersection shows only the shared elements, 3 and 4.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Introduction
            title = Text("Set Operations", font_size=40).to_edge(UP)
            set_a_text = Text("A = {1, 2, 3, 4}", font_size=32).move_to(LEFT * 2 + UP)
            set_b_text = Text("B = {3, 4, 5, 6}", font_size=32).move_to(RIGHT * 2 + UP)
            self.play(Write(title))
            self.play(
                FadeIn(set_a_text),
                FadeIn(set_b_text)
            )
            self.wait()
            # Part 2: Venn Diagram
            self.play(
                FadeOut(set_a_text),
                FadeOut(set_b_text)
            )
            # Create circles
            circle_a = Circle(radius=1.2, color=BLUE).move_to(LEFT * 0.8)
            circle_b = Circle(radius=1.2, color=RED).move_to(RIGHT * 0.8)
            circle_a.set_fill(BLUE, opacity=0.3)
            circle_b.set_fill(RED, opacity=0.3)
            # Labels for circles
            label_a = Text("A", font_size=32).move_to(LEFT * 1.5 + UP)
            label_b = Text("B", font_size=32).move_to(RIGHT * 1.5 + UP)
            # Numbers
            nums_a = [
                Text("1", font_size=28).move_to(LEFT * 1.0 + UP * 0.3),
                Text("2", font_size=28).move_to(LEFT * 1.0 + DOWN * 0.3),
            ]
            nums_intersection = [
                Text("3", font_size=28).move_to(LEFT * 0.2 + UP * 0.2),
                Text("4", font_size=28).move_to(LEFT * 0.2 + DOWN * 0.2),
            ]
            nums_b = [
                Text("5", font_size=28).move_to(RIGHT * 1.0 + UP * 0.3),
                Text("6", font_size=28).move_to(RIGHT * 1.0 + DOWN * 0.3),
            ]
            # Animate Venn diagram
            self.play(
                Create(circle_a),
                Create(circle_b),
            )
            self.play(
                Write(label_a),
                Write(label_b)
            )
            # Animate numbers appearing
            self.play(
                *[Write(num) for num in nums_a],
                *[Write(num) for num in nums_intersection],
                *[Write(num) for num in nums_b]
            )
            # Part 3: Operations
            union_text = Text("A ∪ B = {1, 2, 3, 4, 5, 6}", font_size=32).move_to(LEFT * 2.5 + DOWN * 2)
            intersection_text = Text("A ∩ B = {3, 4}", font_size=32).move_to(RIGHT * 2.5 + DOWN * 2)
            # Union highlight
            union_highlight = VGroup(circle_a.copy(), circle_b.copy())
            union_highlight.set_fill(YELLOW, opacity=0.2)
            # Intersection highlight
            intersection_highlight = Intersection(circle_a, circle_b)
            intersection_highlight.set_fill(PURPLE, opacity=0.4)
            intersection_highlight.set_stroke(width=0)
            # Show union
            self.play(Write(union_text))
            self.play(FadeIn(union_highlight))
            self.wait(0.5)
            self.play(FadeOut(union_highlight))
            # Show intersection
            self.play(Write(intersection_text))
            self.play(FadeIn(intersection_highlight))
            self.wait(0.5)
            self.play(FadeOut(intersection_highlight))
            self.wait()

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
