import connexion

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='git checkout -bgit checkout -b../open_api/')
    app.add_api('api.yaml', validate_responses=True)
    app.run(debug=True)
