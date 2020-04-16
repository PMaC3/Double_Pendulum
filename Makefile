vp: requirements.txt
	-virtualenv -p python3.7 vp
	vp/bin/pip3 install -r requirements.txt
	. vp/bin/activate && cd ../t15lib && T15AUTOBUILDS=. python3 ../t15lib/setup.py install
	touch vp
	@echo "type 'source vp/bin/activate' to activate virtualpython"

vp-test: requirements.txt requirements-test.txt
	-virtualenv -p python3.7 vp-test
	vp-test/bin/pip3 install -r requirements.txt
	vp-test/bin/pip3 install -r requirements-test.txt
	. vp-test/bin/activate && cd ../t15lib && T15AUTOBUILDS=. python3 ../t15lib/setup.py install
	touch vp-test

ipython: vp
	vp/bin/pip3 install ipython
	PYTHONPATH=src vp/bin/ipython

lint: vp-test
	vp-test/bin/black -t py37 .

tests: vp-test
	PYTHONPATH=src vp-test/bin/pytest test

run: vp
	vp/bin/python3 src/main.py

clean:
	-rm -rf vp vp-test
