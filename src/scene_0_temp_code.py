from manim import *

class BasicVectorTransformation(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={
                "stroke_width": 2,
                "color": BLACK,
                "include_tip": True,
            },
        )
        
        # Create grid
        grid = NumberPlane(
            x_range=[-3, 3],
            y_range=[-3, 3],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )

        # Initialize vectors
        vector_v = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(2, 2),
            buff=0,
            color=BLUE
        )
        
        vector_av = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(4, 4),
            buff=0,
            color=RED
        )

        # Create labels
        v_label = MathTex(r"\vec{v} = [2,2]").next_to(
            axes.c2p(2, 2),
            direction=UR,
            buff=0.2
        )
        
        av_label = MathTex(r"A\vec{v} = [4,4]").next_to(
            axes.c2p(4, 4),
            direction=UR,
            buff=0.2
        )

        # Create matrix and eigenvalue text
        matrix = MathTex(
            r"A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}"
        ).to_corner(UL, buff=1)
        
        eigenvalue = MathTex(r"\lambda = 2").next_to(
            matrix,
            DOWN,
            buff=0.3
        )

        # Animation sequence
        # 1. Fade in grid and axes
        self.play(
            FadeIn(grid),
            FadeIn(axes),
            run_time=2
        )

        # 2. Draw original vector and its label
        self.play(
            GrowArrow(vector_v),
            Write(v_label),
            run_time=2
        )

        # 3. Show matrix and eigenvalue
        self.play(
            Write(matrix),
            Write(eigenvalue),
            run_time=2
        )

        # 4. Transform vector
        faded_v = vector_v.copy().set_opacity(0.3)
        self.play(
            ReplacementTransform(vector_v, faded_v),
            GrowArrow(vector_av),
            Write(av_label),
            run_time=3
        )

        # Final pause
        self.wait(1)