# File Imports
from core import retriever
from utils.utils import Logger
from utils import config, constants

# Library Imports
import os
import time
from langchain_huggingface import HuggingFaceEndpoint



'''
!Docstring
- This module handles the language generation part.
- Functionalities include:
    - Integration with LLMs.
    - Functions to format the Retrieved documents into prompts.
    - Logic to call an LLM and return a response.
'''
from transformers import AutoTokenizer, AutoModelForCausalLM

class TextGenerator:
    def __init__(self, model_name=config.core["Model Name"]):
        """
        Initialize the text generator with a specified model from Hugging Face.
        :param model_name: Name of the Hugging Face model to use.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=50, temperature=1.0, top_k=50):
        """
        Generate text based on the input prompt.
        :param prompt: The input text to start the generation.
        :param max_length: Maximum length of the generated text.
        :param temperature: Sampling temperature for generation.
        :param top_k: Number of highest probability vocabulary tokens to keep for top-k sampling.
        :return: Generated text as a string.
        """
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            do_sample=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

def HuggingFace_LLM(prompt):
    # Initialize the text generator with a specified model from Hugging Face.
    llm = HuggingFaceEndpoint(
        repo_id=config.core["Repo Id"],
        max_length=128,
        temperature=0.7,
        token=config.core["Hugging Face Access Token"]
    )
    return llm.invoke(prompt)

if __name__ == "__main__":
    try:
        start_time = time.time()
        # llm_Generator = HuggingFace_LLM()
        Logger(
            log=f"Generator Output: {HuggingFace_LLM("What is Machine Learning?")}",
            logLevel="info"
        )
        # GenAI = TextGenerator()
        # for i in constants.constants.standardPrompts:
        #     Logger(
        #         log=f"Prompt : {i}, Response : {HuggingFace_LLM(i)}",
        #         logLevel="debug"
        #     )
        #     time.sleep("5")
        # if not os.path.exists("chroma_store"):
        #     retriever.CreateVectorStorage_ChromaDB()
        #     Logger(log="Vector Storage Created", logLevel="info")
        # else:
        #     Logger(log="Vector Storage Already Exists", logLevel="debug")
        Logger(log=f"generator.py took {time.time() - start_time}s to execute", logLevel="debug")
    except Exception as e:
        Logger(log=f"Error: {e}", logLevel="error")