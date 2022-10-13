from flask import jsonify, request
from services.backend.database import init_db as db
from services.backend.custom_exceptions.HTTPRequestError import HTTPRequestError


def get_objects(model, schema):
    """
    get JSON info of all objects
    :param model : any schema inherent from Base
    :param schema : any schema inherent from SQLAlchemyAutoSchema
    :return: all objects info
    """
    with db.session_scope() as s:
        _object = s.query(model).all()
        result = schema.dump(_object, many=True)
        return jsonify(result), 200


def show_object_info(object_id: int, model, schema):
    """
    show the JSON info for a specific object
    :param model:
    :param object_id
    :param schema
    :return: object info
    """

    try:
        with db.session_scope() as s:
            _object = s.query(model).get(object_id)
            if _object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            result = schema.dump(_object)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_object(schema, controller_type: str):
    """
    insert new object into JSON file
    :param controller_type:
    :param schema
    :return:
    """

    try:
        _object = schema.load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(_object)
        new_object = schema.dump(_object)
        return {
                   "message": f"Created new {controller_type}.",
                   controller_type: new_object
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_object_info(object_id: int, model, schema, controller_type: str):
    """
    update the object info
    :param controller_type:
    :param schema:
    :param model:
    :param object_id: id of the object
    :return: the updated info of the object
    """
    try:
        with db.session_scope() as s:
            _object = s.query(model).get(object_id)
            if _object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            request.json["id"] = object_id
            existing_object_deserialized = schema.load(request.json, session=db.sess)
            s.merge(existing_object_deserialized)
            new_object_serialize = schema.dump(existing_object_deserialized)
            return {
                       "message": f"{controller_type} with id :{object_id} Updated successfully",
                       controller_type: new_object_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def delete_object_info(object_id: int, model, controller_type: str):
    """
    delete specific object
    :param model:
    :param controller_type:
    :param object_id: the id of the object
    :return: all objects info
    """

    try:
        with db.session_scope() as s:
            _object = s.query(model).get(object_id)
            if object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            deleted_id = _object.id
            s.delete(_object)
            return {"message": f"{controller_type} with id :{deleted_id} deleted successfully"}, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
