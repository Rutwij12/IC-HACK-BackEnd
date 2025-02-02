from manim import *

class UnderstandingSetUnion(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Set Union", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Create Set A
        set_a_text = MathTex(
            "A = \\{1, 2, 3\\}",
            font_size=36
        ).set_color(BLUE)
        set_a_text.shift(LEFT * 3)
        
        # Create Set B
        set_b_text = MathTex(
            "B = \\{3, 4, 5\\}",
            font_size=36
        ).set_color(RED)
        set_b_text.shift(RIGHT * 3)

        # Display sets with fade in
        self.play(FadeIn(set_a_text))
        self.play(FadeIn(set_b_text))
        self.wait(1)

        # Create and display union symbol
        union_symbol = MathTex("\\cup", font_size=44)
        self.play(
            GrowFromCenter(union_symbol)
        )

        # Create union text
        union_text = MathTex(
            "\\text{Union: } A \\cup B",
            font_size=36
        )
        union_text.shift(DOWN * 0.5)
        self.play(Write(union_text))
        self.wait(1)

        # Create final result
        final_result = MathTex(
            "A \\cup B = \\{",
            "1", ",\\,", "2", ",\\,", "3", ",\\,", "4", ",\\,", "5",
            "\\}",
            font_size=36
        )
        final_result.shift(UP * 1)
        
        # Color the elements
        final_result[1].set_color(BLUE)  # 1
        final_result[3].set_color(BLUE)  # 2
        final_result[5].set_color(PURPLE)  # 3 (common element)
        final_result[7].set_color(RED)   # 4
        final_result[9].set_color(RED)   # 5

        # Animate sets moving to center and forming union
        self.play(
            set_a_text.animate.shift(RIGHT * 1.5),
            set_b_text.animate.shift(LEFT * 1.5),
        )
        
        self.play(
            TransformFromCopy(
                VGroup(set_a_text, union_symbol, set_b_text),
                final_result
            )
        )
        self.wait(1)

        # Pulse animation for final result
        self.play(
            final_result.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1
        )
        
        # Final pause
        self.wait(1)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )