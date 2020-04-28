# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!


Barista

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNDFjY2U1NGIxNGMwYzEyNTYzYzBjIiwiYXVkIjoiY29mZmVlLXNob3AiLCJpYXQiOjE1ODc4MjkzNTAsImV4cCI6MTU4NzgzNjU1MCwiYXpwIjoiazlxQ3hkTnBiRFMzNmlHektMN2NTZGQ0NEtuRlZoaXEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlscyJdfQ.eeQ4ZkrspLb5txUdITrTdIfW1srt0MxrZgrI6eImTqtU9D--FprOvISePJxDwuLa_LDdAN1R28gGWdRHp4V5a3u6fzavTgnNHdNdgoTl6MCyY-gMCMkAZmeWJBwpDe12VqpQCehRbci5FBFYtz4R-VfZf2_U4xG7UfdgL4JTvLm-HAhxLSDloHcBjo-GGfH55zZpVQEvEhfZCSP9LU1MOD-iHPMEuOyj4v9QJhDaicSqmG7uJZKJqo-sEbPyEyXYsFEJOzcn9uqHtBfBlURuRVnJbW3U79cn1rhcyd7zo6BEehnKHEcJTcwDe3eQmSMlSnnGkB_Dz_Y1yATzY1TmxQ

manager

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNDViNWY1NGIxNGMwYzEyNTZhZmNkIiwiYXVkIjoiY29mZmVlLXNob3AiLCJpYXQiOjE1ODc4Mjk4NzMsImV4cCI6MTU4NzgzNzA3MywiYXpwIjoiazlxQ3hkTnBiRFMzNmlHektMN2NTZGQ0NEtuRlZoaXEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.YTsuMbV6Nl7Idkxz0Gf4ckAGvxuqTrsu27OTe6F62pGIzrgAdUGF9pJGMKDWR_UwetD35Th91G3uZcHpB_AblLyVpXfZbJARRnoR1RBhlBAZnKbzQ2L7_ss6rBZCF8zz4gssU-oUIxTzkb7Xi_mYcVVJdJVX3HgEdQ6QemUBinOZA6uxwwSbLkay82btyXfZYosXySHG3C2-V7pJRgM7wWJPCXrBNaBr8AX2NF05uS1lCwfB40hhUzFgBwItmewWuBLVfYXGyNjeSA7G94AW8bPxUQ6QjE7no-ZM2KwKVF3BfMDcmynrBdN_lmtXERc5ahIR5pNFH2ngFK5zAVjlZw

<!-- 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1ESTFORFl3TmtKQ00wUkROalV3TlVKRk16ZEdSVU5ETVVKRU5EZzVOVGxFTVRrME5rUXdOZyJ9.eyJpc3MiOiJodHRwczovL2Rldi05OHc5LTVlaC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNDFjY2U1NGIxNGMwYzEyNTYzYzBjIiwiYXVkIjoiY29mZmVlLXNob3AiLCJpYXQiOjE1ODc4Mjk0MDMsImV4cCI6MTU4NzgzNjYwMywiYXpwIjoiazlxQ3hkTnBiRFMzNmlHektMN2NTZGQ0NEtuRlZoaXEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlscyJdfQ.UjN4ibzOBlRqeKR8g068J2LDFJQEQjkqF8NAp46tf6ydV6mE02rBCXUyKCRzarji2tYcH2RvmIYBcXe7h2M71ZYAJaQAjwkzu27mJP3oZpHSVMwyHPxqpseywAHRlYxAtoDNzHTlMn4doz6QAaJiU8T5d_KPb0Hz8FQuAK4Zj5wWvDoCXNng2D_Okgxi1l8yoSt_iDtNSOzHrz78dhyuMw4xsmRZ50bI4RjVOGI-EknXqtmDRHhF0H1AmJAL8LR8XZE4BZgYKQo3npVl1u3jZbahGC30AmNK6ur4-rQ7uWQbc3wIO3x0KuJLUMPu9SJCyFugcgeZ26NwfvPr-kE_-w -->

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
