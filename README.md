# PaperSumGPT
<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/release/python-370/)

*PaperSumGPT is a tool for abbreviating **long scientific paper contents** using ChatGPT, designed to help researchers and students to quickly understand the key points of academic papers.*
> **한국 분들은 [여기](README-ko_kr.md)에 있는 문서를 읽어주세요!**

<img src="demorun.gif" width="70%">

## Table of Contents
- [NOTE 1: For ChatGPT free users!](#note-1-for-chatgpt-free-users)
- [NOTE 2: PDF converting functionality deprecated](#note-2-pdf-converting-functionality-deprecated)
- [NOTE 3: ANSI escape sequences updated!](#note-3-ansi-escape-sequences-updated)
- [How to Install](#how-to-install)
  - [(0) For Windows users (first time only!)](#0-for-windows-users-first-time-only)
  - [(1) Clone this repository](#1-clone-this-repository)
  - [(2) Install dependencies](#2-install-dependencies)
  - [(3) Install PaperSumGPT](#3-install-papersumgpt)
- [Usage](#usage)
  - [(1) Run `chatgpt_wrapper` before using `papersumgpt`](#1-run-chatgpt_wrapper-before-using-papersumgpt)
  - [(2) Run `papersumgpt` to summarize the content of a paper](#2-run-papersumgpt-to-summarize-the-content-of-a-paper)
- [Dependencies](#dependencies)
- [License](#license)
- [Extra: The easy way (using ChatGPT splitter)](#extra-the-easy-way-using-chatgpt-splitter)

---
## NOTE 1: For ChatGPT free users!
> ::2023-04-03 updated::

After I tested with several accounts with ChatGPT, I found that there were __significant differences in the performance of ChatGPT__ depending whether the account is a __free user__ or __a paid user (*ChatGPT Plus*)__.

If you are a free user of ChatGPT, and you have a long paper to summarize, I recommend you to upgrade your account to __[ChatGPT Plus](https://openai.com/blog/chatgpt-plus)__ to get a better performance. 

Unfortunately, the free version of ChatGPT cannot understand and store the long context of the input text, which leads to a poor performance; it will export a summary that is NOT related to the input text at all, or it will export an output related to the certain part of the input text.

## NOTE 2: PDF converting functionality deprecated
> ::2023-06-21 updated::

The PDF converting functionality is now deprecated. Instead, I recommend you to use the following online PDF to text converter: 

- [PDF to Text](https://pdftotext.com/)
- [PDF to Text Converter](https://www.pdf2go.com/pdf-to-text)
- [AvePDF](https://avepdf.com/ko/pdf-to-text)

## NOTE 3: ANSI escape sequences updated!
> ::2023-04-12 updated:: 

ANSI escape sequences are now updated to support the rich text formatting of the messages in the terminal. Important notices and warnings are now highlighted in bolded red font. 

---

## How to Install

> If you are using Mac, you can skip [(0) For Windows users](#0-for-windows-users) step.

> ### (0) For Windows users (first time only!)
> Since there are no pre-built binaries for Windows, follow the instructions below to install PaperSumGPT on Windows.
> 1. In the search tab, type `Turn Windows features On (Windows 기능 켜기/끄기 in Korean)`. Then, check the box of `Windows Subsystem for Linux`. 
> 2. Next, reboot your computer.
> 3. Now, you need to install [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW?hl=en-us&gl=kr&rtc=1) in your local computer.
> 4. Open Ubuntu and make your UNIX accounts and passwords.
> 5. For ease of use, you should install `Anaconda` by following instructions. 
>     ```
>     wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
>     ```
>     ```
>     bash Anaconda3-2019.10-Linux-x86_64.sh
>     ```
>     Read all the instructions with Enter and type `yes` to agree with the license.
> 
>     ```
>     source ~/.bashrc
>     ```
> 
>     Now, type
>     ```
>     conda activate
>     ```
>     in your terminal. If you see `(base)` in your terminal, you have successfully installed Anaconda.
> 6. Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/) in your local computer.
>     Download `VcXsrv` installer and run it. <br/>
>     Then, click `Finish`. 
>     
>     Next, open `XLaunch` and click `Next`.
> 
>     After you open `XLaunch`, you should check the following options:
>     - [x] Multiple windows
>     - [x] Start no client
>     - [x] Disable access control
> 
>     Done! Now let's move on to the terminal.
> 
> 7. Type the below commands in your terminal. 
>     ```
>     sudo systemd-machine-id-setup
>     ```
>     ```
>     sudo dbus-uuidgen --ensure
>     ```
>     ```
>     cat /etc/machine-id
>     ```
>     If terminal shows a long string of numbers and letters, you have successfully installed `systemd-machine-id-setup` and `dbus-uuidgen`.
> 
>     Finally, you can install `x11-apps` by typing the following command:
>     ```
>     sudo apt-get install x11-apps xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic
>     ```
> 
>     Add the environment variable `DISPLAY` to your `.bashrc` file by typing the following command:
>     ```
>     echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
>     sudo /etc/init.d/dbus start &> /dev/null" >> ~/.bashrc
>     ```
>     ```
>     source ~/.bashrc
>     ```
> 
>     Test your X11 GUI by typing the following command:
>     ```
>     xeyes
>     ```
>     If you see a pair of eyes, you have successfully installed X11 GUI.
> 
> These steps are essential (in Windows) for successfully executing `playwright` in Windows terminal (which is critical when you configure your `ChatGPT` account).

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

Note that you must put the paper you want to summarize in the current working directory. For a demonstration, we will use `chatgpt-a+meta+analysis+after+2.5+months.txt` as an example. Refer to the `ExampleRun/` folder. A `chatgpt-a+meta+analysis+after+2.5+months.txt` file was prepared by just copying the text contents of `chatgpt-a+meta+analysis+after+2.5+months.pdf` and pasting it into a text file.

Copy that file to the current working directory and run `papersumgpt` again:
```bash
papersumgpt
```

And then, papersumgpt will ask you to choose the file type that you want to use:
```
INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. Plain text (`.txt`) file

:

```
Since we have `chatgpt-a+meta+analysis+after+2.5+months.txt` in the `ExampleRun/` folder, we will choose option 2. The papersumgpt will show the list of text files in the current directory and ask you to choose the file you want to summarize. 

```
------------------------------------------------
+---------------+------------------------------------------------+
|   File number | File name                                      |
|---------------+------------------------------------------------|
|             1 | ./chatgpt-a+meta+analysis+after+2.5+months.txt |
+---------------+------------------------------------------------+
------------------------------------------------

INFO: Please select the file number or press "0" to exit:
```
Then, we will choose option 1. 

```
INFO: The file name that would be utilized is ./chatgpt-a+meta+analysis+after+2.5+months.txt
------------------------------------------------
INFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n):
```
If you want to see the intermediate results, you can type `y`. Otherwise, you can type `n`. In this case, we will type `y` to see the intermediate results.

```text
INFO: Tossing initial prompt...
INFO: ChatGPT started abbreviating the input contents...
INFO: Progressing... (3/11) 
...
```
The tool will process the content summary of the paper and make an output file in the same directory as the input file. Let's wait for a while! ☕️

While we are waiting, I have to mention that all these steps are synchronized with your current ChatGPT session in [ChatGPT website](https://chat.openai.com/). You can visit the website later to see all the progresses of the content summary. 

After the abbreviation process is finished, the program will show the following message:

```text
INFO Choose output format (stream / txt / md):
```
You can choose the output format by typing `stream`, `txt`, or `md`. In this case, we will choose `md` to output the result as a markdown file.

```text
INFO: Output saved to ./chatgpt-a+meta+analysis+after+2.5+months.txt.md
```
You can find `chatgpt-a+meta+analysis+after+2.5+months.txt.md` in the `ExampleRun/` folder. 

Open the markdown file with markdown-compatible editors. You can see the awesome result! 🎉
(Click [here](ExampleRun/chatgpt-a+meta+analysis+after+2.5+months.txt_output.md) to see the output markdown file)

> ### **Output format has been more improved!**
> ::2023-04-16 updated:: <br/>
> Now, the abbreviation result is more improved! Since the prompt has been more enhanced, the abbreviation output is more excellent. You can see the output contents as __table__ format. The table format is more readable and clean. I've also added the updated version of output markdown file in the `ExampleRun/` folder. You can check [here](ExampleRun/[NEW] chatgpt-a+meta+analysis+after+2.5+months_output.md)! 🍾
>
> #### **Output preview**
> 
>> | Sections | Abbreviated contents |
>> | :---: | :---: |
>> | __Title__ | Perception of ChatGPT: An Analysis of Social Media and Scientific Publications |
>> | __Introduction__ | ChatGPT is a chatbot released by OpenAI that has gained over 100 million subscribers in two months. This paper presents a comprehensive analysis of how ChatGPT is perceived based on over 300k tweets and 150+ scientific papers. |
>> | __Methodology__ | The authors used NLP technology to analyze sentiment and emotion in tweets and machine translation systems to analyze tweets in languages other than English. For scientific papers, four co-authors annotated 48 Arxiv and 104 SemanticScholar papers on three dimensions: topic, impact, and quality. |
>> | __Experimental procedure__ | The authors annotated scientific papers using guidelines developed after low agreement in initial annotation rounds. Only paper abstracts were used for classification, and guidelines were developed for prioritizing labels in ambiguous cases. |
>> | __Data analysis__ | ChatGPT is generally perceived positively, with high quality and associated emotions of joy dominating. Its perception has slightly decreased since its debut, and non-English tweets tend to have more negative sentiment. ChatGPT is viewed as a great opportunity across various scientific fields, including the medical domain, but it is also seen as a threat in the education domain and from an ethical perspective. |
>> | __Results & discussion__ | The authors found that ChatGPT is viewed as an opportunity in most scientific fields, but also as a threat from an ethical perspective and in education. ChatGPT is mostly perceived positively on social media, with some decrease in positivity since its debut. |
>> | __Conclusions__ | This analysis contributes to shaping the public debate and informing the future development of ChatGPT. Future work should investigate trends over longer periods, consider popularity of tweets and papers, and investigate additional dimensions beyond sentiment and emotion. |
>> | __Significance of this study__ | This study provides insights into the perception of a highly popular chatbot, which can inform future development and public debate surrounding AI language models. |
>> | __Things to look out for in follow-up research__ | Future research should investigate the real impact of language models like ChatGPT on society, including their potential to exacerbate or mitigate existing inequalities and biases. |
>> | __Useful references to consider__ | Haque et al. (2022), Borji (2023), Bowman (2022), Beese et al. (2022) |

> ### NOTES
> Note that ChatGPT sometimes makes undesired outputs. In this case, you should try a few times to get the best result. Good luck with your research! 🚀

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Extra: The EASY way (using ChatGPT splitter)
> ::2023-09-15 updated:: 

You can even achieve the same results even without installing `papersumgpt`! 

Thanks to the website [ChatGPT splitter](https://chatgpt-prompt-splitter.jjdiaz.dev/), you can easily summarize the contents of a paper (but it requires you to click the splitted contents manually :) ). Here how you can do it: 

1. Convert the paper texts & contents by using PDF-to-text converter. You can visit any of the following websites: 
    - [PDF to Text](https://pdftotext.com/)
    - [PDF to Text Converter](https://www.pdf2go.com/pdf-to-text)
    - [AvePDF](https://avepdf.com/ko/pdf-to-text)

2. Save the converted text file into your local computer with the file type `.txt` (`.md` is also possible).

3. Next, visit [ChatGPT splitter](https://chatgptsplitter.com/) website, and click `Upload file(s)` button (or you can paste the text contents into the `Or paste your text` section).

4. Into the `Prompt` section, paste the following prompt: 
    ```
    Please, act as 'High-quality content abbreviator'. Since you have the input limits (OpenAI limited your input limit), you have to firstly take the all the inputs iteratively. To do this, I've already truncated the long inputs into each subpart. You'll now have to take the inputs iteratively. The important thing is that you should NOT answer directly or respond to the previous message. Make sure that you have to accomplish the task when all the inputs are given. I'll let you know if all the inputs are given.
    ```

5. Click `Process` button! 

6. The truncated texts would be splitted into several parts. You can click the `Copy` button to copy the splitted contents, and iteratively paste the contents into the ChatGPT (this takes time and effort).

7. If you pasted the final chunk, then you can copy either of the following **final prompts** that I've prepared:

    **(1) Tabulated version**
    ```
    Now, all the inputs are given to you. You should combine and abbreviate all the inputs by fitting them into the following markdown format. The markdown format is as follows:
    
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

    **(2) Abbreviated markdown version** 
    ```
    Now, all the inputs are given to you. You should combine and abbreviate all the inputs by fitting them into the following format. Note that you have to write the outputs __assuming you are making a paper sharing powerpoint presentation (ppt) for the audience__. You have to make audiences understand the content and methodology of this paper very well. Therefore, clearly abbreviate and express the important information only. Thank you for your consideration.
    
    ```markdown
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
    ```

8. That's it! You can see the awesome results! 🎉

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/papersumgpt).
