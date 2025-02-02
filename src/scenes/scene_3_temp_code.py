from manim import *

class EigenvalueCalculation(Scene):
    def construct(self):
        # Title
        title = Text("Finding Eigenvalues", font_size=36)
        title.to_edge(UP)
        
        # Initial Matrix A
        matrix_A = MathTex(r"\begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}")
        matrix_A.scale(0.8)
        
        # Show initial matrix with title
        self.play(
            Write(title),
            FadeIn(matrix_A)
        )
        self.wait()
        
        # Prepare eigenvalue equation components
        lambda_I = MathTex(r"\begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}")
        lambda_I.scale(0.8)
        
        minus = MathTex("-")
        equals = MathTex("=")
        
        # Characteristic matrix
        char_matrix = MathTex(r"\begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix}")
        char_matrix.scale(0.8)
        
        # Arrange equation A - λI
        equation_group = VGroup(
            matrix_A.copy(), minus, lambda_I, equals, char_matrix
        ).arrange(RIGHT)
        equation_group.next_to(title, DOWN, buff=1)
        
        # Transform to characteristic equation
        self.play(
            Transform(matrix_A, equation_group[0]),
            FadeIn(minus),
            FadeIn(lambda_I),
            FadeIn(equals),
            FadeIn(char_matrix)
        )
        self.wait()
        
        # Determinant equation
        det_eq = MathTex(
            r"\det", r"\begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix}", "=", "0"
        )
        det_eq.next_to(equation_group, DOWN, buff=1)
        
        self.play(
            FadeIn(det_eq)
        )
        self.wait()
        
        # Expanded determinant
        expanded_det = MathTex(
            r"(4-\lambda)(3-\lambda) - (1)(2) = 0"
        )
        expanded_det.next_to(det_eq, DOWN, buff=0.5)
        
        self.play(
            Write(expanded_det)
        )
        self.wait()
        
        # Final quadratic equation
        quadratic = MathTex(
            r"\lambda^2 - 7\lambda + 10 = 0"
        )
        quadratic.next_to(expanded_det, DOWN, buff=0.5)
        
        self.play(
            Write(quadratic)
        )
        self.wait()
        
        # Solutions
        solutions = MathTex(
            r"\lambda = 5 \text{ or } \lambda = 2"
        ).set_color(GREEN)
        solutions.next_to(quadratic, DOWN, buff=0.5)
        
        self.play(
            Write(solutions)
        )
        self.wait()