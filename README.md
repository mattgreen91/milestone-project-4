<img src="readme-files/logo.png" width="200" style="margin: 0;">

# Milestone Project 4 - Gamestore - by Matt Green

My fourth project was to create an Full Stack website.  

I have chosen to design a website for gamers, which is a store that users can search and buy games.  The admin can also add and remove products.  The database uses CRUD methods of Create Read Update and Delete.

 _**You can access the completed website by [clicking here](https://game-store-uk.herokuapp.com) :rocket:**_

The website was created using HTML5, CSS, Javascript, JQuery, Python, Django, PostgreSQL, Amazon Web Services (AWS), Stripe and external Libraries and Frameworks

The website has been designed and tested to be fully functional on all devices, including a drop-down mobile navigation menu for smaller devices.

<img src="readme-files/s1.png" width="500" style="margin: 0;">
<img src="readme-files/s2.png" width="500" style="margin: 0;">
<img src="readme-files/s3.png" width="500" style="margin: 0;">
<img src="readme-files/s4.png" width="500" style="margin: 0;">
<img src="readme-files/s5.png" width="500" style="margin: 0;">
<img src="readme-files/s6.png" width="500" style="margin: 0;">
<img src="readme-files/s7.png" width="500" style="margin: 0;">
<img src="readme-files/s8.png" width="200" style="margin: 0;">
<img src="readme-files/s9.png" width="500" style="margin: 0;">
<img src="readme-files/s10.png" width="500" style="margin: 0;">
<img src="readme-files/s12.png" width="500" style="margin: 0;">
<img src="readme-files/s13.png" width="150" style="margin: 0;">
<img src="readme-files/s14.png" width="150" style="margin: 0;">
<img src="readme-files/s15.png" width="300" style="margin: 0;">

 
## Contents Page

* [1. UX - User Experience](#1-ux---user-experience)
* [2. Features](#2-features)
* [3. Technologies Used](#3-technologies-used)
* [4. Testing](#4-testing)
* [5. Deployment](#5-deployment)
* [6. Credits](#6-credits)

## 1. UX - User Experience 
 
- The Website is predominantly designed for gamers looking to purchase new games, but it can be used by anyone who is looking to by as a present for family or friends.  
- The user is able to create an account, and log-in/log-out of the store.  
- The user is able to login with their Google Account instead of creating an account.
- The user is able to change their password, or reset their password when logged in with normal account.
- The user is able to create, read, update and delete any of their profile information, such as address or phone number.
- The user is able to read their previous orders once completed.
- The user is able to search for items, filter items, and with administrator rights they can also modify items.   
- The user is able to add products to basket, view the basket, proceed to checkout and pay for the items.
- The user will recieve an order by email once payment completed.
- The website is very eye-catching as an external library was used to aid appearance.

**User Stories**

- As a user, I want the website layout to be clear and concise.
- As a user, I want the colours to be appealing but also easy on the eye.
- As a user, I want the navigation to be easy to use, and for me not to get lost in the website.
- As a user, I want all the links to work correctly.
- As a user, I want the website to be very interactive.
- As a user, I don't want too much text to scroll through.
- As a user, I want all the information to be easy to find.
- As a user, I want all the images to be clear, not pixelised.
- As a user, I want the search bar to work correctly, and if no information to inform me that no results are found.
- As a user, I want to be able to filter the items.
- As a user, I want to be able to create, read, update and delete required information.
- As a user, I want to see the correct information, and not find any veriations of date formats, car makes, or country names - to avoid confusion.
- As a user, I want the website to be secure, that my password cannot be found, and no one can see my data except the administrator and me.
- As a user, I want to be able to change my password or reset my password.
- As a user, I want the content to adjust automatically when using multiple screen sizes and devices.

**Design**

This project was designed with Balsamiq Wireframes, which can be seen below:

<img src="readme-files/1.png" width="200" style="margin: 0;">
<img src="readme-files/2.png" width="300" style="margin: 0;">
<img src="readme-files/3.png" width="300" style="margin: 0;">
<img src="readme-files/4.png" width="300" style="margin: 0;">
<img src="readme-files/5.png" width="300" style="margin: 0;">
<img src="readme-files/6.png" width="300" style="margin: 0;">

In order to display nice layout I used a Library from [StartBootstrap](https://startbootstrap.com/)

The Product names were taken randomly from [Game](https://www.game.co.uk/) and [Amazon](https://www.amazon.co.uk/), selected by popularity with accurate age and retail prices, which were placed into a spreadsheet before implementing, so the products are more accurate to the current market.  This can be accessed by [clicking here](readme-files/games_list.pdf)

**Accessibility**

The project has many features such as:

* Fall-back fonts, in case Google Fonts are not compatible with the browser - built in with the library
* Alternate Text' attributes for images, in case the images do not display

<img src="readme-files/alt_labels.jpg" width="300" style="margin: 0;">

* Aria Labels' in navigation menu for screen readers

<img src="readme-files/aria.png" width="300" style="margin: 0;">

* @media Queries, to modify content to fit different sized screens

## 2. Features

The main features of this project are:
 
- Simplistic Colour Design (black/navy blue/light blue) - allows users to see and process information more easily, as the colours are much more appealing to the eye. 
- Stylish Font Theme - more appealing to the eye, ready built in with the library.
- Navigation Menu - allows users switch between pages. Menu options change depending on whether logged in, logged out, or admin user.
- Mobile Navigation Menu - allows users to save screen space on Mobile Devices by using an animated dropdown menu, using well known 'hamburger' icon, so users can see more content.
- Animated logo - the main logo was designed animated to add overall effect.
- Search bar - to make it easier to find games when lots of products.

**Security**

- The app uses Allauth to ensure passwords cannot be stolen.
- Secret key generated used [Passwords Generator](https://passwordsgenerator.net/) so cannot be guessed easily.
- Any non-admin cannot enter 'Add Products' page.
- Only Admin can see the link to the 'Add Product' page in the navigation bar, or the buttons in product description for 'modify' and 'delete'.
- When incorrect password or username is entered, the app doesn't reveal which is incorrect, instead generally states login details incorrect, to avoid someone knowing half login details, and guessing other half.
- Users can only see their own profile information, and edit or delete any data, no one else.
- Admin is the only account who can add, edit and delete products.
- Users are unable to browse any products without signing in or registering.
- Users have the option to change their password whenever they want, or reset it.

**Error Pages**

As per Django documentation, the main error messages are 400, 403, 404 and 500.
These error pages have been saved in the templates directory which will override the Django default errors.

<img src="readme-files/404.png" width="500" style="margin: 0;">

### Features Left to Implement

- Some more settings in the 'account settings' page, such as modify username, delete account, profile picture, are still to be implemented
- The ability to add number of products to settings, so when sold out it will display unavailable.
- Stripe Payments to be taken off demo mode, and activated so actual payments can be made
- Other social accounts such as Discord and Facebook to be options for log in.

## 3. Technologies Used

In order to construct this project, the below technologies were used: 

- [Gitpod IDE](https://gitpod.io)
    - The project uses **Gitpod IDE** with build in Bash CLI to write and push code to GitHub.
- [HTML5](https://html.spec.whatwg.org)
    - The project uses **HTML5** to create the basic structure, text, images and other elements.
- [CSS3](https://www.w3.org/Style/CSS/specs.en.html)
    - The project uses **CSS3** to add customised style to the webpage.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** with Javascript to add additional interactive features, such as the buttons.
- [StartBootstrap Library](https://startbootstrap.com)
    - The project uses **StartBootstrap** as a library for displaying an appealing html/css template.
- [Python](https://www.python.org)
    - The project uses **Python** as one of the main programming languages in the app.
- [PostgreSQL](https://www.postgresql.org/)
    - The project uses **PostgreSQL** as a database to create, read, update and delete the information passed to and from the app.
- [Stripe](https://www.stripe.com)
    - The project uses **Stripe Payments** to take process payments, then using webhooks to complete orders.
- [Amazon Web Services](https://aws.amazon.com)
    - The project uses **AWS** to store images such as products.
- [FontAwesome](https://cdnjs.com/libraries/font-awesome)
    - The project uses **FontAwesome** for icons.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** to display the app to the user.   
- [Balsamiq WireFrames](https://balsamiq.com/wireframes/desktop)
    - The project uses **Balsamiq WireFrames** to generate a digital prototype of the webpage before coding.
- [Responsive Viewer Extension - Chrome](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
    - The project uses **Responsive Viewer Extension - Chrome** to easily test the webpage on multiple sized devices at once.
- [HTML5 Validator](https://validator.w3.org)
    - The project uses **HTML5 Validator** to check all the HTML5 code is working, without any errors.
- [CSS3 Validator](https://jigsaw.w3.org/css-validator)
    - The project uses **CSS3 Validator** to check all the CSS3 code is working, without any errors.
- [JS Hint](https://jshint.com)
    - The project uses **JS Hint** to test all the Javscript code, and fix any errors.
- [PEP8 Online](http://pep8online.com/)
    - The project uses **PEP8** to check all Python code is PEP8 Compliant.


## 4. Testing

This website has been fully tested and is working correctly.  

I used the Google Chrome and Mozilla FireFox developer tools to tweak code when testing.

**Main Areas of Testing**

I did both manual and automated testing for the website. 
- The manual testing can be opened by clicking [here](readme-files/manual_testing.pdf).
- The automated testing can be opened by clicking [here](readme-files/automated_testing.pdf).
- I also used 'Responsive Viewer' a tool on Chrome, in order to test the pages on different screen sizes, which can be opened by clicking [here](readme-files/screen_sizes.pdf).

**Bugs Found**

- The website works perfectly but for some users if cookies are disabled in their browser, it may display message "CSRF Verification failed"

## 5. Deployment

**Heroku**

GitHub Pages is only designed for viewing static webpages.  Therefore, for viewing the app I had to use another website called Heroku.
First I had to create a user account by clicking [here](https://signup.heroku.com/login)

Once logged in we click Create New App

You can write any app name, this will be part of the URL, but it must be unique. After choose a region and click Create App

Open the Deploy section and click 'Connect to GithHub'

Search for your repository by the repository name and connect

The hidden variables such as AWS KEYS, STRIPE KEYS, POSTGRESQL URL need to be recorded in Heroku.  This is the same details on your `settings.py` file.
Go to Settings, click Reveal Config Vars and write the correct values.

Click on Deploy Branch, then enable Auto Deploy. 

When the app is deployed by Heroku correctly, there is a confirmation that you can access the app

**GitPod**

This project was created using GitPod IDE which was recommended by Code Institute.  The reason for choosing this IDE is because it is all online, so no additional software needs to be installed, and the project can be accessed and edited on any workstation, as long as internet is available.
Code Institute had provided an Initial Template which included all the relevent extensions to aid with my project. The template can be accessed by [clicking here](https://github.com/Code-Institute-Org/gitpod-full-template).
For ease, I downloaded the GitPod [Google Chrome extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en) and [Mozilla Firefox extension](https://addons.mozilla.org/en-GB/firefox/addon/gitpod/).  By doing this, a green Gitpod button appears on the project's GitHub page - linking the project directly to the workspace.
The CLI (Command Line Interface) is built into GitPod, which means no additional software needs to be downloaded.

Before deploying from GitPod we need to do the following steps:
- Install Django using `pip3 install django`
- Install packges to be used in Python, i.e. django-allauth.  Then save them by using `pip3 freeze --local > requirements.txt`. To install mine you can type `pip3 install -r requirements.txt` 
- Create Procfile that contains the name of the application file so that Heroku knows what to run.
- Install the remote for Heroku using `npm install -g Heroku` then login with `heroku login -i` then add the remote using `git remove -v`
- Push them into GitHub and Heroku using `git push -u heroku master` then `git push origin master`.

In order to first access the admin page (your site name/admin), you have to create an administrator account using the following command:

`python3 manage.py createsuperuser`

The process for adding/modifying/removing content is as per below:

`django-admin startproject gamestore` _to create the initial project_

`python3 manage.py startapp (app name)` _to create an app inside the project_

`python3 manage.py makemigrations` _to make migrations after modifying models.py_

`python3 manage.py migrate` _to run migrations that were made in step above_

`git add -A` _to add all new/modified files to the staging area_

`git commit -m "commit message goes here"` _the commit message needs to be entered inside the inverted commmas " "_

`git push origin master` _this commmand push the content into the GitHub repository and Heroku App_

To view the app live, type in the terminal `python3 run.py`.  If the app is open and you cannot close it, type `pkill -9 python3`

**Amazon Web Services (AWS)**

In order to set up AWS, you must first register an account then it can be linked to the site.  I found a nice guide how to set up AWS, you can open by [clicking here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)

**PostgreSQL**

In order to set up PostgreSQL on Heroku, I followed the steps from Heroku Dev Center, which you can view by [clicking here](https://devcenter.heroku.com/articles/heroku-postgresql)

**Stripe**

In order to set up Stripe Payments, I followed the steps from Stripe Documentation, which you can view by [clicking here](https://stripe.com/docs/checkout/quickstart)

**All-Auth**

In order to set up All-Auth, I followed the steps from All-Auth website, which you can view by [clicking here](https://django-allauth.readthedocs.io/en/latest/installation.html)

**Google Authentication**

In order to set up Google Authentication, I followed the steps from All-Auth Providers, which you can view by [clicking here](https://django-allauth.readthedocs.io/en/latest/providers.html#google)

In trial mode you can add test accounts only, but once published the site needs verifying.  This Google is published, so in order for Google to verify the site, I had to add their authenticated page and view in my code.

<img src="readme-files/url1.png" width="500" style="margin: 0;">

<img src="readme-files/url2.png" width="500" style="margin: 0;">

**Fixtures**

Products are backed up and stored in JSON file.  

To save them I used the commands: 

`python3 manage.py dumpdata products.category > categories.json`

`python3 manage.py dumpdata products.product > products.json`  

Both are stored in products/fixtures folder.  

To load new data the database, the JSON files should be added to fixture folder, and then the following commands should be run:

`python3 manage.py loaddata categories`

`python3 manage.py loaddata products`

When switching from SQLite3 to PostgreSQL in the final deployment of my project, I did these steps to avoid losing my data.

**Readme Template**

Code Institute provided a [Readme Template](https://github.com/Code-Institute-Solutions/readme-template) which I used as a guideline for creating this Readme file.

**Cloning Repository**

If you would like to clone this repository locally:
- Download and install [Git](https://git-scm.com/downloads).
- Open Command Prompt (Windows) or Terminal (Mac).
- Type `cd ~/Desktop` and press 'enter' to change the folder to Desktop. (You can choose a different folder, or move the folder manually after completing these steps).
- Type `git clone https://github.com/mattgreen91/milestone-project-4.git`, then press 'enter'.
- Once complete, the repository will be saved on your desktop (or other directory if you changed).
- In order to use this website, you will need to install python and django, and run the requirements by the command `pip3 install -r requirements.txt`.
- You will need to update your Environment Variables in your gitpod settings to match yours, such as secret keys for AWS or Stripe.

**Final Project**

The project can be opened by [clicking here](https://game-store-uk.herokuapp.com)

## 6. Credits

### Content

- The Template Library was taken from [StartBootstrap](https://startbootstrap.com/themes/business-corporate).
- The product descriptions were taken from [Game](https://www.game.co.uk/) and [Amazon](https://www.amazon.co.uk/) 
- The settings for AllAuth were taken from [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html) for the site settings.py file
- Modals for confirming if to delete or not created with the help of [GetBoostrap](https://getbootstrap.com/docs/4.0/components/modal/)


### Media
- The pictures of games cover pages were taken from [Game](https://www.game.co.uk/) and [Amazon](https://www.amazon.co.uk/) 
- The main logo was designed using [Canva](https://www.canva.com/create/logos/)


### Acknowledgements

- Thanks to Code Institute for training me on Python, Django, Allauth, AWS, PostgreSQL and Stripe.
- Thanks to my mentor Allen Thomas Varghese for supporting me.
- Thanks to Slack Community for helping me solve any issues with code not working.
- Thanks to Stackoverflow community for suggesting ideas to help solve any bugs in my code
- Thanks to Code Institute Tutors for helping me fix any glitches with the IDE that I came across.