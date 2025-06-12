import redis
from connect_redis import r

# essa funcao vai apagar todos os dados existente, garantindo que nao haja dados duplicados e gere erro nas consultas.
def limpar_todas_as_chaves():
    try:
        padroes = ["sorteio:*", "data:*"]
        total_deletados = 0

        for padrao in padroes:
            for chave in r.scan_iter(padrao, count=100):
                r.delete(chave)
                print(f"🧹 Deletado: {chave.decode() if isinstance(chave, bytes) else chave}")
                total_deletados += 1

        print(f"\n✅ Limpeza concluída. Total de chaves apagadas: {total_deletados}")
    except redis.exceptions.ConnectionError as e:
        print("❌ Erro de conexão com Redis:", e)
    

if __name__ == "__main__":
    limpar_todas_as_chaves()

#r.close()  # Fecha a conexão com o Redis e libera a conexao novamente para o proximo uso.