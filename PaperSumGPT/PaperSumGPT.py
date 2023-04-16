# ------------------ Import libraries ------------------ #
import os
import glob
import pyfiglet
import numpy as np
from tabulate import tabulate
from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.config import Config

# Manipulating PDF
import cv2
import pytesseract as tess
from pdf2image import convert_from_path
from PIL import Image

# For spinning wheel
import sys
import time
import threading

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
print('\nVisit \033[;4mhttps://github.com/wjgoarxiv/papersumgpt\033[0m for more information.')
print('------------------------------------------------')

# Showing spinning_wheel effect

def spinning_wheel(message, stop_event):
    wheel = ['-', '\\', '|', '/']
    i = 0
    while not stop_event.is_set():
        sys.stdout.write('\r' + str(message) + ' ' + str(wheel[i % len(wheel)]))
        sys.stdout.flush()
        time.sleep(0.05)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
    sys.stdout.flush()

def main():
    # Ask user if the brought input file is a markdown file or plain text file 
    print('\n')
    file_type = int(input("""\033[31;1;mINFO: Please type the number the file type that you want to use:\033[0m

    1. Markdown (`.md`) file
    2. Plain text (`.txt`) file
    3. PDF (`.pdf`) file

    : """))
    print('\n')
    print('------------------------------------------------')

    # Print the list of files in the current directory
    if file_type == 1:
        file_list = glob.glob('./*.md')
        file_list = [file.split('\\')[-1] for file in file_list]
        file_list.sort()

    elif file_type == 2:
        file_list = glob.glob('./*.txt')
        file_list = [file.split('\\')[-1] for file in file_list]
        file_list.sort()

    elif file_type == 3:
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
        print('\033[31;1;mERROR: There is no file in the current directory. Please check the current directory.\033[0m')
        print('------------------------------------------------')
        exit()

    # Print the list of files in the current directory
    file_num = [] 
    for i in range(len(file_list)):
        file_num.append(i+1)
    print(tabulate({'File number': file_num, 'File name': file_list}, headers='keys', tablefmt='psql'))
    print('------------------------------------------------')
    user_input = int(input('\n\033[31;1;mINFO: Please select the file number or press "0" to exit: \033[0m'))

    if user_input == 0:
        print("\033[31;1;4mINFO: Exiting the program.\033[0m")
        exit()
    else:
        try: 
            print("\033[31;1;mINFO: The file name that would be utilized is: \033[0m", file_list[user_input-1])
        except:
            print("\033[31;1;mERROR: Your input number is out of range. Please check the file number.\033[0m")
            print("\033[31;1;mERROR: The program will stop.\033[0m")
            exit()

    # Ask user to turn on `verbose` mode. 
    # If the user turns on `verbose` mode, the program will print the intermediate results.
    print('------------------------------------------------')
    verbose = input("\033[31;1;mINFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n): \033[0m")
    if verbose == 'y' or verbose == 'Y':
        verbose = True
    elif verbose == 'n' or verbose == 'N':
        verbose = False
    print('------------------------------------------------')

    # Ask user their desired ChatGPT model
    chatgpt_model = input("""\033[31;1;mINFO: Please type the number the ChatGPT model that you want to use: \033[0m

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
        print("\033[31;1;mERROR: Your input number is out of range. Please check the file number.\033[0m")
        print("\033[31;1;mERROR: The program will stop.\033[31;1;m")
        exit()
    print('------------------------------------------------')

    # ------------------ Convert pdf to markdown ------------------ #
    # This process requires following processes: 
    # 1. Convert pdf to images
    # 2. Perform OCR
    # 3. Convert the images to a markdown file 

    def pdf_to_images(pdf_file):
        return convert_from_path(pdf_file, 500)
    
    def process_image(image):
        # Convert PIL image to OpenCV image
        original_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        rectangular_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        dilated_image = cv2.dilate(threshold_image, rectangular_kernel, iterations=1)

        contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        copied_image = original_image.copy()

        ocr_text = ""

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = copied_image[y:y + h, x:x + w]
            text = tess.image_to_string(cropped, config='--oem 3 --psm 1')
            ocr_text += text

        return ocr_text
    
    def perform_ocr(images):
        ocr_text = ""
        for i, image in enumerate(images):
            text = process_image(image)
            ocr_text += f"Page {i+1}:\n{text}\n\n"
        return ocr_text
    
    if file_type == 3:
        formatted_message = '\033[31;1;mINFO: Converting the PDF file to a markdown file...\033[0m'

        stop_event = threading.Event()
        spinner = threading.Thread(target=spinning_wheel, args=(formatted_message, stop_event))
        spinner.daemon = True
        spinner.start()

        pdf_text = perform_ocr(pdf_to_images(file_list[user_input-1]))

        with open(file_list[user_input-1] + '_markdowned.md', 'w', encoding='utf-8') as f:
            for line in pdf_text:
                f.write(line)

        file_list[user_input-1] = file_list[user_input-1] + '_markdowned.md'

        # ends the spinning wheel with stop_event.set()
        stop_event.set()
        spinner.join()

        print('\033[31;1;mINFO: The PDF file has been converted to a markdown file.\033[0m')
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
    max_length = 7000

    # truncate input text into smaller parts
    input_parts = [input_text[i:i+max_length] for i in range(0, len(input_text), max_length)]

    # define initial prompt message
    initial_prompt = "Please, act as 'High-quality content abbreviator'. Since you have the input limits (OpenAI limited your input limit), you have to firstly take the all the inputs iteratively. To do this, I've already truncated the long inputs into each subpart. You'll now have to take the inputs iteratively. The important thing is that you should NOT answer directly or respond to the previous message. Make sure that you have to accomplish the task when all the inputs are given. I'll let you know if all the inputs are given."

    # send initial prompt message to ChatGPT
    print("\033[31;1;mINFO: Tossing initial prompt...\033[0m")
    success, response, message = bot.ask(initial_prompt)
    if success:
        print(f"\033[31;1;mINFO: ChatGPT started abbreviating the input contents...\033[0m")
    else:
        raise RuntimeError(message)

    # initialize response list
    response_parts = []

    # define prompt message while iterating over input parts and send them to ChatGPT
    for i, part in enumerate(input_parts):
        if i == len(input_parts) - 1:
            # {i+1} / {len(input_parts)} is for the last part of the input contents
            prompt = f"This is the ({i+1} / {len(input_parts)}) part of the truncated input contents. And PLEASE! Do NOT answer and if you understood the input, just keep asking me to input the leftover contents.\n\n```\n{part}\n```\nThank you for taking all the inputs."
        else:
            prompt = f"This is the ({i+1} / {len(input_parts)}) part of the truncated input contents. And PLEASE! Do NOT answer and if you understood the input, just keep asking me to input the leftover contents.\n\n```\n{part}\n```"

        formatted_progressing = f"\033[31;1;mINFO: Progressing... ({i+1}/{len(input_parts)})\033[0m"
        stop_event_2 = threading.Event()
        spinner_2 = threading.Thread(target=spinning_wheel, args=(formatted_progressing, stop_event_2))
        spinner_2.daemon = True
        spinner_2.start()

        # send prompt message and prompt part to ChatGPT
        success, response, message = bot.ask(prompt)
        if success:
            response_parts.append(response)
        else:
            raise RuntimeError(message)

        # Handling the `verbose` mode 
        if verbose == True:
            print(f"\033[31;1;mINFO: Tossed prompt in {i+1}/{len(input_parts)} part(s): {prompt}\033[0m")
            print(f"\033[31;1;mINFO: Response from ChatGPT: {response}\033[0m")
        else:
            pass

        stop_event_2.set()
        spinner_2.join()

    # define final prompt message
    final_prompt = """Now, all the inputs are given to you. You should combine and abbreviate all the inputs by fitting them into the following markdown format. The markdown format is as follows:
    
    ------ TEMPLATE STARTS ------

    # **[TITLE]**
    (Bring the title from the foremost heading in the document. The powerful hint is that the title comes before the people who wrote the document.)

    ## **Introduction**

    ## **Methodology**
    ### **Apparatus**
    ### **Experimental procedure**
    ### **Computational procedure (if exists)**
    ### **Data analysis**

    ## **Results & discussion**

    ## **Conclusions**

    ## **Significance of this study**

    ## **Things to look out for in follow-up research**

    ### **Useful references to consider**
    ...

    ------ TEMPLATE ENDS ------
    You have to write the outputs in a way that the readers can understand the contents easily. Don't forget to miss any important information from inputs. Detailed things that should be noticed would be included in the output (if possible, please bold them with `__BOLD__` or `**BOLD**` markdown marking for clear visibility). Consecutively, if possible, please find some useful references (including title and authors) from the Text or Markdown input file, and re-write them into `### Useful references to consider` subheader. 
    Sort all these things into TABLE format; which will be efficient to understand what is what. Something like this:

    ```markdown 
    | Sections | Abbreviated contents | 
    | :----: | :----: |
    | __Title__ | [TITLE] |
    | __Introduction__ | [INTRODUCTION] |
    | __Methodology__ | [METHODOLOGY] | 
    | __Experimental procedure__ | [EXPERIMENTAL PROCEDURE] |
    | __Computational procedure__ | [COMPUTATIONAL PROCEDURE] | 
    | __Data analysis__ | [DATA ANALYSIS] | 
    | __Results & discussion__ | [RESULTS & DISCUSSION] |
    | __Conclusions__ | [CONCLUSIONS] |
    | __Significance of this study__ | [SIGNIFICANCE OF THIS STUDY] | 
    | __Things to look out for in follow-up research__ | [THINGS TO LOOK OUT FOR IN FOLLOW-UP RESEARCH] | 
    | __Useful references to consider__ | [USEFUL REFERENCES TO CONSIDER] |
    ```

    """

    # send final prompt message to ChatGPT
    print("\033[31;1;mINFO: Tossing final prompt...\033[0m")

    # join response parts to form final response
    # If final response doesn't exist, use the last response part
    try: 
        final_response = response_parts[-1]
    except:
        print("\033[31;1;mERROR: List index out of range. Exiting...\033[0m")
        sys.exit(1)

    success, response, message = bot.ask(final_prompt)
    if success:
        final_response = response  # Change this line
        print(f"INFO: Response from ChatGPT: {response}")
    else:
        raise RuntimeError(message)
    
    count_yes = 0
    again_final_prompt_base = "I think you are not done yet. Please input the leftover contents."

    # Create a variable to store the concatenated responses
    concatenated_responses = ""

    while True: 
        user_input = input("\n\033[31;1;mINFO: Does the answer seem to be truncated? (y/n): \033[0m")
        if user_input.strip().lower() == "y":
            count_yes += 1 
            print("\n\033[31;1;mINFO: Tossing final prompt again...\033[0m")
            last_response_part = response.strip().split()[-1] # Get the last word
            again_final_prompt = f"{again_final_prompt_base}" + "\n" + "However, keep in mind that you SHOULD NOT PRINT THE TEMPLATE that I gave you now on; JUST KEEP GENERATING from the truncated part. NEVER RESTART the conversation. Thank you."
            success, response, message = bot.ask(again_final_prompt)
            if success: 
                # Find the overlapping part between the last response and the new response
                overlap_start = response.find(last_response_part)
                if overlap_start != -1:
                    response = response[overlap_start + len(last_response_part):]

                concatenated_responses += response  # Append the response without the overlapping part to the concatenated_responses
                print(f"\033[31;1;mINFO: Concatenated response from ChatGPT: {concatenated_responses}\033[0m")
            else:
                raise RuntimeError(message)
        elif user_input.strip().lower() == "n":
            break
        else: 
            print("\033[31;1;mERROR: Invalid choice. Please try again.\033[0m")

    # Concatenate all the response parts upto the number of times the user says yes. Direction: end to start
    final_response = final_response + "\n" + concatenated_responses

    # prompt user to choose output format
    output_format = input("\n\033[31;1;mINFO Choose output format (stream / txt / md): \033[0m")

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
                user_input = input("\033[31;1;mINFO: Press enter to continue or type 'quit' to exit: \033[0m")
                if user_input.strip().lower() == "quit":
                    break
                else: 
                    print("\033[31;1;mERROR: Invalid choice. Quitting...\033[0m")

    # Export the file name as same as the input file name (`file_list[user_input-1]`)
    elif output_format.lower() == "txt":
        # write response to a text file
        with open("OUTPUT.txt", "w") as f:
            f.write(final_response)
        print("\033[31;1;mINFO: Output saved to OUTPUT.txt\033[0m")
    elif output_format.lower() == "md":
        # write response to a markdown file
        with open("OUTPUT.md", "w") as f:
            f.write(f"\n{final_response}\n")
        print("\033[31;1;mINFO: Output saved to OUTPUT.md\033[0m")
    else:
        print("\033[31;1;mERROR: Invalid output format selected. Please choose 'stream', 'txt', or 'md'.\033[0m")

if __name__ == "__main__":
    main()