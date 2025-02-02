from manim import *

class ApplicationsPreview(Scene):
    def construct(self):
        # Initial Title
        title = Text("Real-World Applications of Integration", font_size=36)
        title.move_to(UP * 3)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Part 1: Distance from Velocity
        axes1 = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 7, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).add_coordinates()
        
        labels1 = axes1.get_axis_labels(x_label="t (seconds)", y_label="v (m/s)")
        
        def velocity(t):
            return 2*t + 1
        
        velocity_graph = axes1.plot(velocity, x_range=[0, 3], color=BLUE)
        area = axes1.get_area(velocity_graph, x_range=[0, 3], color=[BLUE], opacity=0.3)
        
        integral_eq = MathTex("D = \\int_0^3(2t + 1)dt").move_to(UP * 2.5)
        result = MathTex("D = [t^2 + t]_0^3 = 13.5\\text{ meters}").move_to(DOWN * 2.5)
        distance_text = Text("Distance = Area under velocity curve", font_size=28).move_to(DOWN * 2)

        self.play(Create(axes1), Create(labels1))
        self.play(Create(velocity_graph), Write(integral_eq))
        self.play(FadeIn(area))
        self.play(Write(distance_text), Write(result))
        self.wait(1)
        self.play(FadeOut(VGroup(axes1, labels1, velocity_graph, area, integral_eq, distance_text, result)))

        # Part 2: Volume of Revolution
        axes2 = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).add_coordinates()
        
        labels2 = axes2.get_axis_labels(x_label="x", y_label="y")
        
        def sqrt_func(x):
            return np.sqrt(x)
        
        sqrt_graph = axes2.plot(sqrt_func, x_range=[0, 4], color=BLUE)
        volume_eq = MathTex("V = \\pi\\int_0^4[\\sqrt{x}]^2dx").move_to(UP * 2.5)
        volume_result = MathTex("V = 32\\pi\\text{ cubic units}").move_to(DOWN * 2)

        self.play(Create(axes2), Create(labels2))
        self.play(Create(sqrt_graph), Write(volume_eq))
        
        # Create a rotating surface (simplified representation)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                sqrt_func(u) * np.cos(v),
                sqrt_func(u) * np.sin(v)
            ]),
            u_range=[0, 4],
            v_range=[0, PI/2],
            checkerboard_colors=[BLUE_D, BLUE_E]
        ).set_opacity(0.3)
        
        surface.scale(0.5).shift(RIGHT * 2)
        
        self.play(Create(surface))
        self.play(Write(volume_result))
        self.wait(1)
        self.play(FadeOut(VGroup(axes2, labels2, sqrt_graph, volume_eq, volume_result, surface)))

        # Part 3: Average Value
        axes3 = Axes(
            x_range=[0, 2, 1],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).add_coordinates()
        
        labels3 = axes3.get_axis_labels(x_label="x", y_label="y")
        
        def squared(x):
            return x**2
        
        squared_graph = axes3.plot(squared, x_range=[0, 2], color=BLUE)
        area3 = axes3.get_area(squared_graph, x_range=[0, 2], color=[GREEN], opacity=0.3)
        
        avg_eq = MathTex("\\text{Average} = \\frac{1}{2-0}\\int_0^2 x^2dx").move_to(UP * 2.5)
        avg_line = axes3.get_horizontal_line(axes3.c2p(0, 8/3), color=YELLOW)
        avg_result = MathTex("\\frac{1}{2}\\int_0^2 x^2dx = \\frac{1}{2}[\\frac{x^3}{3}]_0^2 = \\frac{8}{3}").move_to(DOWN * 2)

        self.play(Create(axes3), Create(labels3))
        self.play(Create(squared_graph), Write(avg_eq))
        self.play(FadeIn(area3))
        self.play(Create(avg_line))
        self.play(Write(avg_result))
        self.wait(1)
        self.play(FadeOut(VGroup(axes3, labels3, squared_graph, area3, avg_eq, avg_line, avg_result)))