emp = {"eno": "E1002", "ename": "杜甫", "sex": "男", "nation": "汉族"}
html = '''
<table border="1" width="55%">
     <tr>
       <td>员工编号</td>
       <td>{eno}</td>
     </tr>
     <tr>
       <td>姓名</td>
       <td>{ename}</td>
     </tr>
     <tr>
       <td>性别</td>
       <td>{sex}</td>
     </tr>
   </table>
'''.format_map(emp)
print(html)
