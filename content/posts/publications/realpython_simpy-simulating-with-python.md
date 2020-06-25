Title: SimPy: Simulating Real-World Processes With Python | Real Python
Date: 2020-03-25
Modified: 2020-03-11
Lang: en
Category: Publications
Slug: publications/realpython-simpy-simulating-with-python
Cover: images/posts/publications/realpython-simpy-simulating-with-python.jpg
Tags: python, simpy
Summary: In this step-by-step tutorial, you'll see how you can use the SimPy package to model real-world processes with a high potential for congestion. You'll create an algorithm to approximate a complex system, and then you'll design and run a simulation of that system in Python.

The real world is full of systems, like airports and highways, that frequently experience congestion and delay. When these systems are not optimized, their inefficiency can lead to countless unhappy customers and hours of wasted time. In this tutorial, you’ll learn how to use Python’s simpy framework to create virtual simulations that will help you solve problems like these.

In this tutorial, you’ll learn how to:

* **Use** a simulation to model a real-world process
* **Create** a step-by-step algorithm to approximate a complex system
* **Design** and run a real-world simulation in Python with simpy

In this tutorial, you’ll create a simulation for a local movie theater. Your goal is to provide the manager with a script to help find the optimal number of employees to have on staff.

**Read it on [Real Python](https://realpython.com/simpy-simulating-with-python/)**

Here's the source code for this script:

```python
"""Companion code to https://realpython.com/simulation-with-simpy/
'Simulating Real-World Processes With SimPy'
Python version: 3.7.3
SimPy version: 3.0.11
"""

import simpy
import random
import statistics

wait_times = []


class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3 / 60)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1, 5))


def go_to_movies(env, moviegoer, theater):
    # Moviegoer arrives at the theater
    arrival_time = env.now

    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(moviegoer))

    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    if random.choice([True, False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # Moviegoer heads into the theater
    wait_times.append(env.now - arrival_time)


def run_theater(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    while True:
        yield env.timeout(0.20)  # Wait a bit before generating a new person

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))


def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. Simulation will use default values:",
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params


def main():
    # Setup
    random.seed(42)
    num_cashiers, num_servers, num_ushers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=90)

    # View the results
    mins, secs = get_average_wait_time(wait_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )


if __name__ == "__main__":
    main()
```
