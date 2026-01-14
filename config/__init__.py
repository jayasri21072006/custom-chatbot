import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AppConfig:
    """Class to handle application configuration for TNPSC Guru."""
    
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from config.yaml and inject env variables."""
        # Use absolute path to ensure config is found even when running from root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'config', 'config.yaml')
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Inject API keys from environment variables
        if 'api' not in config:
            config['api'] = {}
        
        # Primary API keys for Group 4 Guru logic
        config['api']['groq_key'] = os.getenv('API_KEY')
        config['api']['tavily_key'] = os.getenv('TAVILY_API_KEY')
        
        return config

# Create a single instance to be used by the app
app_config_instance = AppConfig()
config = app_config_instance.config

# Easy access variables for your other modules
GROQ_API_KEY = config['api'].get('groq_key')
TAVILY_API_KEY = config['api'].get('tavily_key')