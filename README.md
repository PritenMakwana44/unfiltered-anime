# Contents

[Unfiltered Anime](#unfiltered-anime)

[UX](#ux)
+ [User Stories](#user-stories)
+ [Agile](#agile)
+ [Wireframes](#wireframes)
    + [Main Page](#main-page)
    + [Sign-Up Page](#sign-up-page)
    + [Sign-In Page](#sign-in-page)
    + [User logged-in Home Page](#user-logged-in-home-page)
    + [Admin logged-in Home Page](#admin-logged-in-home-page)
    + [User or Admin watchList page](#user-or-admin-watchlist-page)
    + [User Review detail user or non user Page](#user-review-detail-user-or-non-user-page)
    + [User Review detail own post or admin Page](#user-review-detail-own-post-or-admin-page)
+ [Existing Features](#existing-features)
    + [Navbar](#navbar)
    + [Review detail](#review-detail)
    + [Sign In](#sign-in)
    + [Sign Up](#sign-up)
    + [Sign Out](#sign-out)
    + [Log in Alert](#log-in-alert)
    + [User Nav](#user-nav)
    + [Review List](#review-list)
    + [Add Review](#add-review)
    + [Watch Later List](#watch-later-list)
    + [Review detail admin or user own](#review-detail-admin-or-user-own)
    + [Upvote or Downvote](#upvote-or-downvote)
    + [Comments](#comments)
    + [Comments as an admin](#comments-as-an-admin)
    + [Comment approval](#comment-approval)
    + [Footer](#footer)
    + [Login as admim](#login-as-admin)
    + [Admin center](#admin-center)
+ [Future Features](#future-features)

[Technologies Used](#technologies-used)
+ [Technologies and Programs Used](#technologies-and-programs-used)


[Testing](#testing)
+ [Functionality and Compatibility Testing](#functionality-and-compatibility-testing)
+ [Code Validator Testing](#code-validator-testing)
+ [SEO Testing](#seo-testing)




# Unfiltered Anime

[![home page](readme/images/responsive.png)](https://unfiltered-anime.herokuapp.com/)

Live Site: [Click Here](https://unfiltered-anime.herokuapp.com/)
Github: [Click Here](https://github.com/PritenMakwana44/unfiltered-anime)

The purpose of this website is to allow users to write reviews on their favourite Anime. The website then allows other users to read the reviews, comment on reviews and add to the reviews to their Watch List so they can watch their new favourite anime film/show later.

The Ultimate goal is to bring Anime fans togther, share their passion of Anime and find new Anime.

## UX

### User Stories
Github was used to manage User stories and bugs.

#### User stories

1. USER STORY: View Review list
    - Review List is on home page for users to see all Reviews.
    - If you click a review in the review list it opens up the review.

2. USER STORY: Create Review
    - There is a Create review button for any user to create Anime reviews.
    - User must have account created to create a review.
    - Once review is created it's shown on the Review list.
3. USER STORY: Delete Review
    - User can delete their own Reviews using a button.
    - Button does not show unless user is creator of the review.
4. USER STORY: Edit Review
    - User can edit their own Reviews using a button.
    - Button does not show unless user is creator of the review.
5. USER STORY: Upvote/downvote review
    - User can upvote or downvote any post
    - Upvotes and downvotes numbers are shown in Review list. 
    - One can not upvote and downvote the same post.
6. USER STORY: Account Registration
    - User must register an account.
    - User gets access to many diffrent functions once registered such as adding reviews,comments and reviews to their review list.
    - A user can login or logout as they please.
    - A user can create as many accounts as they want.
7. USER STORY: Comment On Review
    - Users can Comment on any Review including their own.
    - Function is used to create a feel of community. 
8. USER STORY: View Comments
    - Users can view anyones comments on any post.
9. USER STORY: View upvote/downvotes
    - Users can see number of Upvotes and downvotes on each review.
10. USER STORY: Site pagitnation
    - If user reaches 10 reviews on a page, they will then have pagitnation acitive which then gives them a next page button.
11. USER STORY: Add review to watch later
    - If user is logged in they can add any review to their Watch later list via a button.
12. USER STORY: Watch later section view
    - If user is logged in they get an extra tab on their Navigation bar called Watch later.
    - The watch later button leads them to see all Anime reviews on another page.
13. USER STORY: Manage Reviews
    - If User is an admin then they can manage reviews via admin panel or certain features on webiste.
    - They can delete or edit any review via public site or admin panel.
14. USER STORY: Manage comments
    - If User is an admin then they can manage comments via admin panel or limited features on website.
    - They can delete any comment via either admin panel or site. 
    - Future functionality will allow them to approve or disapprove any comment as all comments require authorisation.
15. User Story: 404 error
    - Future feature will have a 404 error website which allows them to navigate to the real site.

### Agile

![UserStories](readme/images/Userstories.png)

Github issues was used to create the User stories. 
Can find my Github issues here: [Cick Here](https://github.com/users/PritenMakwana44/projects/4/views/1).
The sections are split into Todo, Inprogress, End user function done, Admin function done and future.


## Wireframes 

I used Balsamiq to create my wireframes. I based my designs on a desktop site first then made them responsive after built.

### Main Page
The main page is my home page for the review site.
![Mainpage](readme/images/wireframe/Mainpagelayout.png)

### Sign-Up Page: 
This is the page for users to sign up.
![Signup](readme/images/wireframe/Signup.png)

### Sign-In Page:
This is the page for users to sign in.
![Signip](readme/images/wireframe/Signin.png)

### User logged-in Home Page:
Once the user logs in the nav bar changes. Here is the view.
![Userloginhome](readme/images/wireframe/UserloginHome.png)

### Admin logged-in Home Page:
Once the admin logs in the nav bar changes. Here is the view.
![Adminloginhome](readme/images/wireframe/AdminloginHome.png)

### User or Admin watchList page:
This is the view for the WatchList.
![User-or-admin-watchlist](readme/images/wireframe/User-admin-WatchList.png)

### User Review detail user or non user Page:
When the user or non logged in user clicks on a post this is the detail page.
![User-Review-detail-user-or-non-user](readme/images/wireframe/User-Review-detail-user-or-non-user.png)

### User Review detail own post or admin Page
This is what the page would look like when admin or user is logged in.
![User-Review-detail-own-post-or-admin-Page](readme/images/wireframe/user-review-detail-own-post-or-admin.png)



## Existing Features


### Navbar
For anyone who comes into the site this is the default navbar. The navbar includes a sign in and sign out function.
![navbar](readme/images/features/review-home-signup-signin.png)


### Review detail
Here is the view when you click on a post when your not logged in.
![review-detail-1](readme/images/features/review-detail-1.png)
![review-detail-2](readme/images/features/review-detail-2.png)


### Sign In
Here is the sign in page.
![signin](readme/images/features/signin.png)


### Sign Up
Here is the sign up page.
![signup](readme/images/features/signup.png)


### Sign Out
Here is the sign out page.
![signout](readme/images/features/signout.png)


### Log in Alert.
Here is what the alert looks like when you log in. 
![login-alert](readme/images/features/logged-in-alert.png)


### User Nav
Here is what the Nav bar looks like when your logged in.
![user-login](readme/images/features/user-nav.png)


### Review List
Here is the list of reviews on the home page under the navbar.
![review-list](readme/images/features/review-list.png)


### Add Review
Here is what it looks like for a logged in user to add a review. Only logged in users can do this. This is a form for Users to fill out. 
![Add-review-1](readme/images/features/add-review-1.png)
![Add-review-2](readme/images/features/add-review-2.png)


### Watch Later List
Each review has a add to watch list button for a logged in user. This adds the review to the watch later list. There is a remove from watch later button each review. It removes the review from the watch later list. Users also are able to open the review by clicking the post too. 
![watch-list-1](readme/images/features/watch-list-1.png)
![watch-list-2](readme/images/features/watch-list-2.png)


### Review detail admin or user own
If an admin logs in they get the option in the review post itself to edit or delete a review. If a user is logged in then they can edit or delete their own post only.
![review-detail-admin-user-1](readme/images/features/review-detail-admin-or-user-own-1.png)
![review-detail-admin-user-2](readme/images/features/review-detail-admin-or-user-own-2.png)


### Upvote or Downvote
If a user is logged in then they can either upvote or downvote. They can't do both.

![upvote/downvote](readme/images/features/upvote-downvote-icons.png)


### Comments
Here is what the comments section looks like for any logged in user. If you comment on a post as a user it then gets sent to the admin for authorisation.
![comment-section](readme/images/features/comments-section.png)
![comments-auth](readme/images/features/comment-auth-alert.png)


### Comments as an admin
Here is what the comments section looks like as an admin. The extra feature is that admin can delete any comment from any user as feature to make sure all comments are appropriate.
![admin-comment](readme/images/features/admin-comment.png)


### Comment approval
Here is where the admin can approve comments. This is in the admin panel.
![admin-panel-comments](readme/images/features/admin-center-comments.png)


### Footer
The footer has been kept basic just my trademark as for who created the site.
![footer](readme/images/features/footer.png)


### Login as admin
If an admin is logged in. They get access to a diffrent nav bar with access to the admin panel.
![review-admin-login](readme/images/features/review-login-admin.png)


### Admin center
Here is where the admin can make any changes they would like within the admin panel.
![admin-panel](readme/images/features/admin-center-menu.png)

## Future Features
    1. 404 error pages
    2. Allow admin to approve comments via the Review site itself.
    3. Be able to add friends and direct message.
    4. Better account management i.e email address and profile picture.
    5. Crunchy roll Anime streaming site integration.

# Technologies Used
### Technologies and Programs Used:
+ GitHub
    + Used for version control
    + Used for issue management
    + Used for Agile manage tool
    + Hosted platform for website
+ Heroku 
    + App deployment
+ ElephantSQL
    + Used as the database for project
+ Cloudinary
    + Used for static media storage
+ Balsamiq:
    + Create wireframes
+ Bootstrap:
    + Style webiste
+ Font Awesome:
    + Used for Icons
+ Google Fonts
    + Used for Fonts
+ Languages used
    + HTML5
    + CSS3
    + Javascript]
    + Python
    + Django
+ Gitpod - IDE
+ Google - Research platform.

# Testing
## Functionality and Compatibility Testing
For functionality testing I tested my website in all diffrent sizes in chrome, firefox and safari.
My project looked great on all browsers and were responsive on mobile, tablet and desktop. There was room for improvement but the responsiveness was still functional.

## Code Validator Testing
HTML:


I used the following Html validator to validate my project. It was validated via: https://validator.w3.org/
![html-val](readme/images/testing/html-val.png)


CSS:


I used the following CSS validator to validate my project. It was validated via: https://jigsaw.w3.org/css-validator/
![css-val](readme/images/testing/css-val.png)

Jshint:


I used the following JS validator to validate my project. It was validated via: https://jshint.com/
![jshint-val](readme/images/testing/jshint-val.png)

Python:


Within Gitpod I used the Code Institute template to create my project. Within this template there is a PEP8 validator. All errors were fixed for each and every file. Firstly the template constructed by Code Institute have add-ons which checks that the code remains at a pep8 standard. Hence no errors are in my code apart from 3 add-on issues. The errors are known and do not effect code in anyway so can be ignored.
![pep8-val](readme/images/testing/pep8-val.png)

## SEO Testing
Below are screenshots taken from the chrome dev tools lighthouse function to evaluate SEO of the website which includes all HTML sites.


SEO Home Desktop testing result:

![seo-home-desktop](readme/images/testing/seo-home-desktop.png)

SEO Home Desktop testing result:
![seo-home-mobile](readme/images/testing/seo-home-mobile.png)

SEO Review Detail Desktop testing result:
![seo-reviewdetail-desktop](readme/images/testing/seo-reviewdetail-desktop.png)

SEO Review Detail mobile testing result:
![seo-reviewdetail-mobile](readme/images/testing/seo-reviewdetail-mobile.png)

SEO add review desktop testing result:
![seo-addreview-desktop](readme/images/testing/seo-addreview-desktop.png)

SEO add review mobile testing result:
![seo-addreview-mobile](readme/images/testing/seo-addreview-mobile.png)

SEO watchlist desktop testing result:
![seo-watchlist-desktop](readme/images/testing/seo-watchlist-desktop.png)

SEO watchlist mobile testing result:
![seo-watchlist-mobile](readme/images/testing/seo-watchlist-mobile.png)
