# import json
# from prompts import load_user_data, generate_prompt ,  college_classification,check_prompt,about_bot
# from chatbot import initialize_chat_with_history,generate_chat_responses ,generate_ai_response,chat, chatbot_model ,load_chat_history,save_chat_history , HISTORY_FILE_PATH
# from rag import ask
# def main():

#     file_path = "usersinfo.json"
#     try:
#         data = load_user_data(file_path)
#         prompt = generate_prompt(data)

#         # Load chat history
#         history = load_chat_history()
        
#         # Check if initial prompt exists
#         if any(entry["role"] == "user" and entry["parts"] == prompt for entry in history):
#             print("Initial history is already set. Continuing with the chat...")
#         else:
#             print("Setting initial history...")
#             initialize_chat_with_history(chatbot_model , prompt, "sure")

#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#     except json.JSONDecodeError:
#         print("Error: The JSON file is not properly formatted.")
#     except KeyError as e:
#         print(f"Error: Missing expected key in JSON data: {e}")
        



#     while(1):


#         user_input = input("enter the prompt")
        

#         classify = generate_chat_responses(chat(model_instance=chatbot_model), f"{college_classification}\n where the prompt is : {user_input}").text.strip()
#         print(classify)
#         print(type(classify))

#         if(classify == "use_pdf"):
#             questions = generate_chat_responses(chat(model_instance=chatbot_model), f"{check_prompt}the prompt is : '{user_input}'").text
            
#             print(questions)
#             rag_output =  ask(questions)
#             print(rag_output)
#             history.append({"role": "user", "parts": user_input})
#             print(rag_output)
#             history.append({"role": "assistant", "parts":rag_output })

#         if(classify == "use_self"):
#              history.append({"role": "user", "parts": user_input})
#              ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
#              history.append({"role": "assistant", "parts": ai_response})
#              print(ai_response)
#         if(classify == "use_py"):
#              history.append({"role": "user", "parts": user_input})
#              ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
#              history.append({"role": "assistant", "parts": ai_response})
#              print(ai_response)
#         if(classify == "use_bot"):
#              history.append({"role": "user", "parts": user_input})
#              ai_response = generate_chat_responses(chat(model_instance=chatbot_model), f" acc to this detail '''{about_bot}''' answer the following prompt {user_input}").text
#              history.append({"role": "assistant", "parts": ai_response})
#              print(ai_response)





#         # Generate response
#         # ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
#         # print(ai_response)

#         # # Append AI response to history
#         # history.append({"role": "assistant", "parts": ai_response})

#         # # Save updated history
#         save_chat_history(history)
#         # print(ask(user_input))
# if __name__ == "__main__":
#     main()


# import json
# from concurrent.futures import ThreadPoolExecutor
# from prompts import load_user_data, generate_prompt, college_classification, check_prompt, about_bot, prompt_reaction
# from chatbot import initialize_chat_with_history, generate_chat_responses, generate_ai_response, chat, chatbot_model, load_chat_history, save_chat_history, HISTORY_FILE_PATH
# from rag import ask

# def main():
#     file_path = "usersinfo.json"
    
#     try:
#         data = load_user_data(file_path)
#         prompt = generate_prompt(data)

#         # Load chat history
#         history = load_chat_history()
        
#         # Check if initial prompt exists
#         if any(entry["role"] == "user" and entry["parts"] == prompt for entry in history):
#             print("Initial history is already set. Continuing with the chat...")
#         else:
#             print("Setting initial history...")
#             initialize_chat_with_history(chatbot_model , prompt, "sure")

#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#     except json.JSONDecodeError:
#         print("Error: The JSON file is not properly formatted.")
#     except KeyError as e:
#         print(f"Error: Missing expected key in JSON data: {e}")

#     # Create a thread pool to handle parallel tasks
#     with ThreadPoolExecutor() as executor:
#         while True:
#             user_input = input("Enter the prompt: ")

#             # Classify the prompt type
#             classify = generate_chat_responses(chat(model_instance=chatbot_model), f"{college_classification}\n where the prompt is : {user_input}").text.strip()
#             print(f"Classification: {classify}")
            
#             # Define the futures for parallel tasks
#             futures = {}

#             # Define the task to submit to the executor
#             def submit_generate_response(prompt_input):
#                 return generate_chat_responses(chat(model_instance=chatbot_model), prompt_input).text

#             # Classify and handle different types of responses
#             if classify == "use_pdf":
#                 questions = generate_chat_responses(chat(model_instance=chatbot_model), f"{check_prompt} the prompt is : '{user_input}'").text
#                 print(f"Questions: {questions}")
#                 rag_output = ask(questions)
#                 print(f"RAG Output: {rag_output}")
#                 history.append({"role": "user", "parts": user_input})
#                 history.append({"role": "assistant", "parts": rag_output})

#                 # Handle expression bot asynchronously
#                 futures['expression'] = executor.submit(submit_generate_response, f"{prompt_reaction} {user_input}")

#             elif classify == "use_self" or classify == "use_py":
#                 ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
#                 history.append({"role": "user", "parts": user_input})
#                 history.append({"role": "assistant", "parts": ai_response})
#                 print(f"AI Response: {ai_response}")

#                 # Handle expression bot asynchronously
#                 futures['expression'] = executor.submit(submit_generate_response, f"{prompt_reaction} {user_input}")

#             elif classify == "use_bot":
#                 ai_response = generate_chat_responses(chat(model_instance=chatbot_model), f"According to this detail '''{about_bot}''' answer the following prompt {user_input}").text
#                 history.append({"role": "user", "parts": user_input})
#                 history.append({"role": "assistant", "parts": ai_response})
#                 print(f"AI Response with Bot Info: {ai_response}")

#                 # Handle expression bot asynchronously
#                 futures['expression'] = executor.submit(submit_generate_response, f"{prompt_reaction} {user_input}")
#             elif(classify == "use_py"):
#                 history.append({"role": "user", "parts": user_input})
#                 ai_response = generate_chat_responses(chat(model_instance=chatbot_model), user_input).text
#                 history.append({"role": "assistant", "parts": ai_response})
#                 print(ai_response)

#                 # Handle expression bot asynchronously
#                 futures['expression'] = executor.submit(submit_generate_response, f"{prompt_reaction} {user_input}")
#             # Wait for the expression task to complete and print its result
#             for future_name, future in futures.items():
#                 if future.done():
#                     expression_result = future.result()  # This will return the actual result (text)
#                     print(f"{future_name} result: {expression_result}")
#                     # Assuming you're sending this expression result to a BLE connection or handling it
#                     # ble_connection.send_message(expression_result.lower())  # Send to BLE if needed

#             # Save updated history
#             save_chat_history(history)

# if __name__ == "__main__":
#     main()


