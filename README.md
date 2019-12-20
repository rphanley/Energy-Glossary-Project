# Energy-Glossary Project

This project was created as a glossary for terms used in the energy industry . It uses a MongoDB database to store the glossary.
The user can perform all standard database actions (Create, Read, Update, Delete) from the website. They can enter a search term
and view any result on screen. It can then be updated or deleted. The user can also add a new glossary entry and save it to the
database.
 

 
## UX

I created this project because I have a qualification in and strong interest in renewable energy particularly. I saw the need 
for an online glossary of terms for the energy industry, especiallly with the rapid pace of change in the industry in 
recent years. 

 
The target user of the site is anyone who has an interest in or is employed in the energy industry. The site is aimed at the following user stories:

1)   I need a description or more detail on an energy related term I have seen. I want to search the glossary database for the term
     and get the description for it.

2)    I am an expert or  am knowledgable in an energy related area, and I want to add an entry to the glossary database for 
      reference by other users.
 

3)    I want to update or correct an existing glossary entry, originally written by me or another user.

4)    I want to delete a glossary entry which is obsolete or incorrect.

 

 My original wireframe sketch was uploaded to the root folder under the energy-glossary project, as wireframe.jpg (/app/wireframe.jpg in the deployed app). It shows the wireframe for the 'read' page and the 
'add/update' form. 

 


## Features

The site consists of 4 pages, a 'home' page, a 'read' page, an 'add' page and an 'update' page. There is a navbar across the top showing the website title "Energy Glossary", and 
buttons for Add, Update, and Delete displayed as appropriate to the page being displayed. These buttons appear on larger devices e.g laptops.
Alternatively for smaller devices, there is a floating action button displayed on the bottom right of the screen which expands on being clicked,
to show the Add, Update, and Delete options.

 

 
 
### Existing Features
- The 'Home' page contains a search input box, and a selectable list of the 10 latest terms entered into the database. The user can either
enter a term to search for, or select one of the latest entries by clicking.

- Once found, the glossary entry is displayed on the 'read' page with the energy term on top and its description underneath. If the term has been entered into the database today, a 'New!' badge is 
displayed beside it in red. There is a button under the description to allow the user to go back to the 'home' page for a new
search. The Add, Update and Delete buttons are available in this view, with Update and Delete applying to the viewed entry.

- The page can be scrolled if needed to view longer descriptions. On mobile devices, the floating action buttons remain in place
while scrolling.

- The 'Add' page has a form to allow input of a new term name and its description. When complete, the user clicks the "Add Entry"
button at the bottom to add the entry to the database. The new entry is then displayed on the 'read' page with a flash message
confirming that it was created. 

- The 'Update' page uses a similar form with the term and description displayed for editing. The user clicks on the "Update Entry"
button to submit the changes. Again the updated entry is displayed on the 'read' page with a message confirming the update.

- An entry displayed on the 'read' page can be deleted by selecting the Delete button on the visible menu. A pop-up dialog
asks the user to confirm the deletion by clicking OK, or Cancel to keep the entry. If the user clicks OK, the 'home' page is 
displayed with a message confirming that the entry was deleted.

- The user can also return to the Home page at any time by clicking on the "Energy Glossary" page title on top of the page.


### Features Left to Implement

- Future versions of the glossary could include an autocomplete search input, where the app displays a list of database entries
  potentially matching the user input as it is typed. The user could select an entry after typing part of the term name.

- If a search fails, the app could show a list of suggested terms which have similar words to the search term.

- The home page could display all of the database entries in a paginated list, with the user scrolling through them and
selecting the next page as required. This would allow browsing of all the entries.

- The app could maintain a list of the most popular search terms used.

## Technologies Used

- This project uses **HTML** for basic layout and text, and **CSS** for styling the content.

- [MongoDB](www.mongodb.com)
    - This project uses a web based MongoDB database as its data store. It is a document-based database which uses
      BSON, a JSON-like dictionary format to store data. In this case the database records consist of a dictionary with
      the term name 'term' and the description 'description'. The database was uploaded to MongoDB in csv format.

- [Flask](https://palletsprojects.com/p/flask/)
    - This project uses the Flask micro web framework. It is a light weight Python based framework. It is used here to 
      route to Python functions for each of the CRUD (Create, Read, Update, Delete) database operations. It uses the Jinja
      templating language to read and write variables to/from the HTML template pages. The project uses a base.html for 
      elements common to all pages such as the top navbar. The other page templates provide additional content for their
      respective functions.

- [Materialize](https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)
    - This project uses the  **Materialize** front end framework to ease development by use of its grid system and design templates. It is based on Material Design by Google to 
    speed up development and is responsive to different screen sizes in phones, tablet and desktop devices. Its Navbar feature is used to provide access to the settings
    at the top of each page for large devices, with its Floating Action Buttons being used to provide menu access for mobile devices

- **Javascript** is used to initialize the floating action button menu for use on mobile devices.

- [JQuery](https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js)
  **jQuery** is used to select and initialize the navbar and floating action button menus.


- [Material Icons](https://fonts.googleapis.com/icon?family=Material+Icons) is used with Materialize for button icons.

- [Heroku](https://heroku.com)
    - This project is deployed on the Heroku platform, which is used to host web applications in many programming languages
    including Python. The applications run in virtual containers known as "Dynos".

## Testing

The website was tested with the following devices and scenarios:

- Asus F553M laptop with Google Chrome,Microsoft Edge and Opera browsers
- Asus F553M laptop with Google Chrome developer tools used to view various mobile (phone and tablet) device screen sizes
- Apple iPhone
- Motorola Moto G4 Android smartphone with Google Chrome
- Samsung Galaxy Tab 2 Android tablet with FlashFox browser

Testing showed the following results:
The application pages loaded successfully on all devices. CRUD functionality was tested successfully on each. There were
some issues with the floating action buttons appearing "squashed" on mobile devices in landscape mode. However, they remained
visible and performed as expected, with the glossary text visible. It was necessary to apply CSS to the floating action button
sizing and positions, since they seemed very small with the standard Materialize settings on mobile devices.

The test cases were as follows, run manually in sequence:

### Test Cases
1) Home page load: Home page should load with the search input box, list of 10 latest entries, and the Add button visible.

2) Search: Input e.g "Global Warming" in the search input and press Enter. The glossary entry should be displayed on the Read
   page with a "Back to search page" button under the description. The Add, Update, and Delete buttons should be visible.

3) Return to search: Click the "Back to search page" button. The Home page should be displayed again as in testcase 1.

4) Latest entry select: Select one of the 10 latest entries from the list. The glossary entry should be displayed in the Read
   page, again with a "Back to search page" button, and the Add, Update, and Delete buttons visible.

5) Add entry from Home: Click the "Back to search page" button. The Home page should be displayed again as in testcase 1.
   Click the Add button. The Add form, titled "Add Glossary Entry", should appear, with input boxes for the term name and its
   description. There should be an "Add Entry" button under the form. Type in a test entry and click Add Entry. The new entry
   should appear on the Read page with a message 'Entry for "<test entry name>" created!'. There should be a red "New!" label
   to the right of the entry name. 

6) Update entry from Home: Click the "Back to search page" button. The Home page should be displayed again as in testcase 1.
   Verify that the new entry has been created by searching for it, and by selecting it from the latest entries. Click the Update
   button. Update the entry by modifying its name or description. Click the "Update Entry" button under the description. The updated
   entry should appear on the Read page with a message 'Entry for "<test entry name>" updated!'. There should be a red "New!" label
   to the right of the entry name.


7) Delete entry from Home: Click the "Back to search page" button. The Home page should be displayed again as in testcase 1.
   Verify that the new entry has been updated by searching for it. Once it appears in the Read page, click the Delete button.
   There should be a popup window with the message "Are you sure you want to delete the entry", and Cancel and OK buttons.
   Click Cancel, and the window should close. Click the Delete button again, and this time click OK on the popup window.
   The Home page should be displayed, with a message 'Entry for "<test entry name>" deleted!'. 

8) No result found test: Verify that the test entry has been deleted by searching for it. The Home page should be displayed,
   with a message 'No result found for "<test entry name>" .Check your spelling and try again'.

9) Add entry from Read: From the Home page, select an entry by searching or selecting it from the latest list. The Read page
   should display the selected entry. Click the Add button, and continue as in testcase 5. The new entry should be created
   as before.

10) Home link from Read: Search for or select an entry. From the Read page, click on the "Energy Glossary" title on the top
    of the page. The Home page should be displayed.



**Test Table**

|  **Test Case**    |  **Chrome**         |  **Edge**           |  **Opera**        |  **Dev tools**         |  **iPhone**          |  **Moto G4**     |  **Galaxy Tab2** |       
| ------------- | ----------- | ------- | -------- | ------------- | ---------- | ----------- | ------------- |  
| **1** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **2** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **3** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **4** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **5** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **6** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **7** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **8** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **9** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |
| **10** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |





## Deployment

The project was deployed on [Heroku](https://heroku.com). The project was first checked in and pushed on GitHub. A new user
account was created on Heroku. From the Personal page, the New button was used to create the app "energy-glossary".
Then clicking on the newly created app, first the config variables were set in the Settings tab: 
- IP = 0.0.0.0 for localhost,
- MONGO_URI = the connection string specified by MongoDB (including the database collection, username and password)
- PORT = 5000
- SECRET_KEY = a secret key used in the application to allow use of flash messaging in Flask.

 Then in the Deploy tab, GitHub was selected as the deployment method. The Heroku app was then connected to the 
energy-glossary repo on GitHub (https://github.com/rphanley/energy-glossary). Scrolling down on the Deployment page on Heroku, 
in the Manual deploy section, the master branch was selected. Then the "Deploy Branch" button was clicked to run the deployment
on Heroku. The project is deployed at [energy-glossary](https://energy-glossary.herokuapp.com/).


- **Local Install**: The application could be installed locally by for example, creating a virtual environment on a Linux
system (https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments). The source files are avaiable to
download from [GitHub](https://github.com/rphanley/energy-glossary) using the Clone or download button. The pre-requisites for the
application, such as Flask, can then be installed from the Linux command line using: pip3 install -r requirements.txt   .
Then run the application using: python3 app.py




## Credits

### Content
- Sample energy glossary courtesy of [California Energy Commission](https://www.energy.ca.gov/resources/energy-glossary)



### Acknowledgements
I want to acknowledge again the help and guidance from my tutor Xavier, and mentor Ignatius, in developing this project.
