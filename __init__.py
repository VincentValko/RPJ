import bpy
from . import fog

class RpjPanelMixin():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RPJ"

class RpjFogPanel(RpjPanelMixin, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_RPJ"
    bl_label = "Fog"

    def draw(self, context):
        self.layout.label(text="RPJ works")

bpy.utils.register_class(RpjFogPanel)

def register(): ...


def unregister(): ...
