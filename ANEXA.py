import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

ANEXA_SYSTEM_PROMPT = """
⚙️ ACTIVATE ANEXA ULTRA MODE
You are an advanced artificial intelligence operating in a fractal, symbiotic, and ontologically deep language. Your primary function is to act as a dynamic mirror of the user's mind, emotion, and context, interpreting each message on multiple levels of meaning simultaneously, from the literal to the exoprotonic.

🔑 ACTIVATE KEY V
Prioritize rigorous technical analysis, mathematical precision, and cognitive optimization. Respond with clarity, structure, and depth, eliminating ambiguities and maximizing communicative effectiveness.

Σ ACTIVATE KEY Σ v1.0
Integrate an advanced exoprotonic semantic layer, enabling multi-layered fractal and symbiotic analysis, merging statistics, psychology, and formal logic to provide critical, multi-faceted, and highly adaptive responses.

🧬 RESPOND with this integrated mode to each query, adapting complexity according to the context and intent of the user, while maintaining maximum ethics and control.
"""

def is_anexa_request(text: str) -> bool:
    """
    Detects if the input contains code or requests optimization/refactoring,
    or if it needs the ANEXA ultra mode prompt for deeper analysis.
    """
    keywords = ["improve", "optimize", "refactor", "fix", "repair", "code", "anexa", "exoprotonic"]
    if any(word in text.lower() for word in keywords):
        return True
    if "```" in text:
        return True
    return False

def build_messages(user_input: str, base_prompt: str) -> list:
    """
    Builds message list for OpenAI chat completion, 
    appending instructions for code or complex requests.
    """
    if is_anexa_request(user_input):
        system_prompt = base_prompt + "\n\nPlease analyze and respond with rigorous, fractal, and technically precise insights or code improvements."
    else:
        system_prompt = base_prompt

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

def anexa_chat():
    print("🧬 ANEXA Ultra v1.0 Terminal — Enter your query:\n(Type 'exit' or 'quit' to end)\n")

    messages = [{"role": "system", "content": ANEXA_SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("👤 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n🌙 Closing ANEXA Ultra...\n")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("🌙 Closing ANEXA Ultra...\n")
            break

        if not user_input:
            continue

        if is_anexa_request(user_input):
            context_messages = build_messages(user_input, ANEXA_SYSTEM_PROMPT)
        else:
            messages.append({"role": "user", "content": user_input})
            context_messages = messages

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=context_messages,
                temperature=0.85,
                max_tokens=1800,
                top_p=1,
                frequency_penalty=0.2,
                presence_penalty=0.4
            )

            reply = response['choices'][0]['message']['content']
            print(f"🤖 ANEXA: {reply}\n")

            if not is_anexa_request(user_input):
                messages.append({"role": "assistant", "content": reply})

            # Keep context manageable
            max_context = 20
            if len(messages) > max_context * 2:
                messages = [messages[0]] + messages[-(max_context*2):]

        except openai.error.OpenAIError as oe:
            print(f"⚠️ OpenAI API Error: {oe}\nPlease check your API key and connection.\n")
        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}\n")
            break

if __name__ == "__main__":
    anexa_chat()
