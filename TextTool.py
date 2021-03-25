import bpy 
from bpy.types import Panel, Operator

class TextTool(Panel):
    bl_label = "TextTool"
    bl_idname = "OBJECT_PT_text"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lazy Felina'
    bl_parent_id = 'Lazy_PT_felina'
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 3
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='FONTPREVIEW')
    
    
    def draw(self, context):
        layout = self.layout
     
        
        row = layout.row()
        row.operator("wm.textop", text= "TextTool", icon= 'FILE_FONT')
        
        
        
        
        
#dialog box operator         
class WM_OT_textOp(Operator):
    
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
    
    
#keymaps---------------------------------------------------------------------------------------------------------------

#DO NOT MESS WITH 

addon_keymaps = []



#register--------------------------------------------------------------------------------------------------------------


#Class register
classes = [TextTool, WM_OT_textOp]


#Thing that does the process
def register(bl_info):
    
#class register
    for cls in classes:
        bpy.utils.register_class(cls)
        
       
        
    wm = bpy.context.window_manager 
    kc = wm.keyconfigs.addon
    
    if kc:
        km = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi = km.keymap_items.new("wm.textop", type= 'F' and 'T', value= 'PRESS', shift= True)
       
        addon_keymaps.append((km, kmi))
        
        
    
        
def unregister():
#class unregister
    for cls in classes:
        bpy.utils.unregister_class(cls) 
        
        
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

     
if __name__  == "__main__":
    register() 