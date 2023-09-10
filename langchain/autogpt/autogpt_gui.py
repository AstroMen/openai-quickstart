import gradio as gr
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.chat_models import ChatOpenAI

def initialize_agent():
    # 这里的 'tools' 和 'vectorstore' 需要被正确初始化，我在这个示例中省略了它们
    # 你需要根据你的代码来设置这些对象

    agent = AutoGPT.from_llm_and_tools(
        ai_name="Jarvis",
        ai_role="Assistant",
        tools=tools,
        llm=ChatOpenAI(temperature=0),
        memory=vectorstore.as_retriever(),
    )
    agent.chain.verbose = True
    return agent

def ask_question(agent, question):
    return agent.run([question])

def build_gui():
    agent = initialize_agent()

    def wrapper_func(question):
        return ask_question(agent, question)

    iface = gr.Interface(
        fn=wrapper_func,
        inputs=gr.inputs.Textbox(label="请输入您的问题"),
        outputs="text",
        live=True
    )
    iface.launch()

if __name__ == "__main__":
    build_gui()
