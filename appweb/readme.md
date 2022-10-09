# How to create an application of Python to .snap

* references: 
    - https://snapcraft.io/docs/python-apps
    - https://snapcraft.io/docs/python-plugin


# Step 1.
Create the file snapcraft.yaml and create a file setup.py

# Step 2.
Set the file.

# Step 3
Run the command to build the snap, the console must be in directorio of your python script folder.
* cd [directorio...]
* command: snapcraft

At the end, an executable .snap is created

# Step 4.
Install the application.
* command: sudo snap install [app_name].snap --devmode --dangerous

If you want uninstall the application, run the following command.
* Uninstall app: sudo snap remove appweb

# Step 5.
Run command of activate of application.
