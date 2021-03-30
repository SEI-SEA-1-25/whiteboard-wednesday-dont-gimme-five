# Whiteboard Wednesdays - Don't Gimme Five

## Please Read!

Your mission is to solve a problem we'll describe below.

But your _real_ mission is to prepare to help someone else solve it.

## Help Someone Else Solve It?!

Tomorrow you'll be interviewing someone, helping them through the process of solving this problem. So as you solve this, think through your process. You'll be able to use that to, with the benefit of hindsight, guide your partner through that same process.

Also... that same person will interview you too!

## Things To Think About As You Do This

- As an interviewer, you'll have to think about how YOU solved the problem.
- Remember that you won't be solving the problem for them, but helping guide them there.
- Think about what helped get you unstuck on this problem. They may get stuck in the same places!
- This will be an amazing learning experience for YOU, as a teacher--you'll need to understand the problem enough to help someone though it.
- Don't forget that tomorrow you can give _them_ the advice below!

## When you're getting interviewed tomorrow

- Talk through the problem - it's about the process, not the solution
- Don't give up
- Ask about edge cases - 0 and negative numbers and empty strings and multiple words and all that!
- Solve the problem, don't build the app
  - Don't sweat syntax
  - Pseudocode
  - Invent helper functions if necessary... you don't need to actually _write_ those functions! Just imagine a function to, say, check if a string is in another string, use it, and if you ever code it FOR REAL you could always write it then.

## The Problem You'll Be Interviewing Someone On

Make a `solution.py` that solves the following problem: given two numbers, print out every number between them (including both numbers) that DOESN'T have a 5 in it. 5 has a 5 in it, but so does 15 and 50 and 20057. 10 does not! (This is NOT about multiples.)

You should _not_ try to solve this with math. (And thank _goodness_.)

Run the program frequently. There are a lot of potential pitfalls here!

## Basic Run-Through

- Ask the user running the program (using `input()`) for two numbers. They should come in with a space separating them, e.g. "5 8" or "14 23". You should assume they'll come in in ascending order.
- Ideally, you want to make two numbers out of that big string. `.split()` is your friend, and then you can convert the strings to numbers with `int` (we're not concerned with decimals here).
- Now you'll want to make a list of numbers from the low number to the high. (Again, _inclusive_.) Python has a built-in function for this!
- For each number in that range, print it out if it _doesn't_ contain a "5". You may want to consider converting each number to a string, because then you can check if one thing is `in` another. Hint hint!
