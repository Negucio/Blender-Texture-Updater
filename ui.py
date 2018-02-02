import bpy, os

class VIEW3D_PT_TextureUpdater_Main(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Texture Updater"

    def draw(self, context):
        layout = self.layout
        layout.operator("scene.texture_updater", text="Update Scene Textures")

       
class SCENE_OT_TextureUpdater_Update(bpy.types.Operator):
    bl_idname = "scene.texture_updater"
    bl_label = "Update"
    bl_description = "Updates every texture in the scene which has been modified"

    def execute(self, context):
        reloaded = []
        for img in bpy.data.images:
            try:
                mod_date = int(os.path.getmtime(img.filepath_from_user()))
                if mod_date > img.mod_date:
                    reloaded.append(img.name)
                    img.reload()                       
                img.mod_date = mod_date
            except: continue                
            
        for area in bpy.context.screen.areas:
            if area.type in ['IMAGE_EDITOR', 'VIEW_3D']:
                area.tag_redraw()
                
        state = context.space_data.viewport_shade
        if state in ['RENDERED','MATERIAL','TEXTURED']:
            context.space_data.viewport_shade = 'SOLID'
            context.space_data.viewport_shade = state
        
        if len(reloaded)>0: print("Reloaded textures: " + str(reloaded))
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCENE_OT_TextureUpdater_Update)
    bpy.utils.register_class(VIEW3D_PT_TextureUpdater_Main)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_TextureUpdater_Main)
    bpy.utils.unregister_class(SCENE_OT_TextureUpdater_Update)

