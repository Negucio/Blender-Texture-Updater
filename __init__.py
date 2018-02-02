bl_info = {
    "name": "Texture Updater",
    "author": "Roberto Noya <negucio@gmail.com>",
    "version": (0, 0, 2),
    "blender": (2, 79, 0),
    "location": "View3D",
    "description": "Updates every texture in the scene which has been modified",
    "warning": "Uses python operative system commands to retrieve the modification date. Should work in any o.s. but it was only tested in Windows.",
    "wiki_url": "",
    "category": "Texture"}

import bpy
from . import ui, handler


def register():
    ui.register()
    handler.register()
    bpy.types.Image.mod_date = bpy.props.IntProperty(default=0)


def unregister():
    del bpy.types.Image.modification_date
    handler.unregister()
    ui.unregister()
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()


