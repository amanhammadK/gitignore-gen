#!/usr/bin/env python3
import argparse
import requests
import sys

def list_templates():
    """Fetch and print all available .gitignore template names."""
    url = "https://api.github.com/gitignore/templates"
    try:
        response = requests.get(url)
        response.raise_for_status()
        templates = response.json()
        print("Available .gitignore templates:")
        for template in templates:
            print(f"- {template}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching templates: {e}", file=sys.stderr)
        sys.exit(1)

def get_template(name):
    """Fetch and print the content of a specific .gitignore template."""
    url = f"https://api.github.com/gitignore/templates/{name}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error: Template '{name}' not found.", file=sys.stderr)
            sys.exit(1)
        response.raise_for_status()
        data = response.json()
        print(data.get("source", ""))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching template '{name}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Fetch .gitignore templates from GitHub's API."
    )
    parser.add_argument(
        "language",
        nargs="?",
        help="The language/technology name (e.g., Python, Node, Go)."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available template names."
    )

    args = parser.parse_args()

    if args.list:
        list_templates()
    elif args.language:
        get_template(args.language)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
