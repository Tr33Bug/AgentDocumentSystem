"""
CLI for DocumentAgentSystem.
"""
import click

from .agent import DocumentAgentSystem


@click.group()
def cli():
    """DocumentAgentSystem CLI."""
    pass


@cli.command()
@click.argument("codebase_path", type=click.Path(exists=True))
@click.option(
    "--wiki-path",
    default="wiki",
    show_default=True,
    help="Output directory for generated wiki markdown.",
)
def run(codebase_path, wiki_path):
    """
    Run the documentation agent on the given CODEBASE_PATH.
    """
    agent = DocumentAgentSystem(codebase_path, wiki_path)
    agent.run()


if __name__ == "__main__":
    cli()