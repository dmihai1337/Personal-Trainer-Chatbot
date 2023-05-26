import openai
import gradio

# Set up your OpenAI API credentials
openai.api_key = 'INSERT YOUR API KEY'

# Define the conversation history
conversation_history = ['System: You are a fitness personal trainer.' +
                        'Answer questions on fitness and nutrition.']

def CustomChatGPT(user_input):
 
    # Add user input to conversation history
    conversation_history.append('User: ' + user_input)

    # Send the conversation history to ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='\n'.join(conversation_history),
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None
    )

    # Get the generated reply from ChatGPT
    chatgpt_reply = response.choices[0].text.strip()

    # Add ChatGPT's reply to the conversation history
    conversation_history.append('ChatGPT: ' + chatgpt_reply)

    return chatgpt_reply

demo = gradio.Interface(fn=CustomChatGPT, 
                        inputs="text", 
                        outputs="text", 
                        title="Personal Trainer Chatbot")

demo.launch(share=True)