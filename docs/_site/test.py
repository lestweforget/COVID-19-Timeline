import json



block={
    'date':'march 30',
    'groups':[
        {
            'group_name':'wuhan',
            'items':[
                'item1',
                'item2'
            ]
        }
        ]
}

whole=[
    block,
    block
    ]

#print(json.dumps(whole, indent=2))

import yaml

f=open('_data/news.yml')
data=yaml.full_load(f)
f.close()

file_output=open('_data/news.json','w')
json.dump(data,file_output)
file_output.close()


