from manim import *

class MatrixTransformUnitVectors(Scene):
    def construct(self):
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": GREY_C,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # Create original unit vectors
        i_hat = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), color=RED, buff=0)
        j_hat = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), color=BLUE, buff=0)
        
        # Create labels for original vectors
        i_label = MathTex("\\hat{\\imath}", color=RED).next_to(i_hat.get_end(), DOWN)
        j_label = MathTex("\\hat{\\jmath}", color=BLUE).next_to(j_hat.get_end(), LEFT)
        
        # Create matrix
        matrix = MathTex(
            "\\begin{bmatrix} 2 & 1 \\\\ 1 & 1 \\end{bmatrix}"
        ).scale(0.8).to_corner(UR)
        
        # Create transformed vectors
        i_hat_transformed = Arrow(
            plane.c2p(0, 0), 
            plane.c2p(2, 1), 
            color=RED, 
            buff=0
        )
        j_hat_transformed = Arrow(
            plane.c2p(0, 0), 
            plane.c2p(1, 1), 
            color=BLUE, 
            buff=0
        )
        
        # Create labels for transformed vectors
        i_transformed_label = MathTex("(2,1)", color=RED).next_to(i_hat_transformed.get_end(), RIGHT)
        j_transformed_label = MathTex("(1,1)", color=BLUE).next_to(j_hat_transformed.get_end(), RIGHT)
        
        # Create ghost vectors (dashed versions of original vectors)
        i_hat_ghost = DashedVMobject(i_hat.copy()).set_opacity(0.3)
        j_hat_ghost = DashedVMobject(j_hat.copy()).set_opacity(0.3)
        
        # Animation sequence
        
        # 1. Fade in coordinate plane and original vectors
        self.play(
            Create(plane),
            run_time=1
        )
        self.play(
            Create(i_hat),
            Create(j_hat),
            Write(i_label),
            Write(j_label),
            run_time=2
        )
        
        # 2. Fade in matrix
        self.play(
            Write(matrix),
            run_time=1
        )
        
        # 3. Transform vectors
        self.play(
            ReplacementTransform(i_hat.copy(), i_hat_transformed),
            ReplacementTransform(j_hat.copy(), j_hat_transformed),
            FadeIn(i_hat_ghost),
            FadeIn(j_hat_ghost),
            run_time=3
        )
        
        # 4. Add final position labels
        self.play(
            Write(i_transformed_label),
            Write(j_transformed_label),
            run_time=1
        )
        
        # Final highlight
        self.play(
            Flash(i_hat_transformed.get_end(), color=RED, line_length=0.2),
            Flash(j_hat_transformed.get_end(), color=BLUE, line_length=0.2),
            run_time=1
        )
        
        # Hold final state
        self.wait(2)