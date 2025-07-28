from flask import Flask
from redis import Redis

app = Flask(__name__)
# O nome 'redis' aqui é crucial! É o nome do nosso outro serviço no Docker Compose.
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Ola! Esta pagina foi visitada {count} vezes.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
