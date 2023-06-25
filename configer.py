import json

class ConfigLoader:
    def __init__(self, config_path="./"):
        self.config_path = config_path + "config.json"
        self.config = self.read()
    
    def read(self) -> dict:
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        return config
    
    def write(self) -> None:
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def get_api_key(self) -> str:
        return self.config["OPEN_AI_API"]
    
    def get_api_base(self) -> str:
        return self.config["OPEN_AI_BASE"]


if __name__ == "__main__":
    from plugins import VectorDBSearch
    Ve = VectorDBSearch()
    loader = ConfigLoader()
    print(loader.get_api_key())