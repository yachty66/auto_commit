#!/usr/bin/env python3
import json
import argparse
import subprocess
import sys
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), process.returncode


def get_git_diff():
    return run_command("git diff --cached")[0]


def generate_commit_message():
    diff = get_git_diff()
    prompt = f"Based on the following git diff, generate a concise and informative commit message:\n\n{diff}\n\nReturn your response in JSON like {{'commit_message': 'your message'}}:"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Make sure to use an appropriate model
        response_format={"type": "json_object"},
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    json_response = json.loads(response.choices[0].message.content)

    commit_message = json_response["commit_message"]
    return commit_message


def get_git_status():
    return run_command("git status --porcelain")


def main():
    print("testing")
    parser = argparse.ArgumentParser(
        description="LFG - Let's Freakin' Go (Git add, commit, and push)"
    )
    parser.add_argument("-m", "--message", help="Custom commit message")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    args = parser.parse_args()

    commit_message = args.message if args.message else generate_commit_message()

    if args.dry_run:
        pass

    # Perform git operations
    print("Adding all changes...")
    run_command("git add .")

    print(f"Committing with message: {commit_message}")
    _, stderr, rc = run_command(f'git commit -m "{commit_message}"')
    if rc != 0:
        print(f"Error during commit: {stderr}")
        sys.exit(1)

    print("Pushing changes...")
    _, stderr, rc = run_command("git push")
    if rc != 0:
        print(f"Error during push: {stderr}")
        sys.exit(1)

    print("LFG! Changes have been added, committed, and pushed.")


if __name__ == "__main__":
    main()
