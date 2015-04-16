#!/usr/bin/make
PYTHON := /usr/bin/env python

lint:
	@flake8 --exclude hooks/charmhelpers actions hooks unit_tests tests
	@charm proof

unit_test:
	@echo Starting tests...
	@$(PYTHON) /usr/bin/nosetests --nologcapture unit_tests

bin/charm_helpers_sync.py:
	@mkdir -p bin
	@bzr cat lp:charm-helpers/tools/charm_helpers_sync/charm_helpers_sync.py \
        > bin/charm_helpers_sync.py

sync: bin/charm_helpers_sync.py
	@$(PYTHON) bin/charm_helpers_sync.py -c charm-helpers-hooks.yaml
	@$(PYTHON) bin/charm_helpers_sync.py -c charm-helpers-tests.yaml

test:
	@echo Starting Amulet tests...
	# coreycb note: The -v should only be temporary until Amulet sends
	# raise_status() messages to stderr:
	#   https://bugs.launchpad.net/amulet/+bug/1320357
	@juju test -v -p AMULET_HTTP_PROXY,AMULET_OS_VIP --timeout 900 \
        00-setup 14-basic-precise-icehouse 15-basic-trusty-icehouse \
        16-basic-trusty-icehouse-git 17-basic-trusty-juno \
        18-basic-trusty-juno-git

publish: lint unit_test
	bzr push lp:charms/neutron-openvswitch
	bzr push lp:charms/trusty/neutron-openvswitch
