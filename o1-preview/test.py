
import os
import time
from openai import OpenAI

# Set your OpenAI API key here
isana_api_key = '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'

client = OpenAI(
    # This is the default and can be omitted
    api_key=isana_api_key,
)

start_time = time.time()

#chat_completion = client.chat.completions.create(
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an experienced data engineer."},
        {
            "role": "user",
            "content": "What are the NoSQL options to store JSON documents?"
        }
    ],
    model="o1-preview",
#    stop=["\n", "End of response"],
    temperature=0.2,
    stream=True
)

#print(chat_completion.choices[0].message)

# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
for chunk in response:
    chunk_time = time.time() - start_time  # calculate the time delay of the chunk
    collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk.choices[0].delta.content  # extract the message
    collected_messages.append(chunk_message)  # save the message
    #print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

# print the time delay and text received
print(f"Full response received {chunk_time:.2f} seconds after request")

# clean None in collected_messages
collected_messages = [m for m in collected_messages if m is not None]
full_reply_content = ''.join(collected_messages)
print(f"Full conversation received: {full_reply_content}")
