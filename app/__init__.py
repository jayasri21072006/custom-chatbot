from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import CustomLogger 
from .api_client import GroqClient 

# Load environment variables
load_dotenv()

class AppConfig:
    """Class to handle application configuration."""
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from config.yaml and inject secret keys."""
        config_path = os.path.join(os.getcwd(), 'config', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        if 'api' not in config:
            config['api'] = {}
            
        config['api']['groq_key'] = os.getenv('API_KEY')
        config['api']['tavily_key'] = os.getenv('TAVILY_API_KEY')
        
        return config

def create_app():
    """Create and configure the Flask application."""
    # MODIFICATION: Changed template_folder to 'templates' (relative to this file)
    # and fixed static_folder path.
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')

    # 1. Load configuration
    app_config = AppConfig()
    app.config.update(app_config.config)

    # 2. Set up logging
    logger = CustomLogger().get_logger()
    logger.info("TNPSC Guru Bot is starting up...")

    # 3. Initialize the RAG Client
    app.guru_bot = GroqClient()

    # 4. Import and register routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app