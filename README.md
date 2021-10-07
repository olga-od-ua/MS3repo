# Baby Noms

[Live project can be viewed here](https://baby-noms.herokuapp.com/).

The primary goal of the website is to create a platform for recipe storage that is straightforward and easy to use.

The website is aimed at parents of children who start eating solid foods (that is usually anywhere between 4 and 6 months old) and up until school age. It is also aimed at any other child caregiver who is willing to find or share a recipe. Users can register and save their favourite recipes.

The recipes can be marked as Approved by The Irish Health Service Executive by users saving the recipe in case they found that recipe on the [HSE](https://www.hse.ie/eng/) website. However, a warning sign will always be informing all users that they will have to check with their child's doctor before giving any food to preserve the safety aspect of using this website.

## UX

UX PROCESS

**The Strategy Plane**

THE RESEARCH PHASE

1. The primary goal. 
Baby Noms website is designed to provide a platform for recipes for babies and children starting from introducing solids age up until school age. The users will be able to register, browse recipes, search for recipes, add new recipes and save their favourite recipes to their profile.

2. The users will be able to see suggested recipe collections such as: collections according to age group, meal type, cooking time etc. This will help the users locate recipes that will be the most suitable for their needs faster.

3. The customer's estimated needs are to get recipes quickly and easily, save their favourite recipes and add new ones.

### USER STORIES

The target audience is people of all ages who provide childcare to children from the age of starting solid foods up until school-aged children.

## New Users
1. I am Rebecca and I am a new mother to a 6-month-old baby. It is time to start introducing solid foods to my baby but I want to see what other parents cook for their babies.

2. I am Stacy and I am a mother to a 5-month-old baby. It is time to start introducing solids to my baby but I have no experience in cooking for babies. I want to find recipes that other mothers have tried and loved.

3. I am Anna, a mother-to-be, and I just want to browse the different recipes for babies of different age groups to get an idea about what to expect when the baby arrives.

4. I am Claire and I love cooking for my 9-month-old boy! He loves trying new food and self-feeding so I am looking for finger food ideas.

5. I am Chris, a dad to 15-month-old twins and my wife has left on a business trip for a week. I reassured her that I will do my best to look after our kids so I want to find some easy and nutritious recipes to cook for them.

6. I am Kate and I am looking for the tried and tested recipes for babies and toddlers where I could also save them for future reference.

7. I am Julie, a new mother and I am looking for recipes to cook for my 8-month-old girl. I am only looking for recipes of this age group. I would also like to be able to search for different ingredients, methods of cooking (e.g. steaming, boil etc.).

8. I am Mary and I am a grandmother of 5 grandchildren. I love cooking and I often experiment with recipes for my grandchildren. I am looking for a platform to add and store my recipes so that I can retrieve them next time I am cooking for my grandkids.

## Frequent Users

9. I am Barbara and I have all my favourite baby recipes saved in my account. I open it every time I cook for my baby as I am terrible at remembering all the instructions.

## Returning Users

10. I am Gloria and I have an account with BABY NOMS. I have just realized that I added a recipe into the wrong age group and I want to move it to the appropriate one.

11. I am Martina and I'd like to delete some of the recipes I have previously shared on this website as I have been advised by my GP that it is dangerous to give raisins and whole nuts to children under 4 so I want to delete those recipes.


HOW THIS PROJECT IS DIFFERENT FROM COMPETITORS AND SUBSTITUTES

While there is an abundance of websites with weaning recipes and recipes for children of all ages, not many of them are aiming at recipes shared solely by caregivers. The website provides multiple collections of recipes to choose from in order to help users find the most suitable and most relevant recipes. Some of these collections are: 

- "Dad's Favourites" (the users add their status or relation to the child in their registration form, so the collection is created from recipes added by Fathers)

- "Quick Recipes" (created from recipes with cooking time of less than 20 minutes)

- "Super Quick Recipes" (created from recipes with cooking time of less than 10 minutes)

**The Scope Plane**

The website is planned to have three main releases as identified in the table below in order to unfold new experiences for the users in the future. 

[ScopePlaneTable.pdf](https://github.com/olga-od-ua/MS3repo/tree/main/assets/images/scope_plane_table)

This table shows all the website's existing features in the 1st Release column and Features that are still to be implemented in the 2nd and 3rd Release columns.

**The Structure Plane**

The website has the Navbar that will feature linear menu elements representing the self-explanatory main sections of the project, namely:
- Home
- All Recipes
- Add a Recipe (for signed-in users only)
- Manage Age Groups (for Admin only)
- My Favourites (for signed-in users only)
- Register (when no user is signed in)
- Sign in / Sign out

The footer will appear on each of the pages and will have the following information to hand:
- Copyright
- Social networks 

Home page will display various categories of recipes with a link to the relevant list of recipes.

In the PC version, the navigation is presented by the Navbar with inline elements. In the mobile version the navigation is presented by the Burger Icon.

**The Skeleton Plane**

Wireframe can be found [here](https://github.com/olga-od-ua/MS3repo/tree/main/assets/wireframes).

**The Surface Plane**

***Design***
The website is designed in a minimalistic style in order to create the impression of simplicity to the user.

***Colour Scheme***
A mix of deep orange, teal and white are the main colours used throughout the website, creating a vibrant look.

***Typography***

Arial, Helvetica, sans-serif was selected for the majority of the website content to create a clean, informal, minimalistic look.
 
Papyrus font of Fantasy font family was chosen for all the headings to create a playful tone.

***Imagery***

Avocado favicon and background image were selected to match the teal colour and to represent a healthy food option.  

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

### Frameworks, Libraries & Programs

- [Cloudinary](https://cloudinary.com/)
   Cloudinary was used for storing images used for the website's favicon and background image.

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

- [Google Fonts](https://fonts.google.com/)
   Google Fonts was used to import Halvetica font.

- [LunaPic](https://www10.lunapic.com/editor/)
   LunaPic was used to achieve the desired favicon image format.

- [Font Awesome](https://fontawesome.com/)
   Font Awesome was used on some pages of the website to add icons for aesthetic and UX purposes.

- [jQuery](https://jquery.com/)
   jQuery was used to add short-hand interactivity to some elements.

- [Git](http://git-scm.com/)
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- [GitHub](https://github.com/)
   GitHub is used to store the project's code after being pushed from Git.

- [Balsamiq](https://balsamiq.cloud/syvkevx/projects)
   Balsamiq was used to create the wireframe for this project.

## Testing

All pages of the website, all CSS code, all JavaScript code and Python code were validated. The following validation was performed outside the GitPod environment:

- [W3C Markup Validator](https://validator.w3.org/nu/)

  1. Home page contains two warnings about two lacking headings where headings were not intended.

  2. All Recipes page contains two warnings about two lacking headings where headings were not intended. As well as Duplicate IDs errors and warnings caused by a loop.

  3. Add Recipe page contains two warnings about two lacking headings where headings were not intended.

  4. Manage Age Groups page contains two warnings about two lacking headings where headings were not intended.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

1. No errors were detected.

2. The following warning was displayed: "61 The value break-word is deprecated", however, break-word property is needed for responsive styling purposes.

3. [JShint](https://jshint.com).

    All code passed the validation with one minor issue (missed semicolons) that was fixed.

### Testing User Stories from User Experience (UX) Section

## New Users
1. I am Rebecca and I am a new mother to a 6-month-old baby. It is time to start introducing solid foods to my baby but I want to see what other parents cook for their babies.

    a. Upon opening of the website Rebecca will land on the Home Page with various recipe collections available to browse. As a mother she will most probably open Mom's favourite recipes and will continue exploring the recipe ideas in that section. See [screenshot](assets/images/ux_stories_testing/new-user-1a.png).

   b. Alternatively Rebecca can open All Recipes page and explore all the recipes available on the website. See [screenshot](assets/images/ux_stories_testing/new-user-1b.png).

2. I am Stacy and I am a mother to a 5-month-old baby. It is time to start introducing solids to my baby but I have no experience in cooking for babies. I want to find recipes that other mothers have tried and loved.

   Upon landing on the Home Page Stacy will most probably open Mom's favourite recipes and will continue exploring the recipe ideas in that section. See [screenshot](assets/images/ux_stories_testing/new-user-1a.png).


3. I am Anna, a mother-to-be, and I just want to browse the different recipes for babies of different age groups to get an idea about what to expect when the baby arrives.

   Upon landing on the Home Page Anna will most probably navigate to Browse by Age Groups Section and will continue exploring there. See [screenshot](assets/images/ux_stories_testing/new-user-3.png).

4. I am Claire and I love cooking for my 9-month-old boy! He loves trying new food and self-feeding so I am looking for finger food ideas.

   Upon landing on the Home Page Claire will most probably navigate to Browse by Meal Type Section and will navigate to Finger Food recipe collection. See [screenshot](assets/images/ux_stories_testing/new-user-4.png).

5. I am Chris, a dad to 15-month-old twins and my wife has left on a business trip for a week. I reassured her that I will do my best to look after our kids so I want to find some easy and nutritious recipes to cook for them.

   Upon landing on the Home Page Chris will most probably navigate to Dads' favourites recipe collection. See [screenshot](assets/images/ux_stories_testing/new-user-5.png).

6. I am Kate and I am looking for the tried and tested recipes for babies and toddlers where I could also save them for future reference.

   Upon landing on the Home Page Kate will be able to register (see [screenshot](assets/images/ux_stories_testing/new-user-6a.png)) and then save any recipe to her favourites (see screenshot of [Save to favourites button](assets/images/ux_stories_testing/new-user-6b.png) and [My Favourites view](assets/images/ux_stories_testing/new-user-6c.png))

7. I am Julie, a new mother and I am looking for recipes to cook for my 8-month-old girl. I am only looking for recipes of this age group. I would also like to be able to search for different ingredients, methods of cooking (e.g. steaming, boil etc.).

   a. Upon landing on the Home page Julie will see various recipe collections available to browse, the 6-9 months age group will most probably attract her attention. See [screenshot](assets/images/ux_stories_testing/new-user-1a.png).

   b. Julie will also be able to search for Ingredients or Cooking instructions and will only get results from her chosen age group. See [screenshot](assets/images/ux_stories_testing/new-user-1b.png).

8. I am Mary and I am a grandmother of 5 grandchildren. I love cooking and I often experiment with recipes for my grandchildren. I am looking for a platform to add and store my recipes so that I can retrieve them next time I am cooking for my grandkids.

   Upon landing on the Home page Mary will see a very straightforward Navbar menu where she will be able to register (see [screenshot](assets/images/ux_stories_testing/new-user-6a.png)), add recipes (see [screenshot](assets/images/ux_stories_testing/new-user-8a.png)) and save them to her favourites. She will then be able to open her favourite recipes from My Favourites page (see [screenshot](assets/images/ux_stories_testing/new-user-8b.png)).

## Frequent Users

9. I am Barbara and I have all my favourite baby recipes saved in my account. I open it every time I cook for my baby as I am terrible at remembering all the instructions.

   Upon reopening of the website Barbara will be logged in from her previous session. She will be able to retrieve her saved recipes by going to My Favourites page.

## Returning Users

10. I am Gloria and I have an account with BABY NOMS. I have just realized that I added a recipe into the wrong age group and I want to move it to the appropriate one.

   Upon landing on the Home page Gloria will be able to navigate to All Recipes, where she will find her recipe by either using the search or simply by scrolling and she will see the Edit button next to the recipe she added (assuming she is logged in). See [screenshot](assets/images/ux_stories_testing/returning-user-10a.png). Once the Edit button is hit, Gloria will be brought to the Edit Recipe form (see [screenshot](assets/images/ux_stories_testing/returning-user-10b.png))

11. I am Martina and I'd like to delete some of the recipes I have previously shared on this website as I have been advised by my GP that it is dangerous to give raisins and whole nuts to children under 4 so I want to delete those recipes.

   Upon landing on the Home page Martina will be able to navigate to All Recipes, where she will find her recipe by either using the search or simply by scrolling and she will see the Delete button next to the recipe she added (assuming she is logged in). See [screenshot](assets/images/ux_stories_testing/new-user-10a.png). Once the Delete button is hit, Martina will be asked to Confirm or Cancel the deletion (see [screenshot](assets/images/ux_stories_testing/returning-user-11.png))

### Further testing

   1. The website was tested on the following browsers: Chrome, Safari, Samsung Internet app, Internet Explorer.

   2. The website was viewed on the following devices: MacBook Pro (main device for website creation), Samsung Galaxy S20, Samsung Galaxy S21, Samsung Galaxy S8, iPhone Xs, iPhone 11 Pro, iPad Pro, Samsung Curved C34H890 34", LG UltraFine 27UL650-W 27", Samsung Q7 QE55Q7FNA 55".

   3. Thorough testing was carried out to ensure all website's functionality is correct.

   4. All available friends and family carried out remote testing across multiple devices to share feedback and user experience.

   5. Home page was manually tested:
   
   - all links are working and bring the user to the relevant lists of recipes
   - all the categories of recipes that are present in the Database are listed

   6. All Recipes page and recipes.html template were tested manually and are working as expected:
   
   - all recipes are displayed
   - search function is working, checking the Recipe Name, Ingredients and Cooking Instructions fields. 
   - when the user is signed in, the Save button is displayed next to each recipe; as well as Edit and Delete Buttons are displayed next to the recipes which that particular user added.
   - when clicked on See Recipes on the Home Page and brought to the list of recipes of that particular category, Search shows results of only that particular category as opposed to all recipes.

   7. Add Recipe is functioning correctly and only appears when a user is signed in.

   - submit button submits the recipe
   - cancel button redirects to All recipes
   - all the user input is validated where applicable

   8. My Favourites page only appears when a user is signed in. It displays the signed-in user's name, all the saved recipes with the option to Remove from Favourites.

   9. Sign in page signs the user out and only appears on the navbar when a user is signed in. Once signed in, the user is redirected to the Home page and is welcomed by a message with their name.

   10. Sign Out signs the user out.
   
   11. The Navbar elements were tested on all pages and redirect to the correct pages of the website. The "Baby Noms" logo on the very left of the navbar redirects the user to the All Recipes.
   
   12. The footer was tested: all links are functioning correctly, namely, the four social media icons
      
   13. Health warning sign is responsive, appears on each page and can be closed until a page is refreshed.

   14. Register option only appears when there is no signed in user and is functioning correctly. The link to Sign in at the bottom of the Registration form redirects the user to the sign-in form.

   15. Sign in option only appears when there is no signed in user and is functioning correctly. The link to Registration form at the bottom of the Sign in form redirects the user to the Registration form.

   16. When Admin is logged in, Manage Age Groups option appears on the Navbar. Admin is able to edit Age Group names, delete them or add a new one.


### Fixed bugs

1. Background image was the first image to be used as a background image of the body element of the base.html template and an issue was encountered that was not letting the image load. The following methods were tried:

a. body { 
    background: url(/images/avocados.jpeg) repeat 0 0;
}

b. body { 
            background: url("images/avocados.jpeg") repeat 0 0;
        }

c. body { 
            background: url("../images/avocados.jpeg") repeat 0 0;
        }

d. body { 
            background-image: url("../images/avocados.jpeg") repeat 0 0;
        }

e. tried setting min-height: 100%;

f. tried setting background-size: 25px 25px;

g. tried adding the styling directly to the body element in base.html file using the style="" attribute

The bug was eventually avoided by storing the image on [cloudinary](https://cloudinary.com/) and using the link to the image.
 

### Known bugs

Due to the time constraints the following detected bugs have been fixed yet:

1. When a signed-in user tries to share the link to his/her profile, KeyError: 'user' appears when another user tries to follow that link.

2. The close button on the health warning message slightly moves outside the container on small devices.

3. Views of a recipe are added with every click on the materialize icon. This is not the perfect solution as the views are counted every time the collapsible item opens and closes. This means that if a user clicks on the icon to open the collapsible and then clicks on the icon to close the collapsible, 2 views will be added to the recipe. Views are not displayed when a certain recipe collection is listed.

4. When opening the Edit Recipe form, each recipe's Age Group is changed to 0+ months regardless of what age group it had belonged before.

#### Other
Not a bug but a few remarks on the functionality of the website.

1. Users are not automatically signed out when the window closes for the convenience of not having to log in every time the user opens the website. The majority of users of the website are parents or other childminders, which means that any opportunity to save their time will be appreciated. It was initially planned to have a function that would ask the user whether they forgot to sign out when the user would leave the page. However, after thorough research, no reliable method to implement such a warning was found. The forced sign out is not currently implemented as there is no sensitive information displayed about the user on any of the website pages. It is planned to review this feature in the future for possible solutions to improve the website's security.

2. Health warning message appears at the top of every page. It can be closed but it reappears every time the user is redirected to another page. At first, the idea was to give the user the option to only close it once for the duration of the session. However, as irritating as it may be for the user, the decision was made to keep the message reappear in order to keep reminding the user that they should contact their GP for advice when feeding their children.

3. During the development the author included confirm-password input into the Register template without realizing that it gets stored in the Database without any hashing. This security flaw was noticed and rectified.

4. There was an idea to sort recipes by the number of views but this idea was not implemented in order to give all the recipes equal opportunity to be noticed by users. The most reasonable solution for now was to preserve the alphabetical order.

5. Due to the "Add to favourites" function and showing lits of recipes from different categories (def (category_recipes)) it all went into one commit making it a very large commit. Due to time constraints this could not be prevented.

6. At the moment Admin can only add, edit and delete age groups. In the future Admin might be given the opportunity to manage other groups of recipes.

7. It was initially planned to have "HSE approved" group of recipes. However, this group was later removed due to health safety. Users are currently given the option of turning the HSE approved toggle on and off meaning that it is not the most trusted source of medical advice. Hence this group of recipes was removed in order not to encourage relying on this group of recipes as the safest ones. In the future the HSE approved switch access may only be assigned to the admin, or a hired medical professional. At the moment this is not feasible.

8. Views count is not fully functioning on pages other than All Recipes.

9. The following lines of code in recipes.html template are displaying errors:
 - $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
 - let json_recipes = jQuery.parseJSON({{json_data | tojson | safe}});

 10. Currently Dads' Favourites, Mom's Favourites, Grandma's Favourites and Grandfather's Favourites are displaying recipes that users with the relevant status (i.e. Father, Mother, Grandmother and Grandfather respectively) saved to their favourites. Currently a recipe gets added to such a collection even when only one user saves it. It would be better to create such Favourite Recipes collections when more than one user adds recipes to their Favourites (e.g. Only after 20 Fathers added Chicken Footballs to their favourites, this recipe goes to the Dads' Favourites collection).

 An attempt was made to fix the error by wrapping the result of tojson in quotes, however this created further errors.

## Deployment

### Deployment to Heroku

To deploy this page to Heroku from the GitHub repository:

- Use pip3 freeze > requirements.txt to create a list of the dependencies for the website.
- Create a Procfile for Heroku using the command: echo web: python app.py > Procfile
- Use git add -A , git commit -m "(Your commit message)" , and git push , to push these files to your GitHub repository.
- Navigate to Heroku and log in.
- Create a new app by navigating to 'New' and 'Create New App'. Enter your app name and select your region and create app.
- Under the 'Deploy' tab, select 'GitHub - Connect to GitHub'.
- Enter your repository's name in the input field, and connect once found.
- To set your environment variables navigate to the 'Settings' tab and scroll down to 'reveal config vars'
- Add the following variables:

IP:	0.0.0.0
PORT:	5000
MONGO_DBNAME: (The name of your MongoDB database)
MONGO_URI: (Your MongoURI can be retrieved by going to MongoDB -> Collections -> Connect -> Connect to your application. Here you can use your credentials to generate the URI.)
SECRET_KEY: (The secret key is a unique key known only to the developer)

- Navigate to the 'Deploy' tab. To enable automatic deployment, scroll down to the 'Automatic Deploys' section.
- Choose your GitHub branch and enable automatic deployment.

### GitHub Pages

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/olga-od-ua/MS3repo).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/olga-od-ua/MS3repo).
2. To the left of the Gitpod button, click "Code".
3. To clone the repository using HTTPS, under "Clone with HTTPS", click . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click . To clone a repository using GitHub CLI, click Use GitHub CLI, then click "copy symbol".
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

```
$ git clone https://github.com/olga-od-ua/MS3repo.git
```

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Database 

NB: Initially "Categories" collection had a different role in the project. It would have been more logical to call "Categories" collection "Age Groups" as it only contains Age Groups information in it.

Please find screenshots below:
- [Categories/Age Groups](assets/images/mongodb_scrrenshots/Categories-AgeGroups.png)
- [Cooking Time](assets/images/mongodb_scrrenshots/CookingTime.png)
- [Meal Types](assets/images/mongodb_scrrenshots/MealTypes.png)
- [Recipes](assets/images/mongodb_scrrenshots/Recipes.png)
- [Statuses](assets/images/mongodb_scrrenshots/Statuses.png)
- [Unique Categories](assets/images/mongodb_scrrenshots/UniqueCategories.png) used for the first section of categories on the Home Page
- [User Favourite Recipes](assets/images/mongodb_scrrenshots/UserFavouriteRecipes.png)
- [Users](assets/images/mongodb_scrrenshots/Users.png)

## Credits

### Content

1. Some recipes were taken from [Annabel Karmel's weaning guide](https://www.annabelkarmel.com/recipe-category/baby-recipes/).

2. Other recipes were taken from [BBC Good Food](https://www.bbcgoodfood.com/recipes). 

### Media

1. The Avocado image used for the background of the templates was taken from [here](
https://wallpapercave.com/avocado-desktop-wallpapers).

2. The avocado favicon image was taken from [PNGEGG website](https://www.pngegg.com/en/png-eiayq).

### Code
1. The majority of the website's functionality was built relying on the Code Institute's study materials.

2. category_recipes, _add_view_on_recipe functions was built with guidance from Andrij Derkach.

3. Some other borrowed code blocks or ideas are mentioned in comments of the templates and the app.py file. I am Ukrainian and speak both Ukrainian and Russian so some of the sources are in my native languages.

### Acknowledgements

1. My mentor for professional support and guidance.

2. My husband Kevin for continuous support and encouragement.

3. For the constant assistance from my 11-month-old daughter Mila who was with me throughout and inspired to create the recipes website as she is a proper "foodie".