import bpy

class RpjPanelMixin():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RPJ"

class RpjPanel(RpjPanelMixin, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_RPJ"
    bl_label = "RPJ"

    def draw(self, context):
        self.layout.label(text="RPJ works")

bpy.utils.register_class(RpjPanel)

def register(): ...


def unregister(): ...
