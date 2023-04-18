# PaperSumGPT
<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/release/python-370/)

*PaperSumGPT는 ChatGPT를 사용하여 **긴 과학 논문 내용**을 줄여주는 도구입니다. 연구자와 학생분들이 학술 논문의 요점을 빠르게 이해할 수 있기를 기원합니다!*

## 목차
- [몇 가지 알림 사항들](#몇-가지-알림-사항들)
- [설치 방법](#설치-방법)
- [(0) Windows 사용자분들께 (처음 사용하는 경우에만)](#0-Windows-사용자분들께-처음-사용하는-경우에만)
- [(1) 리포지토리 복사하기](#1-리포지토리-복사하기)
- [(2) 설치 종속](#2-설치-종속)
- [(3) PaperSumGPT 설치하기](#3-PaperSumGPT-설치하기)
- [사용법](#사용법)
- [(1) chatgpt wrapper 실행](#1-chatgpt-wrapper-실행)
- [(2) PaperSumGPT 실행하기](#2-PaperSumGPT-실행하기)
- [Dependencies](#dependencies)
- [License](#license)

---
## 몇 가지 알림 사항들
__ChatGPT 무료 사용자분들께__
> ::2023-04-03 업데이트::

ChatGPT를 여러 계정으로 테스트한 결과 계정이 **무료 사용자**인지 **유료 사용자인지(*ChatGPT 플러스*)** 인지에 따라 __ChatGPT 성능에 상당한 차이__ 가 있었습니다. 

따라서, 만약 여러분이 ChatGPT 무료사용자이며, 요약해야 할 논문이 길다면 (1) 계정을 __[ChatGPT 플러스](https://openai.com/blog/chatgpt-plus)__, 또는 (2) __[입력 텍스트의 최대 길이](#2-run-run-inputumpt-to-the-the-paper-to-the-the-the-the-paper-to-the-paper)__ 를 최대 `7,000~8,000자` 까지 입력해보시길 권장드립니다. 

~~안타깝게도 현재 ChatGPT의 무료 버전은 입력 텍스트의 긴 컨텍스트를 이해하고 잘 저장하지 못하므로, 성공적인 결과를 기대하기가 어렵습니다. 예를 들어, 입력 텍스트와 전혀 관련이 없는 요약을 내보낸다든지, 입력 텍스트의 특정 부분만 고려한 출력을 내보내고는 합니다.~~

__PDF 변환 기능 재활성화__
> ::2023-04-11 업데이트::
> 
OpenCV 및 PyTesseract 라이브러리를 사용하여 PDF 변환 기능을 향상시켰습니다. 이제 파일 형식 선택에서 '옵션 3'을 선택할 수 있습니다.
그러나, 더 나은 결과를 위해선 직접 정돈한 `.md` 및 `.txt` 파일을 사용하는 것이 효과적입니다. OCR이 아무리 잘 되어도 오타나 이상한 문자들이 포함될 수 있기 때문입니다.
PDF 선택은 편의를 위해서만 사용하세요.

---

## 설치 방법

> Mac을 사용하시는 경우 [(0) Windows 사용자분들께 (처음 사용하는 경우에만)](#0-Windows-사용자분들께-처음-사용하는-경우에만-해당)
 섹션을 건너뛰시면 됩니다. 

> ### (0) Windows 사용자분들께 (처음 사용하는 경우에만 해당)
> Windows에는 사전에 설치된 리눅스 프로그램이 없기 때문에, 아래 지침을 따라주셔야만 정상적인 프로그램 이용이 가능합니다.
> 1. 검색 탭에서 'Windows 기능 켜기/끄기'를 입력합니다. 그런 다음 "Windows Subsystem for Linux" 확인란을 선택합니다.
> 2. 컴퓨터를 재부팅합니다.
> 3. 이제 로컬 컴퓨터에 [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW?hl=en-us&gl=kr&rtc=1) 를 설치합니다.
> 4. Ubuntu를 열고 UNIX 계정과 암호를 만듭니다.
> 5. 사용 편의를 위해 아나콘다도 설치해주세요. 터미널에 다음과 같은 명령어들을 순서대로 입력합니다. 
>> ```
>> wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
>> ```
>> ```
>> bash Anaconda3-2019.10-Linux-x86_64.sh
>> ```
>> Enter 키로 모든 지침을 읽은 후, yes를 입력하여 라이센스에 동의합니다.
>>
>> ```
>> source ~/.bashrc
>> ```
>>
>> 아래와 같이 conda를 활성화합니다.
>> ```
>> conda activate
>> ```
>> 터미널에 `(base)`가 표시되면 성공적으로 아나콘다가 설치된 것입니다. 
> 
> 6. [VcXsrv](https://sourceforge.net/projects/vcxsrv/) 를 로컬 컴퓨터에 설치합니다.
> 'VcXsrv' instra를 다운로드하여 실행합니다. <br/>
>> 완료 버튼을 누릅니다. 
>>
>> Windows에서 'Xlaunch'를 열고 'Next'를 클릭합니다.
>>
>> 'Xlaunch'를 연 후 다음과 같은 옵션들이 체크되어 있는지 확인합니다. <br/>
>>     - [x] Multiple windows <br/>
>>     - [x] Start no client <br/>
>>     - [x] Disable access control <br/>
>>
> 이제 터미널로 이동한 후...
>
> 7. 다음 명령을 입력합니다.
>> ```
>> sudo systemd-machine-id-setup
>> ```
>> ```
>> sudo dbus-uuidgen --ensure
>> ```
>> ```
>> cat /etc/machine-id
>> ```
>> 터미널에 긴 문자열의 숫자와 문자가 출력된다면 `systemd-machine-id-setup` 및 `dbus-uuidgen`가 잘 설치된 것입니다. 
>>
>>
>> 이제 다음 명령을 입력하여 `x11-apps`를 설치할 수 있습니다:
>> ```
>> sudo apt-get install x11-apps xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic
>> ```
>>
>> 다음 명령들을 입력하여 환경 변수 `DISPLAY`를 `.bashrc` 파일에 추가합니다:
>> ```
>> echo "export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
>> sudo /etc/init.d/dbus start &> /dev/null" >> ~/.bashrc
>> ```
>> ```
>> source ~/.bashrc
>> ```
>>
>> 다음 명령을 입력하여 X11 GUI를 테스트합니다:
>> ```
>> xeyes
>> ```
>> 마우스를 따라 움직이는 눈이 보인다면, X11 GUI가 성공적으로 설치된 것입니다! 

> 이 절차들은 Windows 터미널에서 `playwright`를 성공적으로 실행하기 위해 꼭 필요합니다 (ChatGPT 계정 입력 시 중요). 귀찮더라도 따라주시면 정상적인 프로그램 이용이 가능해집니다. 

### (1) 리포지토리 복사하기
다음과 같이 터미널에 입력하여 이 리포지토리를 통째로 복사해주세요.
```bash
git clone https://github.com/wjgoarxiv/papersumgpt.git
```
```bash
cd papersumgpt/
```

### (2) 설치 종속
정상적인 프로그램을 위해, `install_old-repo.sh`를 실행하여 옛날 버전의 `chatgpt_wrapper`를 설치해주어야 합니다. 최신 버전의 `chatgpt_messages`는 현재 버전의 `papersumgpt`와 호환되지 않습니다. 

```bash
chmod +x * 
```
```bash
./install_old-repo.sh
```

### (3) PaperSumGPT 설치하기
다음과 같이 터미널에 입력하여 `papersumgpt`를 설치해주세요.

```bash
pip install .
```

## 사용법
### (1) chatgpt wrapper 실행
`papersumgpt` 사용 전, `chatgpt_wrapper`를 실행하여 ChatGPT 서버를 시작해주세요.

컴퓨터에 `playwright`가 설치되어 있지 않다면, 다음과 같이 터미널에 입력하여 `playwright`를 설치해주세요.
```
playwright install
```
*nightly*가 컴퓨터에 설치되고, `playwright`가 실행 가능해집니다.

이제 다음과 같이 입력한 후, ChatGPT 계정을 입력해주세요.

```bash
chatgpt install
```
*nightly* 브라우저에서 ChatGPT 계정을 통해 로그인 후, `chatgpt_wrapper`를 실행합니다. 

```bash
chatgpt
```
여기까지는 기존 `chatgpt_wrapper`의 기능과 동일합니다. 상세한 내용을 위해서는 [chatgpt_wrapper github repository](https://github.com/mmabrouk/chatgpt-wrapper)를 참고해주세요.

이제 터미널에 실행되어 있는 `chatgpt_wrapper`를 종료해줍니다. 종료를 위해서는 `/exit`을 입력해주세요.

### (2) PaperSumGPT 실행하기
이제 `papersumgpt`를 사용하여 논문 요약을 진행할 준비가 되었습니다. 다음을 입력하여 `papersumgpt`를 실행해주세요.

```bash
papersumgpt
```

아마 현재 디렉토리에 논문이 없기 때문에, 다음과 같은 에러 메시지가 출력될 것입니다.
```
------------------------------------------------
ERROR: There is no file in the current directory. Please check the current directory.
------------------------------------------------
```

프로그램이 input 파일을 인식할 수 있도록, 논문 파일을 현재 디렉토리에 놓아주세요. 이 리포지토리 내에 있는 `chatgpt-a+meta+analysis+after+2.5+months.pdf`를 예시 파일로 활용하겠습니다. `ExampleRun/` 폴더 내부를 확인해보세요. 논문 파일을 현재 디렉토리에 옮겨준 후, 다음을 입력하여 `papersumgpt`를 실행해주세요.

```bash
papersumgpt
```

그럼 다음과 같이 논문 파일의 종류를 선택할 수 있는 메뉴가 출력될 것입니다.
```
INFO: Please type the number the file type that you want to use:

    1. Markdown (`.md`) file
    2. PDF (`.pdf`) file

    Note that the option 2 would convert the PDF file to a markdown file using the `PyPDF2` library.
```
PDF 파일을 사용할 것이므로, 2번을 선택해줍니다.

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
1번 파일을 선택하여 input으로 활용하겠습니다.

```
INFO: The file name that would be utilized is ./chatgpt-a+meta+analysis+after+2.5+months.pdf
------------------------------------------------
INFO: Do you want to turn on `verbose` mode? If you turn on `verbose` mode, the program will print the intermediate results. (y/n):
```
`verbose` 모드란, 프로그램이 진행되는 과정을 모두 보여주는 모드입니다. `verbose` 모드를 켜면, 프로그램이 진행되는 과정을 보여주기 때문에, 프로그램이 어떻게 작동하는지 확인할 수 있습니다. `verbose` 모드를 켜고 싶다면, `y`를 입력해주세요. `verbose` 모드를 끄고 싶다면, `n`을 입력해주세요.

```
------------------------------------------------
INFO: Please type the number the ChatGPT model that you want to use:

    1. default (Turbo version for ChatGPT Plus users and default version for free users)
    2. gpt4 (Only available for ChatGPT Plus users; a little bit slower than the default model)
    3. legacy (Only available for ChatGPT Plus users; an older version of the default model)

    Note that the option 2 and 3 are NOT available for free users. If you are the free user, please select the option 1.
```
마지막으로, 우리가 사용할 ChatGPT 모델을 선택해줍니다. 여기서는 `default` 모델을 사용하겠습니다.

```
------------------------------------------------
INFO: Converting the PDF file to a markdown file...
INFO: The PDF file has been converted to a markdown file.
------------------------------------------------
INFO: Please input the maximum length of input text (if don't know, just input 5000):
```
이제 프로그램이 PDF 파일에서 텍스트만을 추출해 Markdown 포맷으로 변경해줍니다. `maximum length`란, 긴 논문을 얼마만큼의 글자 수로 분할 시킬 것인지를 의미합니다. 여기서는 `5000`을 넣도록 하겠습니다.

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
프로그램이 답변을 얻어낼 동안, 잠시 기다려보죠! ☕️

답변이 형성되는 동안, 한 가지 언급드리자면, `papersumgpt`가 입/출력 하는 모든 내용은 여러분의 ChatGPT 계정에 실시간으로 반영이 됩니다. https://chat.openai.com/ 를 참고해보세요. 

요약이 모두 완료되면, 

```
INFO Choose output format (stream / txt / md):
```
`stream`, `txt`, or `md` 중 하나를 타이핑하여 출력할 파일의 형태를 고를 수 있습니다. 저희는 `.md` 파일 형식을 출력 파일 타입으로 지정하겠습니다. 

```
INFO: Output saved to ./chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md
```
`ExampleRun/` 폴더 안에 있는 `chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md`를 확인해보세요!

마크다운 에디터를 열어 출력 파일 내용을 모두 복사해 붙여 넣어보세요. 🎉
(Click [여기](ExampleRun/chatgpt-a+meta+analysis+after+2.5+months.pdf_markdowned.md_output.md) 를 누르시면, 출력 파일 에시를 확인해보실 수 있습니다. 

때때로, ChatGPT는 완벽하지 못한 답변을 도출할 수도 있습니다. 여러분의 연구에 이 프로그램이 큰 도움이 되기를 기원합니다! 🚀

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading and processing PDF files.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

더 많은 정보를 얻고 싶으시거나 피드백을 남기시고 싶으시면, [제 깃허브 링크](https://github.com/wjgoarxiv/papersumgpt) 에 방문해주세요! 감사합니다.  
