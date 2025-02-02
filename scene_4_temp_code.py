from manim import *
import numpy as np

class PendulumAndSineWave(Scene):
    def construct(self):
        # Constants
        PENDULUM_LENGTH = 2
        MAX_ANGLE = 30 * DEGREES
        PERIOD = 2
        OMEGA = PI / PERIOD
        RUNTIME = 12
        NUM_CYCLES = 5

        # Create pendulum elements
        pivot = Dot(point=np.array([-3, 2, 0]), radius=0.05)
        
        def get_pendulum_position(t):
            angle = MAX_ANGLE * np.cos(OMEGA * t)
            x = -3 + PENDULUM_LENGTH * np.sin(angle)
            y = 2 - PENDULUM_LENGTH * np.cos(angle)
            return np.array([x, y, 0])

        bob = Dot(radius=0.1)
        bob.move_to(get_pendulum_position(0))
        
        def get_arm():
            return Line(pivot.get_center(), bob.get_center(), color=WHITE)
        
        pendulum_arm = always_redraw(get_arm)

        # Create axes for sine wave
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE},
        ).shift(RIGHT * 3)

        # Initialize sine wave as empty
        sine_wave = VMobject(color=RED)
        sine_wave.set_points_as_corners([axes.c2p(0, 0)])

        # Fade in initial elements
        self.play(
            FadeIn(pivot),
            FadeIn(pendulum_arm),
            FadeIn(bob),
            Create(axes),
            run_time=2
        )

        # Animation function for updating sine wave
        def update_sine_wave(mob, dt):
            current_t = self.renderer.time
            if current_t <= RUNTIME:
                # Get current pendulum position
                current_pos = bob.get_center()
                # Convert to graph coordinates
                new_point = axes.c2p(current_t, current_pos[1] - 2)
                # Add point to sine wave
                points = mob.points
                points = np.append(points, [new_point], axis=0)
                mob.set_points_as_corners(points)

        # Add updater to sine wave
        sine_wave.add_updater(update_sine_wave)
        self.add(sine_wave)

        # Main animation
        self.play(
            UpdateFromFunc(
                bob,
                lambda m: m.move_to(get_pendulum_position(self.renderer.time))
            ),
            rate_func=linear,
            run_time=RUNTIME-2
        )

        # Remove updater
        sine_wave.clear_updaters()