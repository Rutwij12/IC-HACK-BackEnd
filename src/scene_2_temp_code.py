from manim import *

class AntiderivativeIntroduction(Scene):
    def construct(self):
        # Title
        title = Text("Power Rule for Antiderivatives").scale(0.8)
        title.to_edge(UP, buff=0.5)
        
        # Original function setup
        original_label = Text("Original Function:", color=WHITE).scale(0.6)
        original_function = MathTex("f(x) = x^2", color=BLUE)
        original_group = VGroup(original_label, original_function).arrange(DOWN, buff=0.3)
        original_group.move_to(LEFT * 3)
        
        # Arrows and transformation labels
        arrow1 = Arrow(LEFT * 1.5, RIGHT * 0.5, color=GRAY)
        arrow1.next_to(original_function, RIGHT, buff=0.5)
        step1_label = Text("+1 to exponent", color=WHITE).scale(0.5)
        step1_label.next_to(arrow1, UP, buff=0.2)
        
        # First transformation
        intermediate = MathTex("x^3", color=BLUE)
        intermediate.next_to(arrow1, RIGHT, buff=0.5)
        
        # Second arrow and label
        arrow2 = Arrow(LEFT * 0.5, RIGHT * 1.5, color=GRAY)
        arrow2.next_to(intermediate, RIGHT, buff=0.5)
        step2_label = Text("÷ by new exponent (3)", color=WHITE).scale(0.5)
        step2_label.next_to(arrow2, UP, buff=0.2)
        
        # Final antiderivative
        antider_label = Text("Antiderivative:", color=WHITE).scale(0.6)
        final_function = MathTex("F(x) = \\frac{x^3}{3}", color=GREEN)
        final_group = VGroup(antider_label, final_function).arrange(DOWN, buff=0.3)
        final_group.move_to(RIGHT * 3)
        
        # Animations
        self.play(FadeIn(title), run_time=0.5)
        self.play(
            FadeIn(original_label),
            FadeIn(original_function),
            run_time=1
        )
        
        self.play(
            Create(arrow1),
            FadeIn(step1_label),
            run_time=1
        )
        
        self.play(
            TransformFromCopy(original_function, intermediate),
            run_time=1.5
        )
        
        self.play(
            Create(arrow2),
            FadeIn(step2_label),
            run_time=1
        )
        
        self.play(
            TransformFromCopy(intermediate, final_function),
            FadeIn(antider_label),
            run_time=1.5
        )
        
        # Hold the final scene
        self.wait(2)