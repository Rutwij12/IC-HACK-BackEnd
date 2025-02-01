from manim import *
import random
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class CombinedScene(VoiceoverScene):
    def construct(self):
        # Set up Azure TTS service
        self.set_speech_service(AzureService(
            voice='en-US-JennyNeural',
            style='friendly'
        ))


        # Scene 1
        with self.voiceover(text="""Let's explore functions, starting with y equals 2x. Watch as we plot this line and see how each input x gives us an output y that's twice its value. For example, when x is 1, y becomes 2.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Set background color to light gray
            self.camera.background_color = "#FFFFFF"
            # 1. Initial Setup - Title
            title = Text("Functions: The Building Blocks", font_size=40)
            title.set_color("#3B82F6")
            title.to_edge(UP, buff=0.5)
            # 2. Function Introduction
            function_eq = MathTex("y = 2x")
            function_eq.next_to(title, DOWN, buff=0.5)
            # Create coordinate system
            axes = Axes(
                x_range=[-3, 3],
                y_range=[-3, 3],
                axis_config={
                    "color": BLACK,
                    "stroke_width": 2,
                    "include_tip": True,
                },
                x_length=6,
                y_length=6
            )
            axes.shift(DOWN * 0.5)
            # Add labels
            x_label = axes.get_x_axis_label("x")
            y_label = axes.get_y_axis_label("y")
            # Create function line
            line = axes.plot(lambda x: 2*x, color="#EF4444")
            # Create dot and its labels
            dot = Dot(color="#10B981")
            dot.move_to(axes.c2p(1, 2))
            input_label = MathTex("\\text{Input: }1").scale(0.8)
            output_label = MathTex("\\text{Output: }2").scale(0.8)
            # Position labels near the dot
            input_label.next_to(axes.c2p(1, 0), DOWN)
            output_label.next_to(axes.c2p(0, 2), LEFT)
            # Create dashed lines
            v_line = DashedLine(
                axes.c2p(1, 0),
                axes.c2p(1, 2),
                color=GRAY
            )
            h_line = DashedLine(
                axes.c2p(0, 2),
                axes.c2p(1, 2),
                color=GRAY
            )
            # Animation sequence
            self.play(FadeIn(title), run_time=1)
            self.play(Write(function_eq), run_time=1)
            self.play(
                Create(axes),
                Write(x_label),
                Write(y_label),
                run_time=2
            )
            self.play(Create(line), run_time=2)
            # Animate dot movement
            self.play(
                FadeIn(dot),
                Create(v_line),
                Create(h_line),
                Write(input_label),
                Write(output_label),
                run_time=2
            )
            # Hold final state
            self.wait(2)
            # Fade everything out
            self.play(
                *[FadeOut(mob) for mob in self.mobjects],
                run_time=1.5
            )

        # Scene 2
        with self.voiceover(text="""Let's explore a single artificial neuron - the building block of neural networks. As we draw it, notice how inputs flow through weighted connections into the neuron body, which then processes and outputs a signal using an activation function.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 3
        with self.voiceover(text="""Here's our neural network with three layers. Input nodes in blue receive data, which flows through green hidden nodes, and finally reaches red output nodes - creating a complete pathway for information processing.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Define colors
            input_color = "#3498db"
            hidden_color = "#2ecc71"
            output_color = "#e74c3c"
            connection_color = "#95a5a6"
            # Create input layer neurons
            input_neurons = VGroup()
            input_labels = VGroup()
            for i, y in enumerate([1, -1]):
                neuron = Circle(radius=0.3, color=input_color, fill_opacity=0.5)
                neuron.move_to(np.array([-4, y, 0]))
                label = MathTex(f"x_{i+1}").next_to(neuron, DOWN)
                input_neurons.add(neuron)
                input_labels.add(label)
            # Create hidden layer neurons
            hidden_neurons = VGroup()
            for y in [1.5, 0, -1.5]:
                neuron = Circle(radius=0.3, color=hidden_color, fill_opacity=0.5)
                neuron.move_to(np.array([0, y, 0]))
                hidden_neurons.add(neuron)
            # Create output layer neurons
            output_neurons = VGroup()
            output_labels = VGroup()
            for i, y in enumerate([1, -1]):
                neuron = Circle(radius=0.3, color=output_color, fill_opacity=0.5)
                neuron.move_to(np.array([4, y, 0]))
                label = MathTex(f"y_{i+1}").next_to(neuron, DOWN)
                output_neurons.add(neuron)
                output_labels.add(label)
            # Create connections
            input_connections = VGroup()
            output_connections = VGroup()
            # Input to hidden connections
            for in_neuron in input_neurons:
                for hidden_neuron in hidden_neurons:
                    connection = Arrow(
                        start=in_neuron.get_center(),
                        end=hidden_neuron.get_center(),
                        color=connection_color,
                        buff=0.3,
                        stroke_opacity=0.7
                    )
                    input_connections.add(connection)
            # Hidden to output connections
            for hidden_neuron in hidden_neurons:
                for out_neuron in output_neurons:
                    connection = Arrow(
                        start=hidden_neuron.get_center(),
                        end=out_neuron.get_center(),
                        color=connection_color,
                        buff=0.3,
                        stroke_opacity=0.7
                    )
                    output_connections.add(connection)
            # Animation sequence
            # 1. Input Layer
            self.play(
                FadeIn(input_neurons),
                FadeIn(input_labels),
                run_time=2
            )
            # 2. Hidden Layer and connections
            self.play(
                FadeIn(hidden_neurons),
                Create(input_connections),
                run_time=3
            )
            # 3. Output Layer and connections
            self.play(
                FadeIn(output_neurons),
                FadeIn(output_labels),
                Create(output_connections),
                run_time=3
            )
            # 4. Information flow animation
            path_dots = []
            # Define path: input[0] -> hidden[1] -> output[0]
            path_points = [
                input_neurons[0].get_center(),
                hidden_neurons[1].get_center(),
                output_neurons[0].get_center()
            ]
            # Create dots for animation
            for i in range(len(path_points) - 1):
                dot = Dot(color=WHITE)
                dot.move_to(path_points[i])
                path_dots.append(dot)
                self.play(
                    dot.animate.move_to(path_points[i + 1]),
                    rate_func=linear,
                    run_time=1
                )
                self.play(FadeOut(dot), run_time=0.5)
            # Pause at the end to show final structure
            self.wait(1)

        # Scene 4
        with self.voiceover(text="""Let's see how a simple neural network learns. Starting with two weights connecting three nodes, we'll process an input of 2 to predict an output. After seeing the error, the network adjusts its weights to get closer to the desired result of 1.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 5
        with self.voiceover(text="""Here's a written digit 7, passed through a neural network. As the pixels flow into input nodes, they connect through a hidden layer, leading to ten possible digit outputs. The network confidently identifies this as the number 7.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # 1. Initial Setup
            title = Text("Digit Recognition").move_to([0, 3, 0])
            self.play(FadeIn(title))
            self.wait(1.5)
            self.play(FadeOut(title))
            # 2. Input Visualization
            # Create 5x5 grid
            pixel_pattern = [
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0]
            ]
            grid = VGroup()
            cell_size = 0.4
            for i in range(5):
                for j in range(5):
                    cell = Square(side_length=cell_size)
                    cell.move_to([-3 + j*cell_size, 1 - i*cell_size, 0])
                    if pixel_pattern[i][j] == 1:
                        cell.set_fill(color=GRAY, opacity=0.8)
                    cell.set_stroke(color=GRAY_C, width=1)
                    grid.add(cell)
            self.play(Create(grid))
            self.wait(0.3)
            # 3. Neural Network Layers
            # a) Input Layer
            input_layer = VGroup()
            input_nodes = []
            for i in range(25):
                node = Circle(radius=0.1, color=LIGHT_GRAY)
                row = i // 5
                y_pos = 1.5 - (row * 0.6)
                node.move_to([-1.5, y_pos, 0])
                input_layer.add(node)
                input_nodes.append(node)
            self.play(Create(input_layer))
            # Grid to input connections
            grid_connections = VGroup()
            for i in range(25):
                if pixel_pattern[i//5][i%5] == 1:
                    start = grid[i].get_center()
                    end = input_nodes[i].get_center()
                    line = Line(start, end, stroke_width=0.5, color=LIGHT_GRAY)
                    grid_connections.add(line)
            self.play(Create(grid_connections))
            # b) Hidden Layer
            hidden_layer = VGroup()
            hidden_nodes = []
            for i in range(10):
                node = Circle(radius=0.1, color=LIGHT_GRAY)
                y_pos = 1.2 - (i * 0.27)
                node.move_to([0, y_pos, 0])
                hidden_layer.add(node)
                hidden_nodes.append(node)
            self.play(Create(hidden_layer))
            # Input to hidden connections (30% of connections)
            hidden_connections = VGroup()
            for i in range(25):
                for j in range(10):
                    if np.random.random() < 0.3:
                        start = input_nodes[i].get_center()
                        end = hidden_nodes[j].get_center()
                        line = Line(start, end, stroke_width=0.5, color=LIGHT_GRAY)
                        hidden_connections.add(line)
            self.play(Create(hidden_connections))
            # c) Output Layer
            output_layer = VGroup()
            output_nodes = []
            for i in range(10):
                node = Circle(radius=0.1, color=LIGHT_GRAY)
                y_pos = 1.2 - (i * 0.27)
                node.move_to([1.5, y_pos, 0])
                label = Text(str(i), font_size=16).next_to(node, RIGHT, buff=0.1)
                output_layer.add(VGroup(node, label))
                output_nodes.append(node)
            self.play(Create(output_layer))
            # Hidden to output connections (30% of connections)
            output_connections = VGroup()
            for i in range(10):
                for j in range(10):
                    if np.random.random() < 0.3:
                        start = hidden_nodes[i].get_center()
                        end = output_nodes[j].get_center()
                        line = Line(start, end, stroke_width=0.5, color=LIGHT_GRAY)
                        output_connections.add(line)
            self.play(Create(output_connections))
            # 4. Final Prediction
            target_node = output_nodes[7]  # Node for digit 7
            self.play(
                target_node.animate.set_color(BLUE).set_fill(BLUE, opacity=0.3)
            )
            prediction_text = Text("Prediction: 7", font_size=24).move_to([2.5, 0.2, 0])
            confidence_text = Text("Confidence: 99.2%", font_size=24).move_to([2.5, -0.2, 0])
            self.play(
                Write(prediction_text),
                Write(confidence_text)
            )
            self.wait(1)