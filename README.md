## Installation

test

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/auto_commit.git
   cd auto_commit
   ```

2. Install the required Python packages:
   ```
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Make the script executable:
   ```
   chmod +x lfg.py
   ```

5. Create a symbolic link to the script in a directory that's in your PATH. For example:
   ```
   sudo ln -s "$(pwd)/lfg.py" /usr/local/bin/lfg
   ```
   Note: You might need to use `sudo` depending on the directory you're linking to.

6. Alternatively, you can add the script's directory to your PATH by adding this line to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`):
   ```
   export PATH="$PATH:/path/to/auto_commit"
   ```
   Remember to replace `/path/to/auto_commit` with the actual path to your script.

7. Reload your shell configuration:
   ```
   source ~/.bashrc  # or ~/.zshrc if you're using Zsh
   ```

## Usage

Now you can use the `lfg` command from anywhere:

1. Navigate to any Git repository.

2. Run the script:
   ```
   lfg
   ```

   This will add all changes, generate a commit message, commit the changes, and push to the remote repository.

3. To use a custom commit message:
   ```
   lfg -m "Your custom commit message"
   ```

4. To see what the script would do without making any changes:
   ```
   lfg --dry-run
   ```

## Testing

To test the script:

1. Create a new Git repository:
   ```
   mkdir test_repo
   cd test_repo
   git init
   ```

2. Create a test file:
   ```
   echo "This is a test file" > test.txt
   ```

3. Run the script:
   ```
   lfg
   ```

4. Check your Git history:
   ```
   git log
   ```

   You should see a new commit with an automatically generated message.

5. Check your remote repository (if you've set one up) to ensure the changes were pushed.
