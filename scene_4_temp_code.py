from manim import *

class LinearTransformationProperties(Scene):
    def construct(self):
        # Part 1: Initial Grid Setup
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": "#888888",
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # Make axes slightly brighter
        grid.axes.set_color(WHITE)
        
        # Origin point and label
        origin_dot = Dot(point=ORIGIN, color=RED, radius=0.1)
        origin_label = MathTex("(0,0)", color=WHITE).next_to(origin_dot, UR, buff=0.1)
        
        # Fade in grid and origin elements
        self.play(
            Create(grid),
            GrowFromCenter(origin_dot),
            Write(origin_label)
        )
        self.wait(0.5)

        # Part 2: Parallel Lines and Transformation
        line1 = Line(start=np.array([-3, 1, 0]), end=np.array([3, 1, 0]), 
                    color=BLUE, stroke_opacity=0.8)
        line2 = Line(start=np.array([-3, 2, 0]), end=np.array([3, 2, 0]), 
                    color=BLUE, stroke_opacity=0.8)
        
        # Draw parallel lines
        self.play(
            Create(line1),
            Create(line2)
        )
        self.wait(0.5)

        # Define and apply transformation
        matrix = [[2, 0.5], [0.5, 1.5]]
        transform = grid.animate.apply_matrix(matrix)
        lines_transform = VGroup(line1, line2).animate.apply_matrix(matrix)
        
        self.play(
            transform,
            lines_transform,
            run_time=3
        )
        self.wait(0.5)

        # Part 3: Highlighting Properties
        # Pulse origin
        self.play(
            origin_dot.animate.scale(1.5),
            rate_func=there_and_back,
            run_time=1
        )

        # Add text labels
        origin_text = Text("Origin remains fixed", 
                         color=WHITE, font_size=36).to_edge(UR, buff=0.5)
        parallel_text = Text("Grid lines remain parallel", 
                           color=WHITE, font_size=36).next_to(origin_text, DOWN, buff=0.3)

        self.play(Write(origin_text))

        # Highlight parallel grid lines
        highlights = []
        for i in [-2, 0, 2]:
            # Horizontal lines
            h_line = Line([-4, i, 0], [4, i, 0], color=YELLOW, stroke_opacity=0.3)
            # Vertical lines
            v_line = Line([i, -4, 0], [i, 4, 0], color=YELLOW, stroke_opacity=0.3)
            h_line.apply_matrix(matrix)
            v_line.apply_matrix(matrix)
            highlights.extend([h_line, v_line])

        parallel_highlights = VGroup(*highlights)
        
        self.play(
            Create(parallel_highlights),
            Write(parallel_text),
            run_time=1
        )
        self.play(
            FadeOut(parallel_highlights),
            run_time=0.5
        )

        self.wait(1)