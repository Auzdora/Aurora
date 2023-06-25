from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ChatMessage
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import json

from functions import *
from dump_data import DataDumper
from constants import *
from plugins import *
from typing import Dict

class SuperAgent:
    def __init__(self) -> None:
        print("AI system initializing ...")

        # register plugins
        self.plugins: Dict[str, BasePlugin]= {}
        self.register_plugin(VectorDBSearch())

        # system config
        self.configer = configer
        self.data_dumper = DataDumper(self.configer)
        self.vector_db = None
        if self.configer.config["system"]["vector_db"]["localized"] is True:
            self.vector_db = self.data_dumper.get_vector_db()

        # initialize chatgpt
        self.chatgpt = ChatOpenAI(model="gpt-3.5-turbo-0613", 
                 openai_api_key=OPENAI_API_KEY,
                 openai_api_base=OPENAI_API_BASE,
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()])
        
        self.SYSTEM_PROMPT = self.configer.config["system"]["prompt"]
    
    def register_plugin(self, plugin: BasePlugin):
        """register the plugin into agent
        """
        self.plugins[plugin.get_name()] = plugin

    def _get_functions(self):
        """return formatted function required by function calling
        """
        return [f.format_function() for f in self.plugins.values()]
    
    def _execute_plugins(self, user_input, respond):
        function_name = respond.additional_kwargs["function_call"]["name"]
        function_to_call = self.plugins[function_name]
        function_args = json.loads(respond.additional_kwargs["function_call"]["arguments"])

        function_answer = function_to_call.execute(**function_args)

        second_respond = self.chatgpt([HumanMessage(content=user_input),
                    AIMessage(content=str(respond)),
                    ChatMessage(role='function',
                                additional_kwargs={"name": function_name},
                                content=function_answer
                    )
        ])
        return


    def chat(self):
       """start conversation
       """
       while True:
            print("\n{}: ".format(self.configer.config["USER_NAME"]), end="")
            user_input = input()
            print("\n{}: ".format(self.configer.config["AI_NAME"]), end="")
            respond = self.chatgpt(
                [SystemMessage(content=self.SYSTEM_PROMPT),
                    HumanMessage(content=user_input)],
                functions=self._get_functions()
            )
            if user_input == "goodbye":
                break

            if respond.additional_kwargs:
                    self._execute_plugins(user_input, respond)
            print("")
        


