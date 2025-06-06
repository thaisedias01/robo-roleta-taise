from flask import Flask, render_template
from flask_socketio import SocketIO
from collections import Counter
import time
import threading

app = Flask(_name_)
socketio = SocketIO(app)

historico = [3, 5, 7, 3, 12, 3, 5, 7, 20]

def calcular_numero_mais_frequente():
    contagem = Counter(historico)
    numero, _ = contagem.most_common(1)[0]
    return numero

def enviar_previsao_periodicamente():
    while True:
        numero = calcular_numero_mais_frequente()
        socketio.emit('nova_previsao', {'numero': numero})
        time.sleep(16)

@app.route('/')
def index():
    return render_template('index.html')

if _name_ == '_main_':
    thread = threading.Thread(target=enviar_previsao_periodicamente)
    thread.daemon = True
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)