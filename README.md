## Welcome to my newest..yet not even started..project

__What is it?__
> This is going to be a new scripting language. Basically a "Lazy written form of Shell Script". It is going to be a .s file.
How will you be able to format it? well..as I am not all that advanced(not as good of a Python developer as most) I am making a
hard-coded way to format the code and make it runable.
## ##
<br>


__What and how I plan on hard-coding a python script to format AND run the .s file__
<br>
> As hard of a question that is, the answer is harder. What I plan on happening is actually creating some backend python sections
that define certain variables/items that should be within the file. Then I plan on making another file that builds what a function
and class should look like. Yeah yeah you should get it by now..I am going to hard code how to assign variables, functions, basically just how to write the file.

<br>

> __But how do I make it to where the GitHub user can compile it?__ <br>Well that is going to be another python file(of course) that includes the other files on how to build/code the language. And write some basic Python syntax code that checks if certain data(lines of code) is in the file, then re-format it to shell script so you don't have to waste your time writing Shell Script and can write lazily with the .s file!

<br>

> Yes, in order to format, or be able to run/compile the .s file, you have to have my repository cloned(unames right now), and when you want to run your application you have to write a file(a .sh __Sorry, but there is no other way to actually do this unless you want to go another 4 minutes of typing inside your terminal. I do understand it kinda takes the point away but trust me, it is, what, 4-5 lines of code that is what you do daily if you use your terminal. So don't whine__) that cd(s) into my directory, then you have to type in the file name(unamed right now) that acitvates/reads the .s file, then you got to exit that shell script file.<br>__Yes I know, I am getting ahead of myself and how exactly this is going to work, and IDEK if it will work, but trust me, I don't give up so I will give this project my all__


### What I plan on having in the .s file

__If statement__<br>
```Iffi [ $var_name_here == '' ] = echo "Action Should Happend Here. Doesn't have to be a echo!"```

__Hopefully will be formatted into__
```shell
if [ $var_name_here == '' ];then
  echo "Action Should Happend Here. Doesn't have to be a echo!"
```
__If-Else__<br>
```Ifelfi [ $var_name_here == '' ] = echo "If it evaluates truthy this will print" _ echo "ELSE it won't"```

__Hopefully will be formatted into__
```shell
if [ $var_name_here == '' ]; then
  echo "If iecho "If it evaluates truthy this will print"
else
  echo "ELSE it won't"
fi
```
  
__Comment__<br>
``` #This is a comment ```

__Shoud hopefully be formatted to__
```shell
# COMMENT
```

### Now. There are gonna be some stuff that will stay the same.
__Getting into a directory(same as shell so i'm just gonna format a shell version)__<br>
```shell
cd DIRECTORY_NAME
```
__Will be__<br>
``` cd DIRECTORY_NAME ```

__ls__<br>
```shell
ls
```

__Will be__<br>
``` ls ```

### Now. With the assignments/classes/functions/strongly_typed functions/classes or weakly types functions/classes

*Note: This will just help write the script and will also help format it into shell script. This is just a better way to not change the value of the variable assigned*

__declare if you want the function/class to be weakly typed__<br>
``` # To declare a weakly typed @@./WEAK ```<br>
``` # To declare a strongly typed @@./STRONG ```<br>
*Weakly typed means you can assign a variable name any data type then reassign it.*<br>
*Strongly typed means you declare the type of data(int,char,string,float,double)and it stays that way, unable to change the data type*
