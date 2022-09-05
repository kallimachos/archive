=============
Specification
=============

An application for recording a collection of miniature figures, books, and
games from different systems and companies. Local clients sync with the remote
server through a web-based REST API.

Language
--------
- Python 3.4


Testing, logging, and configuration
-----------------------------------

- tox
- pytest
- pytest-cov - add badge to README based on tests
- flake8
- logging
- configparser


Version control and CI
----------------------

- GitHub
- Travis


Documentation
-------------

- RST
- Sphinx autodoc


Hosting
-------

- Rackspace public cloud
- OpenShift


Model
-----

- model.py
- collection.sqlite


View
----

- cli.py - argparse
- gui.py - tkinter
- web - HTML, CSS, mobile-friendly, bottle templates
- Android


Controller
----------

- controller.py
- REST API (bottle)
- routes for web view

tables
~~~~~~
- game (aka board games)

  - Name
  - Company
  - Number of players
  - Time to play in minutes
  - Age range
  - Link (to webpage, boardgamegeek, vel sim.)
  - Image
  - Notes
  - methods: add, edit, delete

- mini

  - Name
  - Army
  - Unit type (e.g. hero, core, etc.)
  - System
  - Company
  - Quantity
  - Status (painted, unpainted, sprue, bitz, NIB)
  - Link (to webpage, GW, vel sim.)
  - Image
  - Notes
  - Image of model
  - methods: add, edit, delete

- paint

  - Name
  - Colour (= primary colour, so one could, e.g., look at all shades of blue)
  - Type (metallic, wash, ink, matte)
  - Company
  - Notes
  - methods: add, edit, delete


Features
--------
- Load/Download DB
- Sync local DB with remote
- Add/edit list of companies, systems, armies, unit types, etc.
- Upload images
- Search
- Reports
- Save DB/reports as spreadsheets
- Print
- Authentication


To Do
-----
- CLI features

  - Add
  - Edit
  - Delete
  - Search
  - Reports

- Controller features

  - Add
  - Edit
  - Delete
  - Search
  - Reports

- GUI features

  - Add
  - Edit
  - Delete
  - Search
  - Reports

- Web features

  - Add
  - Edit
  - Delete
  - Search
  - Reports

- Add image upload capabilities
