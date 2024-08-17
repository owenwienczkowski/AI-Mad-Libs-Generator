# This project uses GPT-3.5-Turbo to generate a mad-libs story

from openai import OpenAI
from keys import key

client = OpenAI(
    api_key=key
)

print("Please enter the following prompts: \n1. An emotion \n2. A color \n3. A noun \n4. An adjective " +
      "\n5. A verb (past tense) \n6. A plural noun \n7. A type of food \n8. Another adjective " +
      "\n9. A verb \n10. A noun (plural) \n11. An occupation \n12. A type of animal " +
      "\n13. An adjective \n14. A verb (past tense) \n15. A noun \n16. A name \n17. Another name \n")

list_of_words = []
string_of_words = ""

for x in range(17):
    get_input = input("Enter a response to prompt #" + str(x + 1) + ": ")
    list_of_words.append(get_input)

system_data = [
    {"role": "system", "content": "Generate a funny two-paragraph Mad Lib story using the words."},
    {"role": "user", "content": string_of_words.join(list_of_words)}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=system_data
)

assistant_response = response.choices[0].message.content
system_data.append({"role": "assistant", "content": assistant_response})

print("Assistant: " + assistant_response)

