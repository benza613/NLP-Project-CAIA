# WELCOME TO PROJECT CAIA
# Benito Alvares
You can talk to the chatbot about Weather(RealTime api), Bus transport in chicago (mocked data), small talk


1. Install python 3.6 or 3.7 max 64 bit. Tensorflow currently has some issue with python 3.8

2. Setup necessary virtualenv 
Point to the python 3.6 or 3.7 executable for the virtualenv

virtualenv --system-site-packages -p C:\Users\13129\AppData\Local\Programs\Python\Python37\python.exe ./venv-project-caia

    activate the virtual environment created

make sure pip has the latest version 19.3.x
(venv-project-caia) pip install -U pip

3. Now install Rasa packages (Open Source Machine Learning Framework). Rasa provides http server out-of-the-box
(venv-project-caia) pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

    *****( after this You will need to launch another terminal. Total 2. One for action server and one for chat bot)

4. Now navigate to THIS folder in the current terminal INCASE you arent in it (.caiabot\) to launch the action server
(venv-project-caia) rasa run actions

5. OPEN A NEW TERMINAL AND activate the same environment here
Now to launch the chat bot
(venv-project-caia) rasa shell

Alternatively in the case of error you can first train and then launch the chat bot
(venv-project-caia) rasa train
(venv-project-caia) rasa shell



## POSSIBLE INPUTs:
1. hi
2. hello
3. tell me about the weather in New York
4. weather at Mumbai
5. temperature Sydney
6. I need to get to Madison & Clark
7. How to reach Laflin
8. how do i get to Taylor & Throop
9. how do i get to taylor & throop (Proper noun case sensitive. May not work)
10. are u sure this bus will reach me there ?
11. are u sure
12. can you check
13. See you later
14. Bye bot
15. not really
16. show me a picture of a chicken
17. I changed my mind



## Miscellaneous
if at any time the action server terminal hangs or shows error, Just close the terminal. Ctrl-x/c doesnt kill it. 
Reopen a new terminal, activate environment, navigate inside this folder (.caiabot\) and rasa run actions

to close, exit the chatbot terminal type /stop or Ctrl-x/c. 

## PENDING
- Improve vocabulary
- users feedback to improve conversation patterns and diversity
- Range of inflection
- story augmentation