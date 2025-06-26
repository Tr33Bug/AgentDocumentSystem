# DocumentAgentSystem

## Motivation

Code documentation with LLMs often dosnt hold up and is often not helpfull. If your codebase is similar or a different reimplementation of a public codebase or framework, llms often expect the things how they learned that. 

This project aims to create a LLM Agent system that goes through a codebase and documents systematically through testing parts of the codebase in isolated way. 

Goal is to try and test functions and code snippets. Going thourg the codebase and step by step building a documentation. The documentation should be added in form of docstrings in the code and as a markdown wiki in the folder ./wiki .

The System has the following workflow: 
1. Understand the general structure of the codebase
2. Isolate parts of the codebase and test them. If external ressources are needed, simulate them. 
3. Write Docstrings/Comments in the code to document the isolated parts. Add the test examples to the 
4. Understand and test how the isolated parts are working together and write a md wiki from that in ./wiki .
5. Write a "Get Started" md file to give a developer a good starting point for understanding of the codebase.
6. The whole documentation should be in the style of a technical documentation and should be good enough to be hosted in the internet as help for the given codebase. 

Input of the System: 
Undocumented Codebase 

output: 
Documented Codebase

Importand: Dont clutter the code with unhelpfull comments. Just give clean and helpfull comments.

## Installation

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set OPENAI_API_KEY
```

## Usage

Run the documentation agent on your codebase:

```bash
python -m document_agent_system.cli run /path/to/your/codebase --wiki-path ./wiki
```
