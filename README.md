### Avail

### MVP
- [ ] employees can sign in
- [ ] employees can rate work shifts
- [ ] ratings will be shown in a dashboard



### runnning instructions:
- dan, you will need to get vagrant and all the other hb set up stuff done at some point or this will suck
- once you do....
    - in your terminal, cd into vagrant
    - run  ```vagrant up ```
           ```vagrant ssh ```
    - cd into this directory
    - first time, you will need to 
        - ``` virtualenv env ``` to create the env folder
        - ``` source env/bin/activate ``` to run the script to activate the virtual environment
        - ``` pip3 install -r requirements.txt ``` to install all the python libraries
    - to deactivate the env, run ``` deactivate ```
    - next time you want to run the project you only need to 
        - ``` source env/bin/activate ``` to run the script to activate the virtual environment


    