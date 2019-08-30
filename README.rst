=============
Todo List API
=============

Simple API project for demo purposes. Needs testing.

Local Install
=============

1. Copy the ``.env.sample`` to ``.env``.

  .. code-block:: bash
  
     cd <repo-path>/api
     cp .env.sample .env
     # No need to edit .env contents for local development.

2. Create the Virtual Env.

  .. code-block:: bash
  
     cd <repo-path>/
     python3 -m venv .venv

3. Activate the Virtual Env.

  .. code-block:: bash
  
     cd <repo-path>/
     . .venv/bin/activate

4. Update PIP and install the requirements.

  .. code-block:: bash
  
     cd <repo-path>/
     python -m pip install -U pip
     pip install -r requirements.txt

5. Set the Django settings module to be used.

  .. code-block:: bash
  
     cd <repo-path>/
     export DJANGO_SETTINGS_MODULE=core.settings


6. Run the Django Migrations.

  .. code-block:: bash
  
     cd <repo-path>/api
     python manage.py migrate


7. Create your Django Superuser.

  .. code-block:: bash
  
     cd <repo-path>/api
     python manage.py createsuperuser
     # As language, you may input 'pt-BR'
     # As timezone, you may input 'America/Sao_Paulo'

Important
---------

Your local development environment has been set up. From now on, before
running the server or doing anything else, always remember to activate
the env:

.. code-block:: bash
  
   cd <repo-path>/
   . .venv/bin/activate
   export DJANGO_SETTINGS_MODULE=core.settings
   # Good to go now.

Run The Dev Server
==================

.. code-block:: bash

   cd <repo-path>/api
   python manage.py runserver 0.0.0.0:8000

Access The Django Admin
=======================

Open the `the admin URL <http://localhost:8000/admin/>`_ in your browser and 
log in with your superuser credentials.

Access The API Docs
===================

Log in to the Django Admin and then open
`the docs URL <http://localhost:8000/docs/>`_ in your browser.

Access The Browsable API
========================

Log in to the Django Admin and then open
`the browsable API <http://localhost:8000/>`_ in your browser.

More
====

Imports Sorting and Code Linting
--------------------------------

.. code-block:: bash

   cd <repo-path>/
   fab lint

Tests
-----

Coverage report on terminal:

.. code-block:: bash

   cd <repo-path>/
   fab test

Coverage HTML report on ``reports/coverage``:

.. code-block:: bash

   cd <repo-path>/
   fab test:html
