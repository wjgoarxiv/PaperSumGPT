# PaperSumGPT
<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release/python-360/)

*PaperSumGPT is a tool for abbreviating **long scientific paper contents** using ChatGPT, designed to help researchers and students to quickly understand the key points of academic papers.*

## Table of Contents
- [How to Install](#how-to-install)
  - [(1) Clone this repository](#1-clone-this-repository)
  - [(2) Install dependencies](#2-install-dependencies)
  - [(3) Install PaperSumGPT](#3-install-papersumgpt)
- [Usage](#usage)
  - [(1) Run `chatgpt_wrapper` before using `papersumgpt`](#1-run-chatgpt_wrapper-before-using-papersumgpt)
  - [(2) Run `papersumgpt` to summarize the content of a paper](#2-run-papersumgpt-to-summarize-the-content-of-a-paper)
- [Dependencies](#dependencies)
- [License](#license)

## How to Install

### (1) Clone this repository
You can install PaperSumGPT by cloning this repository and install it from the source:

```bash
git clone https://github.com/wjgoarxiv/papersumgpt.git
```
```bash
cd papersumgpt/
```

### (2) Install dependencies
And you must use `install_old-repo.sh` to install the legacy version of `chatgpt_wrapper`. The new version of `chatgpt_wrapper` is not compatible with the current version of `papersumgpt` (since the new version of `chatgpt_wrapper` will use the ChatGPT API, not the stream-based one).
```bash
chmod +x * 
```
```bash
./install_old-repo.sh
```

### (3) Install PaperSumGPT
Then, you can install PaperSumGPT by running the following command:

```bash
pip install .
```

## Usage
### (1) Run `chatgpt_wrapper` before using `papersumgpt`
Before using `papersumgpt`, you must run `chatgpt_wrapper` to start the ChatGPT server. 

Since you are first running `chatgpt_wrapper` in your computer, you might input the following command to install `playwright`:
```
playwright install
```
The *nightly* will be downloaded and installed in your local machine.

Next, you can use the following command to start the server:

```bash
chatgpt install
```
Login to your ChatGPT account in *Nightly* browser. If you see the chat window, close the browser and type `/exit` to close the `chatgpt_wrapper`. After that, you can restart the `chatgpt_wrapper` by running the following command:

```bash
chatgpt
```
This is the original functionality of `chatgpt_wrapper`. For more information, please visit the [chatgpt_wrapper github repository](https://github.com/mmabrouk/chatgpt-wrapper). 

### (2) Run `papersumgpt` to summarize the content of a paper
After running `chatgpt_wrapper`, you can use `papersumgpt` to summarize the content of a paper. You can use the following command to summarize the content of a paper:

```bash
papersumgpt
```

The following error might occur:
```
------------------------------------------------
ERROR: There is no file in the current directory. Please check the current directory.
------------------------------------------------
```

Note that you must put the paper you want to summarize in the current working directory. In this README, we will use `chatgpt-a+meta+analysis+after+2.5+months.pdf` as an example. Refer to the `ExampleRun/` folder. Copy that file to the current working directory and run `papersumgpt` again:
```bash
papersumgpt
```

And then, papersumgpt will ask you to choose between Markdown or PDF as the output format.
```
INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. PDF (`.pdf`) file

    Note that the option 2 would convert the PDF file to a markdown file using the `PyPDF2` library.
```
Since we have `chatgpt-a+meta+analysis+after+2.5+months.pdf` in the `ExampleRun/` folder, we will choose option 2. The papersumgpt will show the list of pdf files in the current directory and ask you to choose the file you want to summarize. 

```
------------------------------------------------
+---------------+------------------------------------------------+
|   File number | File name                                      |
|---------------+------------------------------------------------|
|             1 | ./chatgpt-a+meta+analysis+after+2.5+months.pdf |
+---------------+------------------------------------------------+
------------------------------------------------

INFO: Please select the file number or press "0" to exit:
```
Then, we will choose option 1. 

```
INFO: The file name that would be utilized is ./chatgpt-a+meta+analysis+after+2.5+months.pdf
------------------------------------------------
INFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n):
```
Now, we have to choose whether to turn on the `verbose` mode. If you turn on the `verbose` mode, the program will print all the intermediate results. If you turn off the `verbose` mode, the program will only print the final result. In this case, we will turn off the `verbose` mode by pressing `n`. 

```
------------------------------------------------
INFO: Please type the number the ChatGPT model that you want to use:

    1. default (Turbo version for ChatGPT Plus users and default version for free users)
    2. gpt4 (Only available for ChatGPT Plus users; a little bit slower than the default model)
    3. legacy (Only available for ChatGPT Plus users; an older version of the default model)

    Note that the option 2 and 3 are NOT available for free users. If you are the free user, please select the option 1.
```
Finally, we will choose the ChatGPT model that we want to use. In this case, we will choose the default model. Press `1` to choose the default model.

```
------------------------------------------------
INFO: Converting the PDF file to a markdown file...
INFO: The PDF file has been converted to a markdown file.
------------------------------------------------
INFO: Please input the maximum length of input text (if don't know, just input 5000):
```
The program automatically converts the PDF file to a markdown format. Then, the program will ask you to input the maximum length of input text. In this case, we will input `5000`. 

```
INFO: Tossing initial prompt...
INFO: ChatGPT started abbreviating the input contents...
INFO: Waiting for ChatGPT to respond for 1/11 part(s)...
INFO: 1/11 part(s) tossed to ChatGPT.
INFO: Waiting for ChatGPT to respond for 2/11 part(s)...
INFO: 2/11 part(s) tossed to ChatGPT.
INFO: Waiting for ChatGPT to respond for 3/11 part(s)...
INFO: 3/11 part(s) tossed to ChatGPT.
INFO: Waiting for ChatGPT to respond for 4/11 part(s)...
...
```
The tool will process the content summary of the paper and make an output file in the same directory as the input file. Let's wait for a while! ☕️

While we are waiting, I have to mention that all these steps are synchronized with your current ChatGPT session in [ChatGPT website](https://chat.openai.com/). You can visit the website later to see all the progresses of the content summary. 

After the abbreviation process is finished, the program will show the following message:

```
INFO Choose output format (stream / txt / md):
```
You can choose the output format by typing `stream`, `txt`, or `md`. In this case, we will choose `md` to output the result as a markdown file.

```
INFO: Output saved to ./chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md
```
You can find `chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md` in the `ExampleRun/` folder. 

Open the markdown file with markdown-compatible editors. You can see the awesome result! 🎉
(Click [here](https://github.com/wjgoarxiv/PaperSumGPT/blob/1e405324852b1c7fdfe32da369703348e0887cd6/ExampleRun/chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md_output.md) to see the output markdown file)

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading and processing PDF files.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/papersumgpt).
