# Travel-wishlist-app by Chris Reeves.

# Contents

• Brief

• Architecture

• Tracking

• Risk assessment

• Testing

• Design


# Brief

This app is for the DFE/QA cloud specialism final project. 
The objective of this project is to achieve the following:

    • To create a multi-tier web application that demonstrates CRUD functionality.
    • To utilise containers to host and deploy the application.
    • To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy the application.

The application must consist of two services:

    • A frontend service that uses templating to host and serve the web pages with information from the database. This information is retrieved from the backend API service.

    • A backend API (Application Programming Interface) that interacts with the database via requests to a RESTful API (i.e. receives GET, POST, PUT and DELETE HTTP requests) to create, read, update and delete data.

To achieve these requirements I have built an app that allows the user to add countries to a database, view the countries on the their wishlist, update country names and if visited or not and to delete the country. This satisfies CRUD functionality.

# Architecture

Below is my ERD, showing a one-to-many relationship, however only one table has been implemented in this app. 

I developed an automated continuous integration/deployment pipeline: code is sent to Github and (through a webhook) on to Jenkins. Jenkins then automatically installs my code using Docker and two cloud-based virtual machines.

The jenkins build stages are detailed below:

# Tracking

I used Jira for project tracking as detailed below:

# Risk assessment

My risk assessment is detailed below:

# Testing

I used pytest for the testing of my appliaction achieving 100% coverage, as detailed below:

# Design

The design of the app is showcased below:

