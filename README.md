# Short writeup
This is user input based web application, based on the rational decision-making model. I found this model from my the other course, MGMT S-5800 Judgment and Decision Making. I found it is very useful for make an important decision, yet there is no tool for using this model in easy way, so I decided to make it.

# What's contained in each file

## /qyulzung
### views.py
I put comments on every def in views.py file.

### forms.py
For Login/Logout and Signup, reference from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

### models.py
There is only two models for this application:
1. QZ: The main model of this application. Take a topic to decide as a title, user, alternatives and criteria, each of the scores, and self Comment.
2. Topic: It is model to suggest a topic to a user. It will added as data getting accumulated.

## /templates
about.html: Introduce the course and Textbook.
base.html: base model of the other html, includes <header>, signin/logout button, menu bar(JavaScript, source from w3schools) and modal button(source from w3schools) for instruction.
board.html: The list of posted decisions. If it's current user's decision, user can unpost it.
contact.html: My contact.
error.html/successful.html: Html files for error/successful message.
index.html: Main page after user logged in, and it is step0.
journal.html: List current user's previous decision history.
journals.html: Render selected previous decision.
login.html/signup.html: reference from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
result.html: The last step of worksheet. Shows the result and let user input self-comment.
step1.html: Get input(alternatives) from user.
step2.html: Get input(criteria) from user.
step3.html: Get input(score of each criterion) from user.
step4.html: Render topic, alternatives, criteria that the database has, and get scores for each alternative from user.

## /static
style.css
background.jpg
mgmts5800.jpg
myself.png
qyulzung.png: Main logo
tetbookcover.png

# additional information
As I defined a good/better outcome before, it works and user can save a decision log. Moreover, user can post it into the Board and share it with others. The decision log can be deleted permanently or just deleted from the Board.
I have shown to my classmates and they gave me excellent feedbacks. The best feedback which is I want to build up on my application (in the future) is Categorizing and Search function. It will let user can search by his/her own interest keyword. I think I can make it by using such as SQLAlchemy what we've used for our project1, but I have no time for that.
I like my application and I will keep trying to develop it more in the future so that it can be used for many people.