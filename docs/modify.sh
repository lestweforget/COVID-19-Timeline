# This is the main file. It is called by github action automatically
# You can run this by ./modify.sh

# replace | 
#sed  's/|/\\|/g' ../时间线TIMELINE.md > index.md
sed  's/|/·/g' ../时间线TIMELINE.md > index.md

# extract data and save some formated file like reversed.md. no package needed so far
#pip3 install -r requirement.txt
python3 extract_data_to_yaml.py

# add the two buttons "go to top " and "go to bottom"
echo "<br><a name=\"bottom\">[回到顶部](#top) </a>" >> index.md


# add about page from readme
cp ../README.md about.md
