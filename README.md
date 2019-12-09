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

 

- My wireframe sketch was uploaded to the root folder under the energy-glossary project, as wireframe.jpg (GIVE FULL PATH). It shows the wireframe for the 'read' page and the 
'add/update' form. 

 


## Features

The site consists of 2 main pages, a 'read' page to view glossary entries and a 'add/update' page with a form for creating and
modifying glossary entries. There is a navbar across the top showing the website title "Energy Glossary", a search input box, and 
menu items for Add, Update, and Delete . The main part of the page displays the glossary entry (title and description) or 
the edit form. There is a floating action button displayed on the bottom right of the screen which expands on being clicked,
to show the Add, Update, and Delete options.


 
### Existing Features
- On loading the page for the first time on any device

- A CSS media rule is included to reduce the height of the map area to 65% of the vertical space on the page, for screen heights of 320 pixels or less. This
  keeps the bottom message area visible in landscape mode for the Motorola Moto G4 and iPhone 5/SE phones.

### Features Left to Implement

- Future versions of the webpage could include 

## Technologies Used

- This project uses **HTML** for basic layout and text, and **CSS** for styling the content. The HTML includes screen reader content also.

- [Bootstrap](https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)
    - This project uses **Bootstrap** to ease development by use of the Bootstrap grid system and design templates. It provides responsive CSS to adjust to 
      different screen sizes in phones, tablet and desktop devices. The Bootstrap Navbar feature is used to provide access to the settings, and logo at the       top of the page. A Bootstrap modal is used for the settings inputs.

- **Javascript** is used for the main coding of the interactive and logical elements. It handles the interaction with the Google Maps API, the inputs and prompts to   the user, and the decision/display logic around the search results.

- [JQuery](https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js)
  **jQuery** is used to select and control some of the HTML elements, for example updating the status/prompt text area at the bottom of the webpage.

- [Popper](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js)
For popovers and drop down menus. Provides dynamic positioning and viewport detection.

- The **Google Maps API** is used to interface with Google Maps for the main map display on the page, and all search and display functions for the map.

- [FontAwesome](https://use.fontawesome.com/releases/v5.1.1/css/all.css) for the "lightning" marker icon.

## Testing

The website was tested with the following devices and scenarios:

- Asus F553M laptop with Google Chrome,Microsoft Edge and Opera browsers
- Asus F553M laptop with Google Chrome developer tools used to view various mobile (phone and tablet) device screen sizes
- Apple iPhone
- Motorola Moto G4 Android smartphone with Google Chrome
- Samsung Galaxy Tab 2 Android tablet with FlashFox browser

Testing showed the following results:
The page loaded successfully on all devices. The settings modal popped up on first use on a device, as designed. The map, and charge point markers were visible centred on the search location. The search operated correctly from a GPS located location or alternate location selected by the user, and a default location. Settings were stored correctly in local storage, and available on re-opening the site. There were some cases in landscape mode on mobile devices where the settings modal text area was partially obscured by the footer border. However, the Cancel and Save buttons remained visible.
The test cases were as follows:

### Test Cases
1) First time page load (settings modal should pop up and the user is prompted to configure)

2) Selection of Tesla charge points only filter

3) Blink interval setting (0 and non-zero)

4) Default location setting

5) Map centering and search operation

6) Marker display including closest marker

7) Charge point selection and confirmation

8) Navigation/route preview operation

9) Alternate start point selection and search

10) 65% map height media rule for iPhone 5/SE and Moto G4 in landscape mode

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
| **10** | N/A  | N/A | N/A  | Pass | Pass  | Pass | N/A  | 





## Deployment

The project was deployed on GitHub Pages. To do this, I clicked on the "Settings" tab of the charge-locator repository in GitHub. Then I scrolled down to the GitHub Pages section. From the Source drop-down menu I selected "master branch" to deploy the website from the latest master code. GitHub then published the website at: [charge-locator](https://rphanley.github.io/charge-locator/)

- **Local Install**: The website can be installed locally by clicking the "Clone or download" button at : [charge-locator](https://github.com/rphanley/charge-locator), then clicking on "Download ZIP" to download the folder structure and all files to your device.



## Credits

### Content
- Modal logo and car icon courtesy of bigstockphoto.com. 
- Lightning marker icon courtesy of FontAwesome.

### Media

### Acknowledgements
I want to acknowledge the invaluable help and guidance of my tutor Xavier, and mentor Ignatius, in developing this project.
