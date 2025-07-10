#!/bin/bash
sudo apt update
sudo apt install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
echo "Deploying web UI..."
cat <<EOF > /var/www/html/index.html
<!-- Replace this with the contents from web/index.html -->
EOF

