from manim import *

class FundamentalTheoremScene(Scene):
    def construct(self):
        # Part 1: Title and General Formula
        title = Text("Fundamental Theorem of Calculus", font_size=40)
        title.to_edge(UP, buff=0.5)
        
        general_formula = MathTex(
            r"\int_a^b f(x)dx = F(b) - F(a)",
            font_size=36
        )
        general_formula.next_to(title, DOWN, buff=0.3)
        
        subtitle = Text("where F(x) is the antiderivative of f(x)", font_size=28)
        subtitle.next_to(general_formula, DOWN, buff=0.2)
        
        # Animate Part 1
        self.play(Write(title), run_time=1)
        self.play(
            Write(general_formula),
            Write(subtitle),
            run_time=1.5
        )
        
        # Group and move initial elements up
        initial_group = VGroup(title, general_formula, subtitle)
        self.play(
            initial_group.animate.scale(0.8).to_edge(UP, buff=0.2),
            run_time=1
        )

        # Part 2: Specific Example
        integral = MathTex(
            r"\int_1^2 x^2 dx = \left[\frac{1}{3}x^3\right]_1^2",
            font_size=36
        )
        integral.move_to(ORIGIN)

        steps = VGroup(
            MathTex(r"= \frac{1}{3}(2^3) - \frac{1}{3}(1^3)", font_size=36),
            MathTex(r"= \frac{1}{3}(8) - \frac{1}{3}(1)", font_size=36),
            MathTex(r"= \frac{8}{3} - \frac{1}{3}", font_size=36),
            MathTex(r"= \frac{7}{3}", font_size=36)
        )

        # Position steps
        for i, step in enumerate(steps):
            if i == 0:
                step.next_to(integral, DOWN, buff=0.5)
            else:
                step.next_to(steps[i-1], DOWN, buff=0.3)

        # Animate Part 2
        self.play(Write(integral), run_time=1)
        for step in steps:
            self.play(Write(step), run_time=0.75)

        # Part 3: Highlight Final Answer
        final_answer = steps[-1]
        highlighted_answer = MathTex(r"= \frac{7}{3}", font_size=48, color=YELLOW)
        highlighted_answer.move_to(final_answer)

        brace = Brace(highlighted_answer, DOWN)
        brace_text = Text(
            "Area under curve from x=1 to x=2",
            font_size=24
        )
        brace_text.next_to(brace, DOWN, buff=0.2)

        # Animate Part 3
        self.play(
            ReplacementTransform(final_answer, highlighted_answer),
            run_time=0.75
        )
        self.play(
            Create(brace),
            Write(brace_text),
            run_time=1
        )

        # Pause at the end
        self.wait(1)