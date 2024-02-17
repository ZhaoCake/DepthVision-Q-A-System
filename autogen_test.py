from autogen import ConversableAgent, UserProxyAgent
config_list = [{
    "model": "internlm2",
    "api_key": "abcdefg",
    "base_url": "http://127.0.0.1:8000/",
  }]
# Create the agent that uses the LLM.
assistant = ConversableAgent("agent", llm_config={"config_list": config_list})

# Create the agent that represents the user in the conversation.
user_proxy = UserProxyAgent("user", code_execution_config=False)

# Let the assistant start the conversation.  It will end when the user types exit.
assistant.initiate_chat(user_proxy, message="How can I help you today?")