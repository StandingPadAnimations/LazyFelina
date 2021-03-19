# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy
import os 
from bpy.types import Panel, Operator
from . import addon_updater_ops 


#main panels
class Felina(bpy.types.Panel):
    bl_label = "LazyFelina"
    bl_idname = "Lazy_PT_felina"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='GRAPH')
    
    
    def draw(self, context):
        layout = self.layout
        addon_updater_ops.check_for_update_background()
        addon_updater_ops.update_notice_box_ui(self, context)
        
        
        
        
class Comp_PT_set(bpy.types.Panel):
    bl_label = "Compositing Shortcuts"
    bl_idname = "Comp_PT_felina"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='SHADERFX')
    
    
    def draw(self, context):
        layout = self.layout
    
class Update_PT_set(bpy.types.AddonPreferences):
    
    bl_idname = __package__
    
    auto_check_update = bpy.props.BoolProperty(
    name = "Auto-check for Update",
    description = "If enabled, auto-check for updates using an interval",
    default = True,
    )

    updater_intrval_months = bpy.props.IntProperty(
        name='Months',
        description = "Number of months between checking for updates",
        default=0,
        min=0
    )
    updater_intrval_days = bpy.props.IntProperty(
        name='Days',
        description = "Number of days between checking for updates",
        default=1,
        min=0,
    )
    updater_intrval_hours = bpy.props.IntProperty(
        name='Hours',
        description = "Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_intrval_minutes = bpy.props.IntProperty(
        name='Minutes',
        description = "Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )
    
    def draw(self, context):
        layout = self.layout 
        addon_updater_ops.update_settings_ui(self, context)
    
#render settings---------------------------------------------------------------------------------------------------  
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
            

#text panel--------------------------------------------------------------------------------------------------------        
        
#Dialog box name, icon, and button name thingy
class TextTool(bpy.types.Panel):
    bl_label = "TextTool"
    bl_idname = "OBJECT_PT_text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='FONTPREVIEW')
    
    
    def draw(self, context):
        layout = self.layout
     
        
        row = layout.row()
        row.operator("wm.textop", text= "TextTool", icon= 'FILE_FONT')
        
        
        
        
        
#dialog box operator         
class WM_OT_textOp(bpy.types.Operator):
    
    bl_label = "LazyFelina TextTool"
    bl_idname = "wm.textop"  
    
    
    
    #the dialog box options 
    text = bpy.props.StringProperty(name= "Enter Text")
    font_file = bpy.props.StringProperty(name= "Font")
    center = bpy.props.BoolProperty(name= "Center Origin", default= False)
    extrude = bpy.props.BoolProperty(name= "Extrude", default= False)
    extrude_amount = bpy.props.FloatProperty(name= "Extrude Amount:", default= 0)
    
    
    
    def draw(self, context):
        layout = self.layout

        layout.prop(self, "text")
        layout.separator(factor= 1)
        
        box = layout.box()
        
        row = box.row()
        row.prop(self, "center")
        
        if self.center == True:
            row.label(text= "Origin: Centered", icon= 'PIVOT_CURSOR')
            
        elif self.center == False:
            row.label(text= "Origin: Default", icon= 'CURSOR')
        
        row = box.row()
        row.prop(self, "extrude")
        
        if self.extrude == True:
            box.prop(self, "extrude_amount")
            row.label(text= "Can Extrude", icon= 'EDITMODE_HLT')
            
        elif self.extrude == False:
            row.label(text= "Can't Extrude", icon= 'OBJECT_DATAMODE')
    

   
    
    def execute(self, context):
        
        t = self.text
        c = self.center
        e = self.extrude
        ea = self.extrude_amount
        
        
        #How the tool creates text and does other actions
        bpy.ops.object.text_add(enter_editmode=True, scale=(1, 1, 1))
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text= t)
        bpy.ops.object.editmode_toggle()
        
        #how the dialog box resets
        self.text = ''
        self.extrude = False
        self.center = False
        self.extrude_amount = 0
        
        
        
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
    
#sky--------------------------------------------------------------------------------------------------------------
class Sky_PT_main_panel(Panel):
    bl_label = "Sky"
    bl_idname = "Sky_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lazy Felina"
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    
    
    
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='LIGHT_SUN')

    
    def draw(self, context):
        layout = self.layout
        engine = bpy.context.scene.render.engine
        
        if engine == 'CYCLES':
            layout.operator("sky.myop_operator", icon= 'LIGHT_SUN')
            
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
        
        
        return {'FINISHED'}











    
    
    
    
    
    
    
    