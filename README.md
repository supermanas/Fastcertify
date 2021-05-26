Live link http://fastlycertify.herokuapp.com

In this particular app you can upload a csv file and can design e - certificates
and by accessing both you can email the e - certificates to bulk user 




To run the app clone the repo and run the following command 
            . Create db.sqlite3 file 
            . python3 manage.py collectstatic
            . python3 manage.py makemigrations
            . python3 manage.py migrate

Create a super user with following command 
            . python3 manage.py createsuperuser
            . Fill the credentials and add superuser to database
            . Now add /admin to the current url to access the admin

I have created the google login so to create your own login 
            . Go to Google Cloud Console https://console.cloud.google.com
            . Signup and create a Social Outh app 
            . Now copy it's secret key and Client id and go to admin
            . In sites tab create the site with your localhost if it's already create than leave it 
            . Now Click the social account tab and add the credentials 

You can do this with facebook , twitter as well
