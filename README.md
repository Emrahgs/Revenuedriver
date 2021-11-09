# Revenuedriver

To run this application on your computer, MySQL database has to be installed on your computer.
If it is not installed yet on your computer, please run these commands on your terminal:
1. sudo apt update
2. sudo apt install mysql-server

After you have installed MySQL, run these commands:
    sudo mysql -u root 
    USE mysql;
    UPDATE user SET plugin='mysql_native_password' WHERE User='root';
    FLUSH PRIVILEGES;
    exit;
    sudo service mysql restart

Then you should create, activate virtual environment and install requirements.txt into the virtual environment using these commands:
    1. python -m venv venv
    2. . venv/bin/activate
    3. pip install -r requirements.txt

To start the application, run this command:
    pyhton task.py