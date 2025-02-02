from manim import *

class IntegrationScene(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 3, 0.5],
            x_length=6,
            y_length=6,
            axis_config={"color": GREY},
            x_axis_config={"numbers_to_include": [1, 2]},
            y_axis_config={"numbers_to_include": [1, 2]},
        ).add_coordinates()
        
        # Add grid
        grid = axes.get_grid(color=GREY_D, opacity=0.15)
        
        # Create title
        title = MathTex(r"\text{Integrating } x \, dx").scale(1.2)
        title.to_edge(UP, buff=0.5)
        
        # Create function
        func = axes.plot(lambda x: x, x_range=[0, 2], color=BLUE)
        func_label = MathTex("f(x) = x").next_to(func.get_end(), RIGHT)
        
        # Initial animation
        self.play(
            FadeIn(axes, grid),
            Write(title),
            run_time=1
        )
        self.play(Create(func), Write(func_label), run_time=2)
        
        # Create vertical strip
        x_val = 1
        dx = 0.2
        strip = axes.get_riemann_rectangles(
            func,
            x_range=[x_val, x_val + dx],
            dx=dx,
            color=YELLOW,
            fill_opacity=0.2
        )
        
        # Labels for strip
        x_label = MathTex("x").scale(0.7).next_to(strip, RIGHT, buff=0.1)
        dx_label = MathTex("dx").scale(0.7).next_to(axes.c2p(x_val + dx/2, 0), DOWN, buff=0.1)
        strip_explanation = MathTex(r"\text{Area of strip} = x \cdot dx").next_to(axes, DOWN, buff=0.5)
        
        # Show strip and labels
        self.play(
            FadeIn(strip, x_label, dx_label),
            Write(strip_explanation),
            run_time=2
        )
        
        # Animate area filling
        area = axes.get_riemann_rectangles(
            func,
            x_range=[0, 2],
            dx=0.05,
            color=BLUE,
            fill_opacity=0.3
        )
        
        running_calc = MathTex(r"\int x \, dx = \frac{x^2}{2}").next_to(axes, DOWN, buff=0.5)
        final_area = MathTex(r"\text{When } x=2: \text{ Area} = 2").next_to(axes, RIGHT, buff=0.5)
        
        # Clear previous explanations and show area
        self.play(
            FadeOut(strip, x_label, dx_label, strip_explanation),
            FadeIn(area),
            Transform(strip_explanation, running_calc),
            Write(final_area),
            run_time=4
        )
        
        # Final formula
        final_formula = MathTex(r"\int x \, dx = \frac{x^2}{2} + C").scale(1.2)
        final_formula.next_to(axes, DOWN, buff=0.5)
        
        self.play(
            FadeOut(running_calc, final_area),
            Transform(strip_explanation, final_formula),
            run_time=2
        )
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )