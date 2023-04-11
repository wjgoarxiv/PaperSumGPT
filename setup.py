from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PaperSumGPT",
    version="1.1.0",
    author="wjgoarxiv",
    author_email="woo_go@yahoo.com",
    description="A tool to abbreviate scientific paper contents using ChatGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjgoarxiv/papersumgpt",
    install_requires=[
        "pyfiglet",
        "tabulate",
        "PyPDF2"
        "fitz",
        "pdf2image",
        "pytesseract",
        "frontend",
        "opencv-contrib-python",
        "pillow",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
    packages=['PaperSumGPT'],
    entry_points={
        'console_scripts': [
            'papersumgpt = PaperSumGPT.__main__:main',
        ],
    },
)
