from openai import OpenAI
openai=OpenAI(api_key = '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')




def generate_response(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{'role':'user','content':prompt}]
        )
    
    res = completion.choices[0].message.content.strip()
    return res


prompt = str(input("Ask GPT-3: "))


response = generate_response(prompt)
print(response)
