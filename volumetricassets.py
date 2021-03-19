import bpy
from bpy.types import Panel, Operator 
import os 

class vol_PT_add(Panel):
    bl_label = "Volumetrics by Vortex"
    bl_idname = "vol_PT_add"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='OUTLINER_OB_VOLUME')

    
    def draw(self, context):
        layout = self.layout
        
        
        layout.operator("beam.myop_operator", icon= 'LIGHTPROBE_PLANAR')
        layout.operator("mist_cube.myop_operator", icon= 'MESH_CUBE')
        layout.operator("cloud.myop_operator", icon= 'VOLUME_DATA')
        layout.operator("mist_sphere.myop_operator", icon= 'NODE_MATERIAL')
        layout.operator("aurora.myop_operator", icon= 'MAT_SPHERE_SKY')
        layout.operator("vortex.myop_operator", icon= 'FORCE_VORTEX')
            



class vol_OT_ray(Operator):
    bl_label = "2D Beam"
    bl_idname = "beam.myop_operator"
    
    def execute(self, context):
         
        
        object_name = "SOW-ish 2d beam"
        filename = "LazyFelina/Volumetrics Asset Pack V8 Early version.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=object_name,
                        directory=bpy.path.abspath(f"//{filename}\\Object")
            )
            
        
        
        
        return {'FINISHED'}
    
class vol_OT_cube(Operator):
    bl_label = "Mist Cube"
    bl_idname = "mist_cube.myop_operator"
    
    def execute(self, context):
         
        
        object_name = "Ground Mist Cube"
        filename = "LazyFelina/Volumetrics Asset Pack V8 Early version.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=object_name,
                        directory=bpy.path.abspath(f"//{filename}\\Object")
            )
            
        
        
        
        return {'FINISHED'}
    
class vol_OT_cloud(Operator):
    bl_label = "Cloud"
    bl_idname = "cloud.myop_operator"
    
    def execute(self, context):
         
        
        object_name = "WIP Fake Volumetric Cloud"
        filename = "LazyFelina/Volumetrics Asset Pack V8 Early version.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=object_name,
                        directory=bpy.path.abspath(f"//{filename}\\Object")
            )
            
        
        
        
        return {'FINISHED'}
    
class vol_OT_mist(Operator):
    bl_label = "Mist Sphere"
    bl_idname = "mist_sphere.myop_operator"
    
    def execute(self, context):
         
        
        object_name = "Mist Spheres WIP"
        filename = "LazyFelina/Volumetrics Asset Pack V8 Early version.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=object_name,
                        directory=bpy.path.abspath(f"//{filename}\\Object")
            )
            
        
        
        
        return {'FINISHED'}
    
class vol_OT_aurora(Operator):
    bl_label = "Aurora"
    bl_idname = "aurora.myop_operator"
    
    def execute(self, context):
         
        
        object_name = "Aurora"
        filename = "LazyFelina/Volumetrics Asset Pack V8 Early version.blend"
        
        
        

        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
            
        bpy.ops.wm.append(
                        filename=object_name,
                        directory=bpy.path.abspath(f"//{filename}\\Object")
            )
        
        
        
        
        
        return {'FINISHED'}
    
class vortex_OT_is_epic(Operator):
    bl_label = "Vortex's Pack and Twitter"
    bl_idname = "vortex.myop_operator"
    
    def execute(self, context):
         
        bpy.ops.wm.url_open(url="https://drive.google.com/drive/folders/17BvJ179tpBYndQiS_0bMcjPPI6nZNkiA?usp=sharing")
        bpy.ops.wm.url_open(url="https://twitter.com/vortex15234")
        
        return {'FINISHED'}