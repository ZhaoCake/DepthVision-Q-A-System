from internlm_langchain import InternLM2
# from langchain.chains import SequentialChain
from langchain.agents import AgentExecutor
from agentlego.apis import load_tool

internlm2 = InternLM2()

# test the model
text = "Hello, how are you?"
output = internlm2(text)

print(output)

# create a chain
segment_anything = load_tool("SegmentAnything", device="cpu").to_langchain
segment_object = load_tool("SegmentObject", device="cpu").to_langchain
vqa_tool = load_tool("VQA", device="cpu").to_langchain
depth_tool = load_tool("ImageToDepth", device="cpu").to_langchain

# 创建智能体执行器
agent_executor = AgentExecutor()






