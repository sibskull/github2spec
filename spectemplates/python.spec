%define  modulename $module

Name:    python-module-%modulename
Version: $version
Release: alt1

Summary: $summary
License: $license
Group:   Development/Python
URL:     $url

Packager: $packager

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
$description

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
$stamp-alt1
$lastchange
