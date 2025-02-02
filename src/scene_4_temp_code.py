from manim import *

class SetOperations(Scene):
    def construct(self):
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