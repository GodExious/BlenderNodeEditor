import bpy
from mathutils import Vector

from .runtime import cache_socket_variables, cache_socket_links

class SocketBase():
    compatible_sockets = []

    