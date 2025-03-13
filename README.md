# Monty-Hall-Problem


<h2>Description</h2>
This Python script simulates the Monty Hall Problem, a probability puzzle based on a game show scenario. The goal is to analyze the winning probability when a player follows the switching strategy after the host reveals a non-winning door. The script runs multiple simulations and calculates the empirical probability of winning when switching doors.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 


<h2>Environments Used </h2>

- <b>Windows 11</b> (21H2)

<h2>Program walk-through:</h2>

Game Setup (game(possible_out))

The game consists of three doors, behind which there are two goats and one car.
The prize arrangement is shuffled randomly.
The player randomly selects one door.
The host, who knows the prizes, opens a door that:
Is not the player’s choice
Does not have the car
The function returns:
my_choice (the player's initial choice)
host_choice (the door opened by the host)
car_choice (the door that contains the car)
Determining the Switching Option (new_choice(mine, host))

This function determines the remaining door if the player chooses to switch.
The only available option after removing mine and host is returned.
Simulating 20,000 Games (TOTAL_RUN = 20000)

The simulation runs 20,000 times to estimate the probability of winning when switching.

Each iteration follows these steps:

Play a game and obtain the choices.
Determine the remaining door if the player switches.
Count the number of times the switched door contains the car.
Finally, the winning probability for the switching strategy is computed as:

win_rate =
successful switch wins/
total runs

​

Expected Result:
According to probability theory, the switching strategy should lead to winning in 2/3 (≈66.67%) of the cases. The simulation confirms this by running a large number of trials.
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
