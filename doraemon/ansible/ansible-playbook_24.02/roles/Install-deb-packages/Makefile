APT_REPO=files/tmp/apt-repo

-include deblist.mk

.PHONY: all
all: $(DEBLIST) files/tmp/apt-repo/Packages.gz

.PHONY: clean
clean:
	rm -rf \
		$(APT_REPO)

.PHONY: download
download: $(DEBLIST)

.PHONY: update-filelist
update-filelist:
	$(eval root_package_list=$(shell yq r tasks/main.yml 3.apt.name | sed 's/- //g'))
	$(eval root_package_version_list=$(shell apt-cache madison $(root_package_list) | sort -u -k1,1 | awk '{print $$1 "=" $$3}' | sort -u))
	$(eval package_list=$(shell apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances $(root_package_version_list) | grep "^\w" | sort -u))
	$(eval package_version_list=$(shell apt-cache madison $(package_list) | sort -u -k1,1 | awk '{print $$1 "=" $$3}' | sort -u))
	$(eval _deb_file_list=$(shell apt-get download --print-uris $(package_version_list) | awk '{print $$2}'))
	$(eval deb_file_list=$(addprefix files/tmp/apt-repo/,$(_deb_file_list)))

	cat deblist.mk.in \
		| sed -e 's|%PKGLIST%|$(package_version_list)|g' \
		| sed -e 's|%DEBLIST%|$(deb_file_list)|g' \
		> deblist.mk

.PHONY: veryclean
veryclean: clean
	rm -rf \
		deblist.mk

files/tmp/apt-repo/Packages.gz: FORCE $(DEBLIST)
	mkdir -p $(dir $@)
	cd $(dir $@) && \
		dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz

files/tmp/apt-repo/%.deb:
	mkdir -p $(APT_REPO)
	cd $(APT_REPO) && \
		apt-get download $(PKGLIST)

FORCE: ;
