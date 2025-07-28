import json
from concurrent.futures import ThreadPoolExecutor
from prompts import load_user_data, generate_prompt, college_classification, check_prompt, about_bot, prompt_reaction
from chatbot import initialize_chat_with_history, generate_chat_responses, generate_ai_response, chat, chatbot_model, load_chat_history, save_chat_history, HISTORY_FILE_PATH
from rag import ask
from colorama import Fore, Style, init
import speech_recognition as sr

def main():

    def listen_for_input():
        #  stt 
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print(f"{Fore.GREEN}Listening for your input...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                print(f"{Fore.RED}Recognizing speech...")
                text = recognizer.recognize_google(audio)
                print(f"{Fore.GREEN}Recognized speech: {text}")

                return text
            except sr.UnknownValueError:
                print(f"{Fore.YELLOW}Speech not recognized. Please try again.")
                return listen_for_input()
            except sr.RequestError as e:
                print(f"{Fore.YELLOW}Speech recognition API error: {e}")
                return listen_for_input()
            except Exception as e:
                print(f"{Fore.YELLOW}Unexpected error: {e}")
                return listen_for_input()
    file_path = "usersinfo.json"
    
    try:
        data = load_user_data(file_path)
        prompt = generate_prompt(data)

        # Load chat history
        history = load_chat_history()
        
        # Check if initial prompt exists
        if any(entry["role"] == "user" and entry["parts"] == prompt for entry in history):
            print("Initial history is already set. Continuing with the chat...")
        else:
            print("Setting initial history...")
            initialize_chat_with_history(chatbot_model , prompt, "sure")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: The JSON file is not properly formatted.")
    except KeyError as e:
        print(f"Error: Missing expected key in JSON data: {e}")

    # Create a thread pool to handle parallel tasks
    with ThreadPoolExecutor() as executor:
        while True:
            # user_input = listen_for_input() 
            user_input = input(f"{Fore.GREEN}Enter your prompt (or type 'exit' to quit): ")
            if user_input.lower() == "exit":
                print(f"{Fore.RED}Exiting...")
                break

            # Classify the prompt type
            classify = generate_chat_responses(chat(model_instance=chatbot_model), f"{college_classification}\n where the prompt is : {user_input}").text.strip()
            print(f"Classification: {classify}")
            
            # Define the futures for parallel tasks
            futures = {}

            # Define the task to submit to the executor
            def submit_generate_response(prompt_input):
                K =  generate_chat_responses(chat(model_instance=chatbot_model), prompt_input).text
                print(K)
                return K


            def generate_chats(classify , user_input):
            # Classify and handle different types of responses
                if classify == "use_pdf":
                    questions = generate_chat_responses(chat(model_instance=chatbot_model), f"{check_prompt} the prompt is : '{user_input}'").text
                    print(f"Questions: {questions}")
                    rag_output = ask(questions)
                    print(f"RAG Output: {rag_output}")
                    history.append({"role": "user", "parts": user_input})
                    history.append({"role": "assistant", "parts": rag_output})

                elif classify == "use_self" or classify == "use_py":
                    ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
                    history.append({"role": "user", "parts": user_input})
                    history.append({"role": "assistant", "parts": ai_response})
                    print(f"AI Response: {ai_response}")

                elif classify == "use_bot":
                    ai_response = generate_chat_responses(chat(model_instance=chatbot_model), f"According to this detail '''{about_bot}''' answer the following prompt {user_input}").text
                    history.append({"role": "user", "parts": user_input})
                    history.append({"role": "assistant", "parts": ai_response})
                    print(f"AI Response with Bot Info: {ai_response}")

                elif(classify == "use_py"):
                    history.append({"role": "user", "parts": user_input})
                    ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
                    history.append({"role": "assistant", "parts": ai_response})
                    print(ai_response)
            # Create a task to process the user input asynchronously for classification
            futures['chat_response'] = executor.submit(generate_chats, classify, user_input)

            # Create a task to get the expression based on the prompt_reaction
            futures['expression'] = executor.submit(submit_generate_response, f"{prompt_reaction} {user_input}")

            # Wait for both tasks to complete and print their results
            completed_futures = []
            print("\nProcessing...")

            while len(completed_futures) < len(futures):
                for future_name, future in futures.items():
                    if future.done() and future not in completed_futures:
                        completed_futures.append(future)
                        result = future.result()
                        print(f"{future_name} result: {result}")

            save_chat_history(history)

if __name__ == "__main__":
    main()