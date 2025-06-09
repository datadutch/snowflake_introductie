We will first set up Github integration in Snowflake to be able to pull this repo into Snowflake.

Why is this step? It is a good stick behind the door to work from Git and not scatter your Snowflake code all over the place.

Log in to Snowflake and execute this code, it will also set up some of the basic stuff required to get a headstart:

USE ROLE SECURITYADMIN;
CREATE ROLE DEV;
GRANT USAGE ON ROLE DEV TO <your_username>;
GRANT CREATE API INTEGRATION ON ACCOUNT TO ROLE DEV;

USE ROLE DEV;

CREATE API INTEGRATION SI_GIT
    API_PROVIDER = GIT_HTTPS_API
    API_ALLOWED_PREFIXES = ('https://github.com/datadutch/snowflake_introductie')
    ENABLED = TRUE
    ALLOWED_AUTHENTICATION_SECRETS = ALL
    ;

CREATE GIT REPOSITORY SI_GIT 
    ORIGIN = 'https://github.com/datadutch/snowflake_introductie' 
    API_INTEGRATION = 'SI_GIT' ;