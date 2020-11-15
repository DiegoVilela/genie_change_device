1. Reservar o ambiente de teste [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/756b58ba-15aa-4228-8a41-f94f684330e7?diagramType=Topology)

2. Acessar a VM no AWS<br>
```ssh -i ~/Downloads/jumpbox_to_cisco_sandbox.pem ubuntu@ec2-54-207-179-28.sa-east-1.compute.amazonaws.com```

3. Conectar ao Cisco Sandbox<br>
```sudo openconnect --no-dtls <devnetsandbox-server>```

4. Conectar ao Devbox no ambiente de testes da Cisco<br>
```ssh developer@10.10.20.50```

5. Salvar a configuração boa<br>
```genie learn config --testbed-file multi-platform-network.yaml --output good_config```

6. Clonar o repositório com o script de edição da configuração<br>
```git clone https://github.com/DiegoVilela/genie_change_device.git```

7. Salvar a configuração após a alteração<br>
```genie learn config --testbed-file multi-platform-network.yaml --output changed_config```

8. Verificar as diferenças<br>
```genie diff good_config/ changed_config/```
