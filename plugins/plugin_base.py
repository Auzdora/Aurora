from abc import ABC, abstractclassmethod
from typing import Dict

class BasePlugin:
    """Base class for all sub plugins
    """

    @abstractclassmethod
    def get_name(self) -> str:
        """return the name of the plugin
        """
        pass

    @abstractclassmethod
    def get_description(self) -> str:
        """return the description of the plugin
        """
        pass

    @abstractclassmethod
    def get_parameters(self) -> Dict:
        """return the dict parameters and descriptions
        """
        pass
    
    def format_function(self) -> Dict:
        function = {
            "name": self.get_name(),
            "description": self.get_description(),
            "parameters": self.get_parameters()
        }
        return function
    
    @abstractclassmethod
    def execute(self, **kwargs):
        """LLM return the corresponding parameters, and execute this plugin
        """
        pass
