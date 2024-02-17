from lagent.actions.action_executor import ActionExecutor
from lagent.actions.python_interpreter import PythonInterpreter
from lagent.agents.react import ReAct
from lagent.llms.openai import GPTAPI


def input_prompt():
    print('\ndouble enter to end input >>> ', end='')
    sentinel = ''  # ends when this string is seen
    return '\n'.join(iter(input, sentinel))


def main():
    model = GPTAPI(model_type='internlm', key="abcdefg", openai_api_base="http://127.0.0.1:23333/v1/chat/completions")
    
    chatbot = ReAct(
        llm=model,
        action_executor=ActionExecutor(actions=[PythonInterpreter()]),
    )

    while True:
        try:
            prompt = input_prompt()
        except UnicodeDecodeError:
            print('UnicodeDecodeError')
            continue
        if prompt == 'exit':
            exit(0)

        agent_return = chatbot.chat(prompt)
        print(agent_return.response)


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

