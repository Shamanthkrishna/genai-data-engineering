import pandas as pd
import random
from faker import Faker
import os

class DataGenerator:
    def __init__(self, out_dir="data/synthetic"):
        self.fake = Faker()
        self.out_dir = out_dir
        os.makedirs(out_dir, exist_ok=True)

    def generate_employees(self, n=100):
        data = []
        for _ in range(n):
            data.append({
                "employee_id": self.fake.uuid4(),
                "name": self.fake.name(),
                "department": random.choice(["HR", "Sales", "IT", "Finance"]),
                "salary": random.randint(40000, 120000),
                "joining_date": self.fake.date_this_decade()
            })
        df = pd.DataFrame(data)
        path = os.path.join(self.out_dir, "employees.csv")
        df.to_csv(path, index=False)
        return path, df
