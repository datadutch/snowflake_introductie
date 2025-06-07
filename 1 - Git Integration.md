we will now set up Github integration in Snowflake to be able to pull this repo into Snowflake

Why is this step 1 ? It is a good stick behind the door to work from Git and not scatter your Snowflake code all over the place.

Log in to Snowflake and execute this code:

USE ROLE ACCOUNTADMIN;
CREATE API INTEGRATION SI_GIT
    API_PROVIDER = GIT_HTTPS_API
    API_ALLOWED_PREFIXES = ('https://github.com/datadutch/snowflake_introductie')
    ENABLED = TRUE
    ALLOWED_AUTHENTICATION_SECRETS = ALL
    ;

CREATE GIT REPOSITORY SI_GIT 
    ORIGIN = 'https://github.com/datadutch/snowflake_introductie' 
    API_INTEGRATION = 'SI_GIT' ;

if you want to use another role to create the api integration, execute this command for the role:

USE ROLE ACCOUNTADMIN;
GRANT CREATE API INTEGRATION ON ACCOUNT TO ROLE <role_name>;