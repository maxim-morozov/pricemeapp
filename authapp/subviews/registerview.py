from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from authapp.subforms.registerform import RegisterForm

def register(request):

    # Types of the requests
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Save the user
            form.save(commit=True)

            # Now we would need to show the successful registration page
            # with the infromation about the process after the registration
            assert False # TODO(MAX)

        else:
            # Log the errors
            print (form.errors)

    else:
        # New form for the initialisation
        form = RegisterForm()

    # Now we should render the response including the form
    return render_to_response('register.html', {'form' : form})

            
            
