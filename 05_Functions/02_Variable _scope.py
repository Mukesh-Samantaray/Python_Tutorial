"""
===========================================================
📘 COMPLETE PYTHON NOTES: VARIABLE SCOPE (LEGB RULE + Q&A)
===========================================================

🔶 What is Variable Scope?
---------------------------
Scope refers to the region of a program where a variable is recognized, accessible, and can be used. Variables in Python can have **local**, **enclosing**, **global**, or **built-in** scope.

🔶 LEGB Rule (Scope Resolution Order):
---------------------------------------
Python uses the LEGB rule to resolve the variable name:
- **L - Local:** Names assigned within a function.
- **E - Enclosing:** Names in the local scope of any enclosing functions.
- **G - Global:** Names assigned at the top-level of a module or script.
- **B - Built-in:** Predefined names in the Python language (e.g., `len`, `sum`).

🧠 Note: Python does not have block scope like C or JavaScript (e.g., in `if`, `for`, `while` blocks).

=======================================================================
🔁 TOP 20 INTERVIEW QUESTIONS ON VARIABLE SCOPE (WITH CODE & EXPLANATION)
=======================================================================

-----------------------------------
Q1. What is the output of basic LEGB?
-----------------------------------
"""

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Q1 Output:", x)
    inner()
outer()

"""
Output: local
Explanation: The innermost variable `x` in the local scope is used.
"""

# -------------------------------
# Q2. What if `inner()` doesn't redefine `x`?
# -------------------------------

x = "global"
def outer():
    x = "enclosing"
    def inner():
        print("Q2 Output:", x)
    inner()
outer()

"""
Output: enclosing
Explanation: Local `x` not defined in `inner()`, so Python uses enclosing scope.
"""

# -----------------------------------------------
# Q3. Accessing a global variable inside function
# -----------------------------------------------

name = "Alice"
def greet():
    print("Q3 Output:", name)
greet()

"""
Output: Alice
Explanation: Function can read global variable.
"""

# ------------------------------------------------------------------
# Q4. Modifying global variable inside function without `global`
# ------------------------------------------------------------------

counter = 10
def wrong_update():
    # counter += 1  ❌ Uncomment causes UnboundLocalError
    pass

"""
Output: UnboundLocalError (if uncommented)
Explanation: Python treats counter as local since it's being assigned to, but it's not defined locally.
"""

# ----------------------------------------------
# Q5. Correct way to modify global variable
# ----------------------------------------------

def correct_update():
    global counter
    counter += 1
    print("Q5 Output:", counter)
correct_update()

# ---------------------------------------------------------
# Q6. What is the scope of variables in list comprehensions?
# ---------------------------------------------------------

# In Python 3, list comprehension variable is scoped inside
lst = [i for i in range(5)]
# print(i)  ❌ NameError: 'i' is not defined (Python 3)

"""
Explanation: 'i' is scoped only within the list comprehension in Python 3.
"""

# ----------------------------------
# Q7. Variable shadowing example
# ----------------------------------

value = "outer"
def func():
    value = "inner"
    print("Q7 Output:", value)
func()
print("Q7 Global Output:", value)

"""
Output: inner, outer
Explanation: Local variable `value` shadows global `value` inside function.
"""

# ----------------------------
# Q8. Use of `nonlocal`
# ----------------------------

def outer_func():
    msg = "outer"
    def inner_func():
        nonlocal msg
        msg = "inner"
    inner_func()
    print("Q8 Output:", msg)
outer_func()

"""
Output: inner
Explanation: `nonlocal` allows modification of enclosing scope variable.
"""

# -------------------------------------
# Q9. Use `global` inside nested function
# -------------------------------------

count = 0
def outer():
    def inner():
        global count
        count = 5
    inner()
outer()
print("Q9 Output:", count)

"""
Output: 5
Explanation: `global` changes the global variable from inside inner().
"""

# ---------------------------
# Q10. Built-in scope example
# ---------------------------

print("Q10 Output:", len([1, 2, 3]))

"""
Output: 3
Explanation: `len` is a built-in function in Python.
"""

# ------------------------------------------------
# Q11. Can a global variable be accessed in nested functions?
# ------------------------------------------------

var = "global"
def outer():
    def inner():
        print("Q11 Output:", var)
    inner()
outer()

"""
Output: global
Explanation: Variable found in global scope as no local/enclosing definition exists.
"""

# --------------------------------------------------
# Q12. Modify outer function’s variable using `nonlocal`
# --------------------------------------------------

def outer():
    msg = "hi"
    def inner():
        nonlocal msg
        msg = "hello"
    inner()
    print("Q12 Output:", msg)
outer()

"""
Output: hello
Explanation: `nonlocal` allows changing `msg` from inner to affect outer scope.
"""

# ---------------------------------------------
# Q13. Do if/for blocks create a new scope?
# ---------------------------------------------

if True:
    temp = "inside if"
print("Q13 Output:", temp)

"""
Output: inside if
Explanation: Python does NOT have block-level scope (only function/class do).
"""

# ------------------------------------------
# Q14. Are function parameters local?
# ------------------------------------------

def test(name):
    print("Q14 Output:", name)

test("Python")

"""
Output: Python
Explanation: Parameters are local to the function.
"""

# ------------------------------------------------
# Q15. Does a function create a new variable scope?
# ------------------------------------------------

a = 5
def scope_check():
    a = 10
scope_check()
print("Q15 Output:", a)

"""
Output: 5
Explanation: Changes inside the function don’t affect the global variable.
"""

# -----------------------------------
# Q16. Accessing global via globals()
# -----------------------------------

a = 42
print("Q16 Output:", globals()['a'])

"""
Output: 42
Explanation: globals() gives dictionary of global names.
"""

# -------------------------------------------------------
# Q17. Can we have local and global variable with same name?
# -------------------------------------------------------

x = 100
def test():
    x = 200
    print("Q17 Output:", x)

test()
print("Q17 Global Output:", x)

"""
Output: 200 (local), 100 (global)
Explanation: Local and global scopes are separate.
"""

# -----------------------------------------------------
# Q18. Are default parameter values evaluated at call time?
# -----------------------------------------------------

value = 10
def show(val=value):
    print("Q18 Output:", val)
value = 20
show()

"""
Output: 10
Explanation: Default values are bound at function definition time, not call time.
"""

# ------------------------------------
# Q19. Lambda and enclosing scope
# ------------------------------------

def make_multiplier(factor):
    return lambda x: x * factor

times3 = make_multiplier(3)
print("Q19 Output:", times3(4))

"""
Output: 12
Explanation: Lambda function remembers `factor` via closure (enclosing scope).
"""

# -----------------------------------
# Q20. Using locals() inside function
# -----------------------------------

def local_vars(a, b):
    c = a + b
    print("Q20 Output:", locals())

local_vars(3, 4)

"""
Output: {'a': 3, 'b': 4, 'c': 7}
Explanation: locals() gives dictionary of current local variables.
"""

"""

🎯 Summary:
- Python uses the LEGB rule to resolve names.
- Use `global` to modify global variables inside a function.
- Use `nonlocal` to modify enclosing scope variables in nested functions.
- Python lacks block-level scope (e.g., if, for blocks don’t isolate variables).
- Default parameters are bound at **definition**, not at **call time**.

🔥 Tip: Practice these examples to solidify your understanding!

"""
"""
📘 NESTED FUNCTIONS & ENCLOSING SCOPE — BASIC EXPLANATION WITHOUT nonlocal/global
=============================================================================

- Nested functions are functions defined inside other functions.
- Inner functions can **read** variables from the outer (enclosing) function.
- Inner functions **cannot modify** variables from the outer function unless you use `nonlocal`.
- Without `nonlocal` or `global`, modifying outer variables inside inner functions is not possible.

Example 1: Accessing enclosing variable

def outer():
    message = "Hello from outer"
    
    def inner():
        print("Inner sees:", message)  # Reading enclosing variable
    
    inner()

outer()

# Output:
# Inner sees: Hello from outer

Example 2: Trying to modify enclosing variable without nonlocal (will cause error if uncommented)

def outer():
    count = 0
    
    def inner():
        # count += 1  # Uncommenting causes UnboundLocalError
        print("Count inside inner:", count)
    
    inner()

outer()

# Explanation:
# Without 'nonlocal', Python thinks 'count' inside inner() is a new local variable.
# Reading it before assignment causes error.
# So we can only read, not modify, enclosing variables without 'nonlocal'.

Summary:
- Nested functions can freely read enclosing variables.
- To modify enclosing variables requires 'nonlocal' keyword.
- If you don’t want to use 'nonlocal', just read enclosing variables or pass variables as parameters.

"""
