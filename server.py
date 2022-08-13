import connexion

if __name__ == '__main__':
    # pass
    app = connexion.FlaskApp(__name__, specification_dir='open_api/')
    app.add_api('manager.yaml', validate_responses=True)
    app.run(debug=True)
