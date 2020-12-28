# Contribution guidelines

Below you will find instructions on how to contribute.

1. Find an issue to work on, or create one
2. Assign said issue to yourself. This communicates your intent and commitment, so your work does not go to waste
   because it does not fit in with the project, or someone else is already working on it.
3. Set up your development environment:
   1. Clone the repository with ```git clone https://github.com/JonasMuehlmann/pyaoi```
   2. Enter the repository's directory
   3. Create a virtual environment with ```pyhon3 -m venv .venv```
   4. Activate the virtual environment with one of the scripts under ```.venv/bin/```
   6. Install dependencies with ```pip install -r dev-requirements.txt```
   7. Create a new branch with ```git checkout -b your_branch_name```
   8. Set the commit message template with ```git config commit.template .commit_template.txt```
      - Make sure commented out lines are removed with ```git config commit.cleanup strip```
      - Set the comment char with ```git config --global core.commentChar \#```
   9. Install the pre-commit hooks with ```pre-commit install```
   10. Activate commit-msh stage with ```pre-commit install --hook-type commit-msg```

5. Work on the code
6. If you implemented new functionality, write tests to confirm the validity of your new code and preferably:
   2. Add type hints
   3. Write comments if appropriate
   4. Write Docstrings
7. Make a Pull Request (PR) describing your changes
8. Wait for your PR to get reviewed and merged
