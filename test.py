import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples
import_file_name = examples.download_file('mixing_elbow.pmdb',
'pyfluent/mixing_elbow')
meshing = pyfluent.launch_fluent(
mode="meshing",
precision=pyfluent.Precision.DOUBLE,
processor_count=2
)
wt = meshing.watertight()
wt.import_geometry.file_name.set_state(
import_file_name)
wt.import_geometry.length_unit.set_state('in')
wt.import_geometry()

wt.add_local_sizing.add_child_to_task()
wt.add_local_sizing()