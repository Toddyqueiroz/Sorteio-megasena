import redis   
import json
import random
import datetime
from time import sleep
from connect_redis import r

def gerar_datas(inicio, fim):
    """Gera todas as quartas e sábados entre as datas inicio e fim."""
    datas = []
    dia = inicio
    while dia <= fim:
        if dia.weekday() in [2, 5]:  # 2 = quarta, 5 = sábado
            datas.append(dia)
        dia += datetime.timedelta(days=1)
    print(f"📅 Total de datas geradas: {len(datas)}")
    return datas

def gerar_sorteio(numero_sorteio, data):
    numeros = random.sample(range(1, 61), 6)
    ganhadores = random.randint(0, 20)
    sorteio = {
        "numero_sorteio": numero_sorteio,
        "data": data.strftime("%d-%m-%Y"),
        "numeros": numeros,
        "ganhadores": ganhadores
    }
    print(f"🎲 Sorteio {numero_sorteio} gerado para {sorteio['data']}: {numeros} - Ganhadores: {ganhadores}")
    return sorteio

def salvar_sorteio(sorteio):
    chave = f"sorteio:{sorteio['numero_sorteio']}"
    chave_data = f"data:{sorteio['data']}"
    # Verifica se já existe antes de salvar
    if r.exists(chave) or r.exists(chave_data):
        print(f"⚠️ Sorteio {sorteio['numero_sorteio']} ou data {sorteio['data']} já existe no banco. Pulando...")
        return False
    r.set(chave, json.dumps(sorteio))
    r.set(chave_data, sorteio['numero_sorteio'])
    print(f"✅ Sorteio {sorteio['numero_sorteio']} salvo com sucesso.")
    return True


#funcao que consulta por um unico numero de sorteio
def consultar_por_numero(numero):
    chave = f"sorteio:{numero}"
    dados = r.get(chave)
    if dados:
        sorteio = json.loads(dados)
        return sorteio
    else:
        print(f"❌ Sorteio {numero} não encontrado.")
    return None


#funcao que consulta por data unica no formato dd-mm-yyyy
def consultar_por_data(data_str):
    numero = r.get(f"data:{data_str}")
    if numero:
        return consultar_por_numero(numero)
    else:
        print(f"❌ Nenhum sorteio encontrado para a data {data_str}.")
    return None


#funcao que consulta todos os sorteios entre os numeros de sorteio, ex: entre 1 e 10
def consultar_por_intervalo(num_inicial, num_final):
    chaves = [f"sorteio:{num}" for num in range(num_inicial, num_final + 1)]
    dados = r.mget(chaves)
    resultados = []
    for d in dados:
        if d:
            resultados.append(json.loads(d))
    print(f"🔢 Consulta por intervalo {num_inicial} a {num_final}: {len(resultados)} sorteios encontrados.")
    return resultados


#funcao que consulta todos os sorteios entre duas datas no formato dd-mm-yyyy
def consultar_por_intervalo_datas(data_inicial_str, data_final_str):
    data_inicial = datetime.datetime.strptime(data_inicial_str, "%d-%m-%Y").date()
    data_final = datetime.datetime.strptime(data_final_str, "%d-%m-%Y").date()
    
    if data_inicial > data_final:
        print("❌ Data inicial é posterior à data final.")
        return []

    resultados = []
    dia = data_inicial
    while dia <= data_final:
        chave_data = f"data:{dia.strftime('%d-%m-%Y')}"
        numero = r.get(chave_data)
        if numero:
            sorteio = consultar_por_numero(numero)
            if sorteio:
                resultados.append(sorteio)
        dia += datetime.timedelta(days=1)

    print(f"📅 Consulta de datas entre {data_inicial_str} e {data_final_str}: {len(resultados)} sorteios encontrados.")
    return resultados



if __name__ == "__main__":
    inicio = datetime.date(1999, 10, 10)
    fim = datetime.date.today()
    
    datas = gerar_datas(inicio, fim)
    
    print(f"🚀 Iniciando geração e salvamento dos sorteios... isso pode demorar um pouco...")

    for i, data in enumerate(datas, start=1):
        if not r.exists(f"sorteio:{i}") and not r.exists(f"data:{data.strftime('%d-%m-%Y')}"):
            sorteio = gerar_sorteio(i, data)
            salvar_sorteio(sorteio)
            if i % 50 == 0:
                print(f"⏳ Já foram salvos {i} sorteios...")
                sleep(0.1)  # Pequena pausa pra evitar sobrecarga
        else:
            print(f"⏭️ Sorteio {i} ou data {data.strftime('%d-%m-%Y')} já existe. Ignorando.")

    print("🎉 Tudo salvo com sucesso! Fim do processo.")
