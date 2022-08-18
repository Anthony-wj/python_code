def generate_response(status=10000, message="ok", data=None):
    if not data:
        data = []
    return {
        "status": status,
        "message": message,
        "data": data
    }