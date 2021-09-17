# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
import os
import sys
import importlib
from itertools import groupby

from . import node_system
from . import node_base
from . import node_category
from . import node_socket
from . import node_operator

bl_info = {
    "name" : "PearlNode",
    "author" : "Cuimi",
    "description" : "",
    "blender" : (3, 00, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "DevelopMent",
    "category" : "Test",
    "doc_url" : "",
    "tracker_url" : "https://github.com/SoTosorrow/BlenderNodeEditor",
}

def register():
    node_system.register()
    node_socket.register()
    node_base.register()
    node_category.register()
    node_operator.register()
    print("Pearl Node On")

def unregister():
    node_system.unregister()
    node_socket.unregister()
    node_base.unregister()
    node_category.unregister()
    node_operator.unregister()
    print("Pearl Node Off")
