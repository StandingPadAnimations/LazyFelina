import bpy
from bpy.types import Panel, Operator


class optimize_PT_main_panel(Panel):
    bl_label = "Optimize Scene"
    bl_idname = "optimize_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='RENDER_STILL')

    
    def draw(self, context):
        layout = self.layout
        render_choose = bpy.context.scene.cycles.device  
        engine = bpy.context.scene.render.engine
                
        if engine == 'CYCLES':
            if bpy.context.preferences.addons["cycles"].preferences.compute_device_type == 'NONE':
                if render_choose == 'GPU':
                    row = layout.row()
                    row.label(text= "You have GPU selected but none enabled.")
                    row = layout.row()
                    row.label(text= "Either enable it in user prefs")
                    row = layout.row()
                    row.label(text= "or switch to CPU rendering")
                    row = layout.row()
                    row.operator("switchoptimizecpu.myop_operator", icon= 'MENU_PANEL')
                    row = layout.row()
                    row.operator("enablegpu.myop_operator", icon= 'MENU_PANEL') 
                    return
                    
                if render_choose == 'CPU':
                    row = layout.row()
                    row.operator("optimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                    
                 
                
            if bpy.context.preferences.addons["cycles"].preferences.compute_device_type == 'CUDA' or 'OPTIX' or 'OPENCL':
                
                if render_choose == 'CPU':
                    row = layout.row()
                    row.label(text= "You have CPU selected")
                    row = layout.row()
                    row.label(text= "but have a GPU avalible.")
                    row = layout.row()
                    row.label(text= "Do you want to switch or stay?")
                    row = layout.row()
                    row.operator("switchoptimizegpu.myop_operator", icon= 'MENU_PANEL')
                    row = layout.row()
                    row.operator("optimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
                
                if render_choose == 'GPU':
                    row = layout.row()
                    row.operator("optimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                    
                
                    
        if engine == 'BLENDER_EEVEE':
            row = layout.row()
            row.label(text= "Cycles Only >:C")



class optimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene Now"
    bl_idname = "optimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 1
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 240
        bpy.context.scene.render.tile_y = 216
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 0
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.2
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 256

    
        
        return {'FINISHED'}
    
class optimizeCPU_OT_my_op(Operator):
    bl_label = "Optimize Scene Now"
    bl_idname = "optimizecpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 2
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 32
        bpy.context.scene.render.tile_y = 32
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 0
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.5
        bpy.context.scene.cycles.adaptive_min_samples = 5
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 100

        
        return {'FINISHED'}
    
class switchoptimizeCPU_OT_my_op(Operator):
    bl_label = "Switch to CPU and Optimize Scene"
    bl_idname = "switchoptimizecpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.device = "CPU"
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 2
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 32
        bpy.context.scene.render.tile_y = 32
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 0
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.5
        bpy.context.scene.cycles.adaptive_min_samples = 5
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 100

        
        return {'FINISHED'}
    
class switchoptimizeGPU_OT_my_op(Operator):
    bl_label = "Switch to GPU and Optimize Scene"
    bl_idname = "switchoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 1
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 240
        bpy.context.scene.render.tile_y = 216
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 0
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.2
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 256

    
        
        return {'FINISHED'}
    
class enableGPU_OT_my_op(Operator):
    bl_label = "Enable GPU"
    bl_idname = "enablegpu.myop_operator"
    
    def execute(self, context):
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
        bpy.context.preferences.active_section = 'SYSTEM'

    
        
        return {'FINISHED'}