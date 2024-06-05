# Portfolio Website

This is the repository for my personal portfolio website, implemented using the Django framework, along with HTML, CSS, JavaScript, Bootstrap, and SwiperJS.

## Table of Contents
- [Overview](#overview)
- [Pages](#pages)
  - [Home Page](#home-page)
  - [Projects Page](#projects-page)
  - [Certificates Page](#certificates-page)
  - [About Page](#about-page)
  - [Contact Page](#contact-page)
- [Technologies Used](#technologies-used)
- [Database Models](#database-models)
- [Django Views](#django-views)
- [Website](#website)

## Overview
This project is a personal portfolio website to showcase my projects, certificates, and provide information about myself. It includes a contact form to allow visitors to get in touch with me.

## Pages

### Home Page
The Home Page displays:
- My photo
- My name
- My position
- My university

### Projects Page
The Projects Page features:
- A carousel of my projects
- Each project includes a photo and a brief description
- Projects mainly focus on web development

### Certificates Page
The Certificates Page showcases:
- All of my certificates displayed in a grid (rows * 3 columns)

### About Page
The About Page provides:
- My image
- A summary about myself
- A button to download my resume

### Contact Page
The Contact Page includes:
- My contact information (phone number, email)
- Links to my social media accounts (GitHub, LinkedIn, Facebook, Instagram)
- A form for sending messages directly to me

## Technologies Used
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- SwiperJS

## Database Models
The project uses the following database models:

### Project
- **order**: IntegerField
- **name**: CharField(max_length=64)
- **category**: CharField(max_length=64)
- **image**: CharField(max_length=64)
- **link**: URLField
- **tools**: TextField
- **description**: TextField

### Certificate
- **order**: IntegerField
- **name**: CharField(max_length=64)
- **image**: CharField(max_length=64)

### Texter
- **name**: CharField(max_length=64)
- **email**: CharField(max_length=150)
- **message**: TextField

## Django Views
The project includes the following Django views and functions:

### Index View
- **URL**: `/`
- **Function**: `index`
- **Description**: Displays the home page with my photo, name, position, and university.

### Certificate View
- **URL**: `/certificates/`
- **Function**: `certificate`
- **Description**: Displays all certificates in a grid.

### Contact View
- **URL**: `/contact/`
- **Function**: `contact`
- **Description**: Handles GET requests to display the contact page and POST requests to handle form submissions.

### Projects View
- **URL**: `/projects/`
- **Function**: `projects`
- **Description**: Displays projects categorized into Web Development, AI, and Digital Marketing.

### About View
- **URL**: `/about/`
- **Function**: `about`
- **Description**: Displays the about page with a summary and resume download option.

## Website
To visit the website, follow [this link](https://portfolio-2hv5.onrender.com/).
