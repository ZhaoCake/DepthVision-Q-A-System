from agentlego.apis import load_tool

segment_anything = load_tool("SegmentAnything", device="cpu")

img_path = "/home/zhaocake/eai/DepthVision-Q-A-System/resources/4D241F65254A9EFEC8D4537454BD6D92.jpg"

result = segment_anything(img_path)

print("SegmentAnything done")
print(result)
