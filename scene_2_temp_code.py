from manim import *

class NetworkArchitecture(Scene):
    def construct(self):
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
            Create(output_neu
ron),
            Write(output_label),
            *[Create(conn) for conn in connections_hidden_to_out],
            run_time=0.5
        )
        self.play(Write(output_layer_label))

        # Final pause
        self.wait(2)