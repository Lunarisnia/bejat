<h1 align="center">
    <b>
        <img src="https://raw.githubusercontent.com/Lunarisnia/bejat/main/bejatLogo.png" height="200" /><br />
        Bejat Programming Language
    </b>
</h1>

<div align="center">
    Bejat is an open source programming language that makes it hard to build simple, unreliable, and absolutely not efficient software with style (if you understand indonesian at least).
</div>
<br />
<br />
<br />

# Table of Contents
- [How to Use](#how-to-use)
- [Documentation](#documentation)
  - [Data Types](#data-types)
  - [Variable](#variable)
    - [Creating a New Variable](#creating-a-new-variable)
    - [Reassigning a Variable](#reassigning-a-variable)
  - [Operator](#operator)
    - [Arithmathic Operators](#arithmathic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
  - [Function](#function)
    - [Calling a Function](#calling-a-function)
    - [Defining a Function](#defining-a-function)
  - [Flow Control](#flow-control)
    - [If](#if)
    - [Else If](#else-if)
    - [Else](#else)
- [How To Compile](#how-to-compile)


# How to Use
1. Download the latest interpreter from the release page
2. Create a text file with the name `test.bejat`
3. Add the following line to the file  
`panggilin bilang pake "Hello, World"
4. `./bejat test.bejat`


# Documentation
## Data Types
Bejat is a strongly typed language with no support for type casting because I don't know how to implement type casting.

- String: `tulisan`
- Boolean: `bulen`
- Integer: `nomor`
- Null: It doesn't exist, I am too lazy to implement it.

## Variable
### Creating a New Variable
``` 
"Hello" ini tulisan nya foo
^           ^           ^
Data        Data Type   Variable Name
```

### Reassigning a Variable
```
"World" ini gantinya foo
^                    ^
Data                 Variable Name
```

## Operator
### Arithmathic Operators
- Addition: `ditambah`
- Subtraction: `dikurang`
- Multiplication: `dikali`
- Division: `dibagi`
- Modulo: `sisa bagi`

### Comparison Operators
- Equal: `sama ama`
- Not Equal: `ga sama ama`
- Greater Than: `lebih dari`
- Greater Than or Equal to: `lebih ato sama ama`
- Less Than: `kurang dari`
- Less Than or Equal to: `kurang ato sama ama`

### Logical Operators
I honestly forgot to implement this so I am not gonna bother.

## Function
### Calling a Function
```
panggilin bilang pake "Hello, World"
^         ^           ^
Keyword   Func Name   Data
```

### Defining a Function
There is none... sorry, it's just that when I allow you guys to define your own function I have to deal with variable scope and oh my god what a complex problem to solve, or that I am just too dumb. Which is probably the latter but
you can technically make your own function. If you scour my badly written code
in this repository you can find how I parse my language and write your own standard library function directly.

## Flow Control
### If
```
kalo a sama ama 20 {
    panggilin bilang pake "TRUEEEEE"
}
```

### Else If
```
kalo a sama ama 20 {
    panggilin bilang pake "TRUEEEEE"
} kalo ga a lebih dari 9999 {
    panggilin bilang pake "elif"
}
```

### Else
```
kalo a sama ama 20 {
    panggilin bilang pake "TRUEEEEE"
} kalo ga a lebih dari 9999 {
    panggilin bilang pake "elif"
} ato ga {
    panggilin bilang pake "ELSE"
}
```

# How to Compile
Really? why would you want to compile this? No. Why would you want to download this in the first place? are you okay? Maybe you need to talk to a helpline? https://www.helpguide.org/find-help.htm

But it's actually quite simple  
1. Clone this repository
2. `pip install -r requirements.txt`
3. python3 ./main.py ./step_test.bejat

Python 3.12+

And also I reccomend doing everything inside a virtual environment.