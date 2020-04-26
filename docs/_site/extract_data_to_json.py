# extract data from index.md to _data/news.yml


file_input=open('index.md','r')
file_output=open('_data/news.yml','w')

file_input.readline()
file_input.readline()
file_input.readline()



for line in file_input:
    if line[0:2] == "##":
        file_output.write('\n- date: '+ line[3:]+'  items:\n')
        
        print('date: '+line)
    elif line[0:1] == "【":
        file_output.write('  group: '+line)
        print('group '+ line)
    elif line[0] == '*':
        file_output.write('  - '+line[2:])


file_input.close()
file_output.close()
