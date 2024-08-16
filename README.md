# LFG 

Automate Git add, commit, and push with AI-generated commit messages.

## Quick Setup

- Clone repo: `git clone https://github.com/yourusername/auto_commit.git`
- Install dependencies: `pip install openai python-dotenv`
- Make script executable: `chmod +x lfg.py`
- Add to PATH: `sudo ln -s "$(pwd)/lfg.py" /usr/local/bin/lfg`

## Important: OpenAI API Key

Set your OpenAI API key in your environment:

export OPENAI_API_KEY=your_api_key_here

Add this line to your `~/.bashrc` or `~/.zshrc` for persistence.

## Usage

In any Git repository:
- Run `lfg` to add, commit, and push changes
- Use `lfg -m "Custom message"` for custom commits