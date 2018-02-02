import bpy, os
from bpy.app.handlers import persistent

@persistent
def polycount_load_post(param):
    """
    Called on after loading a .blend file
    :param param: In order to append this function to the load_post handler, this has to receive a parameter. Always None.
    """
    for img in bpy.data.images:
        try: img.mod_date = int(os.path.getmtime(img.filepath_from_user()))
        except: continue

def register():
    if polycount_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(polycount_load_post)    

def unregister():
    bpy.app.handlers.load_post.remove(polycount_load_post)

if __name__ == "__main__":
    register()


