# One-Lined-Rock-Paper-Scissors
rock paper scissors on one line, inspired from a r/programmerhumor post

Features this code has:
- Can quit 
- Input validation
- Tells you what you won/lost/tied to

How it works:
- The whole code is a while loop. It continues to loop until you say "y" to quit.
- It will then proceed to print a giant lambda function, that self executes passing along two arguments.
- Lambda arguments are a random odd number from 1-5, and if the input is valid.
- The arguments use walrus operator to save space.
- Inside the lambda is ternary, and if the input is not valid it will output a error message.
- If input is valid, it will won/lost/tied with s/r/p.
- It knowns which move the computer played using modulo and math

![image](https://github.com/Evickerest/One-Lined-Rock-Paper-Scissors/assets/121898077/0da549ce-61ba-4265-be16-cd9abee17fe6)
