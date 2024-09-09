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
