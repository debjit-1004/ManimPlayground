from manim import *

class TowerOfHanoi(Scene):
    def construct(self):
        num_disks = 5  # Increase number of disks for better visual
        rods = VGroup(*[Line(UP * 3, DOWN * 2, stroke_width=8) for _ in range(3)]).arrange(buff=3)
        base = Line(rods[0].get_left() + LEFT * 0.5, rods[2].get_right() + RIGHT * 0.5, stroke_width=8)

        rod_labels = VGroup(
            Tex("Rod A").next_to(rods[0], DOWN),
            Tex("Rod B").next_to(rods[1], DOWN),
            Tex("Rod C").next_to(rods[2], DOWN)
        )

        self.add(base, rods, rod_labels)

        # Create disks with different sizes and colors
        disks = VGroup(*[self.create_disk(size, color) for size, color in zip(
            range(num_disks, 0, -1), [RED, BLUE, GREEN, ORANGE, PURPLE])])

        # Place disks on the first rod
        for i, disk in enumerate(disks):
            disk.move_to(rods[0].get_bottom() + UP * (i + 0.5))

        self.add(disks)

        # Recursive solution steps
        self.hanoi(num_disks, disks, rods[0], rods[2], rods[1])

    def create_disk(self, size, color):
        """Create a disk with the given size and color."""
        return Rectangle(width=0.8 * size + 1, height=0.3, color=color, fill_opacity=0.9, stroke_width=2).set_fill(color)

    def hanoi(self, n, disks, source, target, auxiliary):
        """Solve the Tower of Hanoi problem with recursive moves."""
        if n == 1:
            self.move_disk(disks[n-1], source, target)
        else:
            self.hanoi(n-1, disks, source, auxiliary, target)
            self.move_disk(disks[n-1], source, target)
            self.hanoi(n-1, disks, auxiliary, target, source)

    def move_disk(self, disk, source, target):
        """Move the disk from the source rod to the target rod."""
        disk_dest = target.get_bottom() + UP * (self.get_rod_height(target) + 0.5)

        self.play(disk.animate.move_to(source.get_top() + UP * 1), run_time=0.5)  # Lift up
        self.play(disk.animate.move_to([disk_dest[0], disk.get_y(), 0]), run_time=0.7)  # Move horizontally
        self.play(disk.animate.move_to(disk_dest), run_time=0.5)  # Drop onto the target rod
        self.wait(0.3)

    def get_rod_height(self, rod):
        """Get the current height of disks stacked on the rod."""
        return len([m for m in self.mobjects if isinstance(m, Rectangle) and m.get_center()[0] == rod.get_center()[0]])
