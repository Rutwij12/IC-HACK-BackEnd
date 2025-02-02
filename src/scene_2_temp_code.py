from manim import *

class EmptyAndFiniteSets(Scene):
    def construct(self):
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