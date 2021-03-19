bl_info = {
    "name" : "Lazy Felina",
    "author" : "StandingPad Animations",
    "version" : (12, 0, 1),
    "blender" : (2, 90, 0),
    "location" : "View3D > Toolbar > LazyFelina",
    "description" : "Shortcut stuff and be lazy. Felina is a reference to a species from Songs of War made by Black Plasma Studios, I highly recomend it",
    "warning" : "Beta Phase, so there may be some bugs",
    "wiki_url" : "https://sites.google.com/view/standingpadanimations/Development-Stuff/lazyfelina-wiki?authuser=0",
    "category" : "3D View and Be Lazy :D",    
}

import bpy
from . import addon_updater_ops
from . LazyFelina import Felina, Render_PT_UI, TextTool, WM_OT_textOp, Comp_PT_set, Mist_PT_main_panel, Mist_OT_my_op, Boosh_PT_main_panel, Boosh_OT_my_op, AdvanceMist_PT_main_panel, advanceMist_OT_my_op, SunBeams_PT_main_panel, SunBeams_OT_my_op, Sky_PT_main_panel, Sky_OT_my_op
from . Render import optimizeGPU_OT_my_op, optimizeCPU_OT_my_op, optimize_PT_main_panel, switchoptimizeCPU_OT_my_op, switchoptimizeGPU_OT_my_op, enableGPU_OT_my_op
from . volumetricassets import vol_PT_add, vol_OT_ray, vol_OT_cube, vol_OT_cloud, vol_OT_mist, vol_OT_aurora, vortex_OT_is_epic


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
        

#keymaps---------------------------------------------------------------------------------------------------------------

#DO NOT MESS WITH 

addon_keymaps = []



#register--------------------------------------------------------------------------------------------------------------


#Class register
classes = [Felina, Update_PT_set, Render_PT_UI, TextTool, WM_OT_textOp, Comp_PT_set, Mist_PT_main_panel, Mist_OT_my_op, Boosh_PT_main_panel, Boosh_OT_my_op, AdvanceMist_PT_main_panel, advanceMist_OT_my_op, SunBeams_PT_main_panel, SunBeams_OT_my_op, Sky_PT_main_panel, Sky_OT_my_op, optimizeGPU_OT_my_op,optimizeCPU_OT_my_op, optimize_PT_main_panel, switchoptimizeCPU_OT_my_op, switchoptimizeGPU_OT_my_op, enableGPU_OT_my_op, vol_PT_add, vol_OT_ray, vol_OT_cube, vol_OT_cloud, vol_OT_mist, vol_OT_aurora, vortex_OT_is_epic]



#Thing that does the process
def register():
    
#class register
    addon_updater_ops.register(bl_info)
    for cls in classes:
        bpy.utils.register_class(cls)
        
       
        
    wm = bpy.context.window_manager 
    kc = wm.keyconfigs.addon
    
    if kc:
        km = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi = km.keymap_items.new("wm.textop", type= 'F', value= 'PRESS', shift= True)
        
        addon_keymaps.append((km, kmi))
        
    
        
def unregister():
    addon_updater_ops.unregister(bl_info)
#class unregister
    for cls in classes:
        bpy.utils.unregister_class(cls) 
        
        
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

     
     
if __name__  == "__main__":
    register() 