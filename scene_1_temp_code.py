from manim import *

class SingleNeuronBasics(Scene):
    def construct(self):
        # 1. Title Display
        title = Text("Single Artificial Neuron", font_size=48).to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=1)
        
        # 2. Basic Neuron Structure
        # Create neuron body
        neuron = Circle(radius=0.5, color=WHITE)
        
        # Create input lines
        input_lines = VGroup(*[
            Line(start=np.array([-3, i, 0]), end=np.array([0, i, 0]), color="#2C88D9")
            for i in [1, 0, -1]
        ])
        
        # Create input labels
        input_labels = VGroup(*[
            MathTex(f"x_{i}", color=WHITE).move_to(np.array([-3.5, i, 0]))
            for i in [1, 2, 3]
        ])
        
        # Create weight labels
        weight_labels = VGroup(*[
            MathTex(f"w_{i}", color="#FFB6C1").move_to(np.array([-2, i, 0]))
            for i in [1, 2, 3]
        ])
        
        # Create output line
        output_line = Line(
            start=np.array([0.5, 0, 0]), 
            end=np.array([3, 0, 0]), 
            color="#98FB98"
        )
        
        # Animate neuron structure
        self.play(
            Create(input_lines, run_time=1),
            FadeIn(input_labels, run_time=1),
        )
        self.play(
            FadeIn(weight_labels, run_time=1),
            Create(neuron, run_time=1),
        )
        self.play(Create(output_line, run_time=0.5))
        
        # 3. Mathematical Expression
        equation = MathTex(
            "y = f(w_1x_1 + w_2x_2 + w_3x_3 + b)",
            color=WHITE
        ).shift(DOWN * 2)
        
        activation_label = Text(
            "activation function", 
            font_size=24,
            color=WHITE
        ).next_to(equation, DOWN, buff=0.3)
        
        self.play(
            FadeIn(equation),
            FadeIn(activation_label)
        )
        
        # 4. Example Values
        example_values = VGroup(
            Text("Input values:", font_size=24),
            Text("x₁ = 0.5", font_size=24),
            Text("x₂ = -1.0", font_size=24),
            Text("x₃ = 0.8", font_size=24),
            Text("Weights:", font_size=24),
            Text("w₁ = 0.3", font_size=24),
            Text("w₂ = 0.6", font_size=24),
            Text("w₃ = -0.2", font_size=24),
            Text("bias = 0.1", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Create background rectangle
        bg_rect = SurroundingRectangle(
            example_values, 
            color=WHITE, 
            buff=0.2,
            corner_radius=0.1
        )
        
        example_group = VGroup(bg_rect, example_values).move_to(
            np.array([4, -0.5, 0])
        ).scale(0.8)
        
        self.play(
            FadeIn(example_group, run_time=1)
        )
        
        # Hold final frame
        self.wait(2)