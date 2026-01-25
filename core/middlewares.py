# class TestingMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):

#         print(f"1.    Method: {request.method}\n")
#         print(f"2.    Path: {request.path}\n")
#         print(f"3.    Path_info: {request.path_info}\n")
#         print(f"4.    GET: {request.GET}\n")
#         print(f"5.    POST: {request.POST}\n")
#         print(f"6.    Headers: {request.headers}\n")
#         print(f"7.    META: {request.META}\n")
#         print(f"8.    COOKIES: {request.COOKIES}\n")
#         print(f"9.    USER: {request.user}\n")
#         print(f"10.    SESSION: {request.session}\n")
        
        
#         response = self.get_response(request)

#         print("---------------Response---------------\n")
#         print(f"1.    Status Code: {response.status_code}\n")
#         # print(f"2.    Content: {response.content}\n")
#         print(f"3.    Header: {response.headers}\n")
#         print(f"5.    Cookies: {response.cookies}\n")

#         return response
    



# Common Request Attributes_______________

# request.method       ==>    GET, POST
# request.path         ==>    /products/5/
# request.path_info    ==>    same as path (usually)
# request.GET          ==>    Query params
# request.POST         ==>    Form data
# request.headers      ==>    All headers
# request.META         ==>    Raw HTTP metadata
# request.COOKIES      ==>    Cookies
# request.user         ==>    Logged-in user (if AuthMiddleware enabled)
# request.session      ==>    Session data (if SessionMiddleware enabled)


# Common Response Attributes_______________

# response.status_code
# response.content
# response.headers
# response["Header-Name"]
# response.cookies
