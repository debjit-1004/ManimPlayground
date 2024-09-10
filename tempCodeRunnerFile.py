

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
