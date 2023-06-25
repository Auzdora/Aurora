import configer

configer = configer.ConfigLoader()
OPENAI_API_KEY = configer.get_api_key()
OPENAI_API_BASE = configer.get_api_base()