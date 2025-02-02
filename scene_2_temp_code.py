from manim import *
import numpy as np

class SineWaveGeneration(Scene):
    def construct(self):
        # Create unit circle and axes for circle
        circle = Circle(radius=1, color=GRAY, stroke_width=1).move_to(LEFT * 3)
        circle_axes = VGroup(
            Line(LEFT * 4, LEFT * 2, color=WHITE),
            Line(LEFT * 3 + DOWN, LEFT * 3 + UP, color=WHITE)
        )

        # Create axes for sine wave
        x_axis = Line(LEFT * 2, RIGHT * 3, color=WHITE)
        y_axis = Line(DOWN, UP, color=WHITE).move_to(LEFT * 2)
        axes = VGroup(x_axis, y_axis)

        # Create initial rotating point and lines
        rotating_point = Dot(circle.point_at_angle(0), color=RED, radius=0.1)
        rotating_point.move_to(circle.point_at_angle(0) + LEFT * 3)
        
        # Create radius line (from circle center to point)
        radius_line = Line(
            circle.get_center(),
            rotating_point.get_center(),
            color=WHITE
        )

        # Create vertical dashed line
        vertical_line = DashedLine(
            rotating_point.get_center(),
            [rotating_point.get_center()[0], -1, 0],
            color=BLUE
        )

        # Create initial angle arc
        angle_arc = Arc(
            radius=0.3,
            angle=0,
            color=GRAY_C,
            arc_center=circle.get_center()
        )

        # Fade in all initial elements
        self.play(
            FadeIn(circle),
            FadeIn(circle_axes),
            FadeIn(axes),
            FadeIn(rotating_point),
            FadeIn(radius_line),
            FadeIn(vertical_line),
            FadeIn(angle_arc),
            run_time=2
        )

        # Create sine curve
        sine_curve = VMobject(color=BLUE)
        sine_curve.set_points_as_corners([[(-2, 0, 0)])  # Start at origin of sine wave

        # Create horizontal connecting line
        connecting_line = Line(
            rotating_point.get_center(),
            [-2, rotating_point.get_center()[1], 0],
            color=BLUE,
            stroke_width=1
        )
        self.add(connecting_line)

        # Animation of rotation and sine wave drawing
        t_tracker = ValueTracker(0)
        
        def update_point(mob):
            t = t_tracker.get_value()
            new_point = circle.point_at_angle(t) + LEFT * 3
            mob.move_to(new_point)

        def update_radius(mob):
            mob.put_start_and_end_on(
                circle.get_center(),
                rotating_point.get_center()
            )

        def update_vertical_line(mob):
            mob.put_start_and_end_on(
                rotating_point.get_center(),
                [rotating_point.get_center()[0], circle.get_center()[1], 0]
            )

        def update_angle_arc(mob):
            t = t_tracker.get_value()
            mob.become(
                Arc(
                    radius=0.3,
                    angle=t,
                    color=GRAY_C,
                    arc_center=circle.get_center()
                )
            )

        def update_sine_curve(mob):
            t = t_tracker.get_value()
            points = [[-2, 0, 0]]  # Starting point
            for ti in np.linspace(0, t, 100):
                points.append([-2 + ti, np.sin(ti), 0])
            mob.set_points_as_corners(points)

        def update_connecting_line(mob):
            mob.put_start_and_end_on(
                rotating_point.get_center(),
                [-2 + t_tracker.get_value(), rotating_point.get_center()[1], 0]
            )

        # Add updaters
        rotating_point.add_updater(update_point)
        radius_line.add_updater(update_radius)
        vertical_line.add_updater(update_vertical_line)
        angle_arc.add_updater(update_angle_arc)
        sine_curve.add_updater(update_sine_curve)
        connecting_line.add_updater(update_connecting_line)

        # Play the main animation
        self.add(sine_curve)
        self.play(
            t_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=linear
        )

        # Hold for 2 seconds
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=3
        )