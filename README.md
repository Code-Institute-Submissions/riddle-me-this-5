# Pratical Python Milestone Project

## Riddle-Me-This (Brief)

A web application game that asks players to guess the answer to a pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
Create a leaderboard that ranks top scores for all users.

## Bootstrap template used

As the main focus of this project is Python and the use of the Flask Framework, it was felt that there was no need to start the HTML & CSS from scratch
and so instead appropriate template files were imported to Cloud9 using the 'wget' command.

Folders that were not necessary were then deleted.

The template used is called Freelancer and is downloadable from https://startbootstrap.com/template-overviews/freelancer/

## Image Credits

All 6 Continent Images used were designed by Vexels.  www.vexels.com

## Mockups / Wireframes

The following are the initial mockups of each page/section - the final prodcut may vary slightly depending on functionaility:

### Sample; Index Page (Section 1 - Masthead):

![index1](https://user-images.githubusercontent.com/28737216/46905476-4761de00-ceec-11e8-9697-a98ed4ba3694.PNG)

### Sample; Index Page (Section 2 - How To Play):

![index2](https://user-images.githubusercontent.com/28737216/46905489-6e201480-ceec-11e8-97c6-798edd54d395.PNG)

### Sample; Index Page (Section 3 - Quiz Selection):

![index3](https://user-images.githubusercontent.com/28737216/46905492-7710e600-ceec-11e8-990e-c86b83ab2834.PNG)

### Sample; Index Page (Section 4 - Contact Form):

![index4](https://user-images.githubusercontent.com/28737216/46905575-cc012c00-ceed-11e8-92ac-30050322ac49.PNG)

## UX

Users knowledge of world capital cities will be tested, with each section being scored out of 10 and a chance to claim their place on the relevant leaderboard.

Upon visiting the site, the user will first be presented with the opening page (index.html) with options to see "How To Play" or "Select a Quiz".  Selecting "How To Play", will bring them to the following instructions section:

![howtoplay](https://user-images.githubusercontent.com/28737216/46914999-7a17df00-cf9d-11e8-82c2-e63205a09aa4.PNG)
(provisional instructions - due to change as project development progresses)

Upon moving to the Quiz Selection area, they will be presented with the following options, per continent:

![quizselect](https://user-images.githubusercontent.com/28737216/46915030-d3800e00-cf9d-11e8-8deb-0a1c2231ab86.PNG)

The user then selects one the button for the quiz of their choice, and this will open the following modal which allows them to enter their Username:

![username](https://user-images.githubusercontent.com/28737216/46915087-6b7df780-cf9e-11e8-9e5e-6ce690a39362.PNG)

"Close" will simply close the modal and return them to the Quiz Selection, whereas "Start Quiz" will redircet them to the appropriate Quiz Page based on their original choice:

![quizpage](https://user-images.githubusercontent.com/28737216/46915116-b7c93780-cf9e-11e8-93dc-3c923e63e0d5.PNG)
(example of Africa Quiz Page - with Welcome note on the left, and questions on the right {for lager screens})

## Testing
