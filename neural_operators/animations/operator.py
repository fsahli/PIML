from manim import *

config.background_color = WHITE


class TransformFunction(Scene):
    def construct(self):
        # Create the initial and final functions
        initial_function = MathTex("x^2", color = BLACK).scale(0.8).to_edge(LEFT)
        transformed_function = MathTex("2x", color = BLACK).scale(0.8).to_edge(RIGHT)

        # Create the "operator" block
        operator_block = Rectangle(width=3, height=2, color=BLACK, fill_opacity=1)
        operator_text = Tex("operator", color=WHITE).scale(0.8)
        operator_group = VGroup(operator_block, operator_text).move_to(ORIGIN)
        operator_group.z_index = 10000

        # Create and display the graph of x^2
        initial_function_graph = self.plot_function(lambda x: x**2, BLUE)
        initial_function_graph.next_to(initial_function, RIGHT, buff = -4).scale(0.3)

        # Display the operator block
        self.add(operator_group)
        self.play(Write(initial_function), Create(initial_function_graph))

        # Create and display the graph of 2x
        transformed_function_graph = self.plot_function(lambda x: 2*x, GREEN).scale(0.3)
        transformed_function_graph.next_to(transformed_function, LEFT, buff=0.05)


        # Move the axes to the right and scale it down as the transformation occurs
        self.play(
            ReplacementTransform(initial_function, transformed_function),
            ReplacementTransform(initial_function_graph, transformed_function_graph)
        )
        # ApplyMethod(axes.animate.next_to(transformed_function, DOWN, buff=0.2).scale(0.5)),


        self.wait(1)

        # Clear the screen
        self.play(FadeOut(transformed_function), FadeOut(transformed_function_graph))

    def plot_function(self, func, color):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 10],
            axis_config={"color": BLUE},
        )
        graph = axes.plot(func, color=color)
        return graph

if __name__ == "__main__":
    config.pixel_height = 500
    config.pixel_width = 500
    config.frame_height = 7.0
    config.frame_width = 7.0

    scene = TransformFunction()
    scene.render()
    scene.play(scene.construct)
