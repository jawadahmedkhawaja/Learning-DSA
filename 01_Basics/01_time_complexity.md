# Time Complexity
---
        Time complexity is the measure of time required to
        run an algorithm as the size of input grows. It is
        not an actual clock time, rather it is measured in
        Asymptotic Notation.

# Asymtotic Notation
---
        It is a notation used to represent time complexity.
        In real world scenerios only one type of this notation is used i.e. Big-O. Because it tells how worse an algorithm can go.

## Example:

Let's take an example of python code:

```python
for i in range(1,6):
    print("Hello World")
```

### Explanation

In above code there is a loop which is running from 1-5 means it will run for 5 times, butt to measure time complexity for it we will keep in mind each operation the given code performs. For instance in given code for each iteration there are 3 operations are happening:

- It is checking for condition `i < 6`
- It is printing `Hello World`
- It is incrementing the `i` in each iteration

So technically, there are `3` operations are happening in each iteration and the loop will run `5` times so `3 x 5 = 15`. So it's time complexity is `O(1)`.

---


Thanks for reaching till the end ❤️
