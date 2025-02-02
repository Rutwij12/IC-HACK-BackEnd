from manim import *
import random
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class CombinedScene(VoiceoverScene, MovingCameraScene):
    def construct(self):
        # Set up Azure TTS service
        self.set_speech_service(AzureService(
            voice='en-US-JennyNeural',
            style='friendly'
        ))
        self.play(self.camera.frame.animate.scale(1.2))

        # Scene 1
        with self.voiceover(text="""Let's see how everyday objects like an apple, a ball, and a star can become a mathematical set. Watch as these items transform into numbers, and then get wrapped in special brackets that make them a proper set.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Physical Items
            # Create circular objects with labels
            apple = Circle(radius=0.4, color=RED, fill_opacity=0.8)
            ball = Circle(radius=0.4, color=BLUE, fill_opacity=0.8)
            star = Circle(radius=0.4, color=YELLOW, fill_opacity=0.8)
            # Add labels below the objects
            apple_text = Text("Apple", font_size=24).next_to(apple, DOWN, buff=0.2)
            ball_text = Text("Ball", font_size=24).next_to(ball, DOWN, buff=0.2)
            star_text = Text("Star", font_size=24).next_to(star, DOWN, buff=0.2)
            # Position objects in a horizontal line
            objects_group = VGroup(apple, ball, star).arrange(RIGHT, buff=1)
            objects_group.shift(UP * 0.5)
            # Position labels
            apple_text.next_to(apple, DOWN, buff=0.2)
            ball_text.next_to(ball, DOWN, buff=0.2)
            star_text.next_to(star, DOWN, buff=0.2)
            # Create a group of all physical objects and their labels
            physical_items = VGroup(
                apple, ball, star,
                apple_text, ball_text, star_text
            )
            # Animate the appearance of physical items
            self.play(
                FadeIn(physical_items),
                run_time=1.5
            )
            self.wait(1)
            # Part 2: Transition to Mathematical Set
            # Create numbers in the same positions as objects
            numbers = VGroup(
                *[MathTex(str(i)) for i in range(1, 4)]
            ).arrange(RIGHT, buff=1)
            numbers.move_to(objects_group.get_center())
            # Transition from objects to numbers
            self.play(
                FadeOut(physical_items),
                FadeIn(numbers),
                run_time=1.5
            )
            self.wait(1)
            # Part 3: Adding Set Notation
            # Create the full set notation
            final_set = MathTex(r"\{1, 2, 3\}")
            final_set.scale(1.5)
            # Position the final set in the center
            final_set.move_to(ORIGIN)
            # Animate the transition to set notation
            self.play(
                TransformMatchingShapes(numbers, final_set),
                run_time=1.5
            )
            self.wait(2)

        # Scene 2
        with self.voiceover(text="""In a set, each number can appear only once. As we combine these identical twos, we see that sets automatically eliminate any duplicates, leaving us with the unique elements one, two, and three.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Initial set elements
            one = Text("1", color=BLUE).scale(1.5)
            two1 = Text("2", color=RED).scale(1.5)
            two2 = Text("2", color=RED).scale(1.5)
            three = Text("3", color=GREEN).scale(1.5)
            # Create braces
            left_brace = Text("{").scale(1.5)
            right_brace = Text("}").scale(1.5)
            # Initial positioning
            elements = VGroup(left_brace, one, two1, two2, three, right_brace)
            elements.arrange(RIGHT, buff=0.5)
            elements.move_to(UP)
            # Fade in initial set
            self.play(FadeIn(elements))
            self.wait(1)
            # Store the original position of the first '2' for later
            two1_original_pos = two1.get_center()
            # Animate the merging of the two 2s
            self.play(
                two2.animate.move_to(two1.get_center()),
                rate_func=smooth,
                run_time=2
            )
            # Flash effect and pulse animation
            self.play(
                Flash(two1.get_center(), color=RED, flash_radius=0.5),
                two1.animate.scale(1.2),
                run_time=0.5
            )
            self.play(two1.animate.scale(1/1.2), run_time=0.5)
            # Remove the second 2
            self.remove(two2)
            # Rearrange remaining elements
            final_set = VGroup(left_brace, one, two1, three, right_brace)
            final_set.arrange(RIGHT, buff=0.5)
            final_set.move_to(UP)
            # Animate the rearrangement
            self.play(
                *[elem.animate.move_to(final_set[i].get_center()) 
                  for i, elem in enumerate([left_brace, one, two1, three, right_brace])],
                run_time=1.5
            )
            # Add explanatory text
            explanation = Text("Sets contain unique elements", 
                             font="Arial").scale(0.8)
            explanation.move_to(DOWN)
            # Fade in the explanation
            self.play(FadeIn(explanation))
            # Final hold
            self.wait(3)

        # Scene 3
        with self.voiceover(text="""A set is a collection of distinct elements. We can show this with the set A containing two, four, six, and eight. Empty sets contain no elements, while sets can be either finite with specific elements, or infinite continuing forever.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Elements and Sets
            title = Text("Sets", font_size=48).shift(UP*2)
            # Create oval and numbers
            oval = Ellipse(width=3, height=2, color=WHITE)
            numbers = VGroup(*[MathTex(str(n), font_size=36) for n in [2, 4, 6, 8]])
            numbers.arrange(RIGHT, buff=0.6).move_to(oval.get_center())
            # Set notation
            set_notation = MathTex("A = \\{2, 4, 6, 8\\}", font_size=32).shift(DOWN*1.5)
            membership = MathTex("2 \\in A", font_size=32).shift(DOWN*2)
            # Animate Part 1
            self.play(Write(title))
            self.play(Create(oval), Write(numbers))
            self.play(Write(set_notation))
            self.play(Write(membership))
            self.play(numbers[0].animate.scale(1.2), run_time=0.3)
            self.play(numbers[0].animate.scale(1/1.2), run_time=0.3)
            # Fade out Part 1
            self.play(
                *[FadeOut(obj) for obj in [title, oval, numbers, set_notation, membership]]
            )
            # Part 2: Empty Set
            empty_set_oval = Ellipse(width=2, height=1.5, color=WHITE).shift(LEFT)
            empty_braces = MathTex("\\{ \\}", font_size=36).shift(LEFT)
            equals = MathTex("=", font_size=36)
            empty_symbol = MathTex("\\emptyset", font_size=36).shift(RIGHT)
            empty_label = Text("Empty Set", font_size=32).shift(DOWN)
            # Animate Part 2
            self.play(
                Create(empty_set_oval),
                Write(empty_braces),
                Write(equals),
                Write(empty_symbol),
                Write(empty_label)
            )
            # Fade out Part 2
            self.play(
                *[FadeOut(obj) for obj in [empty_set_oval, empty_braces, equals, empty_symbol, empty_label]]
            )
            # Part 3: Finite vs Infinite Sets
            finite_set = MathTex("\\{1, 2, 3, 4\\}", font_size=36).shift(LEFT*2)
            infinite_set = MathTex("\\{1, 2, 3, ...\\}", font_size=36).shift(RIGHT*2)
            finite_label = Text("Finite Set", font_size=32).shift(LEFT*2 + DOWN)
            infinite_label = Text("Infinite Set", font_size=32).shift(RIGHT*2 + DOWN)
            # Animate Part 3
            self.play(
                Write(finite_set),
                Write(infinite_set)
            )
            self.play(
                Write(finite_label),
                Write(infinite_label)
            )
            # Hold final state
            self.wait()

        # Scene 4
        with self.voiceover(text="""Let's explore subset relationships. When all elements of set A are also in set B, we call A a subset of B. Here we see that the three numbers in set A - 1, 2, and 3 - are all contained within set B.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # 1. Title
            title = Text("Subset Relationships", font_size=40)
            title.to_edge(UP, buff=0.5)
            # 2. Create Circles for Venn Diagram
            circle_b = Circle(radius=2, color=BLUE, fill_opacity=0.3)
            circle_b.move_to(ORIGIN)
            circle_a = Circle(radius=1, color=RED, fill_opacity=0.3)
            circle_a.move_to(LEFT*0.5)
            # 3. Create Labels
            label_b = MathTex("B", font_size=36).move_to(RIGHT*1.5 + UP)
            label_a = MathTex("A", font_size=36).move_to(LEFT*0.5)
            # Create set notation
            set_a = MathTex("A = \\{1, 2, 3\\}", font_size=36).move_to(LEFT*2 + DOWN*2)
            set_b = MathTex("B = \\{1, 2, 3, 4, 5\\}", font_size=36).move_to(RIGHT*2 + DOWN*2)
            # 4. Create subset notation
            subset_notation = MathTex("A \\subseteq B", font_size=40).move_to(DOWN*3)
            subset_text = Text("A is a subset of B", font_size=24).next_to(subset_notation, DOWN, buff=0.2)
            # Animations
            # 1. Title animation
            self.play(FadeIn(title), run_time=0.5)
            self.wait(0.5)
            # 2. Venn diagram animation
            self.play(
                Create(circle_b),
                run_time=0.5
            )
            self.play(
                Create(circle_a),
                run_time=0.5
            )
            self.wait(0.5)
            # 3. Labels animation
            self.play(
                FadeIn(label_b),
                FadeIn(label_a),
                run_time=0.5
            )
            # Set notation animation
            self.play(
                FadeIn(set_a),
                FadeIn(set_b),
                run_time=0.5
            )
            self.wait(0.5)
            # 4. Subset notation animation
            self.play(
                FadeIn(subset_notation),
                FadeIn(subset_text),
                run_time=0.5
            )
            # Final pause to show complete scene
            self.wait(2)

        # Scene 5
        with self.voiceover(text="""Let's explore set operations using circles. Watch as Set A and Set B form overlapping regions. The union combines all elements, while the intersection shows what they share in common - revealing the numbers 3 and 4 in their overlapping purple section.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Create circles
            circle_a = Circle(radius=2, color=BLUE).shift(LEFT)
            circle_b = Circle(radius=2, color=RED).shift(RIGHT)
            # Set fill opacity
            circle_a.set_fill(BLUE, opacity=0.3)
            circle_b.set_fill(RED, opacity=0.3)
            # Create labels
            label_a = Text("A").next_to(circle_a, LEFT)
            label_b = Text("B").next_to(circle_b, RIGHT)
            # Create numbers for Set A
            num_1 = Text("1").move_to(LEFT*2 + UP)
            num_2 = Text("2").move_to(LEFT*2 + DOWN)
            num_3 = Text("3").move_to(UP*0.5)
            num_4 = Text("4").move_to(DOWN*0.5)
            num_5 = Text("5").move_to(RIGHT*2 + UP)
            num_6 = Text("6").move_to(RIGHT*2 + DOWN)
            # Group numbers for each region
            a_only_nums = VGroup(num_1, num_2)
            b_only_nums = VGroup(num_5, num_6)
            intersection_nums = VGroup(num_3, num_4)
            all_nums = VGroup(num_1, num_2, num_3, num_4, num_5, num_6)
            # Initial display (0-3 seconds)
            self.play(
                FadeIn(circle_a, circle_b),
                FadeIn(label_a, label_b)
            )
            self.play(
                FadeIn(a_only_nums),
                FadeIn(b_only_nums),
                FadeIn(intersection_nums)
            )
            # Union Operation (4-8 seconds)
            union_text = MathTex(r"A \cup B = \{1, 2, 3, 4, 5, 6\}").to_edge(UP)
            # Create union highlight
            union_outline = VGroup(circle_a, circle_b).copy()
            union_outline.set_fill(opacity=0)
            union_outline.set_stroke(color=YELLOW, width=4)
            self.play(Write(union_text))
            self.play(Create(union_outline))
            self.play(
                all_nums.animate.set_color(YELLOW),
                flash_time=0.5
            )
            self.play(
                all_nums.animate.set_color(WHITE),
                FadeOut(union_outline)
            )
            # Intersection Operation (9-15 seconds)
            intersection_text = MathTex(r"A \cap B = \{3, 4\}").to_edge(UP)
            # Fade out union elements and text
            self.play(
                FadeOut(union_text),
                a_only_nums.animate.set_opacity(0.2),
                b_only_nums.animate.set_opacity(0.2)
            )
            # Show intersection
            self.play(Write(intersection_text))
            intersection_highlight = Intersection(circle_a, circle_b)
            intersection_highlight.set_fill(PURPLE, opacity=0.5)
            intersection_highlight.set_stroke(color=YELLOW, width=4)
            self.play(
                FadeIn(intersection_highlight),
                intersection_nums.animate.set_color(YELLOW)
            )
            # Final fade out
            self.wait(1)
            self.play(
                *[FadeOut(mob) for mob in self.mobjects]
            )

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
