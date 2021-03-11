# Rover_bot


## Instructions

### Create venv environment

```
poetry shell
```

### Install dependencies
```
poetry install
```

### Running tests

```
poetry run tests
```

### Running complex instructions

change the INPUT var to put your commands considering the follow rules:

first line it is definition of field separated by spaces;
aftar that, repeat commands by lines following the rule:
  one line which contains start rover position with: x, y, direction (N, S, E, W) separated by spaces;
  one line which contains the moves which It is can be: L, R and M Left, Right and Move as order;

for example:
```5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```
to run complex instructions type the command bellow:

```
poetry run complex_moves
```
