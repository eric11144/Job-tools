PIP_DIR=files/tmp/pip

PACKAGE_LIST=$(shell yq r tasks/main.yml 3.pip.name | sed 's/- //g')

PIP_DOWNLOAD_OPTIONS=\
	--extra-index-url http://pypi.collins.qi/ \
	--trusted-host pypi.collins.qi

-include piplist.mk

.PHONY: all
all: $(PIPFILE_LIST)

.PHONY: clean
clean:
	rm -rf \
		$(PIP_DIR) \
		tmp

.PHONY: download-files
download-files:
	$(eval root_piplist=$(shell yq r tasks/main.yml 4.pip.name | sed 's/- //g'))

	rm -rf tmp
	mkdir -p tmp
	pip download $(PIP_DOWNLOAD_OPTIONS) -d tmp pip $(root_piplist)

.PHONY: update-filelist
update-filelist: download-files
	$(eval piplist=$(strip $(shell ls tmp | grep -E '^[a-zA-Z0-9_-]+-([0-9.]+[0-9]+)?' -o | sed -r 's/(.*)-/\1==/' | tr '\n' ' ')))
	$(eval pipfile_list=$(strip $(shell ls tmp | awk '{print "$(PIP_DIR)/" $$1}' | tr '\n' ' ')))

	cat piplist.mk.in \
		| sed -e "s/%PIPLIST%/$(piplist)/g" \
		| sed -r "s:%PIPFILE_LIST%:$(pipfile_list):g" \
		> piplist.mk

	rm -rf tmp

.PHONY: veryclean
veryclean: clean
	rm -rf \
		piplist.mk

$(PIP_DIR)/%:
	mkdir -p $(PIP_DIR)
	pip download $(PIP_DOWNLOAD_OPTIONS) \
		-d $(PIP_DIR) \
		$(PIPLIST)
