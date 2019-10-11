from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
#from contacts.models import Contact
def register(request):
  if request.method == 'POST':
    # Get form values
    username = request.POST['username']
    email = request.POST['email']
    gender = request.POST['gender']
    email = request.POST['email']
    state = request.POST['state']
    city = request.POST['city']
    password = request.POST['password']
    password2 = request.POST['password2']
      # Check username
    if User.objects.filter(username=username).exists():
      #messages.error(request, 'That username is taken')
      return redirect('register')
    else:
      if User.objects.filter(email=email).exists():
        #messages.error(request, 'That email is being used')
        return redirect('register')
      else:
        # Looks good
        user = User.objects.create_user(username=username, password=password,email=email)
        # Login after register
        # auth.login(request, user)
        # messages.success(request, 'You are now logged in')
        # return redirect('index')
        user.save()
        #messages.success(request, 'You are now registered and can log in')
        return redirect('login')
  
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'students/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  #user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  """context = {
    'contacts': user_contacts
  }"""
  return render(request, 'students/dashboard.html')

