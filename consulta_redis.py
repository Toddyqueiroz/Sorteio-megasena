import redis   
import json
import random
import datetime
import sys
from connect_redis import r
from megasena_redis import (
    consultar_por_numero,
    consultar_por_data,
    consultar_por_intervalo,
    consultar_por_intervalo_datas
)

def menu():
    print("\n🎯 MENU DE CONSULTAS")
    print("1 - Consultar por número do sorteio")
    print("2 - Consultar por data do sorteio")
    print("3 - Consultar por intervalo de números")
    print("4 - Consultar por intervalo de datas")
    print("0 - Sair")

def exibir_sorteio(sorteio):
    print(f"\n📅 Sorteio {sorteio['numero_sorteio']} - {sorteio['data']}")
    print(f"Números sorteados: {sorteio['numeros']}")
    print(f"Ganhadores: {sorteio['ganhadores']}")

def exibir_sorteios(lista_sorteios):
    if not lista_sorteios:
        print("❌ Nenhum sorteio encontrado.")
        return
    for sorteio in lista_sorteios:
        exibir_sorteio(sorteio)

def executar_consulta():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numero = int(input("Digite o número do sorteio: "))
            resultado = consultar_por_numero(numero)
            if resultado:
                exibir_sorteio(resultado)

        elif escolha == "2":
            data = input("Digite a data do sorteio (dd-mm-aaaa): ")
            resultado = consultar_por_data(data)
            if resultado:
                exibir_sorteio(resultado)

        elif escolha == "3":
            inicio = int(input("Digite o número do sorteio inicial: "))
            fim = int(input("Digite o número do sorteio final: "))
            resultados = consultar_por_intervalo(inicio, fim)
            exibir_sorteios(resultados)

        elif escolha == "4":
            data_inicio = input("Digite a data inicial (dd-mm-aaaa): ")
            data_fim = input("Digite a data final (dd-mm-aaaa): ")
            resultados = consultar_por_intervalo_datas(data_inicio, data_fim)
            exibir_sorteios(resultados)

        elif escolha == "0":
            print("👋 Encerrando consultas.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        executar_consulta()
    except KeyboardInterrupt:
        print("\n❌ Consulta interrompida pelo usuário.")
        sys.exit()