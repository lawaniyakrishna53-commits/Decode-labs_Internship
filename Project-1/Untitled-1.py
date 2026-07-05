
def start_chatbot():
    # Welcome message to the user
    print("==================================================")
    print("🤖 DecodeLabs AI Chatbot (System 2: Deterministic) ")
    print("Type 'exit' or 'quit' to end the conversation.    ")
    print("==================================================")

    # 3. Continuous Feedback Loop
    while True:
        # Phase 1: Input & Sanitization
        raw_input = input('You: ')
        clean_input = raw_input.lower().strip() # Normalization process
        
        # Check for Exit Commands immediately
        if clean_input in ['exit', 'quit', 'bye']:
            print("Chatbot: Thank you for chatting! Goodbye. 👋")
            break
            
        # Phase 2: Process (The Logic Skeleton using if-else)
        if clean_input in ['hello', 'hi', 'hey']:
            response = "Chatbot: Hello! Welcome to DecodeLabs. How can I help you today?"
            
        elif clean_input in ['what is your name?', 'who are you']:
            response = "Chatbot: I am a deterministic, rule-based AI engine built as a foundational control layer."
            
        elif 'help' in clean_input:
            response = "Chatbot: I can assist you with understanding basic control flow, logic gates, or project guidelines."
            
        elif clean_input in ['what is a white box?', 'white box']:
            response = "Chatbot: A white box is a transparent generative program where the interpreter can always provide straightforward, traceable explanations."
            
        elif clean_input in ['what are ai guardrails?', 'guardrails']:
            response = "Chatbot: AI guardrails act as a deterministic filter for probabilistic outputs, ensuring safety and compliance."
            
        else:
            # Fallback for unrecognized inputs
            response = "Chatbot: I'm sorry, that input falls outside my current logic engine parameters. Try asking about 'white box' or 'guardrails'."

        # Phase 3: Output Response
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    start_chatbot()