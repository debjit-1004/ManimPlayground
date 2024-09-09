from manim import *

class BasicScene(Scene):
    def construct(self):
        # Create a circle and a square
        circle = Circle()          # Create a circle
        square = Square()          # Create a square

        # Set colors
        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(RED, opacity=0.5)

        # Position the square to the right of the circle
        square.next_to(circle, RIGHT)

        # Add the shapes to the scene
        self.play(Create(circle))  # Animate circle creation
        self.play(Create(square))  # Animate square creation

        # Animate circle and square transformation
        self.play(
            Transform(circle, square),
            Transform(square, circle)
        )

        # Fade out both shapes
        self.play(FadeOut(circle), FadeOut(square))



class BouncingBall(Scene):
    def construct(self):
        # Create a ball
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.move_to(UP * 2)  # Start the ball higher
        
        # Create a floor
        floor = Line(start=LEFT*4, end=RIGHT*4, stroke_width=5).move_to(DOWN * 2.5)

        # Add ball and floor to the scene
        self.add(ball, floor)

        # Simulate bouncing effect
        for i in range(4):
            bounce_height = 2 / (i + 1)  # Decrease height with each bounce
            self.play(ball.animate.move_to(DOWN * 2.3), run_time=0.5)  # Move ball to floor
            self.play(ball.animate.move_to(UP * bounce_height), run_time=0.5)  # Move ball up
            
        # Final settle down
        self.play(ball.animate.move_to(DOWN * 2.3), run_time=0.5)


class BouncingBallWithRetreat(Scene):
    def construct(self):
        # Create a ball
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.move_to(UP * 2 + LEFT * 4)  # Start the ball high and to the left
        
        # Create a floor
        floor = Line(start=LEFT*6, end=RIGHT*6, stroke_width=5).move_to(DOWN * 2.5)

        # Add ball and floor to the scene
        self.add(ball, floor)

        # Initial height and horizontal retreat
        height = 2
        retreat = 1.5

        # Simulate bouncing effect with retreat and reduced height
        for i in range(6):
            # Move the ball down to the floor
            self.play(ball.animate.move_to(DOWN * 2.3 + RIGHT * retreat), run_time=0.5)

            # Move the ball up with reduced height
            self.play(ball.animate.move_to(UP * height + RIGHT * retreat), run_time=0.5)

            # Decrease height and retreat amount with each bounce
            height *= 0.6
            retreat *= 0.8

        # Final settle down
        self.play(ball.animate.move_to(DOWN * 2.3 + RIGHT * retreat), run_time=0.5)




class BouncingBallMovingForward(Scene):
    def construct(self):
        # Create a ball
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.move_to(UP * 2 + LEFT * 4)  # Start the ball high and to the left
        
        # Create a floor
        floor = Line(start=LEFT*6, end=RIGHT*6, stroke_width=5).move_to(DOWN * 2.5)

        # Add ball and floor to the scene
        self.add(ball, floor)

        # Initial height and horizontal forward movement
        height = 2
        forward = 1.5

        # Keep bouncing until the height is less than the threshold
        while height >= 0.00000001:
            # Move the ball down to the floor
            self.play(ball.animate.move_to(DOWN * 2.3 + RIGHT * forward), run_time=0.5)

            # Move the ball up with reduced height and forward movement
            self.play(ball.animate.move_to(UP * height + RIGHT * forward), run_time=0.5)

            # Decrease height and forward movement with each bounce
            height *= 0.6
            forward *= 1.2  # Increase the forward movement

        # Final settle down
        self.play(ball.animate.move_to(DOWN * 2.3 + RIGHT * forward), run_time=0.5)

class SquareToRollingBall(Scene):
    def construct(self):
        # Create a square with a side length of 2
        square = Square(side_length=2, color=BLUE)

        # Add the square to the scene
        self.add(square)
        
        # Number of iterations
        num_steps = 500
        angle_per_step = -PI / (2 * num_steps)  # Incremental rotation angle
        rounding_step = 2 / num_steps  # Incremental rounding radius

        for i in range(num_steps):
            # Create a rounded square with increasing corner radius
            rounded_square = RoundedRectangle(
                width=2,
                height=2,
                corner_radius=i * rounding_step,
                color=BLUE,
                fill_opacity=0
            )

            # Rotate the rounded square
            rounded_square.rotate(i * angle_per_step, about_point=square.get_center())

            # Update the square in the scene
            self.play(Transform(square, rounded_square), run_time=0.05)

        self.wait(1)