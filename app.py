from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Route für die Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Socket.IO-Ereignis für das Senden der Position und Richtung
@socketio.on('update_position')
def handle_position(data):
    print(f'Position erhalten: {data}')
    # Sendet die Positionsdaten an alle verbundenen Clients
    socketio.emit('update_map', data, namespace='/')

if __name__ == '__main__':
    # socketio.run(app) wird nur lokal verwendet
    socketio.run(app, debug=false)  # Für die lokale Entwicklung
