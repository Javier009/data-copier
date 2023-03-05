docker run -it --name data-copier --rm --network data-copier-nw -v /Users/delgadonoriega/Desktop/Research/data/retail_db_json:/retail_db_json -e BASE_DIR=/retail_db_json -e DB_HOST=bdae4a707d7b -e DB_PORT=5432 -e DB_NAME=retail_db -e DB_USER=retail_user -e DB_PASS=itversity data-copier bash

#To create the container, connect to network and image and run the app directly. THIS IS FASCINATING OMG
docker run -it --name data-copier --rm --network data-copier-nw -v /Users/delgadonoriega/Desktop/Research/data/retail_db_json:/retail_db_json -e BASE_DIR=/retail_db_json -e DB_HOST=bdae4a707d7b -e DB_PORT=5432 -e DB_NAME=retail_db -e DB_USER=retail_user -e DB_PASS=itversity data-copier python /data-copier/app/app.py

docker run \
      -it \ --
      name data-copier \
      --rm \
      --network data-copier-nw \
      -v \
      /Users/delgadonoriega/Desktop/Research/data/retail_db_json:/retail_db_json \
       -e BASE_DIR=/retail_db_json \
       -e DB_HOST=bdae4a707d7b \
       -e DB_PORT=5432 \
       -e DB_NAME=retail_db \
       -e DB_USER=retail_user \
       -e DB_PASS=itversity \
       data-copier bash
