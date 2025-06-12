# 🔢 MegaSena Redis

Este projeto simula sorteios fictícios da Mega-Sena, armazenando e consultando os dados em um banco Redis. Ideal para fins didáticos.

---

## 🚨 RECOMENDAÇÕES IMPORTANTES

1. No arquivo `connect_redis.py`, configure corretamente suas credenciais do Redis Cloud. **Se não fizer isso, o sistema não funcionará!**
2. As consultas só funcionarão se os sorteios já tiverem sido gerados. Execute primeiro o script `megasena_redis.py`.
3. Ordem recomendada para rodar o programa:

```
1 - test_connection_redis.py  
2 - limpeza_redis.py  
3 - megasena_redis.py  
4 - consulta_redis.py  
```

Executar `consulta_redis.py` antes de `megasena_redis.py` resultará em erro por falta de dados.

---

## 📁 O QUE CADA ARQUIVO FAZ?

- `connect_redis.py` → Arquivo de configuração. Insira suas credenciais aqui para conectar com o Redis.
- `megasena_redis.py` → Gera os sorteios e salva no banco (somente quartas e sábados).
- `test_connection_redis.py` → Testa se a conexão com o Redis está funcionando corretamente.
- `limpeza_redis.py` → Apaga todos os sorteios salvos no banco. Útil em caso de dados corrompidos ou duplicados.
- `consulta_redis.py` → Menu interativo com opções de consulta por número, data, intervalo de números ou intervalo de datas.

---

## 🧠 COMO FUNCIONA O BANCO REDIS AQUI?

O sistema cria dois grupos de chaves:

- `sorteio:{numero}` → Contém os dados completos de um sorteio (data, números, ganhadores).
- `data:{dd-mm-aaaa}` → Contém apenas o número do sorteio daquela data.

Isso permite buscas eficientes tanto por número quanto por data.

---

## 🛠️ ETAPAS PARA EXECUTAR O PROJETO

### 1️⃣ Criar uma conta e banco no Redis Cloud

1. Acesse: https://redis.io/try-free/
2. Crie uma conta e entre no painel.
3. Clique em **Create Database** e escolha:
   - Um nome para o banco
   - Um provedor (AWS, Google Cloud etc.)
   - A região mais próxima
   - **Tipo**: Redis Stack
4. Pronto! Seu banco está criado.

---

### 2️⃣ Obter suas credenciais do Redis

1. No painel, vá na aba **Databases** e clique em **Connect** no banco que você criou.
2. Selecione a aba **Redis Client** e depois **Python**.
3. Copie os seguintes dados:

```python
host='seu_host_aqui',
port=seu_port,
username="default",
password="sua_senha",
decode_responses=True
```

4. Cole no arquivo `connect_redis.py` nos locais indicados.

---

### 3️⃣ Instalar as dependências

Você pode rodar o projeto pelo VSCode ou CMD.

#### 💻 Pelo VSCode

- Abra o terminal → Selecione "Split Terminal" ou use `Ctrl + Shift + '`
- Execute:

```bash
pip install redis
pip install python-dotenv
```

- Aparecerá uma pasta `venv` no projeto indicando sucesso.

#### 🖥️ Pelo CMD

- Abra o CMD como administrador
- Navegue até a pasta do projeto:

```bash
cd C:\caminho\do\seu\projeto
```

- Execute:

```bash
pip install redis
pip install python-dotenv
```

- Pronto, dependências instaladas.

---

### 4️⃣ Rodar o programa

1. Ative o ambiente virtual:

```bash
.\venv\Scripts\activate
```

2. Execute os arquivos na ordem recomendada:

```bash
python test_connection_redis.py
python limpeza_redis.py
python megasena_redis.py
python consulta_redis.py
```

---


🚀 Projeto feito para aprendizado com Redis e Python!