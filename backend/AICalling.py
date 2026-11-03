from typing import Literal, Optional
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from google import genai
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv


class SmartHomeCommand(BaseModel):
  device: Literal["front_door_lock", "thermostat", "unknown"] = Field(
      description="The targeted device"
  )
  action: Literal["lock", "unlock", "set_temperature", "query_status"] = Field(
      description="Action to take"
  )
  value: Optional[int] = Field(
      default=None, description="Numeric target value (like degrees)"
  )
load_dotenv()
client = genai.Client()

def call_gemini(prompt_value):
  
  text_input = prompt_value.to_string()

  response = client.models.generate_content(
      model="gemini-3.5-flash-lite",
      contents=text_input,
  )
  return response.text


gemini_runnable = RunnableLambda(call_gemini)


parser = PydanticOutputParser(pydantic_object=SmartHomeCommand)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You extract home automation commands.\n{format_instructions}",
    ),
    ("human", "{user_command}"),
]).partial(format_instructions=parser.get_format_instructions())


structured_chain = prompt | gemini_runnable | parser


def callAI(command):
  return structured_chain.invoke({"user_command": command})


def tester():
    parsed_obj = structured_chain.invoke({"user_command": "Unlock the front door"})

    print(f"Device: {parsed_obj.device}")
    print(f"Action: {parsed_obj.action}")

    if(parsed_obj.value != None):
        print(f"Value: {parsed_obj.value}")

#tester()
