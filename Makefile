init:
	pip3 install -r requirements.txt
	scripts/QT_DEVICE
	scripts/gecko_install

test:
	nosetests tests