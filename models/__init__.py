from typing import final
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import Executable
db = SQLAlchemy()

##
# @brief Execute Stored Procedure
#
#   Example:
#       session = 
#       params = {
#           'Foo': foo_value,
#           'Bar': bar_value
#       }
#       exec_procedure(session, 'MyProc', params)
#
# @param session
# @param proc_name
# @param params
#
# @return 
def exec_procedure(proc_name, params):
    connection = db.engine.raw_connection()
    session = connection.cursor()
    sql_params = ",".join(["@{0}={1}".format(name, value) for name, value in params.items()])
    sql_string = """
        DECLARE @return_value int;
        EXEC    @return_value = [dbo].[{proc_name}] {params};
        SELECT 'Return Value' = @return_value;
    """.format(proc_name=proc_name, params=sql_params)
    session.execute(sql_string)
    result = list(session.fetchall())
    session.close()
    connection.commit()
    return result

"""
>>> connection = db.engine.raw_connection()
>>> cursor = connection.cursor()
>>> cursor.execute(callstring)
>>> connection.commit()
>>> cursor.close()
>>> connection.close()
>>> callstring
'CALL "StackExchange"."create_user" (1, 1669558683, \'displayname\', \'username\', \'password\')'
>>>
"""

##
# @brief Execute Postgresql Stored Procedures
#
# @param schema 
# @param proc
# @param params: in format: (para1, para2, para3 .. )
#
# @return No error shall return nothing, Errors shall raise Exception
def exec_pro(schema, proc, params):
    connection = db.engine.raw_connection()
    try:
        cursor = connection.cursor()
        callstring = f"CALL \"{schema}\".\"{proc}\" {params}"
        cursor.execute(callstring)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        raise e
    finally:
        connection.close()
    return 


##
# @brief Run Functions
#
# @param schema
# @param func_name
# @param params
#
# @return 
def exec_func(schema, func_name, params):
    connection = db.engine.raw_connection()
    try:
        cursor = connection.cursor()
        callstring = f"SELECT \"{schema}\".{func_name}{params}"
        cursor.execute(callstring)
        connection.commit()
        ret = cursor.fetchall()
        connection.close()
        return ret
    except Exception as e:
        raise e
    finally:
        connection.close()




##
# @brief Deprecated
#
# @param model
# @param filter
#
# @return 
def delete_pro(model, filter):
    session= db.session()
    try:
        session.query(model).filter(filter).delete()
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()
    return


