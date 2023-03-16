import uuid

employee = [
    {
        "firstName": f"{str(uuid.uuid4())[:8]}name",
        "lastName": f"{str(uuid.uuid4())[:8]}last",
        "email": f"{str(uuid.uuid4())[:8]}@test.com",
        "phoneNumber": "+46827373924",
        "hireDate": "2023-03-01T14:01:00.000Z",
        "salary": 10000,
        "commissionPct": 12345,
        "department": {
            "id": 1,
            "departmentName": "Intensive care unit",
            "location": None,
            "employees": None
        },
        "manager": {
            "id": 1,
            "firstName": "Ramiro",
            "lastName": "Gaylord",
            "email": "Leonora51@hotmail.com",
            "phoneNumber": "Borders",
            "hireDate": "2019-11-04T17:55:36.000Z",
            "salary": 19427,
            "commissionPct": 64996,
            "department": None,
            "jobs": None,
            "manager": None
        }
    }
]
