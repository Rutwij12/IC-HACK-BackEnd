from manim import *

class MatrixDimensions(Scene):
    def construct(self):
        # Title
        title = Text("Matrix Multiplication: Dimensions Matter", color=WHITE)
        title.to_edge(UP)
        
        # Create matrices
        matrix_a = Matrix(
            [[1, 2, 3],
             [4, 5, 6]],
            left_bracket="[",
            right_bracket="]"
        ).set_color(BLUE)
        matrix_a.shift(LEFT * 3)
        
        matrix_b = Matrix(
            [[7, 8],
             [9, 0],
             [1, 2]],
            left_bracket="[",
            right_bracket="]"
        ).set_color(RED)
        matrix_b.shift(RIGHT * 3)
        
        # Create dimension labels
        label_a = Text("A (2×3)", color=BLUE).scale(0.8)
        label_a.next_to(matrix_a, DOWN)
        
        label_b = Text("B (3×2)", color=RED).scale(0.8)
        label_b.next_to(matrix_b, DOWN)
        
        # Create highlighted parts
        highlight_a = Text("3", color=BLUE).scale(0.8)
        highlight_a.next_to(label_a, DOWN)
        highlight_a.align_to(label_a.get_center() + RIGHT * 0.3, RIGHT)
        
        highlight_b = Text("3", color=RED).scale(0.8)
        highlight_b.next_to(label_b, DOWN)
        highlight_b.align_to(label_b.get_center() - RIGHT * 0.3, LEFT)
        
        # Create arrow and bottom text
        arrow = CurvedArrow(
            highlight_a.get_right(),
            highlight_b.get_left(),
            angle=-TAU/4
        ).set_color(YELLOW)
        
        match_text = Text("Inner dimensions must match!", color=GREEN).scale(0.8)
        match_text.to_edge(DOWN, buff=1)
        
        result_text = Text("(2×3) × (3×2) = (2×2)", color=WHITE).scale(0.7)
        result_text.next_to(match_text, DOWN)
        
        # Animation sequence
        self.play(FadeIn(title))
        self.wait()
        
        self.play(
            Write(matrix_a),
            FadeIn(label_a)
        )
        self.wait()
        
        self.play(
            Write(matrix_b),
            FadeIn(label_b)
        )
        self.wait()
        
        self.play(
            FadeIn(highlight_a),
            FadeIn(highlight_b)
        )
        self.wait()
        
        self.play(Create(arrow))
        self.play(Write(match_text))
        self.wait()
        
        self.play(FadeIn(result_text))
        self.wait()