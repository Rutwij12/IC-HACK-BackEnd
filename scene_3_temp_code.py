from manim import *
import numpy as np

class AmplitudeAndPeriod(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-2.5, 2.5, 1],
            axis_config={"color": GREY},
            x_length=10,
            y_length=6
        )
        
        # Add custom x-axis labels
        x_labels = axes.get_x_axis().add_labels({
            -2*PI: MathTex(r"-2\pi"),
            -PI: MathTex(r"-\pi"),
            0: MathTex("0"),
            PI: MathTex(r"\pi"),
            2*PI: MathTex(r"2\pi")
        })
            
        # Add light grid
        grid = axes.get_grid(color=GREY_C, opacity=0.3)
        self.play(Create(axes), Create(grid))
        
        # Part 1: Amplitude Demonstration
        # Base sine wave
        base_sine = axes.plot(lambda x: np.sin(x), color=BLUE)
        base_label = MathTex(r"y = \sin(x)", color=BLUE).to_edge(UP).shift(DOWN*0.5)
        
        # Amplitude lines for base sine
        amp_lines_base = VGroup(
            DashedLine(axes.c2p(-2*PI, 1), axes.c2p(2*PI, 1), color=BLUE, opacity=0.5),
            DashedLine(axes.c2p(-2*PI, -1), axes.c2p(2*PI, -1), color=BLUE, opacity=0.5)
        )
        
        self.play(
            Create(base_sine),
            Write(base_label),
            Create(amp_lines_base)
        )
        self.wait()
        
        # Amplitude transformation
        amp_sine = axes.plot(lambda x: 1.5*np.sin(x), color=RED)
        amp_label = MathTex(r"y = 1.5\sin(x)", color=RED).to_edge(UP).shift(DOWN*0.5)
        
        amp_lines_new = VGroup(
            DashedLine(axes.c2p(-2*PI, 1.5), axes.c2p(2*PI, 1.5), color=RED, opacity=0.5),
            DashedLine(axes.c2p(-2*PI, -1.5), axes.c2p(2*PI, -1.5), color=RED, opacity=0.5)
        )
        
        amp_text = MathTex(r"\text{Amplitude: } 1 \rightarrow 1.5", font_size=36).move_to(axes.c2p(-PI, 2))
        
        self.play(
            Transform(base_sine, amp_sine),
            Transform(base_label, amp_label),
            Transform(amp_lines_base, amp_lines_new),
            Write(amp_text)
        )
        self.wait()
        
        # Clear for Part 2
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )
        
        # Part 2: Period Demonstration
        base_sine = axes.plot(lambda x: np.sin(x), color=BLUE)
        base_label = MathTex(r"y = \sin(x)", color=BLUE).to_edge(UP).shift(DOWN*0.5)
        
        # Vertical period lines for base sine
        period_lines_base = VGroup(*[
            DashedLine(
                axes.c2p(x, -2.5), axes.c2p(x, 2.5),
                color=BLUE, opacity=0.5
            ) for x in [-2*PI, -PI, 0, PI, 2*PI]
        ])
        
        period_text = MathTex(r"\text{Period} = 2\pi", font_size=36).move_to(axes.c2p(PI/2, -2))
        
        self.play(
            Create(base_sine),
            Write(base_label),
            Create(period_lines_base),
            Write(period_text)
        )
        self.wait()
        
        # Period transformation
        period_sine = axes.plot(lambda x: np.sin(2*x), color=GREEN)
        period_label = MathTex(r"y = \sin(2x)", color=GREEN).to_edge(UP).shift(DOWN*0.5)
        
        # New vertical period lines
        x_values = [-2*PI, -3*PI/2, -PI, -PI/2, 0, PI/2, PI, 3*PI/2, 2*PI]
        period_lines_new = VGroup(*[
            DashedLine(
                axes.c2p(x, -2.5), axes.c2p(x, 2.5),
                color=GREEN, opacity=0.5
            ) for x in x_values
        ])
        
        new_period_text = MathTex(r"\text{Period} = \pi", font_size=36).move_to(axes.c2p(PI/2, -2))
        
        self.play(
            Transform(base_sine, period_sine),
            Transform(base_label, period_label),
            Transform(period_lines_base, period_lines_new),
            Transform(period_text, new_period_text)
        )
        self.wait()