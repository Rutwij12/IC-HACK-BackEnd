from manim import *
import numpy as np

class NeuralNetworkDigitRecognition(Scene):
    def construct(self):
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