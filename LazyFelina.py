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
    



#Class register
classes = [Felina, Update_PT_set]



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








    
    
    
    
    
    
    
    