# Consumer Affairs - "The Eye" Monitoring API Takehome
 
---------------
 
## Consumer Affairs - The Eye
The Eye is an API designed to receive requests containing user data for increased analytical data aggregation. Each request delivered via API is stored via Django ORM into a PostgreSQL database and is indexed and queryable both via direct API "get" route and a simplified UI intended for end user consumption.

---------------

## Motivation
The Eye is a service designed to add value to applications by storing and aggregating quickly searchable data for the purpose of analytics to evaluate trends in behavioral data.

---------------

## Screenshots

---------------

* **API POST Route via Postman**

![image](https://cdn.discordapp.com/attachments/493239986917998603/909881271432409098/unknown.png)

---------------

* **API GET Route via Postman**

![image](https://cdn.discordapp.com/attachments/493239986917998603/909881490022760528/unknown.png)

---------------

* **User Interface**

![image](https://cdn.discordapp.com/attachments/493239986917998603/909880762818514984/unknown.png)


* **Postman Error Output**

![image](https://cdn.discordapp.com/attachments/493239986917998603/909883110810857492/unknown.png)


---------------

## Tech/framework used

<b>Built with</b>
- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

---------------

## Features

POST route accepts incoming JSON and stores data to PostgreSQL DB
GET route retrieves specified data
UI allows end user to query stored data

---------------

## Installation

* git pull https://github.com/BaronXOfficial/TheEye-ConsumerAffairs
* CD into project directory
* docker-compose up --build

---------------

## API Reference

**Valid API Endpoints**
* POST /api/event {JSON}
    * Expected Fields:
        * session_id: str
        * category: str
        * name: str
        * timestamp: datetime
        * data: JSON
* GET /api/
    * ?ordering={field}
        * ex: ?ordering=timestamp
    * ?search={search_terms}
        * ex: ?search=form

---------------

## How to use?

Send valid JSON with above described Expected Fields via POST route on /api/event
Retrieve data via GET request queries on /api/
Access and query data via web interface available on the django application homepage, by default accessible via http://localhost:8000/




---------------

## Closing Thoughts

This was an interesting project to work on. Upon initial assessment of the challenge presented, I was worried about throughput for the API and ORM/PGSQL, I tested Celery and Redis for the purpose of queueing requests. With more time, I would have done load testing on the specific packages compared to running Django/PGSQL as a standalone to determine the overall cost/benefit of the implementation but for the purpose of submission functional and presumed to be effective in handling the expected load of an average ~100 requests/sec.

In addition, given more time, I'd have liked to have written up a series of tests for API routes given expected responses and inputs.

Further, with more time, I would have liked to have improved the web client for accessing the PGSQL DB. Namely, I would have liked to have implemented a more intuitive graphical interface, particularly implementing a calendar selection for start range and end range with intended function as follows:

* If provided a Start Date, but no End Date:
    * Return all dates after X
* If provided an End Date, but no Start Date:
    * Return all dates before Y
* If provided both Start and End Date:
    * Return all dates between X and Y

Finally, I'd like to thank you for your patience for this submission. I wish that circumstances during these difficult times were better but unfortunately I was pulled away by the hospitalization of a close relative to whom I was tending throughout. I did my best with the time I had available to me today having finally been able to work on the project.

Thank you for your time, and your consideration. Wishing you all the best!

Keep the Fire Alive Inside You.

- Anthony
