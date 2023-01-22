# Crossmint challenge


The project is easily structured in several namespaces in the `megaverse` module which provide functionality for solving the challenge in the main script.

Here's a short description of each namespace functionality and intent.


| Namespace         | Description |
|-------------------|-------------|
| io                | Contains definitions for interacting with APIs. |
| logic             | Contains definitions for handling API entities. |
| entities          | Contains definitions of API entities. |


Regarding the main script, it only contains two functions, `solve_phase_1`, and `solve_phase_2`.

## Tests

I included some `logic` tests, in order to run them, you must install `pytest` and then run:

`python3 -m pytest` 

