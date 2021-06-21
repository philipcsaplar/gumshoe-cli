# Testing Gumshoe Habit Tracker

## Requirements

You will need to have installed the pytest package from the PyPi package repository

```shell
pip install pytest
```

### Test files

You will find a tests directory in the application folder, in it is the test_app.py file, and the test_db.py file.

The test_app.py file is use the test all gumshoe commands and makes sure they are working correctly.

The test_db.py file is used to create a test database with 4 weeks data and 4 different habits, once this has been
executed a test database will be created in the database folder of the gumshoe application folder, the application will
automatically then use this database until it has been removed. 

To testy and run the above files issue the following command in the application folder.

```shell
pytest
```
To remove the test database issue the following command.

```shell
gumshoe remove testdb
```