import os
import sys

# if os.getenv("XDG_SESSION_TYPE") == "wayland":
#     os.environ["XDG_SESSION_TYPE"] = "x11"

import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations import GlfwRenderer

