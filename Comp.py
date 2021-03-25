import bpy 
from bpy.types import Panel, Operator 

class Comp_PT_set(bpy.types.Panel):
    bl_label = "Compositing Shortcuts"
    bl_idname = "Comp_PT_felina"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 2
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='SHADERFX')
        
    
    
    
    def draw(self, context):
        layout = self.layout




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
    bl_parent_id = 'Comp_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='BOIDS')

    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        vl = scene.view_layers["View Layer"]
        
        
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")
            
        
            

        layout.operator("mist.myop_operator", icon= 'BOIDS')


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
    bl_parent_id = 'Comp_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='FORCE_BOID')
 

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        
        
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")
        
        
        
        

        layout.operator("boosh.myop_operator", icon= 'FORCE_BOID')


class Boosh_OT_my_op(Operator):
    bl_label = "Create Boosh"
    bl_idname = "boosh.myop_operator"
    
    def execute(self, context):
        
        
        
       
        self.report({'ERROR'}, "If you use Boosh in every render, please rethink doing so. Anyway, check Compositor, connect mist to map value and the image into the top input of MixRGB")
        
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        
       
        
        
        
        
        
        boosh_comp_action(context)
        
        
        
        
        
        
        vl.use_pass_mist = True
        camera.show_mist = True
        context.scene.use_nodes = True
        
        


 
        
        return {'FINISHED'}
    
#advance mist----------------------------------------------------------------------------------------------------------

def advancemist_comp_action(context):
    tree = context.scene.node_tree
    
    
    comp_node = tree.nodes.get
    mix_node = tree.nodes.new('CompositorNodeMixRGB')
    mix_node.location = (600, 0)
    mix_node.blend_type = 'SCREEN'
    
    mix2_node = tree.nodes.new('CompositorNodeMixRGB')
    mix2_node.location = (400, 200)
    
    
    map_node = tree.nodes.new('CompositorNodeMapValue')
    map_node.location = (25, 0)
    
    
    texture_node = tree.nodes.new('CompositorNodeTexture')
    texture_node.location = (150, -600)
    bpy.data.scenes["Scene"].node_tree.nodes["Texture"].texture = bpy.data.textures["AdvancedMistCloudsTexture"]
    
   
   
    
    link = tree.links.new
    
    link(map_node.outputs[0], mix_node.inputs[0])
    link(map_node.outputs[0], mix_node.inputs[0])
    link(mix2_node.outputs[0], mix_node.inputs[2])
    link(texture_node.outputs[1], mix2_node.inputs[0])
    

    
    return {'FINISHED'}




    

class AdvanceMist_PT_main_panel(Panel):
    bl_label = "Advance Mist"
    bl_idname = "AdvanceMist_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Comp_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='FORCE_FLUIDFLOW')
    
    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        
        
        layout.prop(world, "start")
        layout.prop(world, "depth")
        layout.prop(world, "falloff")
        

        layout.operator("advancemist.myop_operator", icon= 'FORCE_FLUIDFLOW')


class advanceMist_OT_my_op(Operator):
    bl_label = "Create Advance Mist"
    bl_idname = "advancemist.myop_operator"
    
    def execute(self, context):
        
        
        
        self.report({'INFO'}, "Check Compositor, connect mist to map value and the image into the top input of screen MixRGB.")
        
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        bpy.ops.texture.new()
        bpy.data.textures["Texture"].name = "AdvancedMistCloudsTexture"
        bpy.data.textures["AdvancedMistCloudsTexture"].type = 'CLOUDS'
        



        advancemist_comp_action(context)
        
    
        vl.use_pass_mist = True
        camera.show_mist = True
        context.scene.use_nodes = True
    
        return {'FINISHED'}
    


#sunbeams--------------------------------------------------------------------------------------------------------------

def sunbeams_comp_action(context):
    tree = context.scene.node_tree
    
    
    comp_node = tree.nodes.get
    mix_node = tree.nodes.new('CompositorNodeMixRGB')
    mix_node.location = (1500, 0)
    mix_node.blend_type = 'ADD'
    
    mix2_node = tree.nodes.new('CompositorNodeMixRGB')
    mix2_node.location = (1000, 200)
    
    sunbeams_node = tree.nodes.new('CompositorNodeSunBeams')
    sunbeams_node.location = (200, -200)
    
    
    blur_node = tree.nodes.new('CompositorNodeBlur')
    blur_node.location = (600, 100)
    
    

   
   
    
    link = tree.links.new
    link(sunbeams_node.outputs[0], blur_node.inputs[0])
    link(blur_node.outputs[0], mix2_node.inputs[0])
    link(mix2_node.outputs[0], mix_node.inputs[1])
    
   
    
    

    
    return {'FINISHED'}




    

class SunBeams_PT_main_panel(Panel):
    bl_label = "Sunbeams"
    bl_idname = "SunBeams_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Comp_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='GP_MULTIFRAME_EDITING')
    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        world = scene.world.mist_settings
        
         
        

        layout.operator("sunbeams.myop_operator", icon= 'GP_MULTIFRAME_EDITING')


class SunBeams_OT_my_op(Operator):
    bl_label = "Create SunBeams"
    bl_idname = "sunbeams.myop_operator"
    
    def execute(self, context):
        
        
        
        self.report({'INFO'}, "Check Compositor, connect the image in both the mix and add nodes. Connect the enviroment pass in the sun beams node.")
        
        scene = context.scene
        camera = bpy.data.cameras['Camera']
        vl = scene.view_layers["View Layer"]
        
       
        
        
        
        
        
        sunbeams_comp_action(context)
        context.scene.use_nodes = True
        vl.use_pass_environment = True
        
        return {'FINISHED'}
    

class WM_OT_compop(bpy.types.Operator):
    
    bl_label = "Compositing Options"
    bl_idname = "wm.compop"  
    
    
    
    #the dialog box options 
    
    
    
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.operator("mist.myop_operator", icon= 'BOIDS')
        row = box.row()
        row.operator("boosh.myop_operator", icon= 'FORCE_BOID')
        row = box.row()
        row.operator("advancemist.myop_operator", icon= 'FORCE_FLUIDFLOW')
        row = box.row()
        row.operator("sunbeams.myop_operator", icon= 'GP_MULTIFRAME_EDITING')

        
    

   
    
    def execute(self, context):
         

        return {'FINISHED'}
    
    
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    
#keymaps---------------------------------------------------------------------------------------------------------------

#DO NOT MESS WITH 

addon_keymaps = []


classes = [Comp_PT_set,Mist_PT_main_panel, Mist_OT_my_op, Boosh_PT_main_panel, Boosh_OT_my_op, AdvanceMist_PT_main_panel, advanceMist_OT_my_op, SunBeams_PT_main_panel, SunBeams_OT_my_op, WM_OT_compop]



#Thing that does the process
def register(bl_info):
    
#class register
    for cls in classes:
        bpy.utils.register_class(cls)
        
       
        
    wm = bpy.context.window_manager 
    kc = wm.keyconfigs.addon
    
    if kc:
        km2 = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi2 = km2.keymap_items.new("wm.compop", type= 'F' and 'C', value= 'PRESS', shift= True)
        
        addon_keymaps.append((km2, kmi2))
        
    
        
def unregister():
#class unregister
    for cls in classes:
        bpy.utils.unregister_class(cls) 
        
    
    for km2,kmi2 in addon_keymaps:
        km2.keymap_items.remove(kmi2)
    addon_keymaps.clear()

     
     
if __name__  == "__main__":
    register() 
