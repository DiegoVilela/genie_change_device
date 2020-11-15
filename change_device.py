from genie.conf import Genie


print("Rodando script que aplica uma mudança de configuração ao device 'edge-sw01'.")
print("O device 'edge-sw01' está declarado no testbed-file.")

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

print("As mudanças foram aplicadas.")
print("Agora podemos compará-las com as configurações antigas.")
