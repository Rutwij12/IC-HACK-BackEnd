from manim import *

class CombinedScene(Scene):
    def construct(self):

        # Scene 1
        
        # 1. Coordinate System Introduction
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_ticks": True,
                "include_tip": True,
            },
        )
        
        # Add labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        
        # Create grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )

        # Animate coordinate system
        self.play(
            FadeIn(grid),
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=3
        )

        # 2. Vector Introduction
        # Create main vector
        vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(3, 2),
            buff=0,
            color="#FF4444",
            stroke_width=3,
        )

        # Animate vector creation
        self.play(
            GrowArrow(vector),
            run_time=2
        )
        self.wait()

        # 3. Component Breakdown
        # Create dashed lines for components
        x_component = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(3, 0),
            color="#3498DB",
            dash_length=0.2
        )
        
        y_component = DashedLine(
            axes.c2p(3, 0),
            axes.c2p(3, 2),
            color="#2ECC71",
            dash_length=0.2
        )

        # Create right angle symbol
        right_angle = RightAngle(
            x_component,
            y_component,
            length=0.2,
            color=WHITE
        )

        # Create component labels
        x_component_label = MathTex("3").scale(0.8)
        x_component_label.next_to(x_component, DOWN, buff=0.2)
        
        y_component_label = MathTex("2").scale(0.8)
        y_component_label.next_to(y_component, RIGHT, buff=0.2)

        # Create vector notation
        vector_notation = MathTex(r"\vec{v} = (3,2)")
        vector_notation.scale(0.8)
        vector_notation.move_to(axes.c2p(3, 3))

        # Animate components and labels
        self.play(
            Create(x_component),
            Create(y_component),
            run_time=2
        )
        
        self.play(
            Create(right_angle),
            Write(x_component_label),
            Write(y_component_label),
            run_time=2
        )

        self.play(
            Write(vector_notation),
            run_time=1
        )

        # Final pause
        self.wait(2)

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene

        # Scene 2
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "include_ticks": True,
                "tick_size": 0.1,
            },
        )
        
        # Add labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        coords = VGroup(axes, x_label, y_label)

        # Fade in coordinate system
        self.play(Create(coords), run_time=2)
        
        # Create i-hat vector
        i_hat = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 0),
            color=RED,
            buff=0
        )
        i_hat_label = MathTex(r"\hat{\imath}").next_to(i_hat.get_tip(), UP, buff=0.2).set_color(RED)
        
        # Draw i-hat vector and label
        self.play(Create(i_hat), Write(i_hat_label))
        self.play(Flash(i_hat.get_tip(), color=RED, flash_radius=0.3))
        
        # Create j-hat vector
        j_hat = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(0, 1),
            color=BLUE,
            buff=0
        )
        j_hat_label = MathTex(r"\hat{\jmath}").next_to(j_hat.get_tip(), RIGHT, buff=0.2).set_color(BLUE)
        
        # Draw j-hat vector and label
        self.play(Create(j_hat), Write(j_hat_label))
        self.play(Flash(j_hat.get_tip(), color=BLUE, flash_radius=0.3))
        
        # Create matrix
        matrix = MathTex(
            r"\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}"
        ).scale(0.8).move_to([4, 2, 0])
        matrix_text = Text("Unit vectors as matrix columns", font_size=24).next_to(matrix, DOWN)
        
        # Create dashed lines connecting matrix to vectors
        dash_to_i = DashedLine(
            matrix.get_left() + LEFT * 0.3,
            i_hat.get_tip(),
            color=RED,
            opacity=0.5
        )
        dash_to_j = DashedLine(
            matrix.get_right() + RIGHT * 0.3,
            j_hat.get_tip(),
            color=BLUE,
            opacity=0.5
        )
        
        # Show matrix, text, and dashed lines
        self.play(
            Write(matrix),
            Write(matrix_text),
            Create(dash_to_i),
            Create(dash_to_j)
        )
        
        # Add bottom text
        bottom_text = Text("Basis of 2D space", font_size=28).move_to([0, -2.5, 0])
        
        # Final highlight and text
        self.play(
            Write(bottom_text),
            Flash(i_hat.get_tip(), color=RED, flash_radius=0.3),
            Flash(j_hat.get_tip(), color=BLUE, flash_radius=0.3)
        )
        
        # Pause at the end
        self.wait()

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene

        # Scene 3
        
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

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene

        # Scene 4
        
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

        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene

        # Scene 5
        
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
