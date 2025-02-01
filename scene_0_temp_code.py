from manim import *

class MatrixBasics(Scene):
    def construct(self):
        # 1. Initial Setup
        title = Text("2×2 Matrix", font_size=40).to_edge(UP)
        matrix = Matrix([
            [2, 1],
            [-1, 3]
        ], h_buff=1.5).scale(1.0)
        
        # First animation sequence (0-3 seconds)
        self.play(FadeIn(title))
        self.play(Write(matrix))
        self.wait(0.5)
        
        # 2. Row highlighting sequence (3-7 seconds)
        first_row_text = Text("First Row", font_size=30, color=LIGHT_GRAY).shift(LEFT*3 + UP*1.5)
        second_row_text = Text("Second Row", font_size=30, color=LIGHT_GRAY).shift(LEFT*3 + UP*0.5)
        
        first_row = matrix.get_rows()[0]
        second_row = matrix.get_rows()[1]
        
        self.play(
            Write(first_row_text),
            first_row.animate.set_color(BLUE)
        )
        self.wait(0.5)
        self.play(
            Write(second_row_text),
            second_row.animate.set_color(GREEN)
        )
        
        # 3. Coordinate plane and points sequence (7-11 seconds)
        # Move matrix up and scale down
        self.play(
            matrix.animate.shift(UP).scale(0.8),
            FadeOut(first_row_text),
            FadeOut(second_row_text)
        )
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.3
            },
            axis_config={
                "numbers_to_include": np.arange(-3, 4, 1),
                "font_size": 24
            }
        ).shift(DOWN)
        
        self.play(Create(plane))
        
        # Create points and dashed lines
        point1 = Dot(plane.coords_to_point(2, 1), color=BLUE, radius=0.1)
        point2 = Dot(plane.coords_to_point(-1, 3), color=GREEN, radius=0.1)
        
        # Create dashed lines with correct opacity setting
        dashed_line1 = DashedLine(
            plane.get_origin(), point1.get_center(),
            dash_length=0.1
        ).set_opacity(0.6)
        
        dashed_line2 = DashedLine(
            plane.get_origin(), point2.get_center(),
            dash_length=0.1
        ).set_opacity(0.6)
        
        # Create coordinate notations
        coord_text1 = Text("[2, 1] → (2,1)", font_size=30, color=BLUE).shift(LEFT*2)
        coord_text2 = Text("[-1, 3] → (-1,3)", font_size=30, color=GREEN).shift(LEFT*2 + DOWN*0.5)
        
        self.play(
            Create(dashed_line1),
            Create(dashed_line2),
            FadeIn(point1),
            FadeIn(point2),
            Write(coord_text1),
            Write(coord_text2)
        )
        
        # 4. Final text and fadeout (11-15 seconds)
        final_text = Text(
            "Matrix rows represent points in space",
            font_size=36,
            color=LIGHT_GRAY
        ).to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(1)
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)