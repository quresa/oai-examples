import os
import openai


def get_response(question: str):
    try:
        return openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0, max_tokens=100,
                                        top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"])
    except Exception as err:
        print(err)


def interactive_mode():
    intro_message = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in "
    intro_message += "truth, I will give you the answer.\n"
    intro_message += "If you ask me a question that is nonsense, trickery, or has no clear answer, "
    intro_message += "I will respond with \"Unknown\""
    prompt = "What's your question? [type \"stop\"] to end: "
    print(intro_message)
    while True:
        question = input(prompt)
        if question == "stop":
            print("Goodbye")
            break
        response = get_response(question)
        print(response)


openai.api_key = os.getenv("OPENAI_API_KEY")
if __name__ == "__main__":
    interactive_mode()
else:
    print("to-do: library")
