#!/usr/bin/env zsh

#install requirements
pip install -r requirements.txt

#create an alias so you can run directly from terminal
create_alias="alias weather=\"sh $PWD/weather.sh\""
echo $create_alias >> ~/.zshrc

#change permission
chmod a+x install.sh
