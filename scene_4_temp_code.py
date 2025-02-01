from manim import *

class LearningProcessOverview(Scene):
    def construct(self):
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