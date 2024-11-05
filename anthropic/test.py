import anthropic

# Set your Anthropic API key here
isana_api_key = 'isana-api-key'

# Create an Anthropic client
client = anthropic.Anthropic(api_key=isana_api_key)

# Define the prompt you want to send to Claude 3.5
human_input = "What are the NoSQL options to store JSON documents?"
messages = [
    {"role": "user", "content": human_input}
]

# Call the Anthropic API to get a response from Sonet 3.5 using the Messages API
#message = client.messages.create(
#    model="claude-3-5-sonnet-20240620",
#    max_tokens=1024,
#    messages=messages,
#    system="You are an experienced data engineer.",
#    stop_sequences=["The end."],
#    temperature=0.2
#)
#
#print(message.content)
response_message = ''
with client.messages.stream(
#            model="claude-3-5-sonnet-20240620",
#            model="claude-3-5-sonnet-20241022",
            model="claude-3-5-haiku-20241022",
            max_tokens=4096,
            messages=messages,
            system="You are an experienced data engineer.",
            stop_sequences=["The end."],
            temperature=0.2
        ) as stream:
            for text in stream.text_stream:
                response_message += text
                print(text)

print(response_message)

