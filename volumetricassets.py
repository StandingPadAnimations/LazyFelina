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
    bl_order = 6
    
    
    
    
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
            
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        
        
        
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
            
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        
        
        
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
            
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        
        
        
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
            
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        mist_boi = bpy.data.collections.new('Mist Boi') 
        bpy.context.scene.collection.children.link(mist_boi)
    
        
        objs = bpy.context.selected_objects

        # Set target collection to a known collection 
        coll_target = bpy.context.scene.collection.children.get("Mist Boi")

        # Set target collection based on the collection in context (selected) 
        #coll_target = C.collection

        # If target found and object list not empty
        if coll_target and objs:

            # Loop through all objects
            for ob in objs:
                # Loop through all collections the obj is linked to
                for coll in ob.users_collection:
                    # Unlink the object
                    coll.objects.unlink(ob)

                # Link each object to the target collection
                coll_target.objects.link(ob)

        bpy.ops.scene.view_layer_add(type='EMPTY')
        bpy.context.scene.view_layers["View Layer.001"].name = "Mist Boi"
        bpy.context.layer_collection.children['Mist Boi'].exclude = False
        self.report({'INFO'}, "Scale up mist sphere to your liking")
        
        
        
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
        
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        
        
        
        return {'FINISHED'}
    
class vortex_OT_is_epic(Operator):
    bl_label = "Vortex's Pack and Twitter"
    bl_idname = "vortex.myop_operator"
    
    def execute(self, context):
         
        bpy.ops.wm.url_open(url="https://drive.google.com/drive/folders/17BvJ179tpBYndQiS_0bMcjPPI6nZNkiA?usp=sharing")
        bpy.ops.wm.url_open(url="https://twitter.com/vortex15234")
        
        return {'FINISHED'}
    




#register--------------------------------------------------------------------------------------------------------------


#Class register
classes = [vol_PT_add, vol_OT_ray, vol_OT_cube, vol_OT_cloud, vol_OT_mist, vol_OT_aurora, vortex_OT_is_epic]



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