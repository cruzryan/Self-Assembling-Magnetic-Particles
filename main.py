import numpy as np
import pyray as rl
from particle import Particle

rl.init_window(800, 450, "IAC Particle Simulator")
rl.set_target_fps(60)

camera = rl.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)


#test particle
mg = np.array([(-1, 1), (-1, 1), (-1, 1), (-1, 1)])
p = Particle(0, np.array[0,0,0],  np.array[0,0,0], 4, mg, None)

if __name__ == "__main__":
    print("Starting simulator...")

    while not rl.window_should_close():
        rl.update_camera(camera, rl.CAMERA_ORBITAL)
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        rl.begin_mode_3d(camera)
        rl.draw_grid(20, 1.0)
        rl.end_mode_3d()
        rl.draw_text("Hello world", 190, 200, 20, rl.VIOLET)

        rl.end_drawing()

rl.close_window()