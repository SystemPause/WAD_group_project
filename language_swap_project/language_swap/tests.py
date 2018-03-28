# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from language_swap.admin import ContactAdmin, ProfileAdmin
from language_swap.apps import LanguageSwapConfig
from language_swap.models import Language, UserProfile, Contact
from language_swap.regbackend import MyRegistrationView
from population_script import populate

def createUser(userName):
    user = User.objects.create(first_name='user', last_name='test', username=userName,
                                    email=userName)
    user.set_password('testpassword')
    user.save()
    return user

def createProfile(user):
    profile = UserProfile.objects.create(user=user, city='Glasgow', country='UK', dob='1000-10-10')
    profile.save()
    return profile

class AppConfigTests(TestCase):

    def test_language_swap_app_config(self):
        """
        Ensures language_swap app is configured correctly
        """
        self.assertEqual(LanguageSwapConfig.name, 'language_swap')
        self.assertEqual(apps.get_app_config('language_swap').name, 'language_swap')

class AdminTests(TestCase):

    def setUp(self):
        """
        Creates test users
        """
        self.user = createUser('user@test.com')
        self.user2 = createUser('user2@test.com')
        self.profile = createProfile(self.user)
        self.profile2 = createProfile(self.user2)
        self.contact = Contact.objects.create(sourceUser=self.profile, contactedUser=self.profile2)
        self.client = Client()

    def test_admin_first_name_method_profile_model(self):
        """
        Ensures ProfileAdmin model method returns the first name of the user
        """
        self.assertEqual(ProfileAdmin.first_name(self, self.profile), self.profile.user.first_name)

    def test_admin_last_name_method_profile_model(self):
        """
        Ensures ProfileAdmin model method returns the last name of the user
        """
        self.assertEqual(ProfileAdmin.last_name(self, self.profile), self.profile.user.last_name)

    def test_admin_contacter_method_contact_model(self):
        """
        Ensures ContactAdmin model contacter method returns the username of the sourceUser
        """
        self.assertEqual(ContactAdmin.contacter(self, self.contact), self.contact.sourceUser.user.username)

    def test_admin_contactee_method_contact_model(self):
        """
        Ensures ContactAdmin model contactee method returns the username of the contactedUser
        """
        self.assertEqual(ContactAdmin.contactee(self, self.contact), self.contact.contactedUser.user.username)

class LanguageModelTests(TestCase):

    def test_string_representation(self):
        """
        Ensures Language model str method returns a string representation of language name
        """
        lang = Language(LanguageName='Name of language')
        self.assertEqual(str(lang), lang.LanguageName)

class UserProfileModelTests(TestCase):

    def test_string_representation(self):
        """
        Ensures UserProfile model str method returns a string representation of username
        """
        user = createUser('user@test.com')
        profile = createProfile(user)
        self.assertEqual(str(profile), user.username)

class IndexViewTests(TestCase):

    def test_ensure_index_loads(self):
        """
        Ensures the index page loads with status code 200
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_using_template(self):
        """
        Ensures correct template used to render index page
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'language_swap/index.html')

class SearchResultViewTests(TestCase):

    def setUp(self):
        """
        Populates the database with required data
        """
        populate()
        self.client = Client()

    def test_ensure_search_result_loads(self):
        """
        Ensures search result page loads with status code 200
        """
        response = self.client.get(reverse('result'))
        self.assertEqual(response.status_code, 200)

    def test_search_result_using_template(self):
        """
        Ensures correct template used to render search result page
        """
        response = self.client.get(reverse('result'))
        self.assertTemplateUsed(response, 'language_swap/result.html')

    def test_search_result_no_places(self):
        """
        Ensures that error message is displayed if searched place is not supported
        """
        response = self.client.get(reverse('result'), {'places': 'nonexistentcity,nonexistentcountry'})
        self.assertContains(response, "An error has occurred while fetching the places.")

    def test_search_result_raise_does_not_exist_error_language_object(self):
        """
        Ensures that Language.DoesNotExist error is raised and error message is displayed if searched language is not supported
        """
        response = self.client.get(reverse('result'), {'practicingLanguage': 'Mandarin'})
        self.assertRaises(Language.DoesNotExist)
        self.assertContains(response, "An error has occurred while fetching the languages.")

    def test_search_result_no_user_matches(self):
        """
        Ensures that error message is displayed if no users match search criteria
        """
        response = self.client.get(reverse('result'), {'places': 'Glasgow,UK', 'spokenLanguage': 'Armenian',
                                                            'practicingLanguage': 'English'})
        self.assertContains(response, "There are no matches in this city.")

    def test_search_result_user_matches(self):
        """
        Ensures that no error messages are displayed if users match search criteria
        """
        response = self.client.get(reverse('result'), {'places': 'Milan,Metropolitan City of Milan,Italy',
                                                       'spokenLanguage': 'English', 'practicingLanguage': 'Italian'})
        self.assertEqual(response.context["errors"], [])

class AboutViewTests(TestCase):

    def test_ensure_about_loads(self):
        """
        Ensures about page loads with status code 200
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_using_template(self):
        """
        Ensures correct template used to render about page
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'language_swap/about.html')

class ContactViewTests(TestCase):

    def test_ensure_contact_loads(self):
        """
        Ensures contact us page loads with status code 200
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_using_template(self):
        """
        Ensures correct template used to render contact us page
        """
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'language_swap/contact.html')

class ContactHistoryViewTests(TestCase):

    def setUp(self):
        """
        Creates a test user
        """
        user = createUser('user@test.com')
        createProfile(user)
        self.client = Client()

    def test_contact_history_ensure_login_required(self):
        """
        Ensures anonymous users cannot access contact history page and get redirected to the login page
        """
        response = self.client.get(reverse('contactHistory'))
        self.assertRedirects(response, reverse('auth_login') + "?next=/LanguageSwap/contactHistory/", status_code=302,
                             target_status_code=200)

    def test_contact_history_loads(self):
        """
        Ensures contact history page loads with status code 200 when user is logged in
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('contactHistory'), {'user_id': 'user@test.com'})
        self.assertEqual(response.status_code, 200)

    def test_contact_history_using_template(self):
        """
        Ensures correct template used to render contact history page
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('contactHistory'), {'user_id': 'user@test.com'})
        self.assertTemplateUsed(response, 'language_swap/contactHistory.html')

    def test_contact_history_with_no_contact_history(self):
        """
        If no contact history exists, an appropriate message should be displayed
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('contactHistory'), {'user_id': 'user@test.com'})
        self.assertContains(response, "The contact history is empty.")

class ProfileViewTests(TestCase):

    def setUp(self):
        """
        Creates test user
        """
        user = createUser('user@test.com')
        createProfile(user)
        self.client = Client()

    def test_profile_ensure_login_required(self):
        """
        Ensures anonymous users cannot access profile page and get redirected to the login page
        """
        response = self.client.get(reverse('myProfile'))
        self.assertRedirects(response, reverse('auth_login') + "?next=/LanguageSwap/myProfile/", status_code=302,
                             target_status_code=200)

    def test_profile_loads(self):
        """
        Ensures profile loads with status code 200 when user is logged in
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('myProfile'), {'user_id': 'user@test.com'})
        self.assertEqual(response.status_code, 200)

    def test_profile_using_template(self):
        """
        Ensures correct template used to render profile page
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('myProfile'), {'user_id': 'user@test.com'})
        self.assertTemplateUsed(response, 'language_swap/profile.html')

    def test_edit_profile_ensure_login_required(self):
        """
        Ensures anonymous users cannot access edit profile page and get redirected to the login page
        """
        response = self.client.get(reverse('edit_profile'))
        self.assertRedirects(response, reverse('auth_login') + "?next=/LanguageSwap/myProfile/edit/", status_code=302,
                             target_status_code=200)

    def test_edit_profile_loads(self):
        """
        Ensures edit profile page loads with status code 200 when user is logged in
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('edit_profile'), {'user_id': 'user@test.com'})
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_using_template(self):
        """
        Ensures correct template used used to render edit profile page
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('edit_profile'), {'user_id': 'user@test.com'})
        self.assertTemplateUsed(response, 'language_swap/edit_profile.html')

    def test_delete_account_ensure_login_required(self):
        """
        Ensures anonymous users cannot access delete account page and get redirected to the login page
        """
        response = self.client.get(reverse('delete_account'))
        self.assertRedirects(response, reverse('auth_login') + "?next=/LanguageSwap/myProfile/delete/", status_code=302,
                             target_status_code=200)

    def test_delete_account_loads(self):
        """
        Ensures delete account page loads with status code 200 when user is logged in
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('delete_account'), {'user_id': 'user@test.com'})
        self.assertEqual(response.status_code, 200)

    def test_delete_account_using_template(self):
        """
        Ensures correct template used to render delete account page
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get(reverse('delete_account'), {'user_id': 'user@test.com'})
        self.assertTemplateUsed(response, 'language_swap/delete_account.html')

class RatingViewTests(TestCase):

    def setUp(self):
        """
        Creates a test user
        """
        user = createUser('user@test.com')
        createProfile(user)

    def test_rating_ensure_login_required(self):
        """
        Ensures anonymous users cannot access rating page and get redirected to the login page
        """
        response = self.client.get(reverse('rating'))
        self.assertRedirects(response, reverse('auth_login') + "?next=/LanguageSwap/rating/", status_code=302,
                             target_status_code=200)

    def test_rating_loads(self):
        """
        Ensures that rating page loads with status code 200 when user is logged in and request is an ajax request
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get('/LanguageSwap/rating/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_rating_with_no_ajax_request(self):
        """
        Ensures that if the request is not an ajax request, a Http404 error will be raised
        """
        self.client.login(username='user@test.com', password='testpassword')
        response = self.client.get('/LanguageSwap/rating/')
        self.assertEqual(response.status_code, 404)

    def test_rating_raise_object_does_not_exist_error(self):
        """
        Ensures that if the rated user does not exist an appropriate error will be raised
        """
        self.client.login(username='user@test.com', password='testpassword')
        self.client.get('/LanguageSwap/rating/', HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                   args={'ratedUserId': 'nonexistentuser'})
        self.assertRaises(ObjectDoesNotExist)

class EmailCheckViewTests(TestCase):

    def test_rating_with_no_ajax_request(self):
        """
        Ensures that if the request is not an ajax request, a Http404 error will be raised
        """
        response = self.client.get('/LanguageSwap/emailCheck/')
        self.assertEqual(response.status_code, 404)

class MyRegistrationViewTests(TestCase):

    def setUp(self):
        """
        Creates a test user
        """
        createUser('user@test.com')
        self.client = Client()

    def test_get_success_url_method(self):
        """
        Ensures that user will be redirected to the index following a successful login attempt
        """
        logged_user = self.client.login(username='user@test.com', password='testpassword')
        self.assertEqual(MyRegistrationView.get_success_url(self, logged_user), '/LanguageSwap/')