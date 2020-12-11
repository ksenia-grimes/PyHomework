def Template(template,values):
	return template.format(**values)

template = 'Hello, {username} {lastname},I\'m {username1} {lastname1}'
values = {'username':'Mary','lastname':'Smith','username1':'John','lastname1':'Lively'}
print(Template(template,values))
