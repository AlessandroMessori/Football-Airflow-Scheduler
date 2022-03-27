# Football-Airflow Scheduler


# Introduction

Scheduler made with Airflow that coordinates a simple football news data analysis pipeline.
The Pipeline runs once a day and scrapes data from italian or english football news websites and performs a simple word count in order to discover the trending topics.

## Architecture

The airflow scheduler and the analytics code are hosted and run on an AWS EC2 instance, while the data is stored on an AWS S3.

All of the cloud architecture was managed within the free tier of an AWS Educate account.

## Pipeline

The pipeline is composed of 5 sequential steps:

-  Crawl the football data from news websites using   Scrapy 

- Upload the raw data to an AWS S3 bucket

- Perform the word count on the data with a Pandas script

- Upload the word count results to another AWS S3 Bucket

- Import the counted topics on a mongoDB database that could be possibly connected to a visualization tool in the future 