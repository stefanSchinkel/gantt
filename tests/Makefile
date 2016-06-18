NOSE :=/usr/bin/nosetests

clean:
	rm *.pyc
	rm -fr ./cover

test:
	@$(NOSE) *.py

cover:
	@$(NOSE) --cover-branches  --with-coverage \
	--cover-html --cover-html-dir cover --cover-package gantt 0*.py

.PHONY: clean clean-cover test all cover
