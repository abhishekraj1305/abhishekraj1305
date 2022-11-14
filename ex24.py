print("let's practice everything.")
print('you\'d need to know \'about escapes with\\ that do:')
print('\n newlines and \t tabs.')

poem = """
\n the lovly world 
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intitution 
and requires an explanation
\n\t\twhere there is none.
\n\t\t i love you.
"""

print("------------")
print (poem)
print("------------")


fourteen = 10 + 5 - 2 +1
print(f" this should be {fourteen}")

def secret_formula(started):
    jelly_beans = started* 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars,crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)    

#remember that this is another way to format a string
print("with starting point of: {}".format(start_point))
# it's just like with an f"" string
print("we'd have {beans} beans,{jars} jars, and {crates} crates.")

start_point = start_point/10

print("we can also do this way")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("we'd have {}beans, {}jars, and {}crates.".format(*formula))

