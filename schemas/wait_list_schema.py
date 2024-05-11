def individual_serial(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "emailId": user["emailId"],
    }

def list_serial(wait_list) -> list:
    return [individual_serial(user) for user in wait_list]