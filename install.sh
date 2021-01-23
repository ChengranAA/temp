#!/usr/bin/env zsh

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
#install requirements
pip install -r requirements.txt

#create an alias so you can run directly from terminal

create_alias="alias weather=\"sh $script_dir/weather.sh\""
echo $create_alias >> ~/.zshrc

#change permission
chmod a+x weather.sh
