# Travel with Fun Blog

Welcome to Travel with Fun Blog. As a siteuser, people can share their exciting travel experience with others. The goal of the website is to motivate people for travelling.

<img alt="Responsive Design" src="readmefiles/images/responsive.png">

The live view of the site can be found [here](https://travelblogdjango-d9e22c4148cf.herokuapp.com/)

# Table of Contents

1. [Overview](#overview)
2. [UX](#ux)
   - [User Stories](#user-stories)
   - [Agile Methodology](#agile-methodology)
3. [Design](#design)
   - [Color Scheme](#color-scheme)
   - [Imagery](#imagery)
   - [Data Models](#data-models)
   - [Relationship](#relationship)
   - [Wireframes](#wireframes)
4. [Security](#security)
   - [eny.py](#enypy)
   - [Secured Programming](#secured-programming)
   - [Authentication](#authentication)
5. [Features](#features)
   - [General features](#general-features)
   - [Home Page](#home-page)
   - [Sign Up Page](#sign-up-page)
   - [Login Page](#login-page)
   - [Create Post](#create-post)
   - [Profile](#profile)
   - [Log Out](#log-out)
   - [Edit/Delete Blog](#editdelete-blog)
   - [Footer](#footer)
   - [Future Features](#future-features)
6. [Technologies Used](#technologies-used)
7. [Libraries, Frameworks & Tools](#libraries-frameworks--tools)
8. [Deployment](#deployment)
   - [Settings and Environment](#settings-and-environment)
   - [Heroku Deployment](#heroku-deployment)
9. [Local Development](#local-development)
   - [Fork](#fork)
   - [Clone](#clone)
10. [Bugs](#bugs)
11. [Testing](#testing)
12. [Resources and Tutorials](#resources-and-tutorials)
13. [Future Improvements](#future-improvements)
14. [Content](#content)
15. [Acknowledgments](#acknowledgments)

# Overview

Travel with Fun Blog is a fully responsive website used for travelling motivation purpose. Here users have the freedom to upload and modify their contents. This is a playground for travelling lovers.

# UX

## User Stories

 1. View and create blog posts

 2. User Registration and Login

 3. User can delete his own post

 4. Create Database to enter post

 5. Create site user app

 6. Create User Profile

 7. User Can edit his own post

 8. Create storage for media files after deployment in Heroku

 9. Create Automatd Test

## Agile Methodology

Agile methodology has been used to create user stories and develop features according to the stories. The user story board can be viewed [here](https://github.com/users/farhatamannaislam/projects/3/views/1)

# Design 

## Color Scheme

The main color palette of the website is given below:

  <img alt="Color Palette" src="readmefiles/images/Colorpalette.png">

## Imagery

The imagery used in this website are all real life photos. Only the favicon is an animated picture.

## Data Models

Data models were drawn before implementing it into the SW. It serves as a blue print of the data base design.

<img alt="ERD Diagram" src="readmefiles/images/ERDDiagram.png">

## Relationship:

### Post

* User (OneToMany): One user can write several blog posts. This is a OneToMany relationship. 

### Profile

* User (OneToOne): Each user has a single user profile. This is a OneToOne relationship.


## Wireframes

Wireframes are given here.

* <details>
  <summary>Home</summary>
  <img alt="Home DeskTop" src="readmefiles/wireframe/homedesktop.png">
  <img alt="Home Mobile" src="readmefiles/wireframe/homemobile.png">
</details>

* <details>
  <summary>Sign Up</summary>
  <img alt="Sign Up DeskTop" src="readmefiles/wireframe/signupdesktop.png">
  <img alt="Sign Up Mobile" src="readmefiles/wireframe/signupmobile.png">
</details>

* <details>
  <summary>Login</summary>
  <img alt="Login DeskTop" src="readmefiles/wireframe/logindesktop.png">
  <img alt="Login Mobile" src="readmefiles/wireframe/loginmobile.png">
</details>

* <details>
  <summary>Create Post</summary>
  <img alt="Create Post DeskTop" src="readmefiles/wireframe/createpostdesktop.png">
  <img alt="Create Post Mobile" src="readmefiles/wireframe/createpostmobile.png">
</details>

* <details>
  <summary>Profile</summary>
  <img alt="Profile DeskTop" src="readmefiles/wireframe/profiledesktop.png">
  <img alt="Profile Mobile" src="readmefiles/wireframe/profilemobile.png">
</details>

* <details>
  <summary>Log Out</summary>
  <img alt="Log Out DeskTop" src="readmefiles/wireframe/logoutdesktop.png">
  <img alt="Log Out Mobile" src="readmefiles/wireframe/logoutmobile.png">
</details>

# Security

## eny.py

* API keys and database are stored in the env.py file. This file is included in gitignore to prevent exposure in version control.

## Secured Programming

* In some places login required action is is used to prevent unauthorized entry and actions into the website. 

## Authentication

* Django library django-allauth is used for user authentication. This provides a secure authentication for sign up, login and logout.

# Features

## General features

* The site is fully responsive. 

<img alt="Responsive Image" src="readmefiles/images/responsive.png">

* Navigaions are on the top left corner. 

* Social media links are given in the footer.

* Blog contents with writer name and creation date are found on the Home Page.


## Home Page

* Navigation: On the top left corner of the Home Page there are navigations available. For a new user the Navigation will be seen as Home, Sign Up, Login, Cretae Post, Profile.

<img alt="New User Navigation" src="readmefiles/images/newusernav.png">

* Navigation: If an user is signed up he/she has the navigation of Home , Logout, Create Post and Profile.

<img alt="Signed User Navigation" src="readmefiles/images/signedupnav.png">

* Header: Header is under navigation bar and in the middle of the page. It is called "Travel with Fun!!"

<img alt="Header" src="readmefiles/images/header.png">

* Cover Image: There is an Enthusiastic Cover Image in the Home Page.

<img alt="Cover Image" src="readmefiles/images/coverimage.png">

* Blog Menu: Under the Cover Image there are blog menu with blog title, respective author name and creation date. If the user clicks the title he/she will
be redirected to the content. 

<img alt="Blog Menu" src="readmefiles/images/blogmenu.png">

<img alt="Blog Content" src="readmefiles/images/blogcontent.png">

## Sign Up Page

For the new users there is the sign up page with Username, email address (optional), password and password confirmation field. If the user has already signed up 
before there is a link to sign in.


<img alt="Sign Up Page upper part" src="readmefiles/images/signupupper.png">

<img alt="Sign Up Page lower part" src="readmefiles/images/signuplower.png">


## Login Page

For the signed up user there is the login page where user has to put username and password. There is also a link to sign up for the new users here.


<img alt="Login Page" src="readmefiles/images/Login.png">

## Create Post

If the user is logged in they can go to the Create Post page. There are title, slub, content, status boxes along with save button. If the status is published then the post will appear in the home page. 

<img alt="Create Post" src="readmefiles/images/createpost.png">


## Profile 

Profile page shows the username and profile image. There is a link to edit Your Profile.

<img alt="Profile Page" src="readmefiles/images/Profile.png">

In the edit your Profile section user can update his/her username, upload a profile photo. If no photo is uploaded a default image is used.

<img alt="Edit your Profile" src="readmefiles/images/editprofile.png">

## Log Out

There is the Log out page asking the user if he really wants to go out.

<img alt="Log Out Page" src="readmefiles/images/logout.png">

## Edit/Delete Blog

An user can edit or delete his/her own post. He has to be logged in to do so.

<img alt="Edit Post" src="readmefiles/images/editpost.png">

<img alt="Delete Post" src="readmefiles/images/deletepost.png">


## Footer

There are clickable social media links in the footer.

<img alt="Footer" src="readmefiles/images/Footer.png>

## Future Features

* Add Comments: Add comments to the blog post by the users and use a counter for the comments.

* Use text formatter: Use text formatter such as summernote to beautify blog text.

# Technologies Used

* HTML5 - Used for structuring the web pages of the application.
* CSS - Used to style the HTML content.
* Python 3 - The core backend programming language
* PostgreSQL- Used as the primary database.

# Libraries, Frameworks & Tools

* Django 4.2.14 -  A high-level Python web framework used for developing the web application.
* Django-Allauth 0.57.2 - For user registration, login, and logout functionality.
* Gunicorn 20.1.0 - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
* Whitenoise5.3.0 - WhiteNoise is used for serving static files in a Django application.
* Cloudinary - cloud based storage for images.
* Heroku - for hosting and deployment of the site.
* Font Awesome - to use icons on the website.
* Github - to store and display all files and assets for the website.
* Bootstrap 5.0.1 - A Framework for building responsive sites
* Am I Responsive? - to test responsiveness on several devices.
* Lucidchart - to create Data Models.
* W3C Validator- to validate CSS and HTML
* Pixabay - for Photos used in the website.
* TinyPNG - Compresses images for website.
* Chrome DevTools - Web Developer Tools.
* Lighthouse - to test the accessibility of the website.
* Google Fonts - to import the fonts used on the website.
* Balsamiq - to create Wireframes.
* Coolors - to generate Colour Palette
* Code Institute's Python Linter - to check syntactical problems in Python source code

# Deployment

## Settings and Environment

* I added DATABASE_URL value and a SECRET_KEY value to the env.py file.
* then I imported the DATABASE_URL and SECRETKEY file paths into the settings.py file.
* My django was installed and i added it to requirement.txt.
* I created my project and added static file settings.
* I created a Procfile in the main directory.
* I added my workspace and Heroku into ALLOWED_HOSTS in settings.py.
* I did necessary migrations.

## Heroku Deployment

* I logged into Heroku as I already had an user accout and created new app with an unique neme.
* I connected Heroku with Github repository.
* After connection is established I went to settings tab. I clicked  'Reveal Config Vars' and added environment key & value variables which are DATABASE_URL & SECRET_KEY.
* Then I added DISABLE_COLLECTSTATIC as key and 1 as value to prevent errors.
* I clicked Add Buildpack to confirm Heroku buildpack is present.
* Then I went to Deploy section, search my repository and connected it.
* I chose manual deployment and my main branch where my project is present.
* After the deployment is finished my live site is viewed.


# Local Development

## Fork 
* Log in to Github or crate an account.
* Click on the repository name and click the Fork button in the top right corner.

## Clone

* Log in to Github or crate an account and find or create the repository.
* Click on the code button and select  HTTPS, SSH or GitHub CLI and copy the link shown.
* Open the terminal in your local editor and change the current working directory to the location where you want to use for the cloned directory.
* Type 'git clone' into the terminal and paste the link you copied and press enter.

# Bugs

There is no known bug in the project.

# Testing

All testing information can be found in [TESTING.md.](TESTING.md)

# Resources and Tutorials

* [Django Tutorial and Documentation](https://docs.djangoproject.com/en/5.0/) - Official Django documentation, tutorials, and guides for Django development.
* [Stack Overflow](https://stackoverflow.com/) - For troubleshooting and finding solution.
* [W3C School](https://www.w3schools.com/) - Online Web Tutorials for Programming.
* [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - How to work with Bootstrap.
* [Code Institute Walkthrough Django Project](https://github.com/farhatamannaislam/Django_blog_2) - The idea of how Django blog works comes from this project.
* [OpenAI GPT-4](https://openai.com/index/gpt-4/) - occasionaly used to create tutorial like explanations.
* [Wikipedia](https://www.wikipedia.org/) - To get some detail information about tourist attractions.

# Future Improvements

The user story "Create a Database to enter post" was created when the work was almost finished. Unfortunately it was forgotten by the author to include it in correct time. So there is a scope of Future Improvement for this story time line.

# Content

All the contents are written by the Author from personal experience. Some details information about tourist attractions are collected from Wikipedia.

# Acknowledgments

* My mentor Antonio Rodriguez for his valueable support and guidance.
* Code Institute Tutoring Support.
* Code Institute Slack community for helpful responses and feedback.









 