![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Manchester United Supporters Away Travel Company

![Am I Responsive Image](media/images/README/am_i_responsive2.png)

## CONTENTS

- [Manchester United Supporters Away Travel Company](#manchester-united-supporters-away-travel-company)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Key Information for the site](#key-information-for-the-site)
    - [User Stories](#user-stories)
      - [Client Goals](#client-goals)
      - [First Time Visior Goals](#first-time-visior-goals)
      - [Returning and Frequent Visitor Goals](#returning-and-frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Future Implementations](#future-implementations)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
    - [Accessibility](#accessibility)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
    - [W3C Validator](#w3c-validator)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
    - [Lighthouse](#lighthouse)
      - [Index Page](#index-page)
      - [Base HTML](#base-html)
      - [New Booking](#new-booking)
      - [Edit Booking](#edit-booking)
      - [Booking Success](#booking-success)
      - [My Bookings](#my-bookings)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [ Media](#media)
    - [ Acknowledgments](#acknowledgments)

---

## User Experience (UX)

- Manchester United Supporter Travel Company is a online coach booking club that allows football supporters (Users) to book couch travel to a specific football match. The site allows supporters to view upcoming couch trips for upcoming games and book seats on the coach so they can travel in style to the football game.

### Key Information for the site

- What trips are available to book.
- Trip Details.
- How to create, edit and delete a booking.
- To be able to review what bookings you have.
- How to become a member and sign up.
-

### User Stories

#### Client Goals

- To be able to view the site on a range of device sizes.
- To make it easy for potential memebers to find a Trip and book seats easily.
- To make it clear for members to create, edit and delete bookings.

#### First Time Visior Goals

- I want to find out what Manchester United Travel Company is and how I can take part.
- I want to be able to navigate the site easily to find information.
- I want to be able to find their social links.

#### Returning and Frequent Visitor Goals

- I want to find upcoming trips and be able to book onto them.
- I want to be able to view, edit and delete my bookings.

## Design

### Colour Scheme

![Manchester United Travel Company Wesbite Color Palette](media/images/README/Coolors.png)

- The website uses a palette of reds, whites and blacks that are linked to the colors of Manchester United. The color palette was created using the [Coolors](https://coolors.co/) website.

### Typography

- Default fonts were used for the following:
  - Headings
  - Body
  - Messages

### Imagery

- Images were used from the [Unsplash](https://unsplash.com/) website.

### Wireframes

- Wireframe were created which are linked below:
  - ![Wireframe Designs](media/images/README/Wireframe.png)

## Features

The website is comprised of five pages:

- Index Page (Home)
- My Bookings
- New Booking
- Booking Success
- Edit Booking

Three of the pages are accessible from the navigation bar (Home, My Bookings, and New Booking, however this is dependant on whether a User has registered and is logged in, as some links are only visiable to logged in registered users)

Booking success is only visiable to a user, once they have created a booking. Edit booking is only visiable to a user once they edit an existing booking.

- ALl Pages on the website have:

  - If user has registered and logged in:
    - A responsive navigation bar at the top which allows the users to navigate through the site. To the left of the navigation bar is a space that when a user is registered and logged in displays Welcome 'User Name', this indicts to the user that they are logged in. To the right of this, are the links to the website pages (Home, Logout, My Bookings, New Booking). To allow a good user experience of the site, which the website is shown on smaller devices, the navigation bar changes to a burger toggler. This was implemented to give the site a clean look and to promote a good user experience, as users are used to seeing the burger icon when on smaller devices to navigate a site.
  - If the user is not logged in:
    - A responsive navigation bar at the top which allows the user to navigate through the site. The navigation bar has links to (Register and Login). All other links are hidden from non registered user, as the website requires you to be a registered user to make a booking. To allow a good user experience of the site, which the website is shown on smaller devices, the navigation bar changes to a burger toggler. This was implemented to give the site a clean look and to promote a good user experience, as users are used to seeing the burger icon when on smaller devices to navigate a site.

- A footer which contain social media icon links to Facebook, Twitter, YouTube and Instagram. Icons were used as it keeps the footer clean and becuase they are universally recognisable.

- Home Page

  - A clear heading informing the user what the site is about.
  - A basic section giving information to the user about the services offered by the website.
  - A live Upcoming Trip list, which displays the following to the user:
    - Trip ID - this is the ID number of the trip
    - Trip Name - this display the name of the upcoming trip to the user, informing them of the destination of the trip
    - Seats - Informing the user how many seats the coach has and therefore how many seats are available to book on each trip
    - Remaining Seats - Informs the user how many seats are available to book. This is a live number as once a user books a number of seats, it is subtracted from this number.
    - Price - the price of booking a seat on this trip.

- My Bookings

  - This page displays to the user their bookings. It shows booking that are assigned to them.
    - Trip Booked
    - Trip Date
    - Comments - Any comments the user made when they made their booking.
    - Seats Required - how many seats the user booked.
    - Total Cost - How much the total booking costs. It is the sum of the trip cost x seats required.
    - Edit Button - this allows the user to enter the booking and edit the booking. (Directs them to the editbooking page)
    - Delete Button - this allows the user to delete the booking.

* New Booking

  - This page contains a form which allows the user to make a new booking. It contains fields for the following:
    - Date of Booking - This is set as a default of today's date, but can be edited by the user.
    - Selected Trip - This is a dropdown list, which allows the user to select from the Trips that are available to book.
    - Numbers of Seats Required - This allows the user to input how many seats they would like to book.
    - Additonal Comments - This field allows the user to input any comments about the booking that they want to make when they make their booking.

* Edit Booking

  - - This page contains a form which allows the user to edit an existing booking. It contains fields for the following:
  - Date of Booking - This is set as a default of today's date, but can be edited by the user.
  - Selected Trip - This is a dropdown list, which allows the user to select from the Trips that are available to book.
  - Numbers of Seats Required - This allows the user to input how many seats they would like to book.
  - Additonal Comments - This field allows the user to input any comments about the booking that they want to make when they make their booking.

* It allows the user to edit a existing booking and will update the database accordingly.

* Booking Success
  - The page contains a booking confirmation summary. It display the following to the user:
    - The name of the trip booked.
    - Number of Seats booked.
    - The total cost of the booking.

### Future Implementations

- Create a About Us Page - to provide visitors and users of the site more information about the Manchester United Travel Company
- Create a system where the User can pay for bookings online. At the moment the user merely makes the booking online and this is assigned to them. I would like to create a payment system where the user can pay for the booking and then this will provide them with a booking reference they can provide to the coach driver on the day to gain access to the coach.
- A gallery page where the visitors/users can view images of previous trips to improve the user experience.
- A Booking Trip page, where the user can view multiple upcoming bookings and this will also display which trips are sold out, close to being sold out etc.

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python and Django

### Frameworks, Libraries & Programs Used

Balsamiq - Used to create WireFrames

Codeanywhere - For version control

Github - To save and store the files for the website

Bootstrap - The framework for the website.

Font Awesome - For the icongraphy on the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

[Am I Responsive](http://ami.responsivedesign.is/) To show the website on a range of devices.

### Accessibility

- I have been mindful during the coding to ensure that the website is as accessible friendly as possible. I hav eachieved this by:
  - Using semantic HTML.
  - Using descriptive alt attributes on images on the site.
  - Ensuring that there is a sufficient colour contrast throughout the site.
  - Ensuring menus are accessible by marking the current page as active for screen readers.

## Deployment & Local Development

### Deployment

Heroku was used to deploy the live website. The instruction to achieve this are below:

1. Log in to Heroku.
2. Find the app from this project and open - rbproject-4.
3. Click on deploy.
4. Find 'App connected to Github' and link to Github account.
5. Search for repository and link - RichBurman/Project_4.
6. Find Manual Deploy and click Deploy Branch.
7. Click on Open App at the top right of the screen to view the live site.

[Live site link ](https://rbproject-4-c2dc0a612356.herokuapp.com/)

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, RichBurman/Project_4
3. Click the Fork button in the top right corner.

#### How to Clone

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, RichBurman/Project_4
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

- Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along.

### W3C Validator

All codes for Project and App were tested using the [CI Python Linter](https://pep8ci.herokuapp.com/) and are valid.

Project_4

- [urls.py](media/images/README/projecturls_valid.png)
- [settings.py](media/images/README/settings_valid.png)

football_travel

- [admin.py](media/images/README/admin_view_valid.png)
- [forms.py](media/images/README/forms_view_valid.png)
- [models.py](media/images/README/models_view_valid.png)
- [urls.py](media/images/README/urls_views_valid.png)
- [views.py](media/images/README/views_views_valid.png)

All CSS returned as valid.

- [CSS](media/images/README/css_valid.png)

All HTML returned as valid.

- [base.html]()
- [booking_success.html]()
- [editbooking.html]()
- [index.html]()
- [mybookings.html]()
- [newbooking.html]()


### Solved Bugs

### Known Bugs

### Lighthouse

#### Index Page

#### Base HTML

#### New Booking

#### Edit Booking

#### Booking Success

#### My Bookings

## Credits

### Code Used

### Content

###  Media

- All images were taken from Unsplash
- All images were compressed using Optimizilla to aid website performance.
- Screenshots taken from the following website for this README
- Lighthouse
- Jigsaw validator
- W3C validator
- Am I Responsive?

###  Acknowledgments
