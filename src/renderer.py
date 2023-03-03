import glfw
import lib


# GLFW
def glfw_window(variable):
    glfw.init()
    variable = glfw.create_window(400, 300, "Window", None, None)
    glfw.make_context_current(variable)
    return variable


def glfw_mainloop():
    global window
    while not glfw.window_should_close(window):
        # render.glfw
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


def windower(renderer_selection):
    global window
    if renderer_selection == "glfw":
        window = glfw_window(renderer_selection)
        glfw_mainloop()
# END
