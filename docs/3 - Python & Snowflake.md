Connecting from Python with Snowflake

Before working with the Python script, there are 2 basic steps required:
* create and start a virtual environment
    Python =m venv .venv_sf_int
    on Mac: source .venv_sf_int/bin/activate
    on Windows: run activate.bat

The config.json contains key-value pairs. Replace the values with the ones you created in the previous step:

Run the Python script:

python snowflake_current_user.py -> it will show you the user that is logged in

More detail here: https://medium.com/@bidutch/python-and-snowflake-using-a-configuration-file-69fae82e54f5