from manim import *

class RotationTransformation(Scene):
    def construct(self):
        # 1. Initial Setup
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": "#D3D3D3",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        
        # Axes labels
        x_label = Text("x").move_to([3.5, 0.3, 0])
        y_label = Text("y").move_to([0.3, 3.5, 0])
        
        # Numbers at 1 and -1
        numbers = VGroup(
            MathTex("1").move_to([1, 0.3, 0]),
            MathTex("-1").move_to([-1, 0.3, 0]),
            MathTex("1").move_to([0.3, 1, 0]),
            MathTex("-1").move_to([0.3, -1, 0])
        )

        # Fade in grid and labels
        self.play(
            Create(grid),
            Write(x_label),
            Write(y_label),
            Write(numbers),
            run_time=2
        )

        # 2. Shape Introduction
        original_square = Polygon(
            [1, 1, 0], [1, -1, 0], [-1, -1, 0], [-1, 1, 0],
            color="#89CFF0",
            fill_opacity=0.5
        )
        
        vertices = VGroup(*[
            Dot(point, color=WHITE, radius=0.05)
            for point in original_square.get_vertices()
        ])

        self.play(
            Create(original_square),
            Create(vertices),
            run_time=1.5
        )

        # 3. Matrix Display
        rotation_matrix = MathTex(
            "R_{90°} = \\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}",
            color=WHITE
        ).scale(0.8).to_corner(UR, buff=0.5)

        self.play(
            Write(rotation_matrix),
            run_time=1.5
        )

        # 4. Transformation Animation
        transformed_square = original_square.copy()
        transformed_vertices = vertices.copy()
        
        # Create dashed version of original square
        dashed_square = original_square.copy()
        dashed_square.set_style(
            stroke_color="#89CFF0",
            stroke_width=2,
            stroke_dasharray=[0.2, 0.2]
        )

        # Create curved arrows for vertex paths
        arrows = VGroup()
        for i in range(4):
            start = original_square.get_vertices()[i]
            end = np.array([-start[1], start[0], 0])  # 90-degree rotation
            arc = ArcBetweenPoints(
                start, end,
                angle=PI/2,
                color=WHITE
            )
            arrows.add(arc)

        # Perform rotation
        self.play(
            Transform(original_square, dashed_square),
            run_time=0.5
        )
        
        self.play(
            Create(arrows),
            Rotate(transformed_square, angle=PI/2, about_point=ORIGIN),
            Rotate(transformed_vertices, angle=PI/2, about_point=ORIGIN),
            run_time=3
        )
        
        # Change color of transformed square
        transformed_square.set_style(
            stroke_color="#0066CC",
            fill_color="#0066CC",
            fill_opacity=0.5
        )

        # 5. Final State
        self.wait(1)