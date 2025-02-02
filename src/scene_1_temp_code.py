from manim import *

class AreaUnderCurve(Scene):
    def construct(self):
        # Configure the coordinate system
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 6, 1],
            axis_config={"color": WHITE},
            x_length=10,
            y_length=7
        )
        
        # Shift the entire system to center it properly
        axes.shift(LEFT * 1.5)
        
        # Create axis labels
        x_label = Text("x", font_size=24).move_to([2.8, 0.3, 0])
        y_label = Text("y", font_size=24).move_to([0.3, 5.5, 0])
        
        # Create the function
        curve = axes.plot(lambda x: x**2, color="#3498db")
        function_label = MathTex("f(x) = x^2", font_size=36).move_to([-0.8, 5.2, 0])
        
        # Create the area under the curve
        area = axes.get_area(curve, x_range=[0, 2], color="#3498db", opacity=0.3)
        
        # Create dashed vertical lines
        dash_line_1 = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(0, 4),
            color="#666666"
        )
        dash_line_2 = DashedLine(
            axes.c2p(2, 0),
            axes.c2p(2, 4),
            color="#666666"
        )
        
        area_label = Text("Area under the curve", font_size=36).move_to([1, 5.5, 0])
        
        # Create rectangles
        rectangles = VGroup()
        widths = [0.5, 0.5, 0.5, 0.5]
        x_starts = [0.0, 0.5, 1.0, 1.5]
        heights = [0.25, 1.0, 2.25, 4.0]
        
        for i in range(4):
            rect = Rectangle(
                width=axes.c2p(widths[i], 0)[0] - axes.c2p(0, 0)[0],
                height=axes.c2p(0, heights[i])[1] - axes.c2p(0, 0)[1],
                color="#000000",
                fill_color="#2ecc71",
                fill_opacity=0.6,
                stroke_opacity=0.3
            )
            rect.move_to(
                axes.c2p(x_starts[i] + widths[i]/2, heights[i]/2),
                aligned_edge=ORIGIN
            )
            rectangles.add(rect)
            
        approx_label = Text("Approximating with rectangles", font_size=32).move_to([1, -0.8, 0])
        
        # Animation sequence
        self.camera.frame.move_to([1, 2.5, 0])
        self.camera.frame.set_height(8)
        
        # 1. Fade in coordinate system (0-3s)
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )
        
        # 2. Draw curve and function label (3-6s)
        self.play(
            Create(curve),
            Write(function_label),
            run_time=3
        )
        
        # 3. Show area and vertical lines (6-9s)
        self.play(
            FadeIn(area),
            Create(dash_line_1),
            Create(dash_line_2),
            Write(area_label),
            run_time=3
        )
        
        # 4. Show rectangles (9-15s)
        self.play(
            Write(approx_label),
            run_time=1
        )
        for rect in rectangles:
            self.play(
                Create(rect),
                run_time=1
            )
            
        # Hold final frame
        self.wait()