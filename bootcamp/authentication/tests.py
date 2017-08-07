from django.test import TestCase, Client
class SignUpTest(TestCase):
    def setUp(self):
        client=Client()

    ''' test whether sending a GET request to signUp view will return a http 
    code 200
    '''
    def test_GET(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('authentication/signup.html')


    def test_POST(self):
        # check a vaid form data
        post_data = {
            "username" : "test_name",
            "password" : "test_password",
            "confirm_password" : "test_password",
            "email" : "test_name@mysite.com",
        }
        response = self.client.post("/signup/", post_data)
        self.assertRedirects(response, "/", status_code = 302)

        '''check when passing an empty username, validation on form will fail
        and return an new form'''
        post_data['username'] = ''
        response = self.client.post('/signup/', post_data)
        self.assertTemplateUsed('authentication/signup.html')
        self.assertEqual(response.status_code, 200)

        '''check when confirm_password not equal to password, validation on form
        will fail and return a new form'''
        post_data['username'] = 'test_name'
        post_data['confirm_password'] = 'another_password'
        response = self.client.post('/signup/', post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('authentication/signup.html')



