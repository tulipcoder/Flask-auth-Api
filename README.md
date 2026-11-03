# Flask-auth-Api

Flask-auth-Api is a Flask user-authentication and course-enrollment application backed by MongoDB. Users register or log in through forms, then browse courses and submit enrollment; the routes read and write the corresponding models and render templates. A REST API also provides user CRUD. The repository includes an aggregation helper for retrieving a user’s enrolled courses, but the shown enrollment route assigns that helper rather than calling it. 

# WorkFlow

[![Architecture diagram](https://gitdiagram.com/diagram-badge.svg)](https://gitdiagram.com/tulipcoder/flask-auth-api?utm_source=readme&utm_medium=badge)


[![Architecture diagram of tulipcoder/flask-auth-api](https://gitdiagram.com/tulipcoder/flask-auth-api/diagram.png)](https://gitdiagram.com/tulipcoder/flask-auth-api?utm_source=readme&utm_medium=picture)
