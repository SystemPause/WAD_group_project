# Helper functions

# This function retrieves all the informatin regarding one single User.
# It receives a user (UserProfile) object as parameter and 
# it returns a dictionary that maps a unique username to a dictionary that
# contains all the details of the specified user.

def getUserDetails(userObject):
    user_dictionary = {}
    
    # Map a username to all the user's details 
    user_dictionary[userObject.user.username] = {
        'id': userObject.user.id,
        'email' : userObject.user.email,
        'firstname' : userObject.user.first_name,
        'lastname' : userObject.user.last_name,
        'country' : userObject.country,
        'city' : userObject.city,
        'picture' : userObject.picture if bool(userObject.picture) else False,
        'hobby' : userObject.hobby if bool(userObject.hobby) else False,
        'speaks' : userObject.speaks.all(),
        'practices' : userObject.practices.all()
    }
   
    return user_dictionary