#Python basic project 
# Secure login system 
Class password chota error (exception):
  pass
class galat password error (exception):
  pass
real_password="m1$!23"
try:
   pwd=input("password dalo:")
   if len(pwd)<6:
    raise pwdchota error ("pwd 6 digit se chota hai")
   if pwd !=Real_password:
    raise galat pwd error("pwd galat hai!")
   print("login successfully! welcome hacker")
except pwd chota error as e:
    print("error:",e)
except galat pwd error as e:
    print("error:",e)
except exception as e:
    print("koi aur error:",e)
