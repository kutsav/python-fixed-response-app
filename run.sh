 #!/bin/sh

if [ ${ENABLE_LOGGING} == "true" ];
then
	gunicorn --bind 0.0.0.0:8000 -w 4 --reload --log-level info --access-logfile - 'app:app'
else
	gunicorn --bind 0.0.0.0:8000 -w 4 --reload --log-level info 'app:app'
fi
