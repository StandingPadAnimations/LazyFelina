import bpy
from bpy.types import Panel

class Render_PT_UI(Panel): 
    bl_label = "Quick Render Settings"
    bl_idname = "Render_PT_felina_UI"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        engine = bpy.context.scene.render.engine
        layout.label(text="", icon='BLENDER')
            
        
    
    
    def draw(self, context):
        layout = self.layout
        render = bpy.context.scene.cycles
        renderview = bpy.context.scene.cycles
        light = bpy.context.scene.world.light_settings
        erender = bpy.context.scene.eevee
        erenderview = bpy.context.scene.eevee
        engine = bpy.context.scene.render.engine
         

        
        
        if engine == 'CYCLES': 
                      
            
            row = layout.row()
            box = layout.box()
            box.label(text= "Render Settings")
            row = box.row()
            
            
            #samples
            row.prop(render, "samples")
            row.prop(renderview, "preview_samples")
            layout.separator(factor= .5)
            
            #Light bounces
            row = box.row()
            row.prop(render, "max_bounces")
            
            
            #Clamping
            row = box.row()
            row.prop(render, "sample_clamp_indirect")
            row.prop(render, "sample_clamp_direct")
            
            
            #AO
            row = box.row()
            row.prop(light, "use_ambient_occlusion")
            
            
            if light.use_ambient_occlusion == True:
                box.prop(light, "ao_factor")
                row.label(icon= 'OUTLINER_OB_LIGHT') 
                
            elif light.use_ambient_occlusion == False:
                row.label(icon= 'LIGHT_DATA') 
            
            
            
        if engine == 'BLENDER_EEVEE':
            
            #Samples
            box = layout.box()
            row = box.row()
            
            row.prop(erender, "taa_render_samples")
            row.prop(erenderview, "taa_samples")
            
            
            
            #AO
            row = box.row()
            row.prop(erenderview, "use_gtao")
            
            if erenderview.use_gtao == True:
                box.prop(erenderview, "gtao_distance")
                row.label(icon= "OUTLINER_OB_LIGHT")
                
                
                
            elif erenderview.use_gtao == False:
                row.label(icon= 'LIGHT_DATA')
             
             
            #Bloom   
            row = box.row()
            row.prop(erenderview, "use_bloom")
            
            if erenderview.use_bloom == True:
                
                
                box.prop(erenderview, "bloom_threshold", text= "Bloom Threshold")
                box.prop(erenderview, "bloom_color", text= "Bloom Color")
                row.label(icon= 'GHOST_ENABLED')
                
            elif erenderview.use_bloom == False:
                row.label(icon= 'GHOST_DISABLED')
            
            
            #Tile Size
            row = box.row()
            row.label(icon= 'OUTLINER_DATA_LIGHTPROBE')
            row.prop(erenderview, "volumetric_tile_size")
            
            
            
            #motion Blur
            row = box.row()
            row.prop(erenderview, "use_motion_blur")
            
            if erenderview.use_motion_blur == True:
                box.prop(erenderview, "motion_blur_position")
                row.label(icon= 'FORCE_TURBULENCE')
                
                
            elif erenderview.use_motion_blur == False:
                row.label(icon= 'FORCE_FORCE')
                
            #Volumetric Shadows
            row = box.row()
            row.prop(erenderview, "use_volumetric_shadows")
            
            if erenderview.use_volumetric_shadows == True:
                box.prop(erenderview, "volumetric_shadow_samples")
                row.label(icon= 'OUTLINER_OB_VOLUME')
                
                
            elif erenderview.use_volumetric_shadows == False:
                row.label(icon= 'OUTLINER_DATA_VOLUME') 
            

class Advanced_PT_UI(Panel): 
    bl_label = ""
    bl_idname = "Advanced_PT_felina_UI"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 1
    bl_parent_id = 'Render_PT_felina_UI'
    
    
    def draw_header(self, context):
        layout = self.layout
        engine = bpy.context.scene.render.engine
        erenderview = bpy.context.scene.eevee
        errender = bpy.context.scene.render
        
        if engine == 'CYCLES':
            layout.label(text="Material Mode Settings")
            
        if engine == 'BLENDER_EEVEE':
            layout.label(text="Advanced")
    
    
    
    
    def draw(self, context):
        layout = self.layout
        erenderview = bpy.context.scene.eevee
        engine = bpy.context.scene.render.engine
        errender = bpy.context.scene.render
         

        
        
        if engine == 'CYCLES': 
            box = layout.box()
            row = box.row()
            row.prop(erenderview, "use_gtao")
            
            if erenderview.use_gtao == True:
                box.prop(erenderview, "gtao_distance")
                row.label(icon= "OUTLINER_OB_LIGHT")
                
                
                
            elif erenderview.use_gtao == False:
                row.label(icon= 'LIGHT_DATA')
             
             
            #Bloom   
            row = box.row()
            row.prop(erenderview, "use_bloom")
            
            if erenderview.use_bloom == True:
                
                
                box.prop(erenderview, "bloom_threshold", text= "Bloom Threshold")
                box.prop(erenderview, "bloom_color", text= "Bloom Color")
                row.label(icon= 'GHOST_ENABLED')
                
            elif erenderview.use_bloom == False:
                row.label(icon= 'GHOST_DISABLED')
            
            
            #Tile Size
            row = box.row()
            row.label(icon= 'OUTLINER_DATA_LIGHTPROBE')
            row.prop(erenderview, "volumetric_tile_size")
            
            
            #Volumetric Shadows
            row = box.row()
            row.prop(erenderview, "use_volumetric_shadows")
            
            if erenderview.use_volumetric_shadows == True:
                box.prop(erenderview, "volumetric_shadow_samples")
                row.label(icon= 'OUTLINER_OB_VOLUME')
                
                
            elif erenderview.use_volumetric_shadows == False:
                row.label(icon= 'OUTLINER_DATA_VOLUME') 
                
        
        if engine == 'BLENDER_EEVEE':
            box = layout.box()
            row = box.row()
            row.label(icon= 'INDIRECT_ONLY_ON')
            row.prop(erenderview, "use_ssr")
            if erenderview.use_ssr == True: 
                row = box.row()
                row.label(icon= 'TRACKING_REFINE_FORWARDS')
                row.prop(erenderview, "use_ssr_refraction")
            
            row = box.row()
            row.label(text= "SSS Samples", icon= 'STYLUS_PRESSURE')
            row.prop(erenderview, "sss_samples")
            row = box.row()
            row.label(icon= 'META_CUBE')
            row.prop(erenderview, "shadow_cube_size", text= "Shadow Cube Size")
            row = box.row()
            row.label(icon= 'INDIRECT_ONLY_OFF')
            row.prop(errender, "use_high_quality_normals")


           
classes = [Render_PT_UI, Advanced_PT_UI]


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
        