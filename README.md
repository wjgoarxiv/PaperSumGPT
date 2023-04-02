# PaperSumGPT
<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release/python-360/)

*PaperSumGPT is a tool for abbreviating **scientific paper contents** using ChatGPT, designed to help researchers and students to quickly understand the key points of academic papers.*

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
cd PaperSumGPT/
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
Before using `papersumgpt`, you must run`chatgpt_wrapper` to start the ChatGPT server. You can use the following command to start the server:

```bash
chatgpt install
```
Then, the nightly will be downloaded and installed. AFter that, you can start the server by running the following command:

```bash
chatgpt
```
This is the original functionality of `chatgpt_wrapper`. For more information, please visit the [chatgpt_wrapper github repository](https://github.com/mmabrouk/chatgpt-wrapper).

### (2) Run `papersumgpt` to summarize the content of a paper
After running `chatgpt_wrapper`, you can use `papersumgpt` to summarize the content of a paper. You can use the following command to summarize the content of a paper:

```bash
papersumgpt
```

The tool will process the content summary of the paper and make an output file in the same directory as the input file. 

## Dependencies

- [pyfiglet](https://pypi.org/project/pyfiglet/) - For generating ASCII art of the project name.
- [tabulate](https://pypi.org/project/tabulate/) - For creating clean and readable tables for the output.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading and processing PDF files.
- [chatgpt_wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - An useful open-source unofficial Power CLI, Python API and Flask API that lets us interact programmatically with ChatGPT/GPT4. 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

For more information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/wjgoarxiv/papersumgpt).
