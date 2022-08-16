from flask import jsonify, request
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_objects(obj, obj_schema):
    """
    get JSON info of all objects
    :param obj
    :param obj_schema
    :return: all objects info
    """

    with db.session_scope() as s:
        _object = s.query(obj).all()
        object_schema = obj_schema()
        result = object_schema.dump(_object, many=True)
        return jsonify(result), 200


def show_object_info(object_id: int, obj, obj_schema):
    """
    show the JSON info for a specific object
    :param obj:
    :param object_id
    :param obj_schema
    :return: object info
    """
    try:
        with db.session_scope() as s:
            _object = s.query(obj).get(object_id)
            if _object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            object_schema = obj_schema()
            result = object_schema.dump(_object)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_object(obj_schema, type: str):
    """
    insert new object into JSON file
    :param type:
    :param obj_schema
    :return:
    """

    try:
        _object = obj_schema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(_object)
        object_schema = obj_schema()
        new_object = object_schema.dump(_object)
        return {
                   "message": f"Created new {type}.",
                   "object": new_object
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_object_info(object_id: int, obj, obj_schema, type: str):
    """
    update the object info
    :param type:
    :param obj_schema:
    :param obj:
    :param object_id: id of the object
    :return: the updated info of the object
    """
    try:
        with db.session_scope() as s:
            _object = s.query(obj).get(object_id)
            if _object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            request.json["id"] = object_id
            object_schema = obj_schema()
            existing_object_deserialized = object_schema.load(request.json, session=db.sess)
            s.merge(existing_object_deserialized)
            new_object_serialize = object_schema.dump(existing_object_deserialized)
            return {
                       "message": f"{type} with id :{object_id} Updated successfully",
                       "object": new_object_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def delete_object_info(object_id: int, obj, type: str):
    """
    delete specific object
    :param obj:
    :param type:
    :param object_id: the id of the object
    :return: all objects info
    """
    try:
        with db.session_scope() as s:
            _object = s.query(obj).get(object_id)
            if object is None:
                raise HTTPRequestError(msg=f" id {object_id} Not Found !!", code=404)
            deleted_id = _object.id
            s.delete(_object)
            return {"message": f"{type} with id :{deleted_id} deleted successfully"}, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
