from qiskit import QuantumCircuit, pulse
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_dynamics import Solver, DynamicsBackend
from qiskit_dynamics.backend import default_experiment_result_function
from qiskit_dynamics.array import Array
from qiskit.providers.fake_provider import *
import jax
from qiskit import Aer, IBMQ, QuantumCircuit, execute
from qiskit.visualization import plot_histogram

gate_backend = FakeManila()
gate_backend.configuration().hamiltonian['qub'] = {'0': 2,'1': 2,'2': 2,'3': 2,'4': 2}
jax.config.update("jax_enable_x64", True)
jax.config.update("jax_platform_name", "cpu")
Array.set_default_backend("jax")
pulse_backend = DynamicsBackend.from_backend(gate_backend, evaluation_mode="sparse")
solver_options = {"method": "jax_odeint", "atol": 1e-6, "rtol": 1e-8}
pulse_backend.set_options(solver_options=solver_options)
pulse_backend.configuration = lambda: gate_backend.configuration()
from PIL import Image

qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.measure_all()

#Misura da gate

job = execute(qc, backend=gate_backend, shots=1024)
Gresults = job.result()
Gcounts = Gresults.get_counts()
print('Misure circuito "gate": ',Gcounts)

with pulse.build(gate_backend) as pulse_test:
    pulse.call(qc)

#Misure da impulsi

Presults = pulse_backend.run(pulse_test).result()
Pcounts = Presults.get_counts()
print('Misure circuito "impulsi"',Pcounts)

legend = ['Gate', 'Impulsi']
plot_histogram([Gcounts,Pcounts],legend=legend).savefig('out.png')
img = Image.open('out.png')
img.show()

