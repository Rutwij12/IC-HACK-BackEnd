from manim import *

class NetworkArchitecture(Scene):
    def construct(self):
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