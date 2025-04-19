#ENTJ_task
#gpt_utils.py
import openai
from s3_utils import save_history

openai.api_key = "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"

def chat_with_gpt(user_id, user_msg, history):
    history.append({"role": "user", "content": user_msg})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    reply = response['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": reply})
    save_history(user_id, history)
    return reply

