import redis
from connect_redis import r

try:
    
    print("PING:", r.ping())
    

except redis.exceptions.ConnectionError as e:
    print("Erro de conexão:", e)