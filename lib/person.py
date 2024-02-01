#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = name
        self._job = job

    def get_name(self):
        return self._name 

    def set_name(self, name):
        if((name == str) and (1 <= len(name) <= 25)):
            self._name = name.title()
        else:
            print("Name must be string under 25 characters.")

    def get_job(self):
        return self._job 
    
    def set_job(self, jobs):
        if jobs in APPROVED_JOBS:
            self._jobs = jobs
        
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name,)
    job = property(get_job, set_job,)   

guido = Person("Guido", "Sales")
# guido.get_job()