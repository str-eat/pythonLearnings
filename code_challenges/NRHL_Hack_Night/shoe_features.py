shoe1 = 'shoe1.txt'
shoe2 = 'shoe2.txt'
shoe3 = 'shoe3.txt'
shoe_files = [shoe1, shoe2, shoe3]
material_types = ['suede', 'manmade']
synonyms = {'Synthetic' : 'manmade'}

def adjective_of(noun, f):
    with open(shoe) as f:
        for line in f:
            if noun in line:
                line = line.replace(',', '').replace('-', '').strip().lower().split(' ')
                for index, item in enumerate(line[:-1]):
                    if line[index + 1] == noun:
                        adjective = line[index]
                        return adjective

for shoe in shoe_files:
    with open(shoe) as f:
        output = {'Heel Style' : '', 'Toe Style' : '', 'Material' : '', 'Features' : ''}
        for line in f:
            if 'toe' in line:
                a = line.replace('-', '').strip()
                output['Toe Style'] = a
            if 'heel' in line and output['Heel Style'] is '':
                b = line.replace('-', '').strip()
                output['Heel Style'] = b
            if 'upper' in line:
                c = line.replace(',', '').split(' ')
                for index, item in enumerate(c[:-1]):
                    if 'upper' == c[index + 1]:
                        d = c[index]                        
                        if d not in material_types and d in synonyms.keys():
                            output['Material'] = synonyms[d]
                        elif d in material_types:
                            output['Material'] = d
                        else:
                            material = adjective_of(d.lower(), shoe)
                            output['Material'] = material
            if 'padd' in line:
                output['Features'] = 'Padding'
    print(output)


            
                


            

