# gitignore-gen 🚀

A simple, powerful CLI tool to fetch `.gitignore` templates directly from GitHub's official API.

![Demo](https://raw.githubusercontent.com/amanhammadK/gitignore-gen/main/demo.gif)

## Features

- 🌍 **Cloud-Powered**: Fetches templates in real-time from GitHub.
- 📋 **List Support**: View all available templates with `--list`.
- 🐍 **Python Based**: Lightweight and easy to run.
- ⚡ **Error Handling**: Graceful handling of unknown languages and network issues.

## Tutorial

### 1. Installation

Ensure you have Python and `requests` installed:

```bash
pip install requests
```

### 2. Usage

#### List all available templates:
```bash
python gitignore-gen.py --list
```

#### Generate a template for a specific language (e.g., Python):
```bash
python gitignore-gen.py Python > .gitignore
```

#### Handle errors:
If you provide an invalid language, the tool will let you know:
```bash
python gitignore-gen.py InvalidLang
# Error: Template 'InvalidLang' not found.
```

## CI/CD Pipeline

This project includes a GitHub Actions workflow that automatically verifies the script on every push.

## License

This project is licensed under the [MIT License](LICENSE).
