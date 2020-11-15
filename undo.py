from genie.conf import Genie


print("Running script to undo the previous change.")
print("The device 'edge-sw01' is defined in the testbed-file.")

# Carrega o testebed com todos os devices
testbed = Genie.init('multi-platform-network.yaml')

# Conecta ao device 'edge-sw01'
device = 'edge-sw01'
testbed.devices[device].connect(log_stdout=False)

# Aplica a mudança de configuração
testbed.devices[device].configure(
    [
        "no interface Loopback799"
    ]
)

# Desconecta
testbed.devices[device].disconnect()

print("Changes undone.")
