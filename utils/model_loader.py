import os
from dotenv import load_dotenv
from typing import litral, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI




class ConfigLoader:
    def __init__(self):
        print(f"Loded config...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config:Optional[ConfigLoader] = Field (default = None, exclude = True)

    def model_post_init(self, __context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """load and return the LLM model."""

        print("Loading LLM model...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            # Load Groq model
            print("Groq model loaded.")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            # Load OpenAI model
            print("OpenAI model loaded.")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name = "o4-mini", api_key= openai_api_key)
        else:
            raise ValueError(f"Unsupported model provider: {self.model_provider}")
        
        return llm
    def __init__(self, config):
        self.config = config

    def load_model(self):
        pass