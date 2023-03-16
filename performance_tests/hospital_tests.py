from locust import HttpUser, task, between
from test_data import employee

class MyUser(HttpUser):
    wait_time = between(2, 3)
    
    def on_start(self):
        # authenticate and obtain the bearer token
        json_data = {
            "username": "user",
            "password": "user",
            "rememberMe": False
        }
        response = self.client.post("/authenticate", json=json_data)
        assert response.status_code == 200, f"Authentication failed with status code {response.status_code}."
        self.token = response.json()["id_token"]
    
    def validate_response_code(self, response, expected_response_code):
        if response.status_code == expected_response_code:
            response.success()
        else:
            response.failure(f"Response code was not {expected_response_code}.")
        
    @task(1)
    def get_all_medicines(self):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json, text/plain, */*"
        }
        with self.client.get("/medicines", headers=headers, name="Get All Medicines", catch_response=True) as response:
            self.validate_response_code(response, 200)
        
    @task(1)
    def create_employee(self):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = employee[0].copy()
        with self.client.post("/employees", headers=headers, json=data, name="Create Employee", catch_response=True) as response:
            self.validate_response_code(response, 201)
        
    @task(1)
    def get_all_employees(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        with self.client.get("/employees", headers=headers, name="Get All Employees", catch_response=True) as response:
            self.validate_response_code(response, 200)
