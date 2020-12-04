bl_info = {
    "name" : "Lazy Felina",
    "author" : "StandingPad Animations",
    "version" : (1, 0),
    "blender" : (2, 91, 0),
    "location" : "View3D > Toolbar > Add Object",
    "description" : "Shortcut stuff and be lazy. Felina is a reference to a species from Songs of War made by Black Plasma Studios, I highly recomend it",
    "warning" : "Beta Phase, so there may be some bugs and not all features are added",
    "wiki_url" : "",
    "category" : "",    
}

import bpy

#render settings

class Felina(bpy.types.Panel):
    bl_label = "LazyFelina"
    bl_idname = "Lazy"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    
    
    
    
    def draw(self, context):
        
        
        layout = self.layout
        render = bpy.context.scene.cycles
        renderview = bpy.context.scene.cycles
        erender = bpy.context.scene.eevee
        erenderview = bpy.context.scene.eevee




        row = layout.row()
        row.label(text= "Cycles Render Settings", icon= 'RESTRICT_RENDER_OFF')
        row = layout.row()
        row.label(text= "Render")
        layout.prop(render, "samples")
        row = layout.row()
        row.label(text= "Viewport")
        layout.prop(renderview, "preview_samples")
        
        
        row = layout.row()
        row.label(text= "EEVEE Render Settings", icon= 'BLENDER')
        row = layout.row()
        row.label(text= "Render")
        layout.prop(erender, "taa_render_samples")
        row = layout.row()
        row.label(text= "Viewport")
        layout.prop(erenderview, "taa_samples")
        



#text panel        
        
class TextPanel(bpy.types.Panel):
    
    bl_label = "Text Tool"
    bl_idname = "text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy'
    bl_options = {'DEFAULT_CLOSED'}
   
    

    def draw(self, context):
        layout = self.layout

       
        row = layout.row()
        row.operator("wm.textop", text= "Add Text", icon= 'FILE_FONT')


class WM_OT_textOp(bpy.types.Operator):
    
    bl_label = "Text Tool Operator"
    bl_idname = "wm.textop"
    
    text = bpy.props.StringProperty(name= "Enter Text:")
    scale = bpy.props.FloatProperty(name= "Scale:", default= 1)
    center = bpy.props.BoolProperty(name= "Center Origin", defult= False)
    extrude = bpy.props.BoolProperty(name= "Extrude", defult= False)
    extrude_amount = bpy.props.FloatProperty(name= "Extrude Amount:", default= 0.06)
    
    def execute(self, context):
        
        t = self.text
        s = self.scale
        c = self.center
        e = self.extrude
        ea = self.extrude_amount
        
        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text= t)
        bpy.ops.object.editmode_toggle()
        
        
        if e == True:
            bpy.context.object.data.extrude = ea

        
        
        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'





        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    
        
        









#register

def register():
    bpy.utils.register_class(Felina)
    bpy.utils.register_class(TextPanel)
    bpy.utils.register_class(WM_OT_textOp)
    
def unregister():
     bpy.utils.unregister_class(Felina)
     bpy.utils.unregister_class(TextPanel)
     bpy.utils.unregister_class(WM_OT_textOp)
     
     
if __name__  == "__main__":
    register() 