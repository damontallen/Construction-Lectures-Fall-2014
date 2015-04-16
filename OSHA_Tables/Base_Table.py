# scale: 60% does not work with HTML tables
table_HTML = """<code></code></br>
<strong></strong><code></code>
<table style="width: 100%; height: 60%; font-size:12px">
<thead>
    <tr>
        <th rowspan = 5 style="text-align: center"></th>
        <th colspan = 14 style="text-align: center"></th>
    </tr>
    <tr>
        <th colspan = 7 style="text-align: center"></th>
        <th colspan = 2 style="text-align: center"></th>
        <th colspan = 5 style="text-align: center"></th>
    </tr>
    <tr>
        <th rowspan = 3 style="text-align: center"></th>
        <th rowspan = 3 style="text-align: center"></th>
        <th colspan = 5 style="text-align: center"></th>
        <th rowspan = 3 style="text-align: center"></th>
        <th rowspan = 3 style="text-align: center"></th>
        <th colspan = 5 style="text-align: center"></th>
    </tr>
    <tr>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
        <th style="text-align: center"></th>
    </tr>
</thead>
<tbody>
    <tr>
        <th rowspan = 4></th>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    
    <tr>
        <th rowspan = 4></th>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    
    <tr>
        <th rowspan = 4></th>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
    <tr>
        <th></th>
        <th style="text-align: center"></th>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <th style="text-align: center"></th>
        <td><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
        <td style="text-align: center"><em></em></td>
    </tr>
</tbody>
<tfoot>
    <tr>
        <th style="text-align: center"></th>
        <td colspan = 14></td>
    </tr>
</tfoot>
</table>
<em><strong></strong> </em>
</br>
</br>"""

from IPython.display import HTML
from numpy import array


def shoring_table(Table_data):
    Base = table_HTML.split('\n')
    Base = ['']+Base

    td = Table_data
    soil_line = td[1][0].split(' ')
    soil_type = ' '.join(soil_line[0:3])
    Surcharge = ' '.join(soil_line[3:])
    top_line = '%s, %s'%(td[2][1],td[2][2])
    top_line=top_line.strip('"')
    Actions = [(1,('<code></code>','<code>%s</code>'%td[0][0])),
               (2,('<strong></strong>','<strong>%s:</strong>'%soil_type)),
               (2,('<code></code>','<code>%s</code>'%Surcharge)),
               (6,('><','>%s<'%td[2][0])),
               (7,('><','>%s<'%top_line)),
               (10,('><','>%s<'%td[3][1])),
               (11,('><','>%s<'%td[3][8])),
               (12,('><','>%s<'%td[3][10])),
               (15,('><','>%s<'%td[4][1])),
               (16,('><','>%s<'%td[4][2])),
               (17,('><','>%s<'%td[4][3])),
               (18,('><','>%s<'%td[4][8])),
               (19,('><','>%s<'%td[4][9])),
               (20,('><','>%s<'%td[4][10])),
               (23,('><','>%s<'%td[5][3])),
               (24,('><','>%s<'%td[5][4])),
               (25,('><','>%s<'%td[5][5])),
               (26,('><','>%s<'%td[5][6])),
               (27,('><','>%s<'%td[5][7])),
               (28,('><','>%s<'%td[5][10])),
               (29,('><','>%s<'%td[5][11])),
               (30,('><','>%s<'%td[5][12])),
               (31,('><','>%s<'%td[5][13])),
               (32,('><','>%s<'%td[5][14]))]
    for i in range(3):
        r = 66*i + 37
        R = 4*i + 7
        Actions.append((r,('><','>%s<'%td[R][0])))
        for j in range(4):
            for k in range(13):
                C = k+1
                rr = r + 1 + j*16 + k
                RR = R + j
                if  C in [1,2,8]:
    #                 print((rr,('><','>%s<'%td[RR][C])))
                    Actions.append((rr,('><','>%s<'%td[RR][C])))
                else:
                    Actions.append((rr,('<em></em>','<em>%s</em>'%td[RR][C])))
    Actions.append((236,('><','>%s<'%td[19][0])))  
    Actions.append((237,('><','>%s<'%td[19][1]))) 
    twenty = td[20][0].split('–')
    Actions.append((241,('i><strong','i>%s –<strong'%twenty[0]))) 
    Actions.append((241,('<strong></strong>','<strong>%s</strong>)'%twenty[1].strip(')')))) 
    Actions.append((242,('</br>','</br>%s'%td[21][0]))) 
    Actions.append((243,('</br>','</br>%s'%td[22][0]))) 

    for row, action in Actions:
        Base[row] = Base[row].replace(action[0],action[1])
    Table = '\n'.join(Base)

    return HTML(Table)
    
    
    
    
    
def load_table(File = "Oak_C-1_1.csv"):    
    path = "OSHA_Tables"
    name = path+'/'+File
    txt = []
    all_txt = []
    with open(name,'r') as f:
        for line in f:
            Line = line.strip('\n')
            all_txt.append(Line.split(','))
            txt.append(Line.strip(',,'))
    return array(all_txt)




















