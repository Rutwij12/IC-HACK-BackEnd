from manim import *

class SimpleLearningProcess(Scene):
    def construct(self):
        # Create neural network nodes
        input_node = Circle(radius=0.3).move_to(LEFT * 3)
        hidden_node = Circle(radius=0.2)
        output_node = Circle(radius=0.3).move_to(RIGHT * 3)
        
        nodes = VGroup(input_node, hidden_node, output_node)
        nodes.shift(UP)
        
        # Create arrows
        arrow1 = Arrow(input_node.get_right(), hidden_node.get_left())
        arrow2 = Arrow(hidden_node.get_right(), output_node.get_left())
        arrows = VGroup(arrow1, arrow2)
        
        # Create labels
        input_label = MathTex("x=2").next_to(input_node, DOWN)
        output_label = MathTex("\\hat{y}").next_to(output_node, DOWN)
        w1_label = MathTex("w_1=0.5").next_to(arrow1, UP)
        w2_label = MathTex("w_2=0.3").next_to(arrow2, UP)
        
        # Group initial network elements
        network = VGroup(nodes, arrows, input_label, output_label, w1_label, w2_label)
        
        # 1. Initial Network Display
        self.play(
            FadeIn(nodes),
            Create(arrows),
            Write(input_label),
            Write(output_label),
            Write(w1_label),
            Write(w2_label)
        )
        self.wait()
        
        # 2. Forward Pass
        forward_pass = Text("Forward Pass:", font_size=30).move_to(DOWN * 0.5)
        calculation = MathTex(
            "2 \\rightarrow 2(0.5) = 1 \\rightarrow 1(0.3) = 0.3"
        ).next_to(forward_pass, DOWN)
        
        prediction = Text(
            "Predicted: 0.3, Desired: 1.0",
            font_size=30
        ).next_to(calculation, DOWN)
        
        error = Text(
            "Error = 0.7",
            font_size=30
        ).next_to(prediction, DOWN)
        
        self.play(Write(forward_pass))
        self.play(Write(calculation))
        self.play(Write(prediction))
        self.play(Write(error))
        self.wait()
        
        # 3. Weight Update
        updating = Text(
            "Updating weights...",
            font_size=30
        ).move_to(DOWN * 3)
        
        # New weight labels
        w1_new = MathTex("w_1=0.7").next_to(arrow1, UP).set_color(GREEN)
        w2_new = MathTex("w_2=0.5").next_to(arrow2, UP).set_color(GREEN)
        
        self.play(Write(updating))
        self.play(
            ReplacementTransform(w1_label, w1_new),
            ReplacementTransform(w2_label, w2_new)
        )
        
        final_text = Text(
            "Network adjusted to reduce error",
            font_size=30
        ).next_to(updating, DOWN)
        
        self.play(Write(final_text))
        self.wait()