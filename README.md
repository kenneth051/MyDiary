MyDiary
is a website that enables someone to record their daily activities,personal affairs as well as emotions that may occur from time to time. One registers, logs in and then he or she starts writing.

 The UI pages have been developed with HTML, CSS and Javascript
	
 The link to the UI pages is https://kenneth051.github.io/MyDiary/UI/index.html
	

 **FEATURES OF MYDIARY**
	
			-Creating an account

			-logging into the account

			-Entering content(Writitng)

			-Viewing all entries

			-Viewing a specific entry

			-Updating an entry


 **MY DIARY'S ENDPOINTS**
	
			METHOD             ACTIVITY                     ENDPOINT

			-GET             fetching all entries           /API/v1/entries

			-POST            Creating an entry              /API/v1/entries

			-GET             Fething a specific entry       /API/v1/entries/<int:entryid>

			-PUT             Updating a specific entry      /API/v1/entries/<int:entryid>




**GETTING STARTED WITH MY DIARY**

1- Clone the repository

-git clone https://github.com/kenneth051/MyDiary.git

2-Install the dependencies

-pip install -r requirements.txt

Run the application when you are in it's parent directory

3-python run.py

**Testing**

To run tests

#in root directory

-pytest

-pytest --cov


 The endpoints have been developed Using Python OOP based together with Flask framework implementing non persistent data using data structures for storage.
 
[![Build Status](https://travis-ci.org/kenneth051/MyDiary.svg?branch=develop)](https://travis-ci.org/kenneth051/MyDiary)

<a href="https://codeclimate.com/github/kenneth051/MyDiary/maintainability"><img src="https://api.codeclimate.com/v1/badges/9d29aad9c943fed7228d/maintainability" /></a>

<a href="https://codeclimate.com/github/kenneth051/MyDiary/test_coverage"><img src="https://api.codeclimate.com/v1/badges/9d29aad9c943fed7228d/test_coverage" /></a>

[![Coverage Status](https://coveralls.io/repos/github/kenneth051/MyDiary/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/MyDiary?branch=develop)
