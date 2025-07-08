from manim import *

class VectorSpaceWithPlane(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        
        # Create axes without numbers to avoid LaTeX issues
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
            z_axis_config={"include_numbers": False},
        )
        
        # Use Text instead of MathTex for labels
        axes_labels = axes.get_axis_labels(
            Text("x").scale(0.7),
            Text("y").scale(0.7),
            Text("z").scale(0.7)
        )

        # Create plane using parametric function
        plane = Surface(
            lambda u, v: [u, u, v],
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
            fill_opacity=0.5,
            fill_color=BLUE,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Create points
        points = [
            Dot3D(point=[0, 0, 0], color=RED, radius=0.08),
            Dot3D(point=[1, 1, 1], color=GREEN, radius=0.08),
            Dot3D(point=[2, 2, 2], color=YELLOW, radius=0.08)
        ]
        
        # Create labels using Text
        labels = [
            Text("(0,0,0)", color=RED, font_size=24).next_to(points[0], OUT + RIGHT, buff=0.1),
            Text("(1,1,1)", color=GREEN, font_size=24).next_to(points[1], OUT + LEFT, buff=0.1),
            Text("(2,2,2)", color=YELLOW, font_size=24).next_to(points[2], OUT + RIGHT, buff=0.1)
        ]
        
        # Create vectors
        vectors = [
            Arrow3D(
                start=[0, 0, 0],
                end=[1, 1, 1],
                color=GREEN,
                resolution=8,
                thickness=0.02
            ),
            Arrow3D(
                start=[0, 0, 0],
                end=[2, 2, 2],
                color=YELLOW,
                resolution=8,
                thickness=0.02
            )
        ]
        
        # Add title using Text
        title = Text("Plane defined by x=y=z", font_size=36).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        
        # Animation sequence
        self.play(Write(title))
        self.play(Create(axes), Write(axes_labels))
        self.play(*[Create(p) for p in points], *[Write(l) for l in labels])
        self.play(*[Create(v) for v in vectors])
        self.play(Create(plane), run_time=3)
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # Add plane equation
        plane_eq = Text("x = y = z", color=YELLOW, font_size=36).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(plane_eq)
        self.play(Write(plane_eq))
        self.wait(3)