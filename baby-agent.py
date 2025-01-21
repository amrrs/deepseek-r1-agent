from smolagents import CodeAgent, OpenAIServerModel

model = OpenAIServerModel(
    model_id="deepseek-r1-distill-qwen-7b", # change the r1 model name accordingly
    api_base="http://127.0.0.1:1234/v1",
    api_key='lm-studio',
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 55th number in the Fibonacci sequence?",
)
