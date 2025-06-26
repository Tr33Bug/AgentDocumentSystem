"""
DocumentAgentSystem: A tool to automatically document a Python codebase using LLMs.
"""
import os
from pathlib import Path

import openai
from dotenv import load_dotenv
from rich.console import Console


def call_llm(prompt: str, model: str = "gpt-4") -> str:
    """
    Call the OpenAI LLM with the given prompt and return the response text.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


class DocumentAgentSystem:
    def __init__(self, codebase_path: str, wiki_path: str = "wiki"):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not set. Please set it in environment or .env file."
            )
        openai.api_key = api_key
        self.codebase_path = Path(codebase_path)
        self.wiki_path = Path(wiki_path)
        self.console = Console()
        self.wiki_path.mkdir(exist_ok=True)

    def run(self):
        """
        Execute the full documentation workflow.
        """
        self.console.print("[bold green]Starting DocumentAgentSystem workflow...[/]")
        steps = [
            self.analyze_structure,
            self.isolate_and_test,
            self.write_docstrings,
            self.generate_wiki,
            self.generate_get_started,
        ]
        for step in steps:
            self.console.print(f"[bold blue]Running step: {step.__name__}[/]")
            step()
        self.console.print("[bold green]Documentation generation complete![/]")

    def analyze_structure(self):
        """
        Analyze the codebase structure and write an overview to structure.md.
        """
        py_files = [
            str(p.relative_to(self.codebase_path))
            for p in self.codebase_path.rglob("*.py")
        ]
        prompt = (
            "Analyze the following Python codebase structure and provide a brief overview:\n"
            + "\n".join(py_files)
        )
        result = call_llm(prompt)
        (self.wiki_path / "structure.md").write_text(result)

    def isolate_and_test(self):
        """
        Generate pytest stubs for key functions and write to tests.md.
        """
        prompt = (
            "Generate pytest test stubs for the key functions in the codebase."
        )
        result = call_llm(prompt)
        (self.wiki_path / "tests.md").write_text(result)

    def write_docstrings(self):
        """
        Write helpful Python docstrings for functions and classes in the codebase.
        """
        prompt = (
            "Write helpful Python docstrings for each function and class in the codebase."
        )
        result = call_llm(prompt)
        (self.wiki_path / "docstrings.md").write_text(result)

    def generate_wiki(self):
        """
        Generate a technical documentation wiki in markdown.
        """
        prompt = (
            "Based on previous analysis and tests, write a technical documentation wiki in markdown."
        )
        result = call_llm(prompt)
        (self.wiki_path / "overview.md").write_text(result)

    def generate_get_started(self):
        """
        Generate a Get Started guide for the documented codebase.
        """
        prompt = (
            "Write a Get Started guide for developers using this documented codebase."
        )
        result = call_llm(prompt)
        (self.wiki_path / "get_started.md").write_text(result)