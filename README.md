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

<img width="723" alt="Screenshot 2021-11-30 at 12 07 46" src="https://user-images.githubusercontent.com/91483522/144627358-c5768585-3986-42e6-8a6e-acb1ad0e13a7.png">
<img width="712" alt="Screenshot 2021-12-01 at 09 45 56" src="https://user-images.githubusercontent.com/91483522/144627627-98cac77e-8492-4678-9160-c1403441463b.png">
<img width="712" alt="Screenshot 2021-12-01 at 10 46 07" src="https://user-images.githubusercontent.com/91483522/144627675-36200060-5dc3-434e-b35f-3e210dbe7a5b.png">

I developed an automated continuous integration/deployment pipeline: code is sent to Github and (through a webhook) on to Jenkins. Jenkins then automatically installs my code using Docker and two cloud-based virtual machines.

The jenkins build stages are detailed below:

<img width="917" alt="Screenshot 2021-12-03 at 13 07 13" src="https://user-images.githubusercontent.com/91483522/144628429-362117bb-abdf-42a4-9058-6c3160e705c6.png">
<img width="904" alt="Screenshot 2021-12-02 at 15 11 34" src="https://user-images.githubusercontent.com/91483522/144628468-7698d21f-1817-4d33-bf25-4fd3db18a9d2.png">
<img width="1265" alt="Screenshot 2021-12-02 at 15 36 55" src="https://user-images.githubusercontent.com/91483522/144628857-81749ba3-c77d-4650-9e20-71fca813a86e.png">
<img width="1265" alt="Screenshot 2021-12-02 at 15 36 35" src="https://user-images.githubusercontent.com/91483522/144628865-05b92392-b0c7-4bf3-8770-22881bbf1bde.png">
<img width="1265" alt="Screenshot 2021-12-02 at 15 36 02" src="https://user-images.githubusercontent.com/91483522/144628874-3d974a3b-9e81-4a05-80b0-abed05708a92.png">
<img width="1265" alt="Screenshot 2021-12-02 at 15 35 32" src="https://user-images.githubusercontent.com/91483522/144628880-3cece61d-9959-42a1-8640-f7b2e5daf53c.png">

# Tracking

I used Jira for project tracking as detailed below:

<img width="1030" alt="Screenshot 2021-11-30 at 10 45 23" src="https://user-images.githubusercontent.com/91483522/144625917-d0142fb5-e1dc-402e-8328-869bd75c57c0.png">
<img width="1159" alt="Screenshot 2021-11-30 at 10 49 39" src="https://user-images.githubusercontent.com/91483522/144626866-4675413b-3092-4b44-aea2-bfbec96d5ec6.png">
<img width="860" alt="Screenshot 2021-11-30 at 11 28 17" src="https://user-images.githubusercontent.com/91483522/144626907-b33d601a-a574-47bc-ae1e-8f77dad6bdd5.png">
<img width="531" alt="Screenshot 2021-11-30 at 11 45 12" src="https://user-images.githubusercontent.com/91483522/144626975-b8815d14-2c4b-4388-9d28-ef65319797c5.png">
<img width="939" alt="Screenshot 2021-11-30 at 11 50 07" src="https://user-images.githubusercontent.com/91483522/144627032-10b0a98f-b1e7-4a92-a8c6-a3bc28f220fd.png">

# Risk assessment

My risk assessment is detailed below:

<img width="496" alt="Screenshot 2021-12-02 at 10 49 30" src="https://user-images.githubusercontent.com/91483522/144627893-a4c1aea6-e407-47fa-8df4-2c0f985b0dba.png">

# Testing

I used pytest for the testing of my appliaction achieving 100% coverage, as detailed below:

<img width="576" alt="Screenshot 2021-12-03 at 13 06 33" src="https://user-images.githubusercontent.com/91483522/144628627-313f59d7-b2c0-4320-a965-a4c7f06610f9.png">
<img width="507" alt="Screenshot 2021-12-03 at 13 08 22" src="https://user-images.githubusercontent.com/91483522/144628704-2b579746-a66a-4f66-b9c4-857ce97b2712.png">
<img width="919" alt="Screenshot 2021-12-03 at 13 06 14" src="https://user-images.githubusercontent.com/91483522/144628711-b6615fef-3bb0-426d-9f18-ccdac2cd59a3.png">
<img width="522" alt="Screenshot 2021-12-03 at 12 37 31" src="https://user-images.githubusercontent.com/91483522/144628719-8fe75c2a-28d6-4907-877a-374a786ca065.png">

# Design

The design of the app is showcased below:

<img width="674" alt="Screenshot 2021-12-02 at 15 08 34" src="https://user-images.githubusercontent.com/91483522/144628084-bb5b97a1-d302-433d-9a22-c89817b26759.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 09 01" src="https://user-images.githubusercontent.com/91483522/144628096-bd290631-8bcc-4263-8970-17fee409cae8.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 09 09" src="https://user-images.githubusercontent.com/91483522/144628098-0798edbc-6f7e-42d3-a973-4bf5fe0ed1df.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 09 24" src="https://user-images.githubusercontent.com/91483522/144628100-14c36d4c-b3f5-4e44-afc4-1e6cb2b69f09.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 09 38" src="https://user-images.githubusercontent.com/91483522/144628103-2ab5c1ee-6452-4abd-a84d-0575b2861447.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 09 49" src="https://user-images.githubusercontent.com/91483522/144628105-af91d589-18bf-48de-913e-c70abd275d66.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 10 06" src="https://user-images.githubusercontent.com/91483522/144628107-eaf5ac1a-cd78-4045-875e-a457fd085754.png">
<img width="674" alt="Screenshot 2021-12-02 at 15 10 21" src="https://user-images.githubusercontent.com/91483522/144628110-8c9854f9-fca5-4b3e-99f5-1a940257cb50.png">

