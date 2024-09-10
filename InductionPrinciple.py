from manim import *

class InductionPrinciple(Scene):
    def construct(self):
        # Title
        title = Text("Mathematical Induction").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Base case
        base_case_text = Text("Base Case: True for n = n₀", color=BLUE).to_edge(UP)
        number_line = NumberLine(x_range=[-1, 6, 1], include_numbers=True)
        base_case_dot = Dot(number_line.n2p(1), color=YELLOW)
        base_case_label = Text("n₀", color=YELLOW).next_to(base_case_dot, UP)

        self.play(Write(base_case_text))
        self.play(Create(number_line), FadeIn(base_case_dot), Write(base_case_label))
        self.wait(1)

        checkmark = Tex(r"\checkmark").next_to(base_case_dot, UP + RIGHT, buff=0.3).set_color(GREEN)
        self.play(Write(checkmark))
        self.wait(1)

        # Inductive step
        inductive_step_text = Text("Inductive Step: True for n = k, then for n = k+1", color=ORANGE).next_to(base_case_text, DOWN)
        self.play(Write(inductive_step_text))
        self.wait(1)

        # Assume true for n = k
        assume_k_dot = Dot(number_line.n2p(3), color=YELLOW)
        assume_k_label = Text("k", color=YELLOW).next_to(assume_k_dot, UP)

        self.play(FadeIn(assume_k_dot), Write(assume_k_label))
        self.wait(1)
        self.play(Write(Tex(r"\checkmark").next_to(assume_k_dot, UP + RIGHT, buff=0.3).set_color(GREEN)))

        # True for n = k+1
        k1_dot = Dot(number_line.n2p(4), color=YELLOW)
        k1_label = Text("k+1", color=YELLOW).next_to(k1_dot, UP)

        self.play(FadeIn(k1_dot), Write(k1_label))
        self.play(Write(Tex(r"\checkmark").next_to(k1_dot, UP + RIGHT, buff=0.3).set_color(GREEN)))
        self.wait(2)

        # Final conclusion
        conclusion = Text("Induction holds for all n >= n₀", color=GREEN).scale(1.2).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
