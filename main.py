import math
import matplotlib.pyplot as plt

def newton_raphson(x0, f, df, epsilon = 1e-6):
	fx_list = []
	x = x0
	cur_err = abs(f(x))
	iters = 0
	while abs(cur_err) > epsilon:
		fx_list.append(f(x))

		x_n1 = x - (f(x) / df(x))
		cur_err = abs(f(x_n1))
		x = x_n1
		iters += 1
	
	return x, iters, fx_list

def graph_nr_prog(fx_list):
    iter_list = list(range(1, iters + 1))
    plt.plot(iter_list, fx_list, marker="o", linestyle="-")
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.xlabel("Iteration")
    plt.ylabel("f(x)")
    plt.title("Iteration number vs f(x)")
    plt.grid(True)
    plt.show()

def graph_equation(f, xmin=0, xmax=10, step=0.01, vline=None):
	x_list = [xmin + i * step for i in range(int((xmax - xmin) / step) + 1)]    
	fx_list = [f(i) for i in x_list]

	plt.plot(x_list, fx_list, linestyle="-")
	plt.axhline(0, color="gray", linewidth=0.8)
		
	if vline:
		plt.axvline(x=vline, color="red", linestyle="--", linewidth=1)
    
	plt.autoscale(enable=True, axis='both', tight=False)
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.title("x vs. f(x)")
	plt.grid(True)
	plt.show()

# transcendental equation in the form f(x) = 0
def f(x):
    return math.pow(x, x) - 25


# calculates df/dx using symmetric difference quotient
def df_calc(f, h=1e-6):
    def df(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    return df

df = df_calc(f)

root, iters, fx_list = newton_raphson(2.5, f, df)
print(f"Root = {root:.6f} in {iters} iterations")

graph_equation(f, xmin=2.5, xmax=3.5, step=0.001, vline=root)
graph_nr_prog(fx_list)
