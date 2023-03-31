 #!/bin/sh

port="${APP_PORT:=8000}"

if [[ ${ENABLE_LOGGING} == "true" ]];
then
	gunicorn --bind 0.0.0.0:${port} -w 4 --reload --log-level info --access-logfile - 'app:app'
else
	gunicorn --bind 0.0.0.0:${port} -w 4 --reload --log-level info 'app:app'
fi
