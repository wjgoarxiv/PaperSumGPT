# PaperSumGPT
<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/release/python-370/)

*PaperSumGPT is a tool for abbreviating **long scientific paper contents** using ChatGPT, designed to help researchers and students to quickly understand the key points of academic papers.*
> **한국 분들은 [여기](README-ko_kr.md)에 있는 문서를 읽어주세요!**

<img src="demorun.gif" width="70%">

## Table of Contents
- [NOTE 1: For ChatGPT free users!](#note-1-for-chatgpt-free-users)
- [NOTE 2: PDF converting functionality revitalized](#note-2-pdf-converting-functionality-revitalized)
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

---
## 🗞️ NOTE 1: For ChatGPT free users!
> ::2023-04-03 updated::

After I tested with several accounts with ChatGPT, I found that there were __significant differences in the performance of ChatGPT__ depending whether the account is a __free user__ or __a paid user (*ChatGPT Plus*)__.

If you are a free user of ChatGPT, and you have a long paper to summarize, I recommend you to upgrade your account to __[ChatGPT Plus](https://openai.com/blog/chatgpt-plus)__ to get a better performance. 

Unfortunately, the free version of ChatGPT cannot understand and store the long context of the input text, which leads to a poor performance; it will export a summary that is NOT related to the input text at all, or it will export an output related to the certain part of the input text.

## 🗞️ NOTE 2: PDF converting functionality revitalized!
> ::2023-04-11 updated::

Using the OpenCV and PyTesseract libraries, I've enhanced the PDF conversion functionality. You can now choose `option 3` in the file type selection!

## 🗞️ NOTE 3: ANSI escape sequences updated!
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

And then, papersumgpt will ask you to choose between `Markdown` or `PDF` as the output format.
```
INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. Plain text (`.txt`) file
    3. PDF (`.pdf`) file

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

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/papersumgpt).
