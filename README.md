# Newton-Raphson Method for Transcendental Equations 

The Newton-Raphson method is a way of estimating roots to transcendental(or non-algebraic) equations in the form f(x) = 0. The general algorithm is:

1. Choose an initial guess $x_0$
2. For each $n = 1, 2, 3...$

$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$
1. Stop when after convergence at $|f(x_{n+1})| < \epsilon$, where $\epsilon$ is some small tolerance value. 

The implemented example is for the equation $x^x = 25$, where we set $f(x) = x^x - 25 = 0$. The derivative $f'(x)$ is numerically calculated using the symmetric difference quotient $\frac{f(x+h)-f(x-h)}{2h}$ where $h = 10^{-6}$.

