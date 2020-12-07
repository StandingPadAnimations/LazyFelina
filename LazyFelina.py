bl_info = {
    "name" : "Lazy Felina",
    "author" : "StandingPad Animations",
    "version" : (4, 0),
    "blender" : (2, 91, 0),
    "location" : "View3D > Toolbar > Add Object",
    "description" : "Shortcut stuff and be lazy. Felina is a reference to a species from Songs of War made by Black Plasma Studios, I highly recomend it",
    "warning" : "Beta Phase, so there may be some bugs and not all features are added",
    "wiki_url" : "",
    "category" : "",    
}

import bpy
from bpy.types import Panel, Operator

#render settings

class Felina(bpy.types.Panel):
    bl_label = "LazyFelina"
    bl_idname = "Lazy_PT_felina"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    
    def draw(self, context):
        
        
        layout = self.layout
    
    
    
#cycles render settings---------------------------------------------------------------------------------------------    
    
class CyclesRender(bpy.types.Panel):
    bl_label = "Cycles Render Settings"
    bl_idname = "Cycles_PT_Render"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
   
    
    
    
    def draw(self, context):
        
        
        layout = self.layout
        layout.scale_y = .95
        render = bpy.context.scene.cycles
        renderview = bpy.context.scene.cycles
        light = bpy.context.scene.world.light_settings

        


        row = layout.row()
        row.label(text= "Cycles Render Settings", icon= 'RESTRICT_RENDER_OFF')
        row = layout.row()
        row.label(text= "Render")
        layout.prop(render, "samples")
        row = layout.row()
        row.label(text= "Viewport")
        layout.prop(renderview, "preview_samples")
        row = layout.row()
        row.label(text= "Total Light Bounces")
        layout.prop(render, "max_bounces")
        row = layout.row()
        row.label(text= "Clamping Indirect")
        layout.prop(render, "sample_clamp_indirect")
        row = layout.row()
        row.label(text= "Clamping Direct")
        layout.prop(render, "sample_clamp_direct")
        layout.prop(light, "use_ambient_occlusion")
        layout.prop(light, "ao_factor")
       
        
        
        
    
        
#eevee render settings-------------------------------------------------------------------------------------------
    
class EEVEERender(bpy.types.Panel):
    bl_label = "EEVEE Render Settings"
    bl_idname = "EEVEERender"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    def draw(self, context):
        
        
        layout = self.layout
        layout.scale_y = .95
        erender = bpy.context.scene.eevee
        erenderview = bpy.context.scene.eevee
        
        
        
        row = layout.row()
        row.label(text= "EEVEE Render Settings", icon= 'BLENDER')
        row = layout.row()
        layout.prop(erender, "taa_render_samples")
        row = layout.row()
        layout.prop(erenderview, "taa_samples")
        row = layout.row()
        layout.prop(erenderview, "use_gtao")
        row = layout.row()
        layout.prop(erenderview, "gtao_distance")
        row = layout.row()
        layout.prop(erenderview, "use_bloom")
        row = layout.row()
        layout.prop(erenderview, "bloom_threshold")
        row = layout.row()
        layout.prop(erenderview, "bloom_color")
        row = layout.row()
        layout.prop(erenderview, "volumetric_tile_size")
        row = layout.row()
        layout.prop(erenderview, "use_motion_blur")
        row = layout.row()
        layout.prop(erenderview, "motion_blur_position")
        row = layout.row()
        layout.prop(erenderview, "use_volumetric_shadows")
       
       
       

#text panel--------------------------------------------------------------------------------------------------------        
        

class TextTool(bpy.types.Panel):
    bl_label = "Text Tool"
    bl_idname = "OBJECT_PT_text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    

    def draw(self, context):
        layout = self.layout
     
        
        row = layout.row()
        row.operator("wm.textop", text= "Text Tool", icon= 'FILE_FONT')
        
        
        
        
        
        
class WM_OT_textOp(bpy.types.Operator):
    bl_label = "Text Tool Operator"
    bl_idname = "wm.textop"  
    
    text = bpy.props.StringProperty(name= "Enter Text:")
    center = bpy.props.BoolProperty(name= "Center Origin", default= False)
    extrude = bpy.props.BoolProperty(name= "Extrude", default= False)
    extrude_amount = bpy.props.FloatProperty(name= "Extrude Amount:", default= 0)
   
    
    def execute(self, context):
        
        t = self.text
        c = self.center
        e = self.extrude
        ea = self.extrude_amount
        
        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text= t)
        bpy.ops.object.editmode_toggle()
        
        
        
        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'
            
            
        if e == True:
            bpy.context.object.data.extrude = ea

            

        return {'FINISHED'}
    
    
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
         


#mist--------------------------------------------------------------------------------------------------------------



def mist_comp_action(context):
    tree = context.scene.node_tree
    
    
    comp_node = tree.nodes.get
    mix_node = tree.nodes.new('CompositorNodeMixRGB')
    mix_node.location = (200, 0)
    
    
    map_node = tree.nodes.new('CompositorNodeMapValue')
    map_node.location = (25, 0)
    
    link = tree.links.new
    
    link(map_node.outputs[0], mix_node.inputs[0])
    
    
    
    
    
    
  

    
    return {'FINISHED'}




    

class Mist_PT_main_panel(Panel):
    bl_label = "Mist"
    bl_idname = "Mist_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        
        
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")
        
        
        
        

        layout.operator("mist.myop_operator")


class Mist_OT_my_op(Operator):
    bl_label = "Create Mist"
    bl_idname = "mist.myop_operator"
    
    def execute(self, context):
        
        
        
        self.report({'INFO'}, "Check Compositor, connect mist to map value and the image into the top input of MixRGB")
        
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        
       
        
        
        
        
        
        mist_comp_action(context)
        
        
        
        
        
        
        vl.use_pass_mist = True
        camera.show_mist = True
        context.scene.use_nodes = True
        
        


 
        
        return {'FINISHED'}
    







#Boosh-----------------------------------------------------------------------------------------------------------




def boosh_comp_action(context):
    tree = context.scene.node_tree
    
    
    comp_node = tree.nodes.get
    mix_node = tree.nodes.new('CompositorNodeMixRGB')
    mix_node.location = (200, 0)
    
    
    map_node = tree.nodes.new('CompositorNodeMapValue')
    map_node.location = (25, 0)
    
    colorcorrect_node = tree.nodes.new('CompositorNodeColorCorrection')
    colorcorrect_node.location = (400, 400)
    
    blur_node = tree.nodes.new('CompositorNodeBlur')
    blur_node.location = (600, 400)
    
    mix2_node = tree.nodes.new('CompositorNodeMixRGB')
    mix2_node.location = (800, 200)
    mix2_node.blend_type = 'ADD'
    
    
    
    
    
    
    link = tree.links.new
    
    link(map_node.outputs[0], mix_node.inputs[0])
    link(mix_node.outputs[0], colorcorrect_node.inputs[0])
    link(mix_node.outputs[0], mix2_node.inputs[1])
    link(colorcorrect_node.outputs[0], blur_node.inputs[0])
    link(blur_node.outputs[0], mix2_node.inputs[2])





class Boosh_PT_main_panel(Panel):
    bl_label = "Boosh(From the BPS Tutorials)"
    bl_idname = "Boosh_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        
        
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")
        
        
        
        

        layout.operator("boosh.myop_operator")


class Boosh_OT_my_op(Operator):
    bl_label = "Create Boosh"
    bl_idname = "boosh.myop_operator"
    
    def execute(self, context):
        
        
        
        self.report({'INFO'}, "Check Compositor, connect mist to map value and the image into the top input of MixRGB")
        
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        
       
        
        
        
        
        
        boosh_comp_action(context)
        
        
        
        
        
        
        vl.use_pass_mist = True
        camera.show_mist = True
        context.scene.use_nodes = True
        
        


 
        
        return {'FINISHED'}
    

































































#register---------------------------------------------------------------------------------------------------------------

def register():
    bpy.utils.register_class(Felina)
    bpy.utils.register_class(CyclesRender)
    bpy.utils.register_class(EEVEERender)
    bpy.utils.register_class(TextTool)
    bpy.utils.register_class(WM_OT_textOp)
    bpy.utils.register_class(Mist_PT_main_panel)
    bpy.utils.register_class(Mist_OT_my_op)
    bpy.utils.register_class(Boosh_PT_main_panel)
    bpy.utils.register_class(Boosh_OT_my_op)
    
def unregister():
     bpy.utils.unregister_class(Felina)
     bpy.utils.unregister_class(CyclesRender)
     bpy.utils.unregister_class(EEVEERender)
     bpy.utils.unregister_class(TextTool)
     bpy.utils.unregister_class(WM_OT_textOp)
     bpy.utils.unregister_class(Mist_PT_main_panel)
     bpy.utils.unregister_class(Mist_OT_my_op)
     bpy.utils.unregister_class(Boosh_PT_main_panel)
     bpy.utils.unregister_class(Boosh_OT_my_op)
     
     
if __name__  == "__main__":
    register() 