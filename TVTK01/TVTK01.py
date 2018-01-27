from tvtk.api import tvtk
from tvtk.common import configure_input
from Tvtkfunc import ivtk_scene, event_loop
def read_data():
    plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name="combxyz.bin",
    q_file_name="combq.bin",
    scalar_function_number=100,
    vector_function_number=200
    )
    plot3d.update()
    return plot3d

plot3d = read_data()
grid = plot3d.output.get_block(0)

outline = tvtk.StructuredGridOutlineFilter()
configure_input(outline, grid)

m = tvtk.PolyDataMapper(input_connection=outline.output_port)
a = tvtk.Actor(mapper=m)
a.property.color = 0.3, 0.3, 0.3
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
