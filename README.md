# BHoundS

BHoundS é um script de sniffing que automatiza o processo do arpspoof. 

Para utiliza-lo é necessário ter o arpspoof instalado na sua distribuição Linux e estar na mesma interace de rede do alvo.

Script testado no Kali, onde já tem todos os programas necessários instalado.


### Preparação do ambiente


identificar o gateway

```sh
$ route -n
```
identificar o alvo na rede

```sh
$ sudo nmap X.X.X.0/24
```

iniciar o script

```sh
$ sudo ./bhounds.py
```
