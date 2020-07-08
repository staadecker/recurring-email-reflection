# Recurring email reminders for goal setting and reflection

This repository contains a script that sends me a monthly prompt to reflect on my goals.

## System architecture

I use Google Cloud Platform (GCP) for this project. 
This script is hosted on GCP's Cloud Functions and is triggered by the GCP's Cloud Scheduler through a Pub/Sub topic.

The script makes use of SendGrid and their dynamic email templates to send the email.

## Screenshots

I receive this email on the first of every month!

![Screenshot of monthly reminder email](/docs/example-email.PNG)
