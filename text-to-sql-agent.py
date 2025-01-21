# make sure to run 
# 1. sql-tables.py 
# 2. sql-tool.py
# finally this file!

from smolagents import CodeAgent, OpenAIServerModel

model = OpenAIServerModel(
    model_id="deepseek-r1-distill-qwen-7b",
    api_base="http://127.0.0.1:1234/v1",
    api_key='lm-studio',
)

agent = CodeAgent(
    tools=[sql_engine],
    model= model,
)
agent.run("Can you give me the average tip?")
