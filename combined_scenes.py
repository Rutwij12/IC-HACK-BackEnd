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
        with self.voiceover(text="""A linear function transforms input values into output values using a simple rule. When we input numbers like 0, 1, and 2, our function multiplies each by 2 and adds 1 to produce the corresponding outputs of 1, 3, and 5.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Function Introduction
            title = Text("Linear Function", font_size=36).shift(UP * 3)
            function = MathTex("y = 2x + 1", font_size=36).shift(UP * 2)
            self.play(
                Write(title),
                Write(function)
            )
            self.wait(0.5)
            # Part 2: Create number lines
            x_line = NumberLine(
                x_range=[-3, 5],
                length=6,
                include_numbers=True,
                include_tip=True
            ).shift(LEFT * 3)
            y_line = NumberLine(
                x_range=[-3, 5],
                length=6,
                include_numbers=True,
                include_tip=True
            ).shift(RIGHT * 3)
            x_label = Text("x", font_size=24).next_to(x_line, DOWN)
            y_label = Text("y", font_size=24).next_to(y_line, DOWN)
            self.play(
                Create(x_line),
                Create(y_line),
                Write(x_label),
                Write(y_label)
            )
            # Create function box
            function_box = Rectangle(height=1, width=2, fill_color=LIGHT_GRAY, 
                                   fill_opacity=0.3, stroke_color=GRAY)
            box_text = MathTex("f(x) = 2x + 1", font_size=24)
            box_group = VGroup(function_box, box_text)
            self.play(
                Create(function_box),
                Write(box_text)
            )
            # Create dots and arrows
            input_outputs = [(0, 1), (1, 3), (2, 5)]
            colors = [BLUE, GREEN, RED]
            for i, (x_val, y_val) in enumerate(input_outputs):
                # Create dots
                x_dot = Dot(x_line.number_to_point(x_val), color=colors[i])
                y_dot = Dot(y_line.number_to_point(y_val), color=colors[i])
                # Create labels
                x_text = MathTex(f"x={x_val}", font_size=24, color=colors[i])\
                    .next_to(x_dot, UP)
                y_text = MathTex(f"y={y_val}", font_size=24, color=colors[i])\
                    .next_to(y_dot, UP)
                # Create curved arrow
                arrow = CurvedArrow(
                    start_point=x_dot.get_center(),
                    end_point=y_dot.get_center(),
                    color=colors[i],
                    stroke_width=2,
                    angle=PI/4
                )
                # Animate elements
                self.play(
                    Create(x_dot),
                    Write(x_text),
                    Create(arrow),
                    Create(y_dot),
                    Write(y_text),
                    run_time=1
                )
                self.wait(0.5)
            # Final pause and fadeout
            self.wait(1)
            self.play(
                *[FadeOut(mob) for mob in self.mobjects],
                run_time=1
            )

        # Scene 2
        with self.voiceover(text="""Here's a neuron multiplying inputs with weights, adding a bias, then applying an activation function to produce its output. Watch how information flows through each component, transforming the input signals into a final result.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

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

        # Scene 3
        with self.voiceover(text="""Let's look at a simple neural network. Starting with our input layer of three neurons, connecting to two hidden layer neurons, and finally linking to a single output neuron. Each connection represents how information flows through the network.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Colors
            input_color = "#4B8BBE"
            hidden_color = "#946B9E"
            output_color = "#3F6B4F"
            # Title
            title = Text("Neural Network Architecture").scale(0.8)
            title.to_edge(UP, buff=0.5)
            self.play(FadeIn(title))
            self.wait(0.5)
            # Create layers
            # Input Layer
            input_neurons = VGroup()
            input_labels = VGroup()
            for i in range(3):
                neuron = Circle(radius=0.3, color=input_color, fill_opacity=0.5)
                neuron.shift(LEFT * 2.5 + (i-1) * UP)
                label = MathTex(f"x_{i+1}").next_to(neuron, DOWN, buff=0.2)
                input_neurons.add(neuron)
                input_labels.add(label)
            # Hidden Layer
            hidden_neurons = VGroup()
            hidden_labels = VGroup()
            for i in range(2):
                neuron = Circle(radius=0.3, color=hidden_color, fill_opacity=0.5)
                neuron.shift((i-0.5) * UP)
                label = MathTex(f"h_{i+1}").next_to(neuron, DOWN, buff=0.2)
                hidden_neurons.add(neuron)
                hidden_labels.add(label)
            # Output Layer
            output_neuron = Circle(radius=0.3, color=output_color, fill_opacity=0.5)
            output_neuron.shift(RIGHT * 2.5)
            output_label = MathTex("y").next_to(output_neuron, DOWN, buff=0.2)
            # Layer labels
            input_layer_label = Text("Input Layer", font_size=24).next_to(input_neurons, DOWN, buff=0.8)
            hidden_layer_label = Text("Hidden Layer", font_size=24).next_to(hidden_neurons, DOWN, buff=0.8)
            output_layer_label = Text("Output Layer", font_size=24).next_to(output_neuron, DOWN, buff=0.8)
            # Animate input layer
            for neuron, label in zip(input_neurons, input_labels):
                self.play(
                    Create(neuron),
                    Write(label),
                    run_time=0.5
                )
            self.play(Write(input_layer_label))
            self.wait(0.5)
            # Animate hidden layer and connections
            connections_in_to_hidden = VGroup()
            for h_neuron in hidden_neurons:
                for i_neuron in input_neurons:
                    line = Line(
                        i_neuron.get_center(), 
                        h_neuron.get_center(),
                        stroke_opacity=0.6,
                        stroke_width=2
                    )
                    connections_in_to_hidden.add(line)
            for neuron, label in zip(hidden_neurons, hidden_labels):
                self.play(
                    Create(neuron),
                    Write(label),
                    *[Create(conn) for conn in connections_in_to_hidden if np.array_equal(conn.get_end(), neuron.get_center())],
                    run_time=0.5
                )
            self.play(Write(hidden_layer_label))
            self.wait(0.5)
            # Animate output layer and connections
            connections_hidden_to_out = VGroup()
            for h_neuron in hidden_neurons:
                line = Line(
                    h_neuron.get_center(),
                    output_neuron.get_center(),
                    stroke_opacity=0.6,
                    stroke_width=2
                )
                connections_hidden_to_out.add(line)
            self.play(
                Create(output_neuron),
                Write(output_label),
                *[Create(conn) for conn in connections_hidden_to_out],
                run_time=0.5
            )
            self.play(Write(output_layer_label))
            # Final pause
            self.wait(2)

        # Scene 4
        with self.voiceover(text="""Let's see how a neural network processes inputs through its layers. As our inputs, 0.5 and 1.0, flow through the weighted connections, they combine at the hidden layer, get adjusted by a bias, and transform into our final output of 0.425.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Configure scene
            self.camera.background_color = WHITE
            # Title
            title = Text("Forward Pass Example", color=DARK_GRAY).scale(1.2)
            title.to_edge(UP, buff=0.5)
            # Create network components
            # Neurons
            input1 = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
            input2 = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
            hidden = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
            output = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
            # Position neurons
            input1.move_to(LEFT * 4 + UP * 1)
            input2.move_to(LEFT * 4 + DOWN * 1)
            hidden.move_to(LEFT * 1)
            output.move_to(RIGHT * 2)
            # Create connections
            conn1 = Line(input1.get_right(), hidden.get_left(), color=DARK_GRAY)
            conn2 = Line(input2.get_right(), hidden.get_left(), color=DARK_GRAY)
            conn3 = Line(hidden.get_right(), output.get_right(), color=DARK_GRAY)
            # Input values
            input1_val = MathTex("0.5", color=DARK_GRAY).next_to(input1, LEFT)
            input2_val = MathTex("1.0", color=DARK_GRAY).next_to(input2, LEFT)
            # Weights
            w1 = MathTex("w_1=0.3", color=BLUE_D).next_to(conn1, UP, buff=0.2)
            w2 = MathTex("w_2=0.2", color=BLUE_D).next_to(conn2, DOWN, buff=0.2)
            w3 = MathTex("w_3=0.5", color=BLUE_D).next_to(conn3, UP, buff=0.2)
            # Hidden layer calculations
            calc_hidden = VGroup(
                MathTex("(0.5 × 0.3) + (1.0 × 0.2)", color=DARK_GRAY),
                MathTex("= 0.35", color=DARK_GRAY),
                MathTex("+ b_1(0.1) = 0.45", color=BLUE_D),
                MathTex("ReLU(0.45) = 0.45", color=DARK_GRAY)
            ).arrange(DOWN, aligned_edge=LEFT).next_to(hidden, UP, buff=1)
            # Output layer calculations
            calc_output = VGroup(
                MathTex("0.45 × 0.5 = 0.225", color=DARK_GRAY),
                MathTex("+ b_2(0.2) = 0.425", color=BLUE_D)
            ).arrange(DOWN, aligned_edge=LEFT).next_to(output, UP, buff=1)
            final_output = MathTex("0.425", color=RED_D).next_to(output, RIGHT)
            # Animations
            self.play(Write(title))
            # Draw network
            self.play(
                Create(VGroup(input1, input2, hidden, output)),
                Create(VGroup(conn1, conn2, conn3))
            )
            # Show inputs and weights
            self.play(
                Write(input1_val),
                Write(input2_val)
            )
            self.play(
                Write(w1),
                Write(w2)
            )
            # Hidden layer calculations
            for calc in calc_hidden:
                self.play(Write(calc), run_time=0.8)
            # Output layer calculations
            self.play(Write(w3))
            for calc in calc_output:
                self.play(Write(calc), run_time=0.8)
            # Show final output
            self.play(Write(final_output))
            self.play(
                final_output.animate.scale(1.2),
                final_output.animate.set_color(RED_D)
            )
            self.wait(1)
            # Clean fade out
            self.play(
                *[FadeOut(mob) for mob in self.mobjects]
            )

        # Scene 5
        with self.voiceover(text="""When the network makes a prediction of 0.8, but the actual value is 0.3, it recognizes this error and adjusts its internal weights, gradually improving its accuracy through this learning process.""") as tracker:

            # Transition
            self.wait(0.5)  # Wait for a moment
            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
            self.wait(0.5)  # Brief pause before next scene

            # Part 1: Create Neural Network
            # Create nodes
            input_layer = VGroup(*[Circle(radius=0.3) for _ in range(2)])
            hidden_layer = VGroup(*[Circle(radius=0.3) for _ in range(2)])
            output_layer = Circle(radius=0.3)
            # Position nodes
            input_layer.arrange(DOWN, buff=1)
            hidden_layer.arrange(DOWN, buff=1)
            output_layer.move_to(RIGHT * 2)
            # Position layers
            input_layer.move_to(LEFT * 2)
            hidden_layer.move_to(ORIGIN)
            # Group all nodes
            all_nodes = VGroup(input_layer, hidden_layer, output_layer)
            all_nodes.move_to(ORIGIN)
            all_nodes.shift(UP * 1)  # Move network above center
            # Create connections
            connections = VGroup()
            for input_node in input_layer:
                for hidden_node in hidden_layer:
                    connections.add(Arrow(input_node.get_center(), hidden_node.get_center(),
                                       buff=0.3))
            for hidden_node in hidden_layer:
                connections.add(Arrow(hidden_node.get_center(), output_layer.get_center(),
                                    buff=0.3))
            # Fade in network
            self.play(
                FadeIn(all_nodes),
                Create(connections),
                run_time=2
            )
            # Part 2: Prediction Example
            prediction = Text("Prediction: 0.8", color=RED).scale(0.8)
            actual = Text("Actual: 0.3", color=GREEN).scale(0.8)
            error_text = Text("Error!", color=RED).scale(0.8)
            # Position texts
            prediction.next_to(all_nodes, DOWN, buff=0.5)
            actual.next_to(prediction, DOWN, buff=0.5)
            error_text.next_to(actual, DOWN, buff=0.5)
            # Create X mark
            x_mark = Cross(output_layer, stroke_color=RED)
            # Fade in prediction info
            self.play(
                FadeIn(prediction),
                FadeIn(actual),
                run_time=1
            )
            self.play(
                FadeIn(error_text),
                Create(x_mark),
                run_time=1
            )
            # Part 3: Weight Adjustment
            # Create rotating arrows for weight adjustment
            adjustment_arrows = VGroup()
            for connection in connections[:2]:  # Only add to some connections
                curve = ArcBetweenPoints(
                    connection.get_start() + RIGHT * 0.3 + UP * 0.3,
                    connection.get_end() + LEFT * 0.3 + UP * 0.3,
                    angle=-TAU/4
                ).set_color(YELLOW)
                adjustment_arrows.add(curve)
            adjusting_text = Text("Adjusting weights", color=YELLOW).scale(0.7)
            adjusting_text.next_to(hidden_layer, UP, buff=0.3)
            final_text = Text("Network learns by updating weights").scale(0.7)
            final_text.to_edge(DOWN, buff=0.5)
            # Create animation for rotating arrows
            self.play(
                Create(adjustment_arrows),
                FadeIn(adjusting_text),
                run_time=1
            )
            # Animate arrows rotation
            self.play(
                Rotate(adjustment_arrows, angle=TAU/2, about_point=adjustment_arrows.get_center()),
                run_time=2
            )
            # Add final text
            self.play(
                FadeIn(final_text),
                run_time=1
            )
            # Hold final state
            self.wait(2)