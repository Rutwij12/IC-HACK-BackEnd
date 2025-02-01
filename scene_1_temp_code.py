from manim import *

class SingleNeuronStructure(Scene):
    def construct(self):
        # Title
        title = Text("Single Neuron Structure", font_size=48)
        title.to_edge(UP, buff=0.5)
        title_initial = title.copy().scale(1.5).shift(UP)
        
        # Animate title
        self.play(FadeIn(title_initial))
        self.wait(1)
        self.play(Transform(title_initial, title))
        
        # Input nodes
        inputs = VGroup()
        input_labels = ["x1", "x2", "x3"]
        input_values = ["0.5", "0.3", "0.8"]
        for i, (label, val) in enumerate(zip(input_labels, input_values)):
            circle = Circle(radius=0.3, color=BLUE)
            text = Text(label, font_size=24)
            value = Text(f"={val}", font_size=20).next_to(circle, UP, buff=0.1)
            node = VGroup(circle, text, value).shift(LEFT * 6 + (1-i) * UP)
            inputs.add(node)
        
        # Weight nodes
        weights = VGroup()
        weight_labels = ["w1", "w2", "w3"]
        weight_values = ["0.4", "0.6", "0.2"]
        for i, (label, val) in enumerate(zip(weight_labels, weight_values)):
            rect = Rectangle(height=0.4, width=0.6, color=GREEN)
            text = Text(label, font_size=24)
            value = Text(f"={val}", font_size=20).next_to(rect, UP, buff=0.1)
            node = VGroup(rect, text, value).shift(LEFT * 4 + (1-i) * UP)
            weights.add(node)
        
        # Summation node
        sum_circle = Circle(radius=0.5, color=WHITE)
        sum_symbol = Text("Σ", font_size=36)
        bias = Text("b=0.1", font_size=24).next_to(sum_circle, UP, buff=0.2)
        sum_node = VGroup(sum_circle, sum_symbol)
        
        # Activation function
        activation = RoundedRectangle(height=1, width=1.5, corner_radius=0.2, color=PURPLE)
        activation_label = Text("f", font_size=36)
        activation_text = Text("ReLU", font_size=20).next_to(activation, UP, buff=0.2)
        activation_group = VGroup(activation, activation_label, activation_text).shift(RIGHT * 3)
        
        # Output node
        output_circle = Circle(radius=0.3, color=RED).shift(RIGHT * 6)
        output_label = Text("y", font_size=24)
        output_value = Text("=0.57", font_size=20).next_to(output_circle, UP, buff=0.1)
        output_node = VGroup(output_circle, output_label, output_value)
        
        # Center all text elements in their shapes
        for item in [*inputs, *weights, sum_node, activation_group, output_node]:
            for child in item:
                if isinstance(child, Text):
                    child.move_to(item[0].get_center())
        
        # Arrows
        input_arrows = VGroup(*[
            Arrow(start[0].get_right(), end[0].get_left(), color=WHITE)
            for start, end in zip(inputs, weights)
        ])
        
        weight_arrows = VGroup(*[
            Arrow(start[0].get_right(), sum_circle.get_left(), color=WHITE)
            for start in weights
        ])
        
        activation_arrow = Arrow(sum_circle.get_right(), activation.get_left(), color=WHITE)
        output_arrow = Arrow(activation.get_right(), output_circle.get_left(), color=WHITE)
        
        # Animation sequence
        self.play(FadeIn(inputs))
        self.wait(0.5)
        
        self.play(FadeIn(weights), Create(input_arrows))
        self.wait(0.5)
        
        self.play(FadeIn(sum_node), FadeIn(bias), Create(weight_arrows))
        self.wait(0.5)
        
        self.play(FadeIn(activation_group), Create(activation_arrow))
        self.wait(0.5)
        
        self.play(FadeIn(output_node), Create(output_arrow))
        self.wait(2)