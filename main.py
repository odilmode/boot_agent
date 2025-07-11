import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import available_functions, call_function

def main():

    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("No user prompt")
        sys.exit(1)
    flag = False
    if "--verbose" in args:
        args.remove("--verbose")
        flag = True
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    
    for i in range(20):
        try:
            res = generate_content(client, messages, flag)
            if res.text and not res.function_calls:
                print("Final response:")
                print(res.text)
                break
        except Exception as e:
            print(f"Error occured: {e}")
    
def generate_content(client, messages, flag):
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),)
    if isinstance(response.candidates, list):
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        return response

    function_responses = []
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f" - Calling function: {function_call_part.name}")
            function_call_result = call_function(function_call_part, flag)
            if (not function_call_result.parts or not function_call_result.parts[0].function_response):
                raise Exception("empty function call result")
            
            if flag:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
            function_responses.append(function_call_result.parts[0])
        if not function_responses:
            raise Exception("no function responses generated, exiting.")
        messages.append(types.Content(role="tool", parts=function_responses))

    if flag:
        print("User prompt:", messages[0].parts[0].text)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    return response



if __name__ == "__main__":
    main()
