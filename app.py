from app import app,socketio
if __name__ == '__main__':
    socketio.run(app, port=5000, use_reloader=False, debug=True)