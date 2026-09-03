def check_auth(func):
  def auth():
    print("authentication successful.....")
    func()
  return auth  
@check_auth
def login():
  print("login successful")
login()  
  
