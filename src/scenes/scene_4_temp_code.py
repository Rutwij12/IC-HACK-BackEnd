from manim import *

class EigenvalueStretchingVisualization(Scene):
    def construct(self):
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0.6
            }
        )
        
        # Create axes labels
        x_label = plane.get_x_axis_label("x")
        y_label = plane.get_y_axis_label("y")
        
        # Create the matrix label
        matrix = MathTex(
            "A = \\begin{bmatrix} 2 & 0 \\\\ 0 & 3 \\end{bmatrix}"
        ).scale(0.8).to_corner(UR, buff=0.5)
        
        # Create initial vectors
        v1 = Vector([1, 0], color=BLUE_B)
        v2 = Vector([0, 1], color=RED_B)
        
        # Create vector labels
        v1_label = MathTex("\\vec{v}_1").next_to(v1.get_end(), DOWN).set_color(BLUE_B)
        v2_label = MathTex("\\vec{v}_2").next_to(v2.get_end(), RIGHT).set_color(RED_B)
        
        # Create dots at vector endpoints
        dot1 = Dot(v1.get_end(), color=BLUE_B)
        dot2 = Dot(v2.get_end(), color=RED_B)
        
        # Add everything to scene
        self.play(
            Create(plane),
            Write(x_label),
            Write(y_label)
        )
        self.play(Write(matrix))
        self.play(
            Create(v1),
            Create(v2)
        )
        self.play(
            Create(dot1),
            Create(dot2),
            Write(v1_label),
            Write(v2_label)
        )
        
        # Create stretched vectors
        v1_stretched = Vector([2, 0], color=BLUE)
        v2_stretched = Vector([0, 3], color=RED)
        
        # Create dashed lines for original vectors
        dashed_v1 = DashedLine(
            start=ORIGIN,
            end=v1.get_end(),
            color=BLUE_B,
            stroke_opacity=0.5
        )
        dashed_v2 = DashedLine(
            start=ORIGIN,
            end=v2.get_end(),
            color=RED_B,
            stroke_opacity=0.5
        )
        
        # Create eigenvalue labels
        lambda1_label = MathTex("\\lambda_1 = 2").set_color(BLUE)
        lambda2_label = MathTex("\\lambda_2 = 3").set_color(RED)
        
        # Position eigenvalue labels
        lambda1_label.next_to(v1_stretched.get_end(), DOWN)
        lambda2_label.next_to(v2_stretched.get_end(), RIGHT)
        
        # Animate the stretching
        self.play(
            Transform(v1, v1_stretched),
            Transform(v2, v2_stretched),
            Create(dashed_v1),
            Create(dashed_v2),
            Transform(dot1, Dot(v1_stretched.get_end(), color=BLUE)),
            Transform(dot2, Dot(v2_stretched.get_end(), color=RED)),
            Transform(v1_label, MathTex("\\vec{v}_1").next_to(v1_stretched.get_end(), DOWN).set_color(BLUE)),
            Transform(v2_label, MathTex("\\vec{v}_2").next_to(v2_stretched.get_end(), RIGHT).set_color(RED))
        )
        
        # Add eigenvalue labels
        self.play(
            Write(lambda1_label),
            Write(lambda2_label)
        )
        
        # Hold the final scene
        self.wait(2)