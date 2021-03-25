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
    bl_order = 5
    
    
    
    
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
                    row = layout.row()
                    row.operator("qualityoptimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                    
                 
                
            if bpy.context.preferences.addons["cycles"].preferences.compute_device_type == 'CUDA':
                
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
                    row = layout.row()
                    row.operator("qualityoptimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
                
                if render_choose == 'GPU':
                    row = layout.row()
                    row.operator("optimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    row = layout.row()
                    row.operator("qualityoptimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
                
            if bpy.context.preferences.addons["cycles"].preferences.compute_device_type == 'OPENCL':
                
                if render_choose == 'CPU':
                    row = layout.row()
                    row.label(text= "You have CPU selected")
                    row = layout.row()
                    row.label(text= "but have a GPU avalible.")
                    row = layout.row()
                    row.label(text= "Do you want to switch or stay?")
                    row = layout.row()
                    row.operator("openclswitchoptimizegpu.myop_operator", icon= 'MENU_PANEL')
                    row = layout.row()
                    row.operator("optimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    row = layout.row()
                    row.operator("qualityoptimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
                
                if render_choose == 'GPU':
                    row = layout.row()
                    row.operator("opencloptimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    row = layout.row()
                    row.operator("openclqualityoptimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
            if bpy.context.preferences.addons["cycles"].preferences.compute_device_type == 'OPTIX':
                
                if render_choose == 'CPU':
                    row = layout.row()
                    row.label(text= "You have CPU selected")
                    row = layout.row()
                    row.label(text= "but have a GPU avalible.")
                    row = layout.row()
                    row.label(text= "Do you want to switch or stay?")
                    row = layout.row()
                    row.operator("optixswitchoptimizegpu.myop_operator", icon= 'MENU_PANEL')
                    row = layout.row()
                    row.operator("optimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    row = layout.row()
                    row.operator("qualityoptimizecpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                
                
                if render_choose == 'GPU':
                    row = layout.row()
                    row.operator("optixoptimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    row = layout.row()
                    row.operator("optixqualityoptimizegpu.myop_operator", icon= 'OUTLINER_DATA_CAMERA')
                    return
                    
                
                    
        if engine == 'BLENDER_EEVEE':
            row = layout.row()
            row.label(text= "Cycles Only >:C")



class optimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Speed"
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
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
    
class OptixoptimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Speed"
    bl_idname = "optixoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 3
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 0.5
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 240
        bpy.context.scene.render.tile_y = 216
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 1
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.15
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 300
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
    
class OpenCloptimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Speed"
    bl_idname = "opencloptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 2
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
        bpy.context.scene.cycles.adaptive_threshold = 0.5
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 55
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
    
class optimizeCPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Speed"
    bl_idname = "optimizecpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 2
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 48
        bpy.context.scene.render.tile_y = 48
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
        bpy.ops.outliner.orphans_purge()

        
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
        bpy.context.scene.render.tile_x = 48
        bpy.context.scene.render.tile_y = 48
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
        bpy.ops.outliner.orphans_purge()

        
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
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
    
class OptixswitchoptimizeGPU_OT_my_op(Operator):
    bl_label = "Switch to GPU and Optimize Scene"
    bl_idname = "optixswitchoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 3
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 0.5
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 240
        bpy.context.scene.render.tile_y = 216
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 1
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.15
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 300
        bpy.ops.outliner.orphans_purge()


    
        
        return {'FINISHED'}
    
    
class OpenCLswitchoptimizeGPU_OT_my_op(Operator):
    bl_label = "Switch to GPU and Optimize Scene"
    bl_idname = "openclswitchoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 2
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 2
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
        bpy.context.scene.cycles.adaptive_threshold = 0.5
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 55
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
class enableGPU_OT_my_op(Operator):
    bl_label = "Enable GPU"
    bl_idname = "enablegpu.myop_operator"
    
    def execute(self, context):
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
        bpy.context.preferences.active_section = 'SYSTEM'

    
        
        return {'FINISHED'}
    
class QualityoptimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Quality"
    bl_idname = "qualityoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 3
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 0.5
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
        bpy.context.scene.cycles.adaptive_threshold = 0.02
        bpy.context.scene.cycles.adaptive_min_samples = 20
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 200
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
class OptiXQualityoptimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Quality"
    bl_idname = "optixqualityoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 4
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 0.2
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 240
        bpy.context.scene.render.tile_y = 216
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 2
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.1
        bpy.context.scene.cycles.adaptive_min_samples = 15
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 350
        bpy.ops.outliner.orphans_purge()


    
        
        return {'FINISHED'}
    
class OpenCLQualityoptimizeGPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Quality"
    bl_idname = "openclqualityoptimizegpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 3
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
        bpy.context.scene.cycles.adaptive_min_samples = 15
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 100
        bpy.ops.outliner.orphans_purge()

    
        
        return {'FINISHED'}
    
class QualityoptimizeCPU_OT_my_op(Operator):
    bl_label = "Optimize Scene for Quality"
    bl_idname = "qualityoptimizecpu.myop_operator"
    
    def execute(self, context):
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.max_bounces = 3
        bpy.context.scene.cycles.sample_clamp_indirect = 1
        bpy.context.scene.cycles.blur_glossy = 1
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.render.tile_x = 48
        bpy.context.scene.render.tile_y = 48
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.render.simplify_subdivision = 0
        bpy.context.scene.cycles.ao_bounces_render = 0
        bpy.context.scene.cycles.ao_bounces = 0
        bpy.context.scene.render.use_motion_blur = False
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.use_border = True
        bpy.context.scene.cycles.adaptive_threshold = 0.05
        bpy.context.scene.cycles.adaptive_min_samples = 10
        bpy.context.space_data.shading.use_scene_world = False
        bpy.context.space_data.shading.use_scene_lights = False
        bpy.context.scene.cycles.volume_max_steps = 250
        bpy.ops.outliner.orphans_purge()

        
        return {'FINISHED'}
    
    


#register--------------------------------------------------------------------------------------------------------------


#Class register
classes = [optimizeGPU_OT_my_op,optimizeCPU_OT_my_op, optimize_PT_main_panel, switchoptimizeCPU_OT_my_op, switchoptimizeGPU_OT_my_op, enableGPU_OT_my_op, QualityoptimizeGPU_OT_my_op, QualityoptimizeCPU_OT_my_op, OptixoptimizeGPU_OT_my_op, OpenCloptimizeGPU_OT_my_op, OptixswitchoptimizeGPU_OT_my_op, OpenCLswitchoptimizeGPU_OT_my_op, OptiXQualityoptimizeGPU_OT_my_op, OpenCLQualityoptimizeGPU_OT_my_op]



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