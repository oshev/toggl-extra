# toggl-extra

[![Build Status](https://travis-ci.com/oshev/toggl-extra.svg?branch=master)](https://travis-ci.com/oshev/toggl-extra)

Toggl Extra is a command-line and interactive shell for advanced Toggl users.

It is built on top of [Python-Nubia](https://github.com/facebookincubator/python-nubia) which is a great 
command-line and interactive shell framework.   

### Why?
 
As a Toggl power user, who tracks all useful time, not only work tasks, I find that [Toggl](http://toggl.com/) UI lacks 
some necessary functionality I need.

I wrote bits of Python code for several mini-projects which work via Toggl API. 
This repository is an intent to organise those bits for easier usage and extend its functionality further.      

## Requirements

Currently, only Python 3.6 is supported. 

Python 3.7+ do not work because of [issues in Python-Nubia](https://github.com/facebookincubator/python-nubia/issues/2)).

This repository uses `Pipenv` instead of `pip` and `venv`. 

If you're curious and are not familiar with this tool, see a great guide to `Pipenv` [here](https://realpython.com/pipenv-guide/).

You don't need to, though. To use `Toggl-extra` just run `pip3 install pipenv` and follow instructions below.

## Running Toggl-Extra

Checkout the repository.

Copy `configs/toggl-extra.yaml.sample` to `configs/toggl-extra.yaml` and substitute all words in capitals with your Toggl credentials. 

Run once:

```
pipenv shell  --python 3.6
pipenv install --ignore-pipfile # to use guaranteed working environment from Pipfile.lock
```

To use the tool from the project folder, just run: 

`./toggl_extra/toggl_extra_cli.py`

This will bring you to an interactive [Python-Nubia](https://github.com/facebookincubator/python-nubia) shell 
where you can run different commands.

You can also run the same commands just using Toggl-Extra as a command line tool:

`./toggl_extra/toggl_extra_cli.py [COMMAND] {PARAMETER1} {PARAMETER2}...` 

### Stuff you can do with Toggl-Extra

Use this commands in the interactive shell or as command-line parameters.

#### Dump Toggl entries to JSON files

Example: 

`dump_entries period-type-name="week" period-num=51 year=2018`

Allowed period types: `year`, `quarter`, `week`.  

### TODO Next
- Breaking a query for dumps for long periods into a series of smaller queries (otherwise, Toggl complains).
- Unit tests for all public methods.
- Scripts for linting and fix all linting issues.
- Serialising Toggl data as a Pandas DataFrame, which should be used to speed up / simplify further analysis.
- Saving Toggl data to iCal (which can be imported via Google Calendar UI). 
- Stats using advanced filtering and pre-saved configuration:
    - Several tags connected by OR or AND (Toggl UI only supports stats by OR in tags).
    - Regex for title entry (Toggl supports only "in" inside title filter).
- Graphs for stats based on advanced filtering.
- Commands for listing last entries.
- Commands for adding new entries.

