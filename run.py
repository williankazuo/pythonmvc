from app import app
import config

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.DEFAULT_SERVICE_URI, port=config.DEFAULT_SERVICE_PORT)
