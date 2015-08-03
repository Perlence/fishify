# fishify

Modify environment in fish shell with variables from script output.

## Installation

1.  Clone the repository:

    ```fish
    git clone https://github.com/Perlence/wikigenre.git
    ```

2.  Install the package:

    ```fish
    pip install .
    ```

## Usage

fishify is used to modify environment variables in fish shell from output of programs like `ssh-agent`.

It can acquire environment variable declarations from stdin:

    ```fish
    eval (godep env | fishify)
    ```

It can also execute a program with given args and watch environment changes:

    ```fish
    eval (fishify ssh-agent)
    ```
