import openai

print("Start")

openai.api_key = open("api.key","r").read().strip('\n')

print(openai.api_key);

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"question"}]
)

print(completion.choices[0].message.content)
