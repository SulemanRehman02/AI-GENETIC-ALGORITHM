# AI-GENETIC-ALGORITHM
Genetic Algorithms
1. Genetic Algorithm is a search heuristic (experience) that follows the process of natural
evolution. This heuristic is used to generate useful solutions to optimization and search
problems.
2. Genetic algorithms are inspired by Darwin’s theory about evolution. The solution to a
problem solved by genetic algorithms is evolved.
3. Genetic Algorithm belongs to the larger class of evolutionary algorithm (EA) which
generate solutions to optimization problems and using techniques inspired by natural
evolution like – inheritance, mutation, selection, crossover.

4. Algorithm is started with a set of solutions (represented by chromosomes) called pop-
ulation. Solutions from one population are taken and used to form a new population.

This is motivated by a hope, that the new population will be better than the old one.
Solutions that are selected to form new solutions (offspring) are chosen according to
their fitness - the more suitable they are the more chances they have to reproduce.

5. This is repeated until some condition (for example number of populations or improve-
ment of the best solution) is satisfied.

The goal of this script is to guess a secret word of a fixed length, say 6 characters via a Genetic
algorithm. The population size is 50, and each individual in the population is a string of
6 randomly generated characters. The fitness of an individual is determined by how many
characters it shares with the secret word.
1. The initial population is created by generating random strings of characters.
2. In each generation, the fitness of each individual is calculated. Fitness is assigned based
on the number of correct letters in the correct place.
3. The selection function chooses two parents from the population based on their fitness.
4. The crossover function creates two children by swapping parts of the parents’ strings.
5. The mutation function randomly changes some characters in the children’s strings.
6. The new population is created by combining the parents and children and the best
individual from the previous generation is included in the new population.
7. The best individual in the current generation is printed, and the loop continues until a
solution is found (i.e., the secret word is guessed).
