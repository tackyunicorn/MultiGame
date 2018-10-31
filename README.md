# MultiGame
Multiple CLI games with email notifications [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/tackyunicorn/MultiGame/issues)

## Description
Multi Game is a gaming package containing 3 universal, evergreen games aimed at pleasing
children of all ages and those who are young at heart. It gives the player a choice of playing  
  * Tic Tac Toe
  * Rock Paper Scissors
  * Guessing the Number

The scores are saved into a binary
file. If a player beats the scores of other players, emails are sent to the lower scorers, notifying
them of the win.

## Setup
* Ensure that you edit the senders address and password to your mail server's address and password 
  under the Mail(ID) function
  ```python
  sender = "yourmailserver@gmail.com"
  ```
  ```python
  m['From'] = "yourmailserver@gmail.com"
  ```
  ```python
  session.login(sender,'mailserverpassword')
  ```
* [Allow access to less secure apps in the gmail account of the mail server](https://myaccount.google.com/intro/security) 

> **Note**  
  The current implementation works only with gmail accounts for both the sender and the receiver and must only be done this way.
