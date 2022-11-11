#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp mapquest_breakout_activity.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  mapquest_breakout_activity.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/myapp/mapquest_breakout_activity.py" >> tempdir/Dockerfile

cd tempdir

docker build -t webapp .
docker run -t -d -p 5050:5050 --name webrun webapp
docker ps -a
