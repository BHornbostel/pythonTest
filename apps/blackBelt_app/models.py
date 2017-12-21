from __future__ import unicode_literals

from django.db import models
import re 
from datetime import datetime 
import bcrypt 

class UserManager(models.Manager): 
    def register(self, first, username, password, confirm):
        response = {
            "valid" : True, 
            "errors" : [],
            "user" : None
        }

        if len(first) < 1: 
            response["errors"].append("First name is required")
        elif len(first) < 2: 
            response["errors"].append("First name must be 2 characters or longer")

        if len(username) < 1: 
            response["errors"].append("Username is required")
        elif len(username) < 3: 
            response["errors"].append("Last name must be 3 characters or longer")

        if len(password) < 1: 
            response["errors"].append("Password is required")
        elif len(password) < 8: 
            response["errors"].append("Password must be 8 characters or longer")

        if len(confirm) < 1: 
            response["errors"].append("Confirm Password is required")
        if confirm != password: 
            response["errors"].append("Confirm Password must match password")

        if len(response["errors"]) > 0: 
            response["valid"] = False 
        else: 
            response["user"] = User.objects.create(
                first_name = first, 
                username = username, 
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )
        return response 

    def login(self,username, password): 
        response = {
            "valid" : True, 
            "errors" : [],
            "user" : None
        }

        if len(username) < 1: 
            response["errors"].append("Username is required")
        else: 
            user_list = User.objects.filter(username=username)
            if len(user_list) == 0: 
                response["errors"].append("Username is already in use.")
        
        if len(password) < 1: 
            response["errors"].append("Password is required")
        elif len(password) < 8: 
            response["errors"].append("Password must be 8 character or longer")

        if len(response["errors"]) == 0:
            hashed_pw = user_list[0].password
            if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
                response["user"] = user_list[0]
            else: 
                response["errors"].append("Password is incorrect")
        if len(response["errors"]) > 0:
            response ["valid"] = False 

        return response

class User(models.Model):
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by= models.ForeignKey(User, related_name='Trips')
    users = models.ManyToManyField(User, related_name="trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

