<!-- docker exec -it postgres-container bash -->

psql -U postgres -f user_creation.sql
psql postgres -U polygondev -f database_creation.sql --password
When prompted: polygondev

<!-- Then in vadimap-platform/
source env/bin/activate

sh development_tools/scripts/initialize_django.sh -->
