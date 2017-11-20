%global commit          1a3ca01844799d2126e17783fa8bee37ad1b86cb
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           osops-tools-monitoring-oschecks
Version:        0.1
Release:        0.7.%{shortcommit}git%{?dist}
Summary:        Scripts used to monitor an Openstack Installation

License:        ASL 2.0
URL:            https://github.com/openstack/osops-tools-monitoring
# Source0:        osops-tools-monitoring-%{shortcommit}.tar.gz
Source0:        https://github.com/openstack/osops-tools-monitoring/archive/%{commit}/osops-tools-monitoring-%{shortcommit}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  python-setuptools
Requires: python-psutil
Requires: python-ceilometerclient
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: python-openstackclient
Requires: python-six


BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n osops-tools-monitoring-%{commit}/monitoring-for-openstack -S git
rm requirements.txt test-requirements.txt

rm -rf monitoring_for_openstack.egg-info


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
* Wed Mar 23 2016 Martin Mágr <mmagr@redhat.com> 0.1-0.7.1a3ca01git
- Update to commit 1a3ca01 to pull Pike compatibility fixes in

* Mon Aug 08 2016 Matthias Runge <mrunge@redhat.com> - 0.1-0.6.3986efgit
- pull in fixes for keystone, novaclient

* Wed Mar 23 2016 Martin Mágr <mmagr@redhat.com> 0.1-0.5.a9d3fdagit
- Update to commit a9d3fda to include latest fixes

* Wed Feb 10 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.4.ced73edgit
- Update to commit ced73ed to include latest fixes
- Added dependency on python-openstackclient

* Tue Feb  2 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.3.f0c3a92git
- Moved check scripts into /usr/libexec

* Thu Jan 28 2016 Graeme Gillies <ggillies@redhat.com> 0.1-0.2.f0c3a92git
- Update to commit f0c3a92 to include latest fixes

* Tue Jul 21 2015 Graeme Gillies <ggillies@redhat.com> 0.1-0.1.dd7ca5cgit
- Initial Package
