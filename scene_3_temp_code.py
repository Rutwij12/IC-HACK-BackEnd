from manim import *

class ForwardPassExample(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Forward Pass Example", color=DARK_GRAY).scale(1.2)
        title.to_edge(UP, buff=0.5)
        
        # Create network components
        # Neurons
        input1 = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
        input2 = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
        hidden = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
        output = Circle(radius=0.3, color=DARK_GRAY, fill_opacity=0.1)
        
        # Position neurons
        input1.move_to(LEFT * 4 + UP * 1)
        input2.move_to(LEFT * 4 + DOWN * 1)
        hidden.move_to(LEFT * 1)
        output.move_to(RIGHT * 2)
        
        # Create connections
        conn1 = Line(input1.get_right(), hidden.get_left(), color=DARK_GRAY)
        conn2 = Line(input2.get_right(), hidden.get_left(), color=DARK_GRAY)
        conn3 = Line(hidden.get_right(), output.get_right(), color=DARK_GRAY)
        
        # Input values
        input1_val = MathTex("0.5", color=DARK_GRAY).next_to(input1, LEFT)
        input2_val = MathTex("1.0", color=DARK_GRAY).next_to(input2, LEFT)
        
        # Weights
        w1 = MathTex("w_1=0.3", color=BLUE_D).next_to(conn1, UP, buff=0.2)
        w2 = MathTex("w_2=0.2", color=BLUE_D).next_to(conn2, DOWN, buff=0.2)
        w3 = MathTex("w_3=0.5", color=BLUE_D).next_to(conn3, UP, buff=0.2)
        
        # Hidden layer calculations
        calc_hidden = VGroup(
            MathTex("(0.5 × 0.3) + (1.0 × 0.2)", color=DARK_GRAY),
            MathTex("= 0.35", color=DARK_GRAY),
            MathTex("+ b_1(0.1) = 0.45", color=BLUE_D),
            MathTex("ReLU(0.45) = 0.45", color=DARK_GRAY)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(hidden, UP, buff=1)
        
        # Output layer calculations
        calc_output = VGroup(
            MathTex("0.45 × 0.5 = 0.225", color=DARK_GRAY),
            MathTex("+ b_2(0.2) = 0.425", color=BLUE_D)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(output, UP, buff=1)
        
        final_output = MathTex("0.425", color=RED_D).next_to(output, RIGHT)
        
        # Animations
        self.play(Write(title))
        
        # Draw network
        self.play(
            Create(VGroup(input1, input2, hidden, output)),
            Create(VGroup(conn1, conn2, conn3))
        )
        
        # Show inputs and weights
        self.play(
            Write(input1_val),
            Write(input2_val)
        )
        self.play(
            Write(w1),
            Write(w2)
        )
        
        # Hidden layer calculations
        for calc in calc_hidden:
            self.play(Write(calc), run_time=0.8)
        
        # Output layer calculations
        self.play(Write(w3))
        for calc in calc_output:
            self.play(Write(calc), run_time=0.8)
        
        # Show final output
        self.play(Write(final_output))
        self.play(
            final_output.animate.scale(1.2),
            final_output.animate.set_color(RED_D)
        )
        
        self.wait(1)
        
        # Clean fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )