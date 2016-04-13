%global commit          a9d3fda24e9a81f709f7c44da49725d20d35af88
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           osops-tools-monitoring-oschecks
Version:        0.1
Release:        0.5.%{shortcommit}git%{?dist}
Summary:        Scripts used to monitor an Openstack Installation

License:        ASL 2.0
URL:            https://github.com/openstack/osops-tools-monitoring
Source0:        osops-tools-monitoring-%{shortcommit}.tar.gz
# Source0:        https://github.com/openstack/osops-tools-monitoring/archive/%{commit}/osops-tools-monitoring-%{shortcommit}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  python-setuptools
Requires: python-openstackclient

BuildArch: noarch

%description
%{summary}

%prep
%setup -q -n osops-tools-monitoring/monitoring-for-openstack
rm requirements.txt test-requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
find %{buildroot}%{python2_sitelib}/oschecks/*.py -not -name '__init__.py' -exec chmod +x {} \;

%files
%{_libexecdir}/openstack-monitoring/checks/oschecks-*
%{python2_sitelib}/oschecks
%{python2_sitelib}/monitoring_for_openstack*

%changelog
* Wed Mar 23 2016 Martin Mágr <mmagr@redhat.com> 0.1-0.5.a9d3fdagit
- Update to commit a9d3fda to include latest fixes

* Tue Feb 10 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.4.ced73edgit
- Update to commit ced73ed to include latest fixes
- Added dependency on python-openstackclient

* Tue Feb  2 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.3.f0c3a92git
- Moved check scripts into /usr/libexec

* Thu Jan 28 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.2.f0c3a92git
- Update to commit f0c3a92 to include latest fixes

* Tue Jul 21 2015 Graeme Gillies <ggillies@redhat.com> 0.1-0.1.dd7ca5cgit
- Initial Package
