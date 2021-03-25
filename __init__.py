bl_info = {
    "name" : "Lazy Felina",
    "author" : "StandingPad Animations",
    "version" : (13, 0),
    "blender" : (2, 90, 0),
    "location" : "View3D > Toolbar > LazyFelina",
    "description" : "Shortcut stuff and be lazy. Felina is a reference to a species from Songs of War made by Black Plasma Studios, I highly recomend it",
    "warning" : "Beta Phase, so there may be some bugs",
    "wiki_url" : "https://sites.google.com/view/standingpadanimations/Development-Stuff/lazyfelina-wiki?authuser=0",
    "category" : "3D View and Be Lazy :D",    
}

import bpy
from . import addon_updater_ops
from . import LazyFelina
from . import Render
from . import volumetricassets
from . import Materials
from . import Skys
from . import QuickRenderOptions
from . import Comp
from . import TextTool




#Thing that does the process
def register():
    addon_updater_ops.register(bl_info)
    QuickRenderOptions.register(bl_info)
    LazyFelina.register(bl_info)
    TextTool.register(bl_info)
    Comp.register(bl_info)
    Skys.register(bl_info)
    Render.register(bl_info)
    volumetricassets.register(bl_info)
    Materials.register(bl_info)
    
    
    
    
   
        
    
        
def unregister():
    addon_updater_ops.unregister()
    LazyFelina.unregister()
    Render.unregister()
    volumetricassets.unregister()
    Materials.unregister()
    Skys.unregister()
    QuickRenderOptions.unregister()
    Comp.unregister()
    TextTool.unregister()

   

     
     
if __name__  == "__main__":
    register() 