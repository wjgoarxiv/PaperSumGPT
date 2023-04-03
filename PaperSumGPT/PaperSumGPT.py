# ------------------ Import libraries ------------------ #
import os
import glob
import pyfiglet
from tabulate import tabulate
from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config
import PyPDF2

# ------------------ Main code starts ------------------ #
# Print the title 
os.system('cls' if os.name == 'nt' else 'clear')
title = pyfiglet.figlet_format('PaperSumGPT', font = 'small')
print('\n')
print(title+'\n')
print('\n')
print('------------------------------------------------')
print('If you have any questions, please send your questions to my email.')
print('\nOr, please suggest errors and areas that need updating.')
print('\n 📨 woo_go@yahoo.com')
print('\nVisit https://github.com/wjgoarxiv/papersumgpt for more information.')
print('------------------------------------------------')

def main():
    # Ask user if the brought input file is a markdown file or PDF file 
    print('\n')
    file_type = int(input("""INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. PDF (`.pdf`) file

    Note that the option 2 would convert the PDF file to a markdown file using the `pdf2md` package: """))
    print('\n')
    print('------------------------------------------------')

    # Print the list of files in the current directory
    if file_type == 1:
        file_list = glob.glob('./*.md')
        file_list = [file.split('\\')[-1] for file in file_list]
        file_list.sort()

    elif file_type == 2:
        file_list = glob.glob('./*.pdf')
        file_list = [file.split('\\')[-1] for file in file_list]
        file_list.sort()

    # File not found error handling
    try: 
        if len(file_list) == 0:
            raise FileNotFoundError
        else:
            pass

    # Alert the user 
    except: 
        print('ERROR: There is no file in the current directory. Please check the current directory.')
        print('------------------------------------------------')
        exit()

    # Print the list of files in the current directory
    file_num = [] 
    for i in range(len(file_list)):
        file_num.append(i+1)
    print(tabulate({'File number': file_num, 'File name': file_list}, headers='keys', tablefmt='psql'))
    print('------------------------------------------------')
    user_input = int(input('\nINFO: Please select the file number or press "0" to exit: '))

    if user_input == 0:
        print("INFO: Exiting the program.")
        exit()
    else:
        try: 
            print("INFO: The file name that would be utilized is", file_list[user_input-1])
        except:
            print("ERROR: Your input number is out of range. Please check the file number.")
            print("ERROR: The program will stop.")
            exit()

    # Ask user to turn on `verbose` mode. 
    # If the user turns on `verbose` mode, the program will print the intermediate results.
    print('------------------------------------------------')
    verbose = input("INFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n): ")
    if verbose == 'y' or verbose == 'Y':
        verbose = True
    elif verbose == 'n' or verbose == 'N':
        verbose = False
    print('------------------------------------------------')

    # Ask user their desired ChatGPT model
    chatgpt_model = input("""INFO: Please type the number the ChatGPT model that you want to use:

    1. default (Turbo version for ChatGPT Plus users and default version for free users)
    2. gpt4 (Only available for ChatGPT Plus users; a little bit slower than the default model)
    3. legacy (Only available for ChatGPT Plus users; an older version of the default model)

    Note that the option 2 and 3 are NOT available for free users. If you are the free user, please select the option 1.
    """)
                        
    if chatgpt_model == '1':
        chatgpt_model = 'default'
    elif chatgpt_model == '2':
        chatgpt_model = 'gpt4'
    elif chatgpt_model == '3':
        chatgpt_model = 'legacy'
    else:
        print("ERROR: Your input number is out of range. Please check the file number.")
        print("ERROR: The program will stop.")
        exit()
    print('------------------------------------------------')

    # ------------------ Convert pdf to md ------------------ #

    def extract_text_from_pdf(pdf_file: str) -> [str]:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)
            pdf_text = []

            for page in reader.pages:
                content = page.extract_text()
                pdf_text.append(content)

            return pdf_text
        
    if file_type == 2:
        print('INFO: Converting the PDF file to a markdown file...')
        pdf_text = extract_text_from_pdf(file_list[user_input-1])

        with open(file_list[user_input-1] + '_markdowned.md', 'w') as f:
            for line in pdf_text:
                f.write(line)

        file_list[user_input-1] = file_list[user_input-1] + '_markdowned.md'
        print('INFO: The PDF file has been converted to a markdown file.')
        print('------------------------------------------------')

    # ------------------ Function starts ------------------ #
    # Load config settings
    config = Config()
    config.set('chat.model', chatgpt_model)

    # Initialize ChatGPT
    bot = ChatGPT(config)

    # read input file
    with open(file_list[user_input-1], 'r') as f:
        input_text = f.read()

    # Ask user maximum length of input text (if don't know, just input 3000)
    max_length = int(input("INFO: Please input the maximum length of input text (if don't know, just input 5000): "))

    # truncate input text into smaller parts
    input_parts = [input_text[i:i+max_length] for i in range(0, len(input_text), max_length)]

    # define initial prompt message
    initial_prompt = "Please, act as 'High-quality content abbreviator'. Since you have the input limits (OpenAI limited your input limit), you have to firstly take the all the inputs iteratively. To do this, I've already truncated the long inputs into each subpart. You'll now have to take the inputs iteratively. The important thing is that you should NOT answer directly or respond to the previous message. Make sure that you have to accomplish the task when all the inputs are given. I'll let you know if all the inputs are given."

    # send initial prompt message to ChatGPT
    print("INFO: Tossing initial prompt...")
    success, response, message = bot.ask(initial_prompt)
    if success:
        print(f"INFO: ChatGPT started abbreviating the input contents...")
    else:
        raise RuntimeError(message)

    # initialize response list
    response_parts = []

    # define prompt message while iterating over input parts and send them to ChatGPT
    for i, part in enumerate(input_parts):
        if i == len(input_parts) - 1:
            prompt = f"This is the {i+1}th part of the truncated input contents. And PLEASE! Do NOT answer and if you understood the input, just keep asking me to input the leftover contents.\n\n```\n{part}\n```\nThank you for providing all the inputs."
        else:
            prompt = f"This is the {i+1}th part of the truncated input contents. And PLEASE! Do NOT answer and if you understood the input, just keep asking me to input the leftover contents.\n\n```\n{part}\n```"

        print(f"INFO: Waiting for ChatGPT to respond for {i+1}/{len(input_parts)} part(s)...")

        # send prompt message and prompt part to ChatGPT
        success, response, message = bot.ask(prompt)
        if success:
            response_parts.append(response)
        else:
            raise RuntimeError(message)

        # print status update
        print(f"INFO: {i+1}/{len(input_parts)} part(s) tossed to ChatGPT.")

        # Handling the `verbose` mode 
        if verbose == True:
            print(f"INFO: Tossed prompt in {i+1}/{len(input_parts)} part(s): {prompt}")
            print(f"INFO: Response from ChatGPT: {response}")
        else:
            pass

    # define final prompt message
    final_prompt = """Now, all the inputs are given to you. Please, abbreviate all the input contents fitting them into the following markdown format. You have to fill the contents in the markdown format. The markdown format is as follows:
    /* 

    # TITLE
    (Bring the title from the foremost heading in the document. The powerful hint is that the title comes before the people who wrote the document.)

    ## INTRODUCTION

    ## METHODOLOGY

    ## RESULTS & DISCUSSION

    ## CONCLUSION

    ## SIGNIFICANCE OF THIS STUDY

    ## THINGS TO LOOK OUT FOR IN FOLLOW-UP RESEARCH
    ...

    */
    And please, write the outputs thinking you are writing PPT slides. But NOT too simple. You have to write the outputs in a way that the readers can understand the contents easily.
    """

    # join response parts to form final response
    final_response = response_parts[-1]

    # send final prompt message to ChatGPT
    print("INFO: Tossing final prompt...")
    success, response, message = bot.ask(final_prompt)
    if success:
        final_response = response  # Change this line
        print(f"INFO: Response from ChatGPT: {response}")
    else:
        raise RuntimeError(message)

    # prompt user to choose output format
    output_format = input("\nINFO Choose output format (stream / txt / md): ")

    # define maximum length of each response part to be printed at once
    max_response_length = 3000

    if output_format.lower() == "stream":
        # print response parts until the full response is generated
        i = 0
        while i < len(final_response):
            # print next response part
            response_part = final_response[i:i+max_response_length]
            print(response_part)
            i += len(response_part)

            # if there are more response parts, ask the user to continue
            if i < len(final_response):
                user_input = input("INFO: Press enter to continue or type 'quit' to exit: ")
                if user_input.strip().lower() == "quit":
                    break

    # Export the file name as same as the input file name (`file_list[user_input-1]`)
    elif output_format.lower() == "txt":
        # write response to a text file
        with open(file_list[user_input-1] + "_output.txt", "w") as f:
            f.write(final_response)
        print("INFO: Output saved to", file_list[user_input-1])
    elif output_format.lower() == "md":
        # write response to a markdown file
        with open(file_list[user_input-1] + "_output.md", "w") as f:
            f.write(f"\n{final_response}\n")
        print("INFO: Output saved to", file_list[user_input-1])
    else:
        print("ERROR: Invalid output format selected. Please choose 'stream', 'txt', or 'md'.")

if __name__ == "__main__":
    main()
