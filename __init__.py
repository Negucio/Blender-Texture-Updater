bl_info = {
    "name": "Texture Updater",
    "author": "Roberto Noya <negucio@gmail.com>",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3D",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Misc"}

import bpy
from . import ui


def register():
    ui.register()
    bpy.types.Image.mod_date = bpy.props.IntProperty(default=0)


def unregister():
    del bpy.types.Image.modification_date
    ui.unregister()
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()


