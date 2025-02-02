from manim import *
import numpy as np

class UnitCircleAndSine(Scene):
    def construct(self):
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_opacity": 0.4
            }
        )

        # Create axis labels with white backing
        x_labels = VGroup()
        y_labels = VGroup()
        for i in [-1, 0, 1]:
            # X-axis labels
            x_label = MathTex(str(i)).scale(0.7)
            x_label.next_to(plane.c2p(i, 0), DOWN, buff=0.2)
            x_label_bg = BackgroundRectangle(x_label, buff=0.1, color=WHITE, fill_opacity=1)
            x_labels.add(VGroup(x_label_bg, x_label))
            
            # Y-axis labels
            y_label = MathTex(str(i)).scale(0.7)
            y_label.next_to(plane.c2p(0, i), LEFT, buff=0.2)
            y_label_bg = BackgroundRectangle(y_label, buff=0.1, color=WHITE, fill_opacity=1)
            y_labels.add(VGroup(y_label_bg, y_label))

        # Create unit circle
        circle = Circle(radius=2, color=BLACK, stroke_width=2)
        circle.scale(0.5)  # Scale to unit circle size

        # Create moving point
        dot = Dot(plane.c2p(1, 0), color=RED, radius=0.08)
        
        # Create vertical line (initially at x=1)
        vertical_line = DashedLine(
            plane.c2p(1, 0),
            plane.c2p(1, 0),
            color=BLUE,
            stroke_width=1.5,
            dash_length=0.1
        )

        # Create coordinate display
        coord_text = MathTex(r"(\cos \theta, \sin \theta) = (1.00, 0.00)").scale(0.8)
        coord_text.move_to(plane.c2p(1.2, 1.2))
        coord_bg = BackgroundRectangle(coord_text, buff=0.1, color=WHITE, fill_opacity=1)
        coord_group = VGroup(coord_bg, coord_text)

        # Create theta label
        theta_label = MathTex(r"\theta = 0.0").scale(0.7)
        theta_label.move_to(plane.c2p(0.4, 0.2))
        theta_bg = BackgroundRectangle(theta_label, buff=0.1, color=WHITE, fill_opacity=1)
        theta_group = VGroup(theta_bg, theta_label)

        # Initial animations (0-3 seconds)
        self.play(
            FadeIn(plane),
            FadeIn(circle),
            *[FadeIn(label) for label in x_labels],
            *[FadeIn(label) for label in y_labels],
            run_time=3
        )

        # Add point and labels (3-6 seconds)
        self.play(
            FadeIn(dot),
            FadeIn(coord_group),
            FadeIn(theta_group),
            run_time=3
        )

        # Animation function for continuous updates
        def update_point(mob, dt):
            nonlocal t
            t += dt * PI/2  # π/2 radians per second
            x = np.cos(t)
            y = np.sin(t)
            mob.move_to(plane.c2p(x, y))
            
            #Update vertical line
            vertical_line.put_start_and_end_on(
                plane.c2p(x, 0),
                plane.c2p(x, y)
            )
            
            # Update coordinate text
            new_coord_text = MathTex(
                f"(\\cos \\theta, \\sin \\theta) = ({x:.2f}, {y:.2f})"
            ).scale(0.8)
            new_coord_text.move_to(coord_text.get_center())
            coord_text.become(new_coord_text)
            
            # Update theta label
            new_theta = MathTex(f"\\theta = {t:.1f}").scale(0.7)
            new_theta.move_to(theta_label.get_center())
            theta_label.become(new_theta)

        # Initialize time variable
        t = 0
        
        # Add vertical line
        self.add(vertical_line)
        
        # Start continuous animation (6-15 seconds)
        dot.add_updater(update_point)
        self.wait(9)  # Run for 9 more seconds to complete 15 seconds total
        
        # Clean up updater
        dot.remove_updater(update_point)