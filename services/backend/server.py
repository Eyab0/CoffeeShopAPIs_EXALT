import connexion
from auth import validation


def create_app():
    _app = connexion.FlaskApp(__name__, specification_dir='open_api/')
    _app.app.before_request(validation.validate_token)
    _app.add_api('manager.yaml', validate_responses=True)
    _app.add_api('shop.yaml', validate_responses=True)
    _app.add_api('auth.yaml', validate_responses=True)
    return _app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
