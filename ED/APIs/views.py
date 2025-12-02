import json
import time
import hashlib
from django.http import JsonResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from DecesionTree import *
from PredectionCode import *
from helpers.sendMail import *
from helpers.jwtEncoder import *
from helpers.generateOTP import *
from APIs.models import *
from helpers.data.GETData_from_DB import *

from pymongo import MongoClient

@csrf_exempt
def loginApi(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'username' in data and 'password' in data:
                username = data['username']
                password = data['password']
                grant_type = data['grant_type']
                remember_me = data['remember_me']

                # Query MongoDB to find the user by username
                query = {'email': username}
                user = getDataWithoutProjection(collection_Register,query) 
                            
                if user:
                     # If email exists, fetch the information
                    firstname = user.get('firstname', 'N/A')
                    lastname = user.get('lastname', 'N/A')
                    phonenumber = user.get('phonenumber', 'N/A')
                    photoFileName = user.get('profilephoto', 'N/A')
                    Role = user.get('role', 'N/A')
                    
                    # Check if the password matches (assuming passwords are hashed)
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    if hashed_password == user['password']:
                        # Passwords match, login successful
                        print(remember_me)
                        if(remember_me):
                            ExpireTime = 1296000 # 1296000 seconds 15 days.
                        else:
                            ExpireTime = 3600 # 3600 seconds 1 hour.

                        exp_time = round(time.time()) + ExpireTime
                        acc_time = round(time.time())
                        # Claims set (Payload)
                        JsonData = {
                            "email" : username,
                            "sub" : "TOKEN",
                            "acc_time" : acc_time,
                            "exp_time" : exp_time
                        }

                        Token = encodeData(JsonData)
                        collection_Login.update_one(
                            {'username': username},  # Filter to find the document
                            {
                                '$set': {
                                    'password': hashlib.sha256(password.encode()).hexdigest(),
                                    'grant_type': grant_type,
                                    'time': int(time.time()),
                                    'token': Token,
                                    'remember_me': remember_me
                                }
                            },
                            upsert=True  # Insert the document if it doesn't exist
                        )

                        if('ALL_USER_INFO' in grant_type):
                            return JsonResponse({"message": "Login successful","Token":Token,"token_type": "bearer","Userdetails":{"email":username, "firstname":firstname, "lastname":lastname, "phonenumber":phonenumber, "profile_image":photoFileName},"accessTime":time.time(),"expires_in": ExpireTime, "Role":Role}, status=200)
                        elif("AUTH_ONLY" in grant_type):
                            return JsonResponse({"message": "Login successful","Token":Token,"token_type": "bearer","accessTime":time.time(),"expires_in": ExpireTime, "Role":Role}, status=200)
                        else:
                           return JsonResponse({"message": "Required Grant Type"}) 
                    else:
                        # Passwords don't match
                        return JsonResponse({"message": "Login failed. Incorrect password."}, status=401)
                else:
                    # User not found
                    return JsonResponse({"message": "Login failed. User not found."}, status=404)
            else:
                # Username or password not provided
                return JsonResponse({"message": "Username and password are required."}, status=400)
        except Exception as e:
            # Handle any other exceptions
            return JsonResponse({"message": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=500)
    


@csrf_exempt
def registerApi(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'email' in data and 'password' in data:
                emailCheck =  getDataWithoutProjection(collection_Register,{'email': data['email']})
                phonenuCheck = getDataWithoutProjection(collection_Register,{'email': data['phone_number']})
                if(emailCheck == None and phonenuCheck == None):
                    # Encrypt the password using SHA256
                    password = data['password']
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()

                    # Create a new Register instance with the provided data
                    Register(
                        firstname=data.get('firstname', ''),
                        lastname=data.get('lastname', ''),
                        email=data['email'],
                        password=hashed_password,  # Store the hashed password
                        phonenumber=data.get('phone_number', ''),
                        role = data.get('role', ''),
                        timestamp = time.time(),
                        profilephoto = data.get('profilephoto', ''),
                    ).save()  # Save the new Register instance
                    return JsonResponse({"message": "User registered successfully"})
                else:
                    return JsonResponse({"message":"User already registered with the email or Phone Number"}, status=203)
            else:
                return JsonResponse({"message": "Email and password are required"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        

    elif request.method == 'PATCH':

        data = json.loads(request.body)
        event = data['event']

        if(event == "PASSWORD UPDATE"):
            email = data['email']
            password = data['password']
            

            if 'email' in data and 'password' in data:
                emailCheck = getDataWithoutProjection(collection_Register,{'email': data['email']})
                if(emailCheck != None):
                    result = collection_Register.update_one(
                    {'email': email},       # Filter to find the user by email
                    {'$set': {'password': hashlib.sha256(password.encode()).hexdigest()}}
                    )
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
                if result.matched_count > 0:
                    if result.modified_count > 0:
                        return JsonResponse({"message":"Password updated successfully"},status=200)
                    else:
                        return JsonResponse({"message":"Password was already up to date"},status=208)
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
            else:
                return JsonResponse({"message": "Email-Id and password are required"}, status=400)
        
        elif (event == "PROFILE IMAGE UPDATE"):
            email = data['email']
            profilephoto = data['profilephoto']

            if 'email' in data and 'profilephoto' in data:
                emailCheck = getDataWithoutProjection(collection_Register,{'email': data['email']})
                if(emailCheck != None):
                    result = collection_Register.update_one(
                    {'email': email},       # Filter to find the user by email
                    {'$set': {'profilephoto':profilephoto}}
                    )
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
                if result.matched_count > 0:
                    if result.modified_count > 0:
                        return JsonResponse({"message":"Image updated successfully"},status=200)
                    else:
                        return JsonResponse({"message":"Image was already up to date"},status=202)
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
            else:
                return JsonResponse({"message": "Email-Id and password are required"}, status=400)

        elif (event == "USER DETAILS UPDATE"):
            email = data['email']
            if 'email' in data:
                emailCheck = getDataWithoutProjection(collection_Register,{'email': data['email']})
                first_name = data['firstname']
                last_name = data['lastname']
                email = data['email']
                phone_number = data['phone_number']
                if(emailCheck != None):
                    result = collection_Register.update_one(
                    {'email': email},       # Filter to find the user by email
                    {'$set': {'first_name':first_name, 'last_name':last_name, 'phone_number':phone_number}}
                    )
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
                if result.matched_count > 0:
                    if result.modified_count > 0:
                        return JsonResponse({"message":"Details updated successfully"},status=200)
                    else:
                        return JsonResponse({"message":" was already up to date"},status=208)
                else:
                    return JsonResponse({"message":"No document found with the specified email"},status=204)
            else:
                return JsonResponse({"message": "Email-Id is required"}, status=400)
        
        else:
           return JsonResponse({"message": "UNREGISTERED EVENT"}, status=400) 


    elif request.method == 'DELETE':

        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        if 'email' in data and 'password' in data:
            emailCheck = getDataWithoutProjection(collection_Register,{'email': data['email']})

            if(emailCheck != None):
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == emailCheck['password']:
                    result = collection_Register.delete_one(
                    {'email': email},
                    )
                    collection_Login.delete_many(
                    {'email': email}, 
                    )
                    return JsonResponse({"message":"Account Deleted"},status=200)
                else:
                  return JsonResponse({"message":"Wrong Password"},status=400)  
            else:
                return JsonResponse({"message":"No document found with the specified email"},status=204)
        else:
            return JsonResponse({"message": "Email-Id and password are required"}, status=400)


    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)
    


@csrf_exempt
def ForgetPasswordRequestApi(request):
    email_ack = ''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'email' in data:
                emailCheck = getDataWithoutProjection(collection_Register,{'email': data['email']})
                if(emailCheck != None):
                    OTP_value = generateOTPCode(6)
                    email_ack= send_email([data['email']], "OTP to reset your password HBL.", f"Hello user,\r\nYour One-Time Password (OTP) is : {OTP_value}\r\n Please use this OTP to verify your account.\n\n Thank you.")
                    OTP(
                        email=data['email'],
                        otp=OTP_value,
                        timestamp = int(time.time())
                    ).save()
                    return JsonResponse({"msg":email_ack})
                else:
                    return JsonResponse({"message":"User not registered with this email"}, status=201)
            else:
                return JsonResponse({"message": "Email is required"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)



@csrf_exempt
def ForgetPasswordValidateApi(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'email' in data:
                emailCheck_cursor = getDataWithDescending(collection_Otp,{'email': data['email']})

                # Retrieve the document from the cursor
                emailCheck = next(emailCheck_cursor, None)

                print(emailCheck)
                
                if emailCheck is not None:
                    timestamp =  int(emailCheck['timestamp'].to_decimal().to_eng_string())
                    
                    print("time : ",timestamp)
                    if((emailCheck['otp'] == data['otp']) & (timestamp+300 <= time.time())):
                        collection_Otp.delete_one({'_id': emailCheck['_id']})
                        return JsonResponse({"msg":"TIME OUT"})
                    elif emailCheck['otp'] == data['otp']:
                        collection_Otp.delete_one({'_id': emailCheck['_id']})
                        return JsonResponse({"msg":"OTP Validated"},status=200)
                    else:
                        return JsonResponse({"msg":"Wrong OTP"},status=400)
                else:
                    return JsonResponse({"message":"Please press on resend OTP"}, status=201)
            else:
                return JsonResponse({"message": "Email and OTP is required"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)



@csrf_exempt
def QuizMarks(request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body)
            if 'email' in data and 'score' in data and 'label' in data:
                # Connect to MongoDB (default host and port)
                client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')

                db = client['project']
                collection = db['quiz']
                filter_criteria = {"email": data["email"]}
                update_data = {
                    "$set": {
                        data["label"]: data["score"]
                    }
                }
                result = collection.update_one(filter_criteria, update_data, upsert=True)

                if result.upserted_id:
                    print(f"Inserted new document with ID: {result.upserted_id}")
                    return JsonResponse({"Inserted new document with ID": result.upserted_id}, status=200)
                else:
                    print(f"Updated existing document with ID: {result.matched_count}")
                    return JsonResponse({"Updated existing document with ID:": result.matched_count}, status=200)

            else:
                return JsonResponse({"message": "Email and marks is required"}, status=400)
        
        except Exception as e:
            print(e)
            return JsonResponse({"msg": e}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)



@csrf_exempt
def SchoolMarks(request):

    if request.method == 'POST':

        try:
            data = json.loads(request.body)
            if 'email' in data and 'score' in data and 'label' in data:
                # Connect to MongoDB (default host and port)
                client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')

                db = client['project']
                collection = db['marks']
                filter_criteria = {"email": data["email"]}
                update_data = {
                    "$set": {
                        data["label"]: data["score"]
                    }
                }
                result = collection.update_one(filter_criteria, update_data, upsert=True)

                if result.upserted_id:
                    print(f"Inserted new document with ID: {result.upserted_id}")
                    return JsonResponse({"Inserted new document with ID": {result.upserted_id}}, safe=False, status=200)
                else:
                    print(f"Updated existing document with ID: {result.matched_count}")
                    return JsonResponse({"Updated existing document with ID:": result.matched_count}, status=200)

            else:
                return JsonResponse({"message": "Email and marks is required"}, status=400)
        
        except Exception as e:
            print(e)
            return JsonResponse({"msg": e}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
    
    elif request.method == 'GET':
        try:
            data = request.GET.get('email', '')
            client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')

            db = client['project']
            collection = db['marks']
            collection_quiz = db['quiz']
            filter_criteria = {"email": data}
            document = collection.find_one(filter_criteria,{"_id": 0, "email":0})
            document_1 = collection_quiz.find_one(filter_criteria,{"_id": 0, "email":0})
            print("marks : ",document,"quiz : ",document_1)
            return JsonResponse( {"marks":document,"quiz":document_1}, safe=False, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)
    


@csrf_exempt
def webinars(request):
    
    if request.method == 'GET':
        try:
            client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')

            db = client['project']
            collection = db['webinars']
            document = collection.find_one({}, {'_id': 0})
            print(document)
            return JsonResponse( {"data":document}, safe=False, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)



@csrf_exempt
def counselling(request):
    
    if request.method == 'GET':
        try:
            client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')

            db = client['project']
            collection = db['counselling']
            document = collection.find_one({}, {'_id': 0})
            print(document)
            return JsonResponse( {"data":document}, safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"error":e},status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)
    

@csrf_exempt
def DecesionTree(request):
   
    if request.method == 'GET':
        try:
            data = request.GET.get('email', False)
            if data:
                client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')
                db = client['project']
                collection_marks = db['marks']
                collection_quiz = db['quiz']
                document_marks = collection_marks.find_one({"email":data}, {'_id': 0})
                document_quiz = collection_quiz.find_one({"email":data}, {'_id': 0})
                if not any(str(x) in str(document_marks) for x in [8, 9, 10]):
                    return JsonResponse({"msg":"Insufficient Data"}, safe=False, status=400)
                if "Science" not in str(document_quiz) and "Commerce" not in str(document_quiz) and "Arts" not in str(document_quiz):
                    return JsonResponse({"msg":"Insufficient Data"}, safe=False, status=400)
                predc = ModelPredection(document_marks, document_quiz, data)
                return JsonResponse(predc, safe=False, status=200)
            
            else:
                return JsonResponse( {"data":"Email is required"}, safe=False, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({"error":str(e)},status=400)
    else:
        return JsonResponse({"message": "Method Not Allowed"}, status=405)