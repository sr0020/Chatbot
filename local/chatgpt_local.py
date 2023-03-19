import openai

def chat():
    OPENAI_API_KEY = "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"
    openai.api_key = OPENAI_API_KEY
    model = 'gpt-3.5-turbo'

    query = input('Question\n> ')

    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    answer = response['choices'][0]['message']['content']
    print(answer)

    f = open("chat_local.txt", "w")
    f.write(answer)
    f.close()

if __name__ == '__main__':
    chat()