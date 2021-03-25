import bpy 
from bpy.types import Panel, Operator
import os


class Material_PT_set(bpy.types.Panel):
    bl_label = "Materials"
    bl_idname = "Material_PT_set"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='MATERIAL')
        
    def draw(self, context):
        layout = self.layout





class Puddle_PT_add(Panel):
    bl_label = "Puddles"
    bl_idname = "puddle_PT_add"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Material_PT_set'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 7
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='NODE_MATERIAL')

    
    def draw(self, context):
        layout = self.layout 
        
        row = layout.row()
        row.operator("puddle.myop_operator", icon= 'RADIOBUT_OFF')
        row = layout.row()
        row.operator("frozenpuddle.myop_operator", icon= 'DECORATE_KEYFRAME')
        
            



class Puddle_OT_add(Operator):
    bl_label = "Puddle"
    bl_idname = "puddle.myop_operator"
    
    def execute(self, context):
         
        
        node_name = "Puddles"
        filename = "LazyFelina/Puddle.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=node_name,
                        directory=bpy.path.abspath(f"//{filename}\\NodeTree")
            )
        
        node_tree = bpy.context.active_object.active_material.node_tree.nodes

        node_tree.new(type='ShaderNodeGroup').node_tree = bpy.data.node_groups['Puddles']
        
        self.report({'INFO'}, "You can now add it to any material by doing shift a, group")
        

        
        
        return {'FINISHED'}
    
    
class FrozenPuddle_OT_add(Operator):
    bl_label = "Frozen Puddles"
    bl_idname = "frozenpuddle.myop_operator"
    
    def execute(self, context):
         
        
        node_name = "Frozen Puddles"
        filename = "LazyFelina/Puddle.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=node_name,
                        directory=bpy.path.abspath(f"//{filename}\\NodeTree")
            )
        
        node_tree = bpy.context.active_object.active_material.node_tree.nodes

        node_tree.new(type='ShaderNodeGroup').node_tree = bpy.data.node_groups['Frozen Puddles']
        
        self.report({'INFO'}, "You can now add it to any material by doing shift a, group")
        
        

        
        
        return {'FINISHED'}
    
    
class Glass_PT_add(Panel):
    bl_label = "Glass"
    bl_idname = "glass_PT_add"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Material_PT_set'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 7
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='LIBRARY_DATA_OVERRIDE')

    
    def draw(self, context):
        layout = self.layout 
        
        row = layout.row()
        row.operator("glass.myop_operator", icon= 'ORIENTATION_LOCAL')
        
        
            



class Glass_OT_add(Operator):
    bl_label = "Glass"
    bl_idname = "glass.myop_operator"
    
    def execute(self, context):
         
        
        node_name = "Principled Glass BSDF"
        filename = "LazyFelina/glass.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=node_name,
                        directory=bpy.path.abspath(f"//{filename}\\NodeTree")
            )
        
        node_tree = bpy.context.active_object.active_material.node_tree.nodes

        node_tree.new(type='ShaderNodeGroup').node_tree = bpy.data.node_groups['Principled Glass BSDF']
        
        self.report({'INFO'}, "You can now add it to any material by doing shift a, group")
        

        
        
        return {'FINISHED'}
    
    
classes = [Material_PT_set, Puddle_PT_add, Puddle_OT_add, FrozenPuddle_OT_add, Glass_OT_add, Glass_PT_add]



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