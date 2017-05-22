Name:     github2spec
Version:  1.2.0
Release:  alt1

Summary:  Script for generation RPM spec file from github using genspec
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/genspec
Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

BuildPrereq: rpm-build-ruby

Requires: genspec

Source:   %name-%version.tar

%description
Script to get repository data from github and generate RPM spec file with
genspec. Program works in interactive mode, only one required value is URL.
Then you insert URL, the program will ask you to enter another values, but
before asking it would suggest default value. If you accept it then just press
Enter.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- Initial build as separate package (before it was part of genspec)