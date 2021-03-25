import bpy 
from bpy.types import Panel, Operator
import os


class Sky_PT_main_panel(Panel):
    bl_label = "Skys"
    bl_idname = "Sky_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 4
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='LIGHT_SUN')

    
    def draw(self, context):
        layout = self.layout
        engine = bpy.context.scene.render.engine
        
        if engine == 'CYCLES':
            layout.operator("sky.myop_operator", icon= 'LIGHT_SUN')
            layout.operator("Sky_aurora.myop_operator", icon= 'MOD_WAVE')
            
        if engine == 'BLENDER_EEVEE':
            row = layout.row()
            row.label(text= "Cycles Only >:C")



class Sky_OT_my_op(Operator):
    bl_label = "Sky"
    bl_idname = "sky.myop_operator"
    
    def execute(self, context):
         
        
        world_name = "Sky"
        filename = "LazyFelina/EpicSky.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=world_name,
                        directory=bpy.path.abspath(f"//{filename}\\World")
            )
            
        bpy.context.scene.world = bpy.data.worlds.get("Sky")
        bpy.context.space_data.shading.use_scene_world = False
        
        
        return {'FINISHED'}
    
class AuroraSky_OT_my_op(Operator):
    bl_label = "Sky with Aurora"
    bl_idname = "sky_aurora.myop_operator"
    
    def execute(self, context):
         
        
        world_name = "Sky_aurora"
        filename = "LazyFelina/EpicSky.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=world_name,
                        directory=bpy.path.abspath(f"//{filename}\\World")
            )
            
        bpy.context.scene.world = bpy.data.worlds.get("Sky_aurora")
        bpy.context.space_data.shading.use_scene_world = False
        
        
        return {'FINISHED'}
    
classes = [Sky_PT_main_panel, Sky_OT_my_op, AuroraSky_OT_my_op]



#Thing that does the process
def register(bl_info):
    
#class register
    for cls in classes:
        bpy.utils.register_class(cls)
        

        
def unregister():
#class unregister
    for cls in classes:
        bpy.utils.unregister_class(cls) 
        
    

     
     
if __name__  == "__main__":
    register() 