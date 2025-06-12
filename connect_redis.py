import redis



# edite aqui as suas credenciais do banco de dados redis
pool = redis.ConnectionPool(
# somente editar entre as linhas comentadas abaixo pra configurar a sua conexao com o redis.
# ---------------------------------------------

    host='host aqui',
    port= porta aqui, #esta com erro porque ele espera um numero, apos colocar o numero da porta do seu banco de dados vai funcionar.
    decode_responses=True,
    username="username aqui",
    password="password aqui",

# ---------------------------------------------
)

r = redis.Redis(connection_pool=pool)