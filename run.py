from app import create_app
from app.views import *
from config import DevelopmentConfig

if __name__ == "__main__":
    config_object = DevelopmentConfig()
    
    app = create_app(config_object)
    app.run(debug=True)
