# Description

(Instructions not compete yet)

Allowing collaboration on this project will allow me to complete the final features of the project and to tweak some existing features. It will also give me practice in maintaining a project on GitHub. Please follow the below guidelines to help. If you see something that could be reworked please raise it in an issue and get assigned to it before proceeding with any work. Thank you for your contributions. HAPPY LEARNING!

### Python

This project uses Python. Make sure it is installed before working on this project. Check Python version by running: **```python -V```** in the terminal.

*May need to use a virtualenv (instructions)

or

*Use **```pip uninstall -r requirements.txt```** at the end to uninstall what was in the requirements.txt

* May need to create Postgresql database (checking)

## How to Contribute

1. First up you need to fork (make a copy) of this repo to your Github account.

2. Clone (download) your fork to your computer.

3. Set your streams so you can sync your clone with the original repo (get the latest updates) by running the following commands in the terminal:   Or they could already be set depending on your Git integration extensions with your IDE

    * Run **```git remote add upstream```**

    * Run **```git pull upstream master```**

        * These 2 commands will synchronize your forked version of the project with the actual repository.

4. Create a branch: Run **```git branch <insert new branch name>```**

5. Change into the new branch: Run **```git checkout <insert newly created branch name>```**

6. Open the ```mysite/settings.py``` file and scroll to the SECRET_KEY entry and follow the instructions below it to generate a secret key to run the project. Once you have the key insert it after the ```SECRET_KEY``` variable like so: ('SECRET_KEY', **'insert your key between quotes'**) You will need to remove this key before committing this file or just don't commit the ```settings.py``` file to keep your secret key a secret.

7. **DEBUG** will need to be changed to **True** in the **settings.py** file to get the project running locally

8. Scroll down and comment out the current DATABASES section and uncomment the one for local development below it.

****May need to create virtualenv here**** Testing Testing

9. In the terminal Run ***```pip install requirements.txt```*** to install the dependencies for the project.

10. In your terminal: Run: **```python manage.py runserver```** to start the app. You can visit the local link in the browser to view any changes made in real time.

11. Make your changes, Commit, and push the code to your fork. (If you commit the **settings.py** file the SECRET_KEY you generated would need to be deleted and **DEBUG** switched back to **False** before committing.

12. Create a pull request to have your changes merged from your fork into the origin.

