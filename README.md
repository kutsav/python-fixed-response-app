# ABOUT
The app by default returns 404 status code for any request. 
Health check for app is configured at /health at port 8000 which can be configured in Kubernetes

# ENVIRONMENT VARIABLES

Following environment variables can be used to set response code and response message from the app:

RESPONSE_CODE => The HTTP status code to return for every request. Default value is 404.

RESPONSE_TEXT => The response message to be sent

ENABLE_LOGGING => To enable stdout logs for incoming requests. Possible values are {true,false}

APP_PORT => Port on which app has to run. Default: 8000
