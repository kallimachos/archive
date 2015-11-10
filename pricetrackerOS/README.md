pricetrackerOS
==============

A version of pricetracker designed to run on OpenShift using the Bottle framework.


Running on OpenShift
----------------------------

Create a python application based on the code in this repository:

    rhc app create pricetracker python-2.6 --from-code https://github.com/kallimachos/pricetrackerOS.git
