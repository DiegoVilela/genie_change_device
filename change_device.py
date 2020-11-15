from genie.conf import Genie


print("Running script that applies a configuration change to device 'edge-sw01'.")
print("The device 'edge-sw01' is defined in the testbed-file.")

# Carrega o testebed com todos os devices
testbed = Genie.init('multi-platform-network.yaml')

# Conecta ao device 'edge-sw01'
device = 'edge-sw01'
testbed.devices[device].connect(log_stdout=False)

# Aplica a mudança de configuração
testbed.devices[device].configure(
    [
        "interface Loopback799",
        "description Nova Interface Criada Via Script"
    ]
)

# Desconecta
testbed.devices[device].disconnect()

print("Changes applied.")
print("We can now compare the current configuration against the previous one.")
