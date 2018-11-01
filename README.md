# ArtLink
A new app for making it easy for artists and potential commissioners to find each other.

Project Milestone 1
Project Summary
	For my project entitled Art Link, I am creating an online system to help people who wish to commission artists to easily be able to search for different artists based on their specified needs. Artists who sign up can create an account that lists various details about their artistic capabilities, what they are willing or not willing to draw, what their commission prices are, whether they are currently accepting commissions, and links to any other online profiles where people can contact them or see examples of their work. Potential customers would be able to search for artists that fit their needs and see whether they are open to taking commissions. In the search results, artists that are taking commissions will be marked in green, while artists that are closed will be marked in red. Users can then click on artist in the search result and see example pieces of their art, full commission information, and their contact information. If a person particularly likes an artist, the user can subscribe to that artist to be notified by email when they are open to commissions again.
User Stories
As a person searching for artists to commission, I want to be able to search for artists that are currently open to commissions that draw the subject matter I want within my price range, so that I may more easily find the artist that suits my needs.
•	Acceptance Criteria
o	Intuitive search interface
o	Ability to search and filter by multiple criteria
•	Mis-User Story
o	As a person with malicious intent, I want to be able to inject malicious code into my search results so that I can wreak havoc on the server.
•	Mitigation
o	App code will be written to recognize and reject direct SQL injections.
As an artist, I want to have potential customers find me easily, find out my commission prices in a standardized format, see links to my other online presences, and be able to easily inform my followers whether I’m taking commissions right now, without them having to manually check my page.
•	Acceptance Criteria
o	Interface for adding tags for styles, subjects, etc that they are/aren’t willing to draw, prices for their commissions, and their other online accounts.
•	Mis-User Story
o	As a phony user, I want to impersonate an artist so that I can scam people.
•	Mitigation
o	Accounts can be flagged and reported as fraudulent and deleted if needed.


## Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run my awesome app simply,
```bash
docker-compose up
```
See in-app menus for help with using specific features.

# License
The MIT License (MIT)

Copyright (c) Matthew L. Hale 2017

insert MIT License text here
--username admin --email admin