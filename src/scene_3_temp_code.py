from manim import *

class SubsetDemonstration(Scene):
    def construct(self):
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