import streamlit as st
import openai
import json
import os
from dotenv import dotenv_values


class HomeAutomation:
    def TurnOnLights(self, room):
        """
        Turn on the lights in the specified room.

        Args:
            room (str): The room where the lights should be turned on.
        """
        st.markdown(f"Lights turned ON - **{room}**")

    def TurnOffLights(self, room):
        """
        Turn off the lights in the specified room.

        Args:
            room (str): The room where the lights should be turned off.
        """
       st.markdown(f"Lights turned ON - **{room}**")


def call_gpt(prompt):
    """
    Make a ChatCompletion API call to OpenAI GPT-3.5-turbo model.

    Args:
        prompt (str): The user's prompt or input text.

    Returns:
        str: The generated response from the API call.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt}],
        functions=[
            {
                "name": "TurnOnLights",
                "description": "Turn On the lights",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room": {
                            "type": "string",
                            "description": "The room",
                        },
                    },
                    "required": ["room"],
                },
            },
            {
                "name": "TurnOffLights",
                "description": "Turn Off the lights",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room": {
                            "type": "string",
                            "description": "The room",
                        },
                    },
                    "required": ["room"],
                },
            }
        ],
        function_call="auto",
    )
    return completion.choices[0].message


if __name__ == "__main__":
    st.title("Home Automation with GPT")
    env = dotenv_values()
    openai.api_key = env["API_KEY"]

    obj = HomeAutomation()
    prompt = st.text_input("Enter your command:")
    if prompt:
        reply_content = call_gpt(prompt)

        funcName = reply_content.to_dict()['function_call']['name']
        funcArg = reply_content.to_dict()['function_call']['arguments']

        method_name = funcName
        func = json.loads(funcArg)
        params = func['room']

        method = getattr(obj, method_name)
        method(params)
