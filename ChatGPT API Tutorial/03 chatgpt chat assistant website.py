import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "chatbot with gpt turbo powered, plotsby, cryptoapi"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "MOIRA")

demo.launch(share=True)